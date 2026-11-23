# Wiom Design System for iOS

Owner-finalised design guidance for Wiom’s native iOS customer app: SwiftUI, iPhone, iOS 16+, light appearance, Hindi first.

## Read the system

- [Main design-system HTML](docs/wiom-ios-design-system.html): full foundation values, 19 guides, iPhone-style examples, interactive state changes, search and a guided walkthrough.
- [Contrast review HTML](docs/wiom-ios-contrast-review.html): approved Warning pairings and clearly labelled remaining proposals.
- [iOS skills index](skills-ios/README.md), [decisions contract](skills-ios/IOS_DECISIONS.md), and [finalisation summary](FINALISATION.md).

Download or clone this private repository, then open the HTML file locally in a browser. The documents embed their fonts, icons and content; no server or dependency installation is needed. GitHub may display the HTML source rather than render the page. The two HTML files are kept together so their navigation link works offline.

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

All 19 skills are documented and validated; 18 are active and bottom navigation remains an unused reference (D27). This repository is design guidance and an HTML reference, not a compiled SwiftUI SDK. Existing native-app code has not been changed here.

Open implementation/review items remain explicit: switch-thumb mapping, toast/input icon-container geometry, input-border and pressed-brand-text contrast, Dynamic Type policy and native device validation. No unapproved contrast proposal is an agent default.

## Provenance and parity

Derived from Wiom’s shared design-system repository, with owner decisions recorded through 23 Nov 2026. The inspected shared checkout was 3e6780c; D28 selection transitions were aligned in Android skills PR #18 at b480a46. Explicit owner decisions override older source/implementation mismatches. Android source/library alignment is separate work: this repository does not change Android skills, the builder, Figma or customer-app-ios.

D29 records the owner’s 8 pt toast clearance; the inspected shared Android source had reverted to 16 pt. D30 records 2–4 pills. D31 records the final Warning colour rule above. These differences need coordinated downstream alignment, not silent edits by an iOS agent.

See [NOTICE](NOTICE.md) for internal-use ownership. No global skill installation was performed.
