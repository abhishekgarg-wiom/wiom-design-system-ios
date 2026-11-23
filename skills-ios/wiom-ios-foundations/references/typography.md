# Typography on iOS

**Contents:** 1 Font · 2 The 13 text styles · 3 Dynamic Type anchors · 4 Letter spacing and Devanagari · 5 Line height in SwiftUI · 6 Usage rules · 7 Hindi rules · 8 Checks

---

## 1. Font

**Noto Sans only, for Hindi and English (D32).** Do not add or substitute the separate Noto Sans Devanagari font family. References to Devanagari below describe the Hindi script, not a second font family. The four existing customer-app font files were checked with Core Text on 22 Nov 2026: their PostScript names match the table and each covers the tested Devanagari characters in क्षि, र् and ज़. Reuse that approved build; do not assume every download called Noto Sans includes those glyphs. Four weights are bundled and registered in `Info.plist` (`UIAppFonts`):

| Weight | PostScript name |
|---|---|
| Regular 400 | `NotoSans-Regular` |
| Medium 500 | `NotoSans-Medium` |
| SemiBold 600 | `NotoSans-SemiBold` |
| Bold 700 | `NotoSans-Bold` |

Never fall back to the system font (SF Pro) for Wiom text: it would make iOS look different from Android. Check once per font update that "क्षि", "र्" and "ज़" render from Noto Sans, not a system fallback.

---

## 2. The 13 text styles

Same values as Android (`WiomTypography.kt`). Sizes and line heights in pt at the default text size.

| Token | Swift | Weight | Size / LH | Tracking | Use |
|---|---|---|---|---|---|
| `type/display/lg` | `Wiom.Typography.displayLg` | Bold | 48 / 64 | −0.02 em | Hero, splash |
| `type/heading/xl` | `headingXl` | Bold | 32 / 44 | −0.01 em | Section hero |
| `type/heading/lg` | `headingLg` | Bold | 24 / 32 | −0.01 em | Page title |
| `type/heading/md` | `headingMd` | Bold | 20 / 28 | −0.01 em | Bottom-sheet header, card group |
| `type/title/lg` | `titleLg` | Medium | 20 / 28 | −0.01 em | Top-bar title |
| `type/title/sm` | `titleSm` | Bold | 16 / 24 | 0 | Card title, list header |
| `type/body/lg` | `bodyLg` | Regular | 16 / 24 | 0 | **Default reading text** |
| `type/body/md` | `bodyMd` | Regular | 14 / 20 | 0 | Card description, helper, chat bubble |
| `type/body/sm` | `bodySm` | Regular | 12 / 16 | 0 | Caption, chat reply preview, list secondary/meta (owner lock 23f67f9) |
| `type/label/lg` | `labelLg` | SemiBold | 16 / 24 | +0.01 em | **Default interactive**: every CTA, input label, toast action |
| `type/label/md` | `labelMd` | SemiBold | 14 / 20 | +0.01 em | Chip, tab, badge label, inline button |
| `type/label/sm` | `labelSm` | SemiBold | 12 / 16 | +0.01 em | Bottom nav label, chat reply sender |
| `type/meta/xs` | `metaXs` | Regular | 10 / 16 | +0.02 em | **Only** Western-digit timestamps and badge counts (D18) |

Dialog titles and bottom-sheet headers: the component skills own the choice (`wiom-ios-dialog`, `wiom-ios-bottomsheet`).

---

## 3. Dynamic Type anchors

Every style scales with one iOS text style (`UIFontMetrics(forTextStyle:)`). At the default setting ("Large") the size is exactly the table above; it grows and shrinks with the user's setting.

| Wiom style | Scales with |
|---|---|
| `display/lg`, `heading/xl` | `.largeTitle` |
| `heading/lg` | `.title1` |
| `heading/md` | `.title2` |
| `title/lg` | `.title3` |
| `title/sm` | `.headline` |
| `body/lg`, `label/lg` | `.body` |
| `body/md`, `label/md` | `.subheadline` |
| `body/sm`, `label/sm` | `.caption1` |
| `meta/xs` | `.caption2` |

- **Cap:** the app root applies `.dynamicTypeSize(...DynamicTypeSize.accessibility3)` (D17).
- **Targets:** every screen fully usable through `xxxLarge`; through `accessibility3` nothing clips or overlaps (text wraps, rows grow, screens scroll).
- **Line height and tracking scale too**: line height through `UIFontMetrics.scaledValue(for:)`; tracking is em-based so it follows the scaled size.
- Never add a lower Dynamic Type cap to text inside graphics. Dot badges contain no digits. If text cannot fit, use the component fallback or re-layout through accessibility3.

---

## 4. Letter spacing and Devanagari

Tracking = size × em (e.g. `display/lg` 48 × −0.02 = −0.96 pt), applied with `.tracking(_:)`.

Android applies the same tracking to Devanagari, and parity says iOS does too. **But** check on device: Core Text can treat non-zero kerning as a reason to break conjunct shaping. If a conjunct (e.g. "क्ष", "द्ध", "श्र") renders differently from tracking 0, apply tracking only to Latin/digit runs and report it to the design team. Never apply negative tracking tighter than the table.

---

## 5. Line height in SwiftUI (iOS 16)

SwiftUI has no line-height modifier on iOS 16. A Wiom text style is applied with one modifier that does all of this:

1. `font`: `Font.custom(postScriptName, size: size, relativeTo: textStyle)` (scales with Dynamic Type).
2. Extra leading: `extra = scaledLineHeight − uiFont.lineHeight`, where `uiFont` is the same face scaled with `UIFontMetrics(forTextStyle:).scaledFont(for:)` and `scaledLineHeight = UIFontMetrics(forTextStyle:).scaledValue(for: lineHeight)`. Clamp at 0.
3. `.lineSpacing(extra)` (between lines) **and** `.padding(.vertical, extra / 2)` (so a single line is exactly the line height tall, as on Android: this is how a CTA is 12 + 24 + 12 = 48).
4. `.tracking(scaledSize × em)`.
5. Read `@Environment(\.dynamicTypeSize)` so the values recompute when the setting changes. Pass a matching `UITraitCollection(preferredContentSizeCategory:)` to the UIKit metric calculations; otherwise the system category can bypass a SwiftUI cap or preview override. Use the same effective category for font size, leading and tracking. If the font’s natural line height exceeds the target, preserve its glyph bounds and let the container grow; never claim exact line-height parity by clipping matras.

```swift
Text(key).wiomTextStyle(.bodyLg)   // the only way feature code sets type
```

- **Never** set a fixed `.frame(height:)` on text: Devanagari matras above and below the line get clipped.
- Multi-line text: `.fixedSize(horizontal: false, vertical: true)` inside stacks so it wraps instead of truncating.
- Truncation is allowed only where a component skill says so (`.lineLimit(n)` + `.truncationMode(.tail)`).

---

## 6. Usage rules

- **Default 16:** `body/lg` for reading, `label/lg` for anything tappable.
- **Pairing:** title 24 / 20 → description 16; title 16 → description 14.
- **Hierarchy by weight, not colour.** Colour comes from `text/*`.
- **Chat exception:** bubble text is `body/md` (14); not to be generalised to other lists.
- Sizes outside the 13 styles: not allowed. Need one? It is a gap (D24).

---

## 7. Hindi rules

- **Hindi body text is 16 (`body/lg`).** 14 (`body/md`) is allowed for Hindi only in the roles the scale names: card description, helper text, dialog body, sheet subtext, chat bubble. Below 14: captions and owner-locked list secondary/meta (`body/sm`, 12), never paragraphs. Never `meta/xs`.
- A bigger weight never replaces size: 14 Bold Hindi is still 14.
- "Smaller Hindi to fit" is answered by re-layout (wrap, stack, scroll), never by a smaller style.
- Hindi strings are usually longer than English: every component with a character limit counts **grapheme clusters** (`String.count`), so "क्षि" is one.
- Check every screen in Hindi **and** English, at default and at `accessibility3`.

---

## 8. Checks before shipping a screen

- [ ] Every `Text` uses `.wiomTextStyle(…)`; no `Font.system`, no raw sizes.
- [ ] No fixed height on anything holding text.
- [ ] Hindi and English both checked at default, `xxxLarge` and `accessibility3`.
- [ ] Conjuncts render the same with and without tracking (once per font update).
- [ ] `meta/xs` only on digits.

Metric implementation reference: [Apple UIFontMetrics scaling with traits](https://developer.apple.com/documentation/uikit/uifontmetrics/scaledvalue(for:compatiblewith:)).
