# Wiom Design System for iOS

Owner-finalised design guidance for Wiom’s native iOS customer app: SwiftUI, iPhone, iOS 16+, light appearance, Hindi first.

## Live preview

- [Open the interactive iOS design system](https://abhishekgarg-wiom.github.io/wiom-design-system-ios/)
- [Open the contrast review](https://abhishekgarg-wiom.github.io/wiom-design-system-ios/wiom-ios-contrast-review.html)

The repository is public. GitHub Pages serves the complete HTML from `docs/`; no download or local setup is required for previewing.

## Read the system

- [Main design-system HTML](docs/wiom-ios-design-system.html): full foundation values, 20 guides, iPhone-style examples, interactive state changes, search and a guided walkthrough.
- [Contrast review HTML](docs/wiom-ios-contrast-review.html): approved Warning pairings and clearly labelled remaining proposals.
- [iOS skills index](skills-ios/README.md), [decisions contract](skills-ios/IOS_DECISIONS.md), and [finalisation summary](FINALISATION.md).

Download or clone this repository, then open the HTML file locally in a browser. The documents embed their fonts, icons and content; no server or dependency installation is needed. GitHub may display the HTML source rather than render the page. The two HTML files are kept together so their navigation link works offline.

## Typography

Use **Noto Sans only for both Hindi and English** (D32). Regular, Medium, SemiBold and Bold use the supplied NotoSans PostScript names. No separate Noto Sans Devanagari family is used; the existing supplied Noto Sans files support the tested Hindi characters.

## Final Warning combinations

| Use | Icon role | Surface |
|---|---|---|
| Rating stars only | Gold icon/warning | Rating component’s documented background |
| Warning indicator | Dark icon/action | bg/warning/subtle |
| Warning indicator, solid surface specified | Dark icon/action | bg/warning |

D31 applies to toast, input, icon badge and every Warning indicator. Toast/input outer surfaces remain neutral. The word action in the colour token does not make a decorative status glyph tappable. See the [full Warning reference](skills-ios/wiom-ios-foundations/references/warning-combinations.md).

## Package status

All 20 skills are documented and validated; 19 are active and bottom navigation remains an unused reference (D27). This repository is design guidance and an HTML reference, not a compiled SwiftUI SDK. Existing native-app code has not been changed here.

Open implementation/review items remain explicit: input-border and pressed-brand-text contrast, Dynamic Type policy and native device validation. No unapproved contrast proposal is an agent default.

## Provenance and parity

Derived from Wiom’s shared design-system repository, with owner decisions recorded through 23 Nov 2026. The inspected shared checkout was 3e6780c; D28 selection transitions were aligned in Android skills PR #18 at b480a46. Explicit owner decisions override older source/implementation mismatches. Android source/library alignment is separate work: this repository does not change Android skills, the builder, Figma or customer-app-ios.

D29 records the 16 pt toast bottom gap (sides 8 pt), same as the Android skill. D30 records 2–4 pills. D31 records the final Warning colour rule above. These differences need coordinated downstream alignment, not silent edits by an iOS agent.

Public reference publication was requested by the design-system owner. See [NOTICE](NOTICE.md) for ownership and reuse terms. No global skill installation was performed.

## Updating the preview

After editing any skill, reference or `IOS_DECISIONS.md`, refresh the HTML preview:

```
python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python scripts/update_preview.py
```

It re-renders only what changed. A new skill also needs a chapter entry in the page's `SKILLS` list.
