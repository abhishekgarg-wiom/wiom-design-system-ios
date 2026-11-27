---
name: wiom-ios-rating
description: "Wiom star rating for the iOS customer app in SwiftUI: 5 Material Rounded stars, gold when filled, used for the post-installation rating ask. Use when building or reviewing a rating input or a read-only rating display in SwiftUI."
---

# Wiom Rating (iOS)

Five stars the user taps to rate (for example after installation). **The only place gold `icon/warning` is allowed** (D31, D36).

Contract: `../wiom-ios-foundations/references/decisions.md`. Tokens: `wiom-ios-foundations` (`references/tokens.md`, `icons.md`, `warning-combinations.md`).

## 1. Anatomy

| Slot | Value | Token |
|---|---|---|
| Stars | 5 in a row | n/a |
| Star size | 32 pt glyph | `icon/xl` (D43) |
| Gap between stars | 8 pt | `space/8` |
| Tap area | 48 × 48 pt per star (glyph centred) | D14 |
| Filled star | Material Rounded `star` | `icon/warning` (gold) |
| Empty star | Material Rounded `star_border` | `icon/nonAction` |
| Background | The host surface | `bg/default` |

## 2. Behaviour

- Tap star *n* = rating *n*; stars 1..*n* fill. Tap the same star again to keep it (no clearing by tap).
- No half stars. The value commits on tap; selection colour fades on `motion/micro` (D28).
- Read-only display: same look, not tappable, one VoiceOver element ("Rated 4 of 5").
- Put the question above in text ("आपका अनुभव कैसा रहा?", illustrative); stars never stand alone.

## 3. Universal rules

1. Gold is for stars only; never reuse it for Warning glyphs.
2. Always 5 stars; never a 10-point or emoji scale.
3. Empty stars must stay visible (`icon/nonAction`), so the scale is readable.

## Settled rules

- **Star size (D43):** `icon/xl` (32 pt).

## Open questions

1. Figma has no rating component yet; design to draw it from this spec.

## Accessibility strings

Catalog keys this component needs (never literals in code):

| Key | English meaning | Used for |
|---|---|---|
| `rating.value` | "%1$d of 5" | Rating value |
| `rating.readonly` | "Rated %1$d of 5" | Read-only rating label |

Hindi text comes from the catalog; new strings need approval (D39).

## iOS (SwiftUI, iOS 16+)

- **Built from:** an `HStack(spacing: Wiom.Spacing.s8)` of 5 `Button`s, each a template `Image` (`Wiom.Icon.star` / `starBorder`) in a 48 pt frame.
- **VoiceOver:** the group is one adjustable element: label = the question, value "n of 5", `accessibilityAdjustableAction` to change it.
- **Dynamic Type:** stars don't scale (D16); the question text scales and wraps.
- **Reduce Motion:** colour fade stays; nothing moves.
- **Haptics:** none (D21).
