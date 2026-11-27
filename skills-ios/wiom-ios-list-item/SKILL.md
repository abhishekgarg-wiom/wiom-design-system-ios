---
name: wiom-ios-list-item
description: >
  Wiom list item, the one full-width row (leading slot, primary and
  secondary text, trailing meta, chevron, or an embedded checkbox,
  radio or switch) for the SwiftUI iOS customer app. Use when placing,
  building or reviewing a row in a stacked list on iOS.
---

# Wiom List Item (iOS)

One row component for every stacked list in the customer app. It owns the row: width, padding, tap, pressed and selected fills, disabled tokens, and the single VoiceOver element. The things inside it (icon badge, checkbox, radio, switch) only draw their indicator.

Binding contract: `wiom-ios-foundations/references/decisions.md`. Tokens: `wiom-ios-foundations` (`tokens.md`, `typography.md`, `icons.md`, `layout.md`, `accessibility.md`, `motion.md`). Embedded parts: `wiom-ios-icon-badge`, `wiom-ios-selection-controls`.

**1 component · 5 types · 2 states · fills the width · 48 pt minimum height.**

| Type | Leading | Trailing | Use for |
|---|---|---|---|
| Default | optional 24 pt icon (`icon/nonAction`) | optional 20 pt `chevron_right` (`icon/brand`) | Navigation rows, information rows, single-select rows that use the selected fill |
| Icon with bg | 48 pt icon badge (Md, any tone) | optional 20 pt `chevron_right` (`icon/brand`) | Prominent entries, feature entries, status summaries |
| Checkbox | 24 pt checkbox | none | Multi-select rows |
| Radio | 24 pt radio | none | Single-select rows (group of 2 or more) |
| Switch | optional 24 pt icon (`icon/nonAction`) | 52 × 32 pt switch | Instant-apply on/off settings |

## 1. Anatomy

```
┌──────────────────────── fills host width · min 48 pt ─────────────────────────┐
│ space/16 on all four sides                                                    │
│                                                                               │
│  [Lead]  Primary text (type/body/lg, text/default)        Meta   [Trail]     │
│          space/4                                         (type/body/sm)       │
│          Secondary text (type/body/sm, text/subtle)                           │
│                                                                               │
└───────────────────────────────────────────────────────────────────────────────┘
   lead → content: space/12 · content → trailing group: space/12 · meta → trailing icon: space/8
```

| Slot | Value |
|---|---|
| Width | Fills the host (screen, card, sheet). Never a fixed width. |
| Height | **Minimum** 48 pt; the row grows with its content. A one-line row computes to 56 pt (24 pt line + 2 × `space/16`); a switch row to 64 pt (32 pt track + 2 × `space/16`). Two-line Hindi and large Dynamic Type grow it further. |
| Padding | `space/16` all sides |
| Leading → content | `space/12` |
| Content → trailing group | `space/12` |
| Primary → secondary | `space/4` (only when secondary is shown) |
| Trailing meta → trailing icon | `space/8` |
| Content column | Takes all remaining width. Primary and secondary **wrap**; they are never truncated to one line. |
| Vertical alignment | Leading, content and trailing are centred vertically in the row, also when the text wraps. |
| Row background | Transparent at rest (adopts the host surface) |

Leading and trailing glyph sizes are fixed visible sizes (D14, D16): icon `icon/md` (24), chevron `icon/sm` (20), icon badge Md (48), checkbox and radio 24, switch track 52 × 32.

## 2. States

| State | Visual | Notes |
|---|---|---|
| Rest | Transparent row | |
| Pressed | Row fill `bg/subtle` while the finger is down | D13. Instant on and off (Android shows it with no animation and no ripple). |
| Selected | Row fill `bg/selected` | The current or chosen option. Not on Switch rows (the switch position is the signal). |
| Disabled | Content tokens swap to the disabled family (§3) | Tap suppressed. No pressed or selected fill. **Never opacity.** |

Rules:
- **Pressed XOR selected.** A selected row that is pressed keeps `bg/selected`.
- **Disabled wins.** A disabled row shows neither fill.
- No hover, no focus ring, no ripple (D13).

## 3. Tokens

DS V2 names only (Swift names by the rule in `wiom-ios-foundations/references/decisions.md` §2, e.g. `bg/subtle` → `Wiom.Colors.bgSubtle`).

### Layout and type

| Slot | Token |
|---|---|
| Padding | `space/16` |
| Gaps | `space/12` (lead → content, content → trailing), `space/8` (meta → trailing icon), `space/4` (primary → secondary) |
| Primary | `type/body/lg` |
| Secondary, trailing meta | `type/body/sm` |
| Leading icon size | `icon/md` (24) |
| Chevron size | `icon/sm` (20) |

### Colour, by state

| Slot | Default | Disabled |
|---|---|---|
| Primary text | `text/default` | `text/disabled` |
| Secondary text | `text/subtle` | `text/disabled` |
| Trailing meta | `text/subtle` | `text/disabled` |
| Leading icon (Default, Switch) | `icon/nonAction` | `icon/disabled` |
| Leading icon badge | the badge's tone (`wiom-ios-icon-badge`) | Neutral tone (see note) |
| Chevron | `icon/brand` | `icon/disabled` |
| Embedded checkbox / radio / switch | its Default state | its Disabled state (`wiom-ios-selection-controls`) |
| Pressed fill | `bg/subtle` | none |
| Selected fill | `bg/selected` | none |

> **Chevron is `icon/brand` (pink).** It is the row's tap affordance. Leading icons stay `icon/nonAction`.
>
> **Disabled icon badge:** Android renders the badge in its Neutral tone when the row is disabled (the `bg/disabled` circle it draws sits fully behind the badge). iOS matches what Android shows. The design intent was `bg/disabled` fill + `icon/disabled` glyph; see Open questions.

No shadow, no stroke, no divider on the row.

## 4. Rules

1. **Minimum height 48 pt; let it grow.** Never a fixed row height.
2. **The row owns the tap.** On Checkbox, Radio and Switch rows the whole row flips the value. The embedded control has no tap of its own and is not a separate accessibility element.
3. **One row = one VoiceOver element** (§6).
4. **Primary text is the label** for Checkbox, Radio and Switch rows. Never put a label inside the control.
5. **Use the shared parts.** Checkbox, radio and switch come from `wiom-ios-selection-controls`; the icon badge from `wiom-ios-icon-badge` (Md). Don't redraw them.
6. **Disabled is a token swap**, never opacity.
7. **Chevron means "goes somewhere".** Hide it on information rows and on select-and-dismiss rows.
8. **Stack rows with 0 gap and no dividers.** Each row's `space/16` padding separates them. Exception: inside the Wiom dialog's selection body rows sit `space/8` apart (`wiom-ios-dialog`).
9. **Cards hosting rows have 0 padding** (rows own it): `radius/large` corners, `bg/default` or `bg/subtle` fill, circular corner style (D3). The card clips the rows' pressed / selected fills to its corners.
10. **No button inside a row.** If the row leads to an action, the row tap navigates and the destination hosts the button (`wiom-ios-cta`). No second tap target (trailing icon button, inline link) in a row.
11. **Copy is illustrative.** Real strings come from the string catalog (Hindi first, English written separately, sentence case). There is no character cap: text wraps. Keep it short; if a limit is set it is counted in grapheme clusters (D25).

## 5. Patterns

| Pattern | Type | Leading | Trailing | Row action |
|---|---|---|---|---|
| Navigation row | Default | icon | chevron, optional meta (current value) | Push the destination |
| Information row | Default | icon | meta, **no chevron** | None (not tappable) |
| Prominent entry | Icon with bg | badge (tone carries meaning, the text says it too) | chevron | Push the destination |
| Single-select, select-and-dismiss | Default | none | none | Select, `bg/selected` on the chosen row, host closes |
| Single-select, stays open | Radio | radio | none | Select this option |
| Multi-select | Checkbox | checkbox | none | Toggle this option |
| Parent of a multi-select group | Checkbox | checkbox (indeterminate when some children are checked) | none | Tapping indeterminate or unchecked checks all; tapping checked clears all |
| Instant setting | Switch | optional icon | switch | Toggle and apply immediately |

A switch row applies its change at once. If the change needs a "Save", use a Checkbox row.

## 6. VoiceOver contract

| Row | Label (in reading order) | Value | Traits |
|---|---|---|---|
| Navigation / prominent entry | primary, secondary, trailing meta | none | button |
| Information (not tappable) | primary, secondary, trailing meta | none | none (static text) |
| Select-and-dismiss | primary, secondary | none | button, + selected when `bg/selected` |
| Checkbox | primary, secondary | "checked" / "not checked" / "mixed" | button |
| Radio | primary, secondary | none | button, + selected when chosen |
| Switch | primary, secondary | "on" / "off" | switch (toggle) |
| Any disabled row | as above | as above | + dimmed (from `.disabled(true)`) |

- **Hidden from VoiceOver individually:** leading icon, icon badge, chevron, and the embedded checkbox, radio and switch. If a leading icon or badge tone carries meaning, the text (secondary line) must say it.
- Value strings ("checked", "on", …) come from the string catalog, like all copy.
- An error on a checkbox row (consent not given) is shown as the secondary line, so it is read as part of the label.
- A group of radio or checkbox rows may sit in a container with `.accessibilityElement(children: .contain)` and a group label when the screen has a heading for it.

## Open questions

0. **DECIDED: secondary/meta text.** Owner commit `23f67f9` locks `type/body/sm` (12 pt). Android still ships `type/body/md` (14). iOS follows the owner’s locked source rule; **Android app must change**. This is a known implementation mismatch, not an unanswered design choice.

1. **Disabled icon-with-bg row.** Android (`WiomListItem.kt:257-271`) draws a `bg/disabled` circle *behind* a Neutral-tone `WiomIconBadge` of the same size, so the visible result is the Neutral badge (`bg/subtle` fill, `icon/nonAction` glyph), not the skill's `bg/disabled` fill + `icon/disabled` glyph. iOS follows Android for parity. Design team: confirm the intended look; if it is `bg/disabled` + `icon/disabled`, Android and iOS both change.
2. **Text wrapping.** The older skill code set one-line limits on primary, secondary and meta; Android (`WiomListItem.kt:133-150`) sets none, so text wraps. iOS follows Android (wraps). Confirm wrapping is the intended rule for meta too.
3. **Trailing meta at accessibility text sizes** moving under the text column is an iOS-only layout adaptation (Android has no equivalent breakpoint). Confirm with the design team.
4. **Dialog selection body `space/8` between rows** comes from the skill (Figma dialog selection); Android's list item has no such spacing itself, the host adds it. Confirm with `wiom-ios-dialog`.
5. **Row press timing.** SwiftUI delays the pressed state of a `Button` inside a `ScrollView` slightly so a scroll doesn't flash rows; Android shows it on touch-down. Accepted as platform behaviour unless the design team objects.

## iOS (SwiftUI, iOS 16+)

- **Built from:** tappable rows are a `Button` with a custom `ButtonStyle` (pressed and selected fills). Switch rows are a `Toggle` whose custom `ToggleStyle` draws the whole row plus the Wiom switch indicator. Information rows are a plain `HStack` combined into one element. Embedded indicators are the indicator-only views from `wiom-ios-selection-controls` and `wiom-ios-icon-badge`.
- **Tokens:** `space/16`, `space/12`, `space/8`, `space/4`; `type/body/lg`, `type/body/sm`; `text/default`, `text/subtle`, `text/disabled`; `icon/nonAction`, `icon/brand`, `icon/disabled`; `bg/subtle` (pressed), `bg/selected` (selected); sizes `icon/md`, `icon/sm`; `motion/micro`, `ease/standard` (D28). Host card: `radius/large`, `bg/default` or `bg/subtle`.
- **Size:** `.frame(maxWidth: .infinity, minHeight: 48, alignment: .leading)` around the padded content. No fixed height, no 360 / 328 widths (D15). Check iPhone SE (375 pt) to Pro Max (440 pt).
- **Dynamic Type:** primary and secondary scale with their text styles (`typography.md` §3) and wrap without line limit; the row grows. Glyph sizes stay fixed. At accessibility sizes (`dynamicTypeSize.isAccessibilitySize`) move the trailing meta under the text column so the primary keeps its width; the chevron / switch stays trailing and vertically centred. Check Hindi and English at xxxLarge (fully usable) and accessibility3 (no clipping or overlap).
- **VoiceOver:** §6. One element per row: a `Button` label already merges its children; for information rows use `.accessibilityElement(children: .combine)`. Add `.accessibilityAddTraits(.isSelected)` for selected rows and chosen radios, `.accessibilityValue(…)` for checkbox rows. Switch rows use the toggle trait recipe in `wiom-ios-selection-controls` (native toggle accessibility representation on iOS 16+). Indicators inside a row get `.accessibilityHidden(true)`.
- **Hit area:** the whole row, `.contentShape(Rectangle())` over the full width and height (≥ 48 pt tall, D14). The embedded control never has its own hit area inside a row.
- **Motion:** selected background (`bg/selected`) fades in and out with `Wiom.Motion.microStandard`, together with the row’s radio/checkbox (D28). The tap commits immediately. Pressed `bg/subtle` stays instant on a separate layer; selected wins over pressed. Fade from `Wiom.Colors.bgSelected.opacity(0)` to `Wiom.Colors.bgSelected`, never from `.clear`. Reduce Motion retains the fade. The embedded switch’s thumb uses the same selection timing; Reduce Motion removes its slide. No row insert/remove animation is defined here.
- **Safe areas and keyboard:** rows sit in the host's content area; the host keeps them inside the horizontal safe area and keeps the last row clear of the home indicator (`layout.md`). A full-bleed list lets the pressed / selected fill run edge to edge of the host while the content keeps `space/16`. Rows don't interact with the keyboard.
- **Haptics:** none (D21), including on switch and checkbox rows.
- **Not on iOS:** ripple, hover, keyboard focus ring, Android 360-wide frame, SF Symbol chevron (`chevron.right` is banned; use Material Rounded `chevron_right`, asset `ic_rounded_chevron_right`, D4), system `List` / `Form` cell chrome (insets, separators, disclosure indicator, grouped style).

### Row button style (pressed → `bg/subtle`, selected → `bg/selected`)

**Built from:** `Button` with a custom `ButtonStyle`: the label fills the width, minimum 48 pt, full-row content shape. The background has two layers: pressed `bg/subtle` (instant, never animated, only when enabled and not selected) and selected `bg/selected`, fading between the colour and the same colour at opacity 0 on `Wiom.Motion.microStandard` (D28).

### Row content (shared by every type)

**Built from:** an `HStack` (`space/12`) of leading (hidden from VoiceOver), a text column (`space/4`: primary `type/body/lg` in `text/default`; secondary and meta `type/body/sm` in `text/subtle`; `text/disabled` when disabled) and trailing (meta and trailing glyph, `space/8`). At accessibility text sizes the meta moves under the text column. Row padding `space/16`. Glyphs use the template chain in `wiom-ios-foundations` `icons.md`.

### Assembling the types

- **Navigation row:** `Button` + row content + `chevron_right` (`icon/brand`; `icon/disabled` when disabled).
- **Radio row:** the row owns the tap; the radio is indicator only; the row gets the `.isSelected` trait.
- **Checkbox row:** the row toggles (unchecked or mixed → checked; checked → unchecked); value checked / not checked / mixed from the catalog.
- **Information row:** not a button; one combined VoiceOver element, minimum 48 pt.

The switch row is a `Toggle` with a row-drawing `ToggleStyle`; its code and the VoiceOver toggle-trait recipe live in `wiom-ios-selection-controls` (Switch, "Switch row").

`wiomGlyph` is only a local wrapper of the `icons.md` §3 chain; if the module ships its own helper, use that.

### Common mistakes

- `Toggle` / checkbox `Button` placed inside a tappable row: two tap targets, two VoiceOver stops. Make the row the control.
- `.lineLimit(1)` on primary or secondary: clips Hindi and large text. Let it wrap.
- `.frame(height: 56)`: clips at large text sizes. Use `minHeight: 48`.
- `.opacity(0.38)` for disabled: use the disabled tokens.
- `Divider()` between rows: rows separate by padding.
- `List` with `.listStyle(.insetGrouped)`: system chrome and insets differ from Android. Use `LazyVStack(spacing: 0)` / `VStack(spacing: 0)` in a `ScrollView`.
- `Image(systemName: "chevron.right")`: SF Symbols are banned (D4).
