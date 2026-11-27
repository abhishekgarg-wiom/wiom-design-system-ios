"""Update the HTML preview (docs/wiom-ios-design-system.html) from the skills.

Re-renders every skill, reference and the decisions file that changed, using
the same Markdown settings the preview was built with. Run from the repo root:

    python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements.txt
    .venv/bin/python scripts/update_preview.py

New skills or demos still need a chapter entry in the page's SKILLS list.
"""
import json,re,sys,pathlib,markdown
REPO=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else pathlib.Path(__file__).resolve().parent.parent); S=REPO/'skills-ios'; HP=REPO/'docs/wiom-ios-design-system.html'
def md(text,prefix):
 text=re.sub(r'^---\n.*?\n---\n','',text,flags=re.S)
 text=re.sub(r'^# [^\n]+\n','',text,count=1,flags=re.M)
 out=markdown.markdown(text,extensions=['tables','fenced_code','sane_lists','toc'],output_format='html')
 out=re.sub(r'id="([^"]+)"',lambda m:'id="'+prefix+'-'+m[1]+'"',out)
 out=re.sub(r'href="#([^"]+)"',lambda m:'href="#'+prefix+'-'+m[1]+'"',out)
 out=re.sub(r'href="([^\"]*\.md)(#[^\"]*)?"',lambda m:'href="#'+prefix+'" data-local-ref="'+m[1]+'"',out)
 out=re.sub(r'<table>', '<div class="spec-table"><table>',out).replace('</table>','</table></div>')
 out=re.sub(r'<pre><code(?: class="language-(\w+)")?>(.*?)</code></pre>',lambda m:'<details class="code-example"><summary>'+('SwiftUI implementation example' if m[1]=='swift' else 'Example / anatomy')+'</summary><pre><code>'+m[2]+'</code></pre></details>',out,flags=re.S)
 return out
h=HP.read_text()
ENC={'SKILLS':(False,False),'DECISIONS':(False,False),'CONTRACTDOC':(False,True),'FULLDOCS':(False,True),'REFERENCES':(False,True)}
def get(n):
  st=h.index('const %s='%n)+len('const %s='%n); v,end=json.JSONDecoder().raw_decode(h,st); return v,st,end
def put(n,v):
  global h
  _,st,end=get(n); ea,esc=ENC[n]; d=json.dumps(v,ensure_ascii=ea)
  if esc: d=d.replace('</','<\\/')
  h=h[:st]+d+h[end:]
SK,_,_=get('SKILLS'); FD,_,_=get('FULLDOCS'); REF,_,_=get('REFERENCES'); DEC,_,_=get('DECISIONS')
changed=[]
for s in SK:
  src=(S/f"wiom-ios-{s['slug']}/SKILL.md").read_text()
  if src!=s['source']: s['source']=src; FD[s['slug']]=md(src,'spec-'+s['slug']); changed.append(s['slug'])
for r in REF:
  t=(S/f"wiom-ios-{r['parent']}/references/{r['slug']}.md").read_text()
  if t!=r['text']: r['text']=t; r['html']=md(t,'ref-'+r['slug']); changed.append(r['slug'])
dec=(S/'wiom-ios-foundations/references/decisions.md').read_text()
if dec!=DEC: put('DECISIONS',dec); put('CONTRACTDOC',md(dec,'contract')); changed.append('decisions')
put('SKILLS',SK); put('FULLDOCS',FD); put('REFERENCES',REF)
HP.write_text(h); print('updated:',changed)
