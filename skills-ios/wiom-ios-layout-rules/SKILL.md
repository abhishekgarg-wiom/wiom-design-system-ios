---
name: wiom-ios-layout-rules
description: "Structural rules for SwiftUI layout code in the Wiom iOS customer app: sizing (fill, minimum heights, no fixed text heights), who owns gaps, no offsets, no raw numbers, icons from Material Rounded assets, variants that never change size, and the Hindi, English and Dynamic Type checks before a screen ships. Use when writing or reviewing SwiftUI layout for a Wiom screen or component."
---

# Wiom layout rules for SwiftUI

Replaces `wiom-compose-layout-rules` for iOS. Tokens: `wiom-ios-foundations`. Component anatomy: the `wiom-ios-*` component skills. Decisions: [`../wiom-ios-foundations/references/decisions.md`](../wiom-ios-foundations/references/decisions.md).

## 1. Width

| Rule | Do | Don't |
|---|---|---|
| Components fill their parent | `.frame(maxWidth: .infinity, alignment: .leading)` | `.frame(width: 360)` / `328` / `UIScreen.main.bounds.width` |
| The surface owns the gutter | Screen: `.padding(.horizontal, Wiom.Spacing.s16)` once, on the content container | Padding each child to fake a gutter |
| Bounded surfaces use a max | Dialog: `.frame(maxWidth: 312)` with ≥ `s24` margins | A fixed dialog width |
| Equal-width siblings | Two buttons side by side: each `.frame(maxWidth: .infinity)` in an `HStack` | Computing half the screen width |
| Hug only by design | Tertiary CTA, chips, badges hug their content (still ≥ 44 pt hit area) | Hugging a component the skill says is full width |

## 2. Height

| Rule | Do | Don't |
|---|---|---|
| Text sets the height | `.frame(minHeight: 48)` on rows and buttons | `.frame(height: 48)` on anything with text |
| Fixed sizes only for glyph shapes | 8 pt dot, switch track, radio ring, checkbox box, spinner | Fixed height on a chip, badge, tab, top bar, toast |
| Multi-line text wraps | `.fixedSize(horizontal: false, vertical: true)` inside stacks | `.lineLimit(1)` unless the component skill allows truncation |
| Screens scroll | Every screen body is in a `ScrollView` unless it provably fits at accessibility3 on SE | A `VStack` that overflows at large text |
| Images keep their ratio | `.aspectRatio(contentMode:)` with a width | Fixed width and height on photos |

## 3. Spacing

1. **Parents own gaps.** `VStack(spacing: Wiom.Spacing.s16)` between siblings. Mixed gaps: nest stacks, or use an explicit `Spacer().frame(height:)` with a token.
2. **Children own only their inner padding**, as the component skill defines.
3. **No `.offset` for layout.** Offset moves the drawing but not the hit area or the neighbours. Allowed only inside animations.
4. **No raw numbers.** Every spacing, size, radius and border value is a token. Exceptions: `0`, `.infinity`, the dialog's `312` max, and component geometry explicitly documented as an open token gap. Preserve that geometry inside the design-system module with a real ticketed TODO; never create a token to hide the gap.
5. **No negative padding.** Overlap is drawn with `ZStack` / `.overlay` and alignment.

## 4. Variants never change size

A component's variants (state, type, selected, error, loading, pressed) keep its size and position. Swap colours, glyphs and border colours, not frames.

- Borders that appear on a state (active input 2 pt, selected card) are drawn with `.strokeBorder` on an overlay so the content doesn't move, or the rest state reserves the same width with a transparent border.
- Loading CTAs keep the label laid out (hidden) under the spinner so the width doesn't jump.
- Error and helper lines reserve no space when absent, but appear without moving content above them.

## 5. Icons

- Material Icons Round assets only: `Wiom.Icon.<name>` (`ic_rounded_<material_name>`), template rendering, sizes 16 / 20 / 24 / 48. Never `Image(systemName:)`.
- Tappable icons are `Button`s with a 48 × 48 frame (min 44), `.contentShape(Rectangle())` and a label.
- Brand and partner logos: original rendering, from the design team, never drawn.

## 6. Structure

- One screen = one `ScrollView` (or `List` only where the design is a plain list) + optional sticky CTA bar (`wiom-ios-cta`) via `.safeAreaInset(edge: .bottom)`.
- Top bar from `wiom-ios-top-bar`; system navigation bar hidden; swipe-back kept.
- Sheets, dialogs and toasts are presented through the app's overlay host, never `.sheet`, `.alert` or `.confirmationDialog` (D9, D10).
- Lists of many rows use `LazyVStack` inside the `ScrollView`.
- Use `ViewThatFits` (iOS 16) for "side by side if it fits, otherwise stacked" layouts (button groups, title + trailing value).

## 7. Accessibility wiring

- Every tappable element: label, trait, ≥ 44 pt.
- Grouped content (row, card) is one VoiceOver element.
- Decorative views hidden.
- Headers marked `.isHeader`.
- Baseline: `wiom-ios-foundations/references/accessibility.md`.

Shared host responsibilities and native acceptance cases: [native validation](../wiom-ios-foundations/references/native-validation.md). Read this when building the overlay/navigation shell or signing off a screen; documentation completion is not evidence of native behaviour.

## 8. Pre-commit checklist

- [ ] No fixed width; no fixed height on text.
- [ ] No raw numbers or hex; tokens only.
- [ ] No `.offset` used for layout; no child margins; no negative padding.
- [ ] Variants keep the component's size.
- [ ] No SF Symbols, no `Font.system`.
- [ ] Every tappable element ≥ 44 pt with a label.
- [ ] Checked on iPhone SE and Pro Max.
- [ ] Checked in **Hindi and English**.
- [ ] Checked at default, **xxxLarge** and **accessibility3** text sizes.
- [ ] Checked with **VoiceOver** and **Reduce Motion** on.

## Open questions

No separate visual values are defined here. Component mismatches remain in the component Open questions lists; shared unresolved decisions are in `../wiom-ios-foundations/references/decisions.md` §3 and §5.

## iOS (SwiftUI, iOS 16+)

- **Built from:** SwiftUI stacks, `Layout`, `ScrollView`, `LazyVStack`, `ViewThatFits` and safe-area insets; component skills own anatomy.
- **Tokens:** `space/4`, `space/8`, `space/12`, `space/16`, `space/24`, `space/48`, `radius/large`, `stroke/small`, `stroke/medium`.
- **Size:** fill available width; text containers use minimum heights in pt. No device-width constants.
- **Dynamic Type:** wrap, stack, grow and scroll through accessibility3; check Hindi and English on SE and Pro Max.
- **VoiceOver:** group each interactive row, label actions, preserve reading order and hide decoration.
- **Hit area:** ≥ 44 × 44 pt, default 48 × 48; reserve actual layout frames with no overlaps.
- **Motion:** component motion tokens apply; Reduce Motion uses `motion/micro` cross-fades and instant final values as foundations specifies.
- **Safe areas and keyboard:** surfaces paint into device insets, content respects them; last CTA spacing and keyboard spacing come from `wiom-ios-cta`.
- **Haptics:** none.
- **Not on iOS:** hover, Android press effects, hardware back, status-bar colour and keyboard focus rings.
