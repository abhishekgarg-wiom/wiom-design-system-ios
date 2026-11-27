---
name: wiom-ios-foundations
description: "Wiom DS V2 foundation tokens and rules for the iOS customer app in SwiftUI: colour, typography with Dynamic Type, Material Rounded icons, spacing, radius, border width, shadow, motion tokens, safe areas, keyboard, hit areas and accessibility baseline, with the Swift name of every token. Use when choosing a colour, text style, icon, spacing, radius, shadow or motion value in SwiftUI for Wiom, or when a component skill points here."
---

# Wiom foundations for iOS (SwiftUI, iOS 16+)

**Design system:** Wiom DS V2 · **App:** native iOS customer app, iPhone only, portrait, light mode · **Font:** Noto Sans only, for Hindi and English · **Copy:** Hindi first, from the string catalog.

**The parity rule.** iOS and Android users see the same app. Visual values follow the named Android baseline unless the owner has explicitly locked a correction in the decisions contract. iOS differs only in behaviour (gestures, safe areas, keyboard, accessibility). The full decision list is [`references/decisions.md`](references/decisions.md); when this skill and that file disagree, that file wins.

## 1. Where to look

| You need | Read |
|---|---|
| A colour, spacing, radius, border width, shadow or icon size, with its Swift name and hex | [`references/tokens.md`](references/tokens.md) |
| The same tokens as JSON for code generation (generated from tokens.md) | [`references/tokens.json`](references/tokens.json) |
| The decisions every iOS skill follows (D1 to D41), Swift naming, open questions | [`references/decisions.md`](references/decisions.md) |
| A text style, Dynamic Type behaviour, line height in SwiftUI, Hindi rules | [`references/typography.md`](references/typography.md) |
| Choosing colour roles, state combinations, primitive boundaries and existing use cases | [`references/colour-usage.md`](references/colour-usage.md) |
| Any Warning icon or rating-star colour pairing (D31) | [`references/warning-combinations.md`](references/warning-combinations.md) |
| An icon (Material Rounded SVG assets, never SF Symbols) | [`references/icons.md`](references/icons.md) |
| Screen frames, gutters, safe areas, keyboard, status bar, hit areas | [`references/layout.md`](references/layout.md) |
| VoiceOver, Dynamic Type, Reduce Motion baseline | [`references/accessibility.md`](references/accessibility.md) |
| Motion durations, curves, spring, Reduce Motion forms | [`references/motion.md`](references/motion.md) (when to use them: `wiom-ios-motion`) |
| Native verification, shared overlay/navigation host responsibilities and readiness evidence | [`references/native-validation.md`](references/native-validation.md) |
| Structural code rules (no fixed heights, parent owns gaps…) | `wiom-ios-layout-rules` |
| A component | its `wiom-ios-<component>` skill (anatomy and states live there, not here) |

## 2. Tokens at a glance

**Colour: four namespaces, matched to what they colour.** `bg/*` → backgrounds and fills · `text/*` → `Text` · `stroke/*` → borders and dividers · `icon/*` → template images. Swift: `Wiom.Colors.<lowerCamel>` (`bg/brand/subtle` → `bgBrandSubtle`).

| Role | Token |
|---|---|
| Page, card, input, sheet, dialog | `bg/default` |
| Reading text · secondary text | `text/default` · `text/subtle` |
| Placeholder and disabled text | `text/disabled` (there is no `text/placeholder`) |
| Primary CTA | `bg/brand` + `text/onBrand` (max one per screen) |
| Selected chip / tab / row | `bg/selected` + `text/selected` / `stroke/selected` |
| Tappable chrome icon · decorative icon | `icon/action` · `icon/nonAction` |
| Warning text (on `bg/warning`, `bg/warning/subtle` **and** `bg/default`) | `text/onWarning` (no `text/warning` exists) |
| Error status surface | `bg/critical/subtle` + `text/default` body + `text/critical` heading + `icon/critical` glyph |
| Scrim | `overlay/scrim` (the only one) |

**Type:** 13 styles, `Wiom.Typography.*`, applied with `.wiomTextStyle(…)`. Default reading text `type/body/lg` (16/24); default interactive text `type/label/lg` (16/24 SemiBold). Every style scales with Dynamic Type (typography §3).

**Spacing:** 4 pt grid: 4 · 8 · 12 · 16 · 24 · 32 · 40 · 48 · 64 · 72 · 84 (`Wiom.Spacing.s16`). Screen gutter 16; chat 12; dialog padding 24; sheet padding 16.

**Radius (circular corners, never continuous):** none 0 · tiny 4 · small 8 · medium 12 · **large 16** (buttons, cards) · xlarge 24 (dialogs, sheets) · full (`Capsule`).

**Border width:** small 1 · medium 2, drawn inside (`.strokeBorder`).

**Shadow:** none · sm · md (default elevation) · lg · xl (dialogs, with scrim only).

**Icons:** Material Icons **Round**, the same glyphs as Android's `Icons.Rounded.*`, as template SVG assets `ic_rounded_<name>`. Sizes 16 · 20 · **24** · 48.

**Motion:** `motion/micro` 0.2 s · `motion/surface` 0.3 s · `motion/emphasis` 0.45–0.6 s · `ease/standard` (0.4, 0, 0.2, 1) · `spring/settle`. Page changes are system push/pop.

## 3. Cross-foundation rules

1. **Tokens only.** No hex, no raw point sizes for type, spacing, radius, border or shadow in feature code. No eyedropping from Figma, no "closest token". No token fits? Report the gap to the design team and the iOS lead; in code only `// TODO(IOS-123): …` with a ticket.
2. **Border or shadow, never both.** Flat → 1 pt border; elevated → shadow, no border.
3. **Filled means no border.** Checked checkbox, on switch and filled button: the fill is the edge. Selected chips retain the explicit border specified by `wiom-ios-tabs-filters`.
4. **Radius matches the shape.** The border follows the component radius; nested radius = outer − padding.
5. **Parents own gaps.** Siblings are spaced by their stack; children never add outside padding; no `.offset` for layout.
6. **Hit areas ≥ 44 × 44 pt, default 48**, whatever the visible size.
7. **Nothing that holds text has a fixed height.** Minimum heights only; text wraps, then rows grow, then screens scroll.
8. **Status families don't mix.** A positive icon never sits on a warning surface; positive, critical and info stay within their families. Warning uses dark `icon/action` on `bg/warning/subtle` or `bg/warning` (D31); gold `icon/warning` is for rating stars only.
9. **Dividers inside cards are inset** to the card's padding.
10. **Disabled = three tokens together:** `bg/disabled` fill, `text/disabled`, `icon/disabled`; outline components also switch to `stroke/subtle`. Non-neutral colours without a disabled token use 40 % opacity of the base colour. Disabled controls are `.disabled(true)`.
11. **Surfaces own the gutter** (layout §2): top bar and sheet are edge to edge; screen content and sticky CTA bar 16; dialog 24 inside, max width 312.
12. **No hover, no ripple, no keyboard focus ring** on iPhone. Pressed states use the tokens the Android library uses (decisions.md D13).
13. **Light mode only**; colours still live in the asset catalog so dark mode can come later.

## 5. Anti-pattern checklist

- [ ] Hex or raw numbers in feature code
- [ ] `Font.system(…)`, SF Pro, or a size outside the 13 styles
- [ ] `Image(systemName:)` anywhere in Wiom UI
- [ ] `.frame(height:)` on text or on a container of text
- [ ] A width constant (360, 328, 312 other than the dialog max)
- [ ] `RoundedRectangle(cornerRadius:, style: .continuous)`
- [ ] Border and shadow on the same component; border on a filled control
- [ ] `text/default` on a warning surface; an invented `text/warning` or `text/placeholder`
- [ ] `text/brand` or `text/subtle` on `bg/inverse` / `bg/brand/bold`
- [ ] A tappable element under 44 pt, or without an accessibility label
- [ ] A disabled control that is not `.disabled(true)`
- [ ] Hover or focus-ring styling; invented pressed overlays
- [ ] An animation with an inline duration or curve
- [ ] `type/meta/xs` on anything but digits

## Open questions

Tracked in [`references/decisions.md`](references/decisions.md) §3: Figma alignment for `text/subtle` and tracking (Q1–Q2), `bg/surface` (Q3), motion in Figma (Q4), accepted contrast exceptions (Q5, list in tokens §9), blue/orange mapping for server-driven screens (Q12), `codeSyntax.iOS` (Q13).

## iOS (SwiftUI, iOS 16+)

- **Built from:** asset-catalog colour sets (one appearance) exposed as `Wiom.Colors`; a `.wiomTextStyle(_:)` view modifier over `Font.custom(_:size:relativeTo:)` with scaled line spacing and tracking; `Wiom.Spacing`, `Wiom.Radius`, `Wiom.BorderWidth`, `Wiom.IconSize` as `CGFloat` constants; `.wiomShadow(_:)`; `Wiom.Motion` / `Wiom.Easing` animations; `Wiom.Icon` images from `ic_rounded_*` template assets.
- **Tokens:** DS V2 names, Swift names by the rule in decisions.md §2. Old iOS names (`WiomColor.priText`, `WiomRadius.large` = 24, `neutral900` = #161021…) are retired; map by meaning and hex, never by name.
- **Size:** 1 dp = 1 pt. No screen-width constants. Minimum heights for anything with text.
- **Dynamic Type:** every style anchored to an iOS text style (typography §3); usable through xxxLarge, no clipping through accessibility3 (the cap).
- **VoiceOver:** baseline in accessibility.md; every component skill applies it.
- **Hit area:** ≥ 44 × 44, default 48 × 48 (`.frame(minWidth:minHeight:)` + `.contentShape`).
- **Motion:** tokens in motion.md; Reduce Motion replaces movement with a `motion/micro` fade and stops loops except the spinner.
- **Safe areas and keyboard:** surfaces paint into the safe area, content stays inside; last CTA `space/16` above the home indicator (or the screen edge on SE); keyboard rules in layout §6. Status-bar content light or dark per surface; it can't be coloured.
- **Haptics:** none by default.
- **Not on iOS:** hover tokens, ripple, keyboard focus rings, status-bar colour, Android back button, 360 × 720 frames, `sp`, SF Symbols, SF Pro, continuous corners, `bg/surface`.
