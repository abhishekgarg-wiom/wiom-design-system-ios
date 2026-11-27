---
name: wiom-ios-selection-controls
description: >
  Wiom checkbox, radio and switch indicators for the SwiftUI iOS
  customer app. Use when drawing, building or reviewing a Wiom
  checkbox, radio or switch on iOS, inside a list row or inline with
  its own text.
---

# Wiom Selection Controls (iOS): Checkbox · Radio · Switch

Three small indicators that share sizing, stroke and fill rules. They are **indicator-only**: no label, helper text, padding or row chrome. The text next to them, and the tap, belong to the parent: a list row (`wiom-ios-list-item`, the common case), the Acknowledge CTA (`wiom-ios-cta`), or an inline control built as in §6.

Binding contract: `wiom-ios-foundations/references/decisions.md` (D12 switch, D13 pressed, D14 hit area, D16 fixed glyph sizes). Tokens: `wiom-ios-foundations` (`tokens.md`, `icons.md`, `accessibility.md`, `motion.md`).

| Control | Visible size | Selection | States |
|---|---|---|---|
| Checkbox | 24 × 24 pt, `radius/tiny` | unchecked · mixed (indeterminate) · checked | Default · Disabled · Error |
| Radio | 24 × 24 pt, circle | not selected · selected | Default · Disabled · Error |
| Switch | 52 × 32 pt track, 24 pt thumb | off · on | Default · Pressed · Disabled (no Error) |

These sizes are fixed glyph shapes (D16). They never scale, and callers never resize them. The hit area is always the parent's, ≥ 44 pt, default 48 pt (D14).

## 1. Anatomy

### Checkbox

| Slot | Value |
|---|---|
| Box | 24 × 24 pt, `radius/tiny` (4), circular corners (D3) |
| Unchecked | 2 pt inside stroke (`stroke/medium` width), no fill |
| Checked / mixed | Solid fill, **no stroke** |
| Glyph, checked | Material Rounded `check` (asset `ic_rounded_check`), drawn at `icon/md` (24) centred in the box; the glyph's own padding makes it read about 20 pt |
| Glyph, mixed | Material Rounded `remove` (asset `ic_rounded_remove`), same size |

### Radio

| Slot | Value |
|---|---|
| Ring | 24 × 24 pt circle |
| Not selected | 2 pt inside stroke, no fill |
| Selected | Solid fill, no stroke, centred 10 × 10 pt dot |

### Switch

| Slot | Value |
|---|---|
| Track | 52 × 32 pt capsule (`radius/full`) |
| Track stroke | 2 pt inside stroke when **off**; none when on |
| Thumb | 24 × 24 pt circle, inset 4 pt; x = 4 pt (off) or 24 pt (on), vertically centred |
| Thumb colour | Same in every state (§3) |
| Shadow | None on track or thumb |

No shadow on any of the three. All glyphs are Material Rounded (D4); never SF Symbols, never a drawn tick.

## 2. States

### Checkbox and radio

| State | Unselected | Selected / mixed |
|---|---|---|
| Default | stroke `stroke/strong` | fill `bg/brand`, glyph/dot `icon/inverse` |
| Disabled | stroke `stroke/subtle` | fill `bg/disabled`, glyph/dot `icon/disabled` |
| Error | stroke `stroke/critical/focus` | fill `bg/critical`, glyph/dot `icon/inverse` |

Pressed: **no pressed visual** on the checkbox or radio itself (no pressed token, and Android shows none apart from the ripple, which iOS never draws: D13). Inside a list row the row shows `bg/subtle`.

### Switch

| State | Off | On |
|---|---|---|
| Default | track `bg/muted`, stroke `stroke/strong` | track `bg/brand`, no stroke |
| Pressed | track `bg/subtle`, stroke `stroke/strong` | track `bg/brand/pressed`, no stroke |
| Disabled | track `bg/disabled`, stroke `stroke/subtle` | track `bg/disabled`, no stroke |

- The thumb moves only when the value changes, **never on press**.
- The switch's own Pressed state shows only when the switch is the pressed element (inline use, §6). Inside a list row the row shows `bg/subtle` and the switch stays in Default.
- No Error state: a switch applies instantly, so there is nothing to validate. Wanting one means the control should be a checkbox.

### Not shipped (don't invent)

Hover, keyboard focus ring, switch Error, checkbox/radio Pressed (D13).

## 3. Tokens

DS V2 names only (Swift by the rule in `wiom-ios-foundations/references/decisions.md` §2).

| Slot | Token |
|---|---|
| Stroke width (all) | `stroke/medium` (2) → `Wiom.BorderWidth.medium` |
| Unselected stroke | `stroke/strong` · `stroke/subtle` (disabled) · `stroke/critical/focus` (error) |
| Selected fill | `bg/brand` · `bg/disabled` · `bg/critical` |
| Glyph / dot | `icon/inverse` · `icon/disabled` |
| Checkbox corner | `radius/tiny` |
| Switch track | `bg/muted` · `bg/subtle` (pressed off) · `bg/brand` · `bg/brand/pressed` · `bg/disabled`; corner `radius/full` |
| Switch thumb | `icon/inverse` (#FAF9FC), D34. No new token |
| Glyph size | `icon/md` (24) |
| Motion | `motion/micro` with `ease/standard` (selection colour/opacity; switch thumb movement) |

> **Thumb colour (D34):** `icon/inverse`, the same off-white used on pink. It replaces Android's raw white; the difference is not visible.

## 4. Rules

1. **Indicator only.** No label, helper or padding inside the control. The parent owns text, tap and VoiceOver.
2. **One size per control.** No size parameter; never `.frame` / `.scaleEffect` the indicator from a call site.
3. **`stroke/strong` for unselected default**, at 2 pt. Don't lighten it.
4. **Filled = no stroke** (checked, mixed, selected, switch on).
5. **Error swaps the fill** `bg/brand` → `bg/critical` on checkbox and radio; the glyph stays `icon/inverse`.
6. **Mixed only on a parent checkbox** whose children are partly checked. Tapping mixed checks all.
7. **Consent starts unchecked.** The person opts in themselves.
8. **Radios come in groups of 2 or more.** A single radio is the wrong control.
9. **Switches apply instantly.** If the change waits for a "Save", use a checkbox.
10. **No haptics** (D21).
11. **Copy is illustrative.** Labels and VoiceOver values come from the string catalog (Hindi first, English separately, sentence case); any limit is in grapheme clusters (D25).

## 5. VoiceOver contract

The control is announced through its parent element. The indicator view itself is always `.accessibilityHidden(true)`.

| Control | Element | Label | Value | Traits |
|---|---|---|---|---|
| Checkbox | `Button` | the parent's text | "checked" / "not checked" / "mixed" | button |
| Radio | `Button` | the parent's text | none | button, + selected when selected |
| Switch | `Toggle` (custom `ToggleStyle`) | the parent's text | "on" / "off" | switch: "…, switch button, on" (D12) |
| Any, disabled | as above | | | + dimmed (`.disabled(true)`) |
| Any, error | as above | the error text is visible next to the control and part of the label | | |

- Checkbox uses the value, not `.isSelected` (both together read "selected, checked").
- Inside a list row the **row** is this element and carries these values (`wiom-ios-list-item` §6).

### Preserving native switch semantics

A custom `ToggleStyle` built from a `Button` can lose native toggle semantics. On every supported iOS version use `.accessibilityRepresentation { Toggle(isOn: configuration.$isOn) { configuration.label }.toggleStyle(.switch) }`. The explicit system style avoids recursive application of the Wiom style. This representation affects accessibility, while the visible switch remains Wiom. Verify on/off, activation and disabled announcements on device.

## 6. Where they live

| Use | Who owns tap, label, hit area | Control's role |
|---|---|---|
| In a list row (common) | The row: `Button` (checkbox, radio) or `Toggle` (switch), whole row ≥ 48 pt | Indicator, hidden from VoiceOver |
| Acknowledge CTA (consent line) | `wiom-ios-cta` | Indicator |
| Inline with its own text (no row) | A compact `Button` / `Toggle` wrapping indicator + visible text, `space/12` apart, `.frame(minHeight: 48)`, `.contentShape(Rectangle())` | Indicator; the switch shows its Pressed track here |

A control with no visible text is not allowed: there would be nothing to announce. If a screen seems to need one, the text exists somewhere nearby and should be inside the same element.

## Settled rules

- **Thumb (D34):** `icon/inverse`.
- **Switch motion (D28):** thumb and track colour on `motion/micro` + `ease/standard`.
- **Indicator size:** checkbox and radio are 24 × 24 pt.

## Open questions

1. **Checkbox and radio pressed.** There is no pressed token; iOS shows no pressed visual (D13). Is a pressed look wanted?
2. **Error announcement.** iOS puts the error text next to the control. Should it also be announced when it appears (as for input fields)?
3. **Switch semantics.** Verify the native accessibility representation from iOS 16 to current versions; the value must be spoken once.

## iOS (SwiftUI, iOS 16+)

- **Built from:** Checkbox and Radio: indicator views (`Shape` + Material Rounded template image), placed inside a `Button` owned by the parent. Switch: `Toggle` + custom `ToggleStyle` (`WiomSwitchStyle`, row or inline layout) that draws the Wiom track and thumb; never the system `.switch` look. Inline wrappers use a no-op `ButtonStyle` so SwiftUI's default press dimming doesn't appear (D13).
- **Tokens:** §3. `stroke/medium`; `stroke/strong`, `stroke/subtle`, `stroke/critical/focus`; `bg/brand`, `bg/brand/pressed`, `bg/disabled`, `bg/critical`, `bg/muted`, `bg/subtle`; `icon/inverse`, `icon/disabled`; `radius/tiny`, `radius/full`; `icon/md`; `motion/micro`, `ease/standard`.
- **Size:** fixed glyph shapes: 24 × 24 (checkbox, radio), 52 × 32 (switch). The element around them is `minHeight: 48` and fills or hugs per its parent.
- **Dynamic Type:** indicators don't scale. Their text (in the row or inline wrapper) scales and wraps; the indicator stays vertically centred on the text block (as in the list row). Check Hindi and English through accessibility3.
- **VoiceOver:** §5. Indicator views hidden; parent element carries label, value and traits; native switch semantics preserved with `.accessibilityRepresentation` (§5).
- **Hit area:** never the indicator's 24 pt or 32 pt. Always the parent element, ≥ 44 × 44 pt, default 48 (`.frame(minHeight: 48)` + `.contentShape(Rectangle())`).
- **Motion:** switch thumb slides and track colour cross-fades in `motion/micro` with `ease/standard`. **Reduce Motion:** the thumb jumps to its new position (no slide); the track colour may still cross-fade in `motion/micro` (D20). Checkbox and radio update their semantic value immediately; fill, stroke and mark opacity ease in both directions with `Wiom.Motion.microStandard`. Keep indicator geometry fixed and the control identity stable. Reduce Motion retains these colour/opacity fades (D28). Fill/ring and the disappearing Off switch stroke fade to the same token at opacity 0, never `.clear`.
- **Safe areas and keyboard:** none of their own; the parent row or wrapper handles placement.
- **Haptics:** none (D21). The custom style adds none.
- **Not on iOS:** hover, keyboard focus ring (`stroke/brand/focus` ring is not drawn on iPhone), ripple, the system green `UISwitch` look, SF Symbol `checkmark` / `circle.fill`, Android standalone `minimumInteractiveComponentSize`.

### Checkbox indicator

**Built from:** a 24 × 24 pt `radius/tiny` circular rectangle, hidden from VoiceOver. Unchecked: `stroke/medium` border in `stroke/strong` (`stroke/critical/focus` in error, `stroke/subtle` when disabled). Checked or mixed: fill `bg/brand` (`bg/critical` in error, `bg/disabled` when disabled) with the `check` / `remove` glyph at 24 pt in `icon/inverse` (`icon/disabled` when disabled).

The radio is the same shape with `Circle()` and a centred 10 × 10 `Circle()` dot tinted `icon/inverse` (`icon/disabled` when disabled).

### Switch indicator

`WiomSwitchIndicator` draws the track and thumb from §1–§3. Use a leading-aligned `HStack` with conditional spacers and `space/4` inner padding; no layout offset. Track colour changes use `motion/micro` + `ease/standard`. The thumb changes alignment with the same token; Reduce Motion jumps to the new alignment and retains the colour cross-fade. The thumb is filled with `Wiom.Colors.iconInverse` (D34).

### Switch `ToggleStyle` (row and inline)

**Built from:** a custom `ToggleStyle` that renders a `Button` toggling `isOn`. Row layout fills the width with `space/16` padding and a pressed `bg/subtle` (D13); inline layout hugs and shows no pressed fill. Minimum 48 pt; `space/12` between text and indicator. Accessibility comes from `.accessibilityRepresentation` with a system switch `Toggle`, so VoiceOver says "switch button, on/off" (D12).

Switch row: `Toggle(isOn: $isOn) { rowText }.toggleStyle(WiomSwitchStyle())`, where `rowText` is the list item's leading icon + primary + secondary (`wiom-ios-list-item`, `WiomRowContent` without its own padding). The row then is one element: "Push notifications, plan renewals and offers, switch button, on" (illustrative).

### Inline checkbox (own text, no row)

**Built from:** a `Button` with a no-op `ButtonStyle` (no pressed visual, D13) around an `HStack` (`space/12`) of the checkbox and the consent text (`type/body/md`, `text/default`), minimum 48 pt, full content shape; value checked / not checked from the catalog.

### Common mistakes

- System `Toggle` with `.toggleStyle(.switch)` and `.tint(...)`: wrong size, shape and off colour. Use `WiomSwitchStyle`.
- A `Toggle` or checkbox `Button` inside a tappable row: two targets, two VoiceOver stops.
- `.frame(width: 24, height: 24)` as the tap area: below 44 pt. Wrap in the parent's ≥ 48 pt element.
- `.buttonStyle(.plain)` on an inline wrapper: dims on press. Use a no-op style.
- Bouncing, scaling or delaying a checkbox/radio selection. Its semantic value updates immediately; colour and mark opacity use the shared micro transition (§ iOS).
- Moving the thumb on press, or a hex white thumb (use `icon/inverse`, D34).
