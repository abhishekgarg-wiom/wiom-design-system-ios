# Finalised Wiom iOS design skills

23 Nov 2026. All 19 skill documents are finalised and validated as an iOS design-guidance package. Eighteen are active; the navigation-bar reference remains unused under D27.

## Final Warning rule (D31)

Only three combinations apply:

1. Gold icon/warning for rating stars in the rating component only.
2. Dark icon/action on bg/warning/subtle for Warning indicators (10.85:1).
3. Dark icon/action on bg/warning for Warning indicators where the solid surface is specified (6.60:1).

Applied across foundations, tokens, iconography, colour usage, toast, input and icon-badge guidance. Generic same-family and decorative-icon rules now explain this explicit colour-role reuse. No new token was introduced. The main HTML includes a three-combination visual reference and the updated component examples. The review marks both dark Warning pairings approved globally and gold Warning glyphs prohibited.

D29 sets the toast bottom gap to 16 pt (sides 8 pt). D30 keeps 2–4 pill tabs. 27 Nov 2026 answers to the iOS team (D33 to D39): long toasts grow, switch thumb `icon/inverse`, Warning box = Icon Badge Sm, new `wiom-ios-rating`, `loader_infinity` is the brand loader, app animations listed, copy approved by Abhishek Garg. Existing reference files and the old walkthrough HTML were retained.

## Validation

All 19 metadata/contracts passed; 27 published contrast pairs were recomputed. Targeted browser checks verified the three approved combinations, gold rating stars, dark Warning icon badges and input examples, plus 6.60:1 for the solid pairing. All 19 HTML chapters passed with zero browser errors or HTTP requests. Selection, modal/search accessibility, walkthrough, responsive layout, shortlist/language and print checks passed. All 122 protected source/reference files stayed unchanged and no original files were removed.

Finalised documentation is not a native SDK or native accessibility certification. Warning toast/input container geometry, remaining input-border and pressed-brand-text contrast, Dynamic Type policy, switch-thumb mapping and native/device validation remain explicitly listed.

## Delivery

Refreshed outputs/skills-ios, wiom-ios-skills-revised.zip, wiom-ios-design-system.html and wiom-ios-contrast-review.html. The user authorised a new private GitHub repository named wiom-design-system-ios and explicitly requested the HTML inside it. That repository contains the iOS skills and offline HTML documents. No commit is made to the existing shared design-system repo. Android skills, builder, Figma and customer-app-ios remain untouched.


## Publication update

The owner subsequently requested this repository be public and its HTML be hosted. The repo is now public, with GitHub Pages configured from main /docs. Live preview: https://abhishekgarg-wiom.github.io/wiom-design-system-ios/
