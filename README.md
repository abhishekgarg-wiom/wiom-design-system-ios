# Wiom Design System for iOS

Owner-finalised design guidance for Wiom’s native iOS customer app: SwiftUI, iPhone, iOS 16+, light appearance, Hindi first.

## Live preview

- [Open the interactive iOS design system](https://abhishekgarg-wiom.github.io/wiom-design-system-ios/)
- [Open the contrast review](https://abhishekgarg-wiom.github.io/wiom-design-system-ios/wiom-ios-contrast-review.html)

The repository is public. GitHub Pages serves the complete HTML from `docs/`; no download or local setup is required for previewing.

## Read the system

- [Main design-system HTML](docs/wiom-ios-design-system.html): full foundation values, 24 guides, iPhone-style examples, interactive state changes, search and a guided walkthrough.
- [Contrast review HTML](docs/wiom-ios-contrast-review.html): approved Warning pairings and clearly labelled remaining proposals.
- [iOS skills index](skills-ios/README.md), [decisions contract](skills-ios/wiom-ios-foundations/references/decisions.md), and [changelog](CHANGELOG.md).

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

24 skills: 23 active, plus bottom navigation kept as an unused reference (D27). This repository is design guidance and an HTML reference, not a compiled SwiftUI SDK; the Swift API lives in the app repo.

Explicit open items: input-border and pressed-brand-text contrast (accepted exceptions, build with current tokens) and native device validation. No unapproved contrast proposal is an agent default.

Explicit owner decisions override older source or implementation mismatches. See [NOTICE](NOTICE.md) for ownership and reuse terms. History and provenance are in [CHANGELOG.md](CHANGELOG.md).

## Updating the preview

After editing any skill, reference or `wiom-ios-foundations/references/decisions.md`, refresh the HTML preview:

```
python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python scripts/update_preview.py
```

It re-renders only what changed. A new skill also needs a chapter entry in the page's `SKILLS` list.
