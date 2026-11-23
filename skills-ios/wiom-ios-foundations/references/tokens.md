# Tokens: every DS V2 value, with its Swift name

**Contents:** 1 Colour primitives · 2 Semantic colours · 3 Spacing · 4 Radius · 5 Border width · 6 Shadow · 7 Icon size · 8 Opacity and scrim · 9 Contrast table · 10 Not on iOS

Values match the Android library (`wiom-ds-android`, `foundation/`) so both apps render the same colours. Where Figma differs, see `IOS_DECISIONS.md` D1. Live read on 22 Nov 2026: Figma `text/subtle` is #665E75; Android and iOS retain #5C5570. **Hex values are confined to foundations and the iOS decisions contract.** Component skills cite token names.

Colours ship as asset-catalog colour sets (sRGB, one "Any" appearance; D23), named by the DS V2 path, e.g. `bg/brand/subtle`, and exposed as `Wiom.Colors.bgBrandSubtle`.

---

## 1. Colour primitives (internal: never used in feature code)

Exposed only inside the design-system module (`Wiom.Palette`, `internal`).

| Family | 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 950 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Neutral | #FAF9FC | #F1EDF7 | #E8E4F0 | #D7D3E0 | #A7A1B2 | #898296 | #736C82 | **#5C5570** | #473F55 | #352D42 | #161021 |
| Gray | #FFFFFF | #F5F6F7 | #EBEDF0 | #B6B9BF | #9FA1A7 | #84868A | #6E7074 | #595B5E | #424446 | #2A2B2D | #121314 |
| Brand | n/a | #FFE5F6 | #FFCCED | #FFB2E4 | #FF66C9 | #EA5DB8 | **#D9008D** | #C00080 | #A30070 | #443152 | n/a |
| Positive | n/a | #E1FAED | #C9F0DD | #A5E5C6 | #66B588 | #409B66 | #008043 | #0B6D3A | #06522A | #033519 | n/a |
| Critical | n/a | #FFE5E7 | #FFCCD0 | #FFB3B9 | #F07778 | #E2484B | #D92130 | #BF1D2A | #A31824 | #5C0005 | n/a |
| Warning (gold, never orange) | n/a | #FFE9A1 | #FED461 | #E2B203 | #C59C17 | #A48111 | #896C0D | #705708 | #544105 | #372902 | n/a |
| Info (purple) | n/a | #F1E5FF | #E4CCFF | #D6B2FF | #AF81FF | #965AFD | #6D17CE | #5600A9 | #3C007C | #23004E | n/a |

**Step-name trap:** these step numbers are DS V2's. The old iOS `neutral900` (#161021) is DS V2 `Neutral/950`; the old `neutral800` (#352D42) is `Neutral/900`. Map by hex, never by step name.

---

## 2. Semantic colours

Four namespaces matched to what they colour. Never cross them (`bg/*` is never a text colour).

| Namespace | SwiftUI slot |
|---|---|
| `bg/*` | `.background(…)`, shape `.fill(…)` |
| `text/*` | `.foregroundColor(…)` on `Text` |
| `stroke/*` | `.strokeBorder(…)`, `.overlay(RoundedRectangle(…).strokeBorder(…))`, dividers |
| `icon/*` | `.foregroundColor(…)` on a template `Image` |

### 2.1 Background

| Token | Swift | Value ← primitive | Use |
|---|---|---|---|
| `bg/default` | `bgDefault` | #FAF9FC ← Neutral/50 | Page, card, input, sheet, dialog |
| `bg/subtle` | `bgSubtle` | #F1EDF7 ← Neutral/100 | Section cards, list-row pressed, shimmer base |
| `bg/muted` | `bgMuted` | #E8E4F0 ← Neutral/200 | Grouped sections, skeleton fills |
| `bg/disabled` | `bgDisabled` | #D7D3E0 ← Neutral/300 | Disabled component fill |
| `bg/inverse` | `bgInverse` | #161021 ← Neutral/950 | Dark hero, preview, footer |
| `bg/selected` | `bgSelected` | #FFCCED ← Brand/200 | Active chip, current row, selected tab |
| `bg/brand/subtle` | `bgBrandSubtle` | #FFE5F6 ← Brand/100 | Soft brand surface; Secondary and Tertiary CTA pressed fill |
| `bg/brand/bold` | `bgBrandBold` | #443152 ← Brand/900 | Premium header surface (non-action) |
| `bg/brand` | `bgBrand` | #D9008D ← Brand/600 | Primary CTA fill |
| `bg/brand/pressed` | `bgBrandPressed` | #A30070 ← Brand/800 | Primary CTA pressed |
| `bg/brand/accent` | `bgBrandAccent` | #FF66C9 ← Brand/400 | Pre-booking CTA fill (customer app only) |
| `bg/brand/accent/pressed` | `bgBrandAccentPressed` | #EA5DB8 ← Brand/500 | Pre-booking CTA pressed |
| `bg/positive/subtle` | `bgPositiveSubtle` | #E1FAED ← Positive/100 | Success banner, card |
| `bg/positive` | `bgPositive` | #008043 ← Positive/600 | Solid success fill (badge) |
| `bg/critical/subtle` | `bgCriticalSubtle` | #FFE5E7 ← Critical/100 | Error banner, card |
| `bg/critical` | `bgCritical` | #D92130 ← Critical/600 | Destructive CTA fill |
| `bg/critical/pressed` | `bgCriticalPressed` | #A31824 ← Critical/800 | Destructive CTA pressed |
| `bg/warning/subtle` | `bgWarningSubtle` | #FFE9A1 ← Warning/100 | Warning banner, card |
| `bg/warning` | `bgWarning` | #E2B203 ← Warning/300 | Solid warning fill (badge) |
| `bg/info/subtle` | `bgInfoSubtle` | #F1E5FF ← Info/100 | Info banner, card |
| `bg/info` | `bgInfo` | #6D17CE ← Info/600 | Solid info fill (badge) |

### 2.2 Text

| Token | Swift | Value ← primitive | Use |
|---|---|---|---|
| `text/default` | `textDefault` | #161021 ← Neutral/950 | Reading text on light surfaces (not warning surfaces) |
| `text/subtle` | `textSubtle` | #5C5570 ← Neutral/700 | Descriptions, metadata, helper text |
| `text/disabled` | `textDisabled` | #A7A1B2 ← Neutral/400 | Disabled text **and** input placeholder (no `text/placeholder` exists) |
| `text/inverse` | `textInverse` | #FAF9FC ← Neutral/50 | Text on `bg/inverse`, `bg/brand/bold` |
| `text/selected` | `textSelected` | #D9008D ← Brand/600 | Selected tab label, active chip |
| `text/brand` | `textBrand` | #D9008D ← Brand/600 | Secondary/Tertiary CTA label, inline link |
| `text/onBrand` | `textOnBrand` | #FFFFFF ← Gray/50 | Label on `bg/brand` |
| `text/onBrandAccent` | `textOnBrandAccent` | #161021 ← Neutral/950 | Label on `bg/brand/accent` (dark: white fails) |
| `text/critical` | `textCritical` | #D92130 ← Critical/600 | Error heading, inline error, required asterisk |
| `text/onCritical` | `textOnCritical` | #FFFFFF ← Gray/50 | Label on `bg/critical` |
| `text/positive` | `textPositive` | #008043 ← Positive/600 | Success heading |
| `text/onPositive` | `textOnPositive` | #FFFFFF ← Gray/50 | Text on `bg/positive` |
| `text/onWarning` | `textOnWarning` | #372902 ← Warning/900 | **The** warning text token: on `bg/warning`, `bg/warning/subtle`, and inline on `bg/default`. No `text/warning` exists. |
| `text/info` | `textInfo` | #6D17CE ← Info/600 | Info heading, info link |
| `text/onInfo` | `textOnInfo` | #FFFFFF ← Gray/50 | Text on `bg/info` |

### 2.3 Stroke (colour)

| Token | Swift | Value ← primitive | Use |
|---|---|---|---|
| `stroke/subtle` | `strokeSubtle` | #D7D3E0 ← Neutral/300 | Card outline, input rest border |
| `stroke/default` | `strokeDefault` | #E8E4F0 ← Neutral/200 | Inner-card divider |
| `stroke/strong` | `strokeStrong` | #473F55 ← Neutral/800 | Checkbox / radio / switch rest border |
| `stroke/selected` | `strokeSelected` | #D9008D ← Brand/600 | Selected card / chip border |
| `stroke/brand` | `strokeBrand` | #FFB2E4 ← Brand/300 | Soft decorative brand border |
| `stroke/brand/focus` | `strokeBrandFocus` | #D9008D ← Brand/600 | Secondary CTA border; **active (editing) input** border |
| `stroke/positive` | `strokePositive` | #A5E5C6 ← Positive/300 | Success card outline |
| `stroke/positive/focus` | `strokePositiveFocus` | #008043 ← Positive/600 | Saturated positive border |
| `stroke/critical` | `strokeCritical` | #FFB3B9 ← Critical/300 | Soft error outline |
| `stroke/critical/focus` | `strokeCriticalFocus` | #D92130 ← Critical/600 | Invalid-input border |
| `stroke/warning` | `strokeWarning` | #E2B203 ← Warning/300 | Warning outline, inside `bg/warning/subtle` only |
| `stroke/info` | `strokeInfo` | #D6B2FF ← Info/300 | Info card outline |
| `stroke/info/focus` | `strokeInfoFocus` | #6D17CE ← Info/600 | Saturated info border |

On iOS the `*/focus` strokes are used for **state borders** (active input, invalid input, Secondary CTA). They are never drawn as keyboard focus rings (§10).

### 2.4 Icon (colour)

| Token | Swift | Value ← primitive | Use |
|---|---|---|---|
| `icon/action` | `iconAction` | #352D42 ← Neutral/900 | Tappable chrome: back, close, filter, overflow; also dark Warning glyphs on bg/warning/subtle or bg/warning (D31), without making them tappable |
| `icon/nonAction` | `iconNonAction` | #898296 ← Neutral/500 | Decorative / non-tappable |
| `icon/inverse` | `iconInverse` | #FAF9FC ← Neutral/50 | On dark surfaces; inside Primary/Destructive CTAs |
| `icon/brand` | `iconBrand` | #D9008D ← Brand/600 | Secondary/Tertiary CTA icon, selected nav |
| `icon/positive` | `iconPositive` | #008043 ← Positive/600 | Success |
| `icon/critical` | `iconCritical` | #D92130 ← Critical/600 | Error |
| `icon/warning` | `iconWarning` | #E2B203 ← Warning/300 | Rating stars only (D31). Never a Warning status glyph. |
| `icon/info` | `iconInfo` | #6D17CE ← Info/600 | Info |
| `icon/disabled` | `iconDisabled` | #A7A1B2 ← Neutral/400 | Disabled icon |

### 2.5 Chat

| Token | Swift | Value ← primitive | Use |
|---|---|---|---|
| `chat/bg/userBubble` | `chatBgUserBubble` | #FFFFFF ← Gray/50 | User bubble |
| `chat/bg/canvas` | `chatBgCanvas` | #F5F6F7 ← Gray/100 | Chat screen background |
| `chat/bg/systemBubble` | `chatBgSystemBubble` | #EBEDF0 ← Gray/200 | System / agent bubble |
| `chat/stroke/replyAccent` | `chatStrokeReplyAccent` | #B6B9BF ← Gray/300 | Reply-preview accent bar (2 pt) |

---

## 3. Spacing (4 pt grid)

| Token | Swift | pt | Typical use |
|---|---|---|---|
| `space/4` | `Wiom.Spacing.s4` | 4 | Icon ↔ text inside a chip |
| `space/8` | `s8` | 8 | Title ↔ subtitle, icon ↔ label in a button |
| `space/12` | `s12` | 12 | CTA vertical padding, chat gutter |
| `space/16` | `s16` | 16 | **Screen gutter**, card padding, between cards, sheet padding |
| `space/24` | `s24` | 24 | Dialog padding, section gap |
| `space/32` | `s32` | 32 | Between content sections, content → CTA |
| `space/40` | `s40` | 40 | Loose section gap |
| `space/48` | `s48` | 48 | Default hit-area size |
| `space/64` | `s64` | 64 | Hero spacing |
| `space/72` | `s72` | 72 | Hero spacing |
| `space/84` | `s84` | 84 | Hero spacing |

`space/1` and `space/2` are **not tokens** on iOS (they are not Figma variables). Hairlines use `Wiom.BorderWidth.small`. Need something else? It is a gap (D24).

Hierarchy: 8–12 = one unit · 16–24 = same section · 32+ = separate sections.

---

## 4. Radius

Corner style is **circular** everywhere (`RoundedRectangle(cornerRadius:style: .circular)`), never `.continuous` (D3).

| Token | Swift | pt | Use |
|---|---|---|---|
| `radius/none` | `Wiom.Radius.none` | 0 | Top bar, full-bleed images |
| `radius/tiny` | `tiny` | 4 | Badges, tags, checkbox box |
| `radius/small` | `small` | 8 | Small containers, toast |
| `radius/medium` | `medium` | 12 | Inputs, nested containers |
| `radius/large` | `large` | **16** | Buttons, cards (the old iOS `WiomRadius.large` was 24: don't carry it over) |
| `radius/xlarge` | `xlarge` | 24 | Dialogs, bottom sheets (top corners) |
| `radius/full` | `full` | n/a | Pills, avatars, radios, switch: use `Capsule()` / `Circle()`, not 9999 |

Nested: inner radius = outer radius − padding (16 outer + 4 padding → 12 inner).

---

## 5. Border width

Separate from `stroke/*` colours (Figma uses `stroke/small` for both a width and a colour group; Swift doesn't).

| Token | Swift | pt | Use |
|---|---|---|---|
| `stroke/small` (width) | `Wiom.BorderWidth.small` | 1 | Dividers, card outlines, input rest border |
| `stroke/medium` (width) | `Wiom.BorderWidth.medium` | 2 | Secondary CTA, checkbox/radio, active/invalid input, selected card |

Borders sit **inside** the shape (`.strokeBorder`, not `.stroke`). Solid only; dashed only for empty upload zones.

---

## 6. Shadow

Black at 15 %, no spread. SwiftUI's shadow `radius` is about half the CSS blur.

| Token | Swift | CSS spec | SwiftUI |
|---|---|---|---|
| `shadow/none` | `.none` | none | no modifier |
| `shadow/sm` | `.sm` | 0 1 3 0 | `.shadow(color: .black.opacity(0.15), radius: 1.5, x: 0, y: 1)` |
| `shadow/md` | `.md` | 0 2 6 0 | `radius: 3, y: 2` |
| `shadow/lg` | `.lg` | 0 4 12 0 | `radius: 6, y: 4` |
| `shadow/xl` | `.xl` | 0 8 24 0 | `radius: 12, y: 8` |

Apply with `.wiomShadow(.md)` on the **shape's background**, not on a container of text (shadowing text views shadows every glyph). Rules: a component has a border **or** a shadow, never both; `shadow/xl` only with `overlay/scrim` (dialogs); max 1–2 `shadow/lg` per screen. Bottom sheet = `shadow/md` (see `wiom-ios-bottomsheet`).

---

## 7. Icon size

| Token | Swift | Glyph pt | Use |
|---|---|---|---|
| `icon/xs` | `Wiom.IconSize.xs` | 16 | Restricted: inline indicators, input trailing |
| `icon/sm` | `sm` | 20 | Button icons, compact controls |
| `icon/md` | `md` | 24 | **Default**: top bar, list, nav, chips |
| `icon/lg` | `lg` | 48 | Empty states, hero |

Hit areas are a layout rule, not an icon size: `layout.md` §4.

---

## 8. Opacity and scrim

| Token | Value | Use |
|---|---|---|
| `overlay/scrim` | #161021 at 50 % (`Wiom.Colors.overlayScrim`) | The only scrim: dialogs, bottom sheets, full-screen loaders. Replaces the old iOS black 32 / 50 / 80 % scrims. |
| Disabled, non-neutral | 40 % opacity of the base colour | Only for Brand/Positive/Critical/Warning/Info colours with no disabled token. Never on Neutral tokens. CTAs use token swaps, not opacity. |

---

## 9. Contrast table (WCAG 2.1, computed from the values above)

| Pair | Ratio | Verdict |
|---|---|---|
| `text/default` on `bg/default` | 17.71 | AAA |
| `text/subtle` on `bg/default` | 6.70 | AA |
| `text/subtle` on `bg/subtle` | 6.09 | AA |
| `text/brand` on `bg/default` | 4.62 | AA (not 8.4 as the Android skill says) |
| `text/onBrand` on `bg/brand` | 4.84 | AA |
| `text/onBrandAccent` on `bg/brand/accent` | 7.07 | AA |
| `text/onCritical` on `bg/critical` | 4.99 | AA |
| `text/critical` on `bg/default` | 4.75 | AA |
| `text/critical` on `bg/critical/subtle` | 4.18 | Large text / headings only |
| `text/positive` on `bg/positive/subtle` | 4.58 | AA |
| `text/onWarning` on `bg/warning` | 7.16 | AA |
| `text/onWarning` on `bg/warning/subtle` | 11.77 | AAA (not 8.76) |
| `text/onWarning` on `bg/default` | 13.52 | AAA |
| `text/info` on `bg/info/subtle` | 6.53 | AA |
| `text/inverse` on `bg/brand/bold` | 11.08 | AAA |
| `icon/action` on `bg/default` | 12.47 | Pass (graphics 3:1) |
| `icon/nonAction` on `bg/default` | 3.51 | Pass (graphics 3:1) |
| `stroke/strong` on `bg/default` | 9.49 | Pass |
| `stroke/brand/focus` on `bg/default` | 4.62 | Pass |

**Known failures, recorded as accepted exceptions pending a design-team ruling (IOS_DECISIONS Q5).** Don't "fix" them locally: colours stay identical to Android.

| Pair | Ratio | Where it appears | iOS mitigation |
|---|---|---|---|
| `stroke/subtle` on `bg/default` | 1.40 | Input rest border, card outline | The input's label and placeholder identify the field; never rely on the border alone |
| `icon/warning` on `bg/default` | 1.89 | Rating stars only | D31 prohibits this pairing for Warning indicators; the rating host carries a spoken value. |
| `icon/warning` on `bg/warning/subtle` | 1.64 | Historical Warning pairing, prohibited by D31 | Use icon/action on the Warning surface; no gold-on-tint exception. |
| `text/brand` on `bg/brand/subtle` | 4.10 | Pressed Secondary/Tertiary CTA | Transient state only; never as resting text |
| `text/selected` on `bg/selected` | 3.49 | Selected chip / tab label | Selection also carried by `.isSelected` and, where the component has one, a border |
| `text/brand` on `bg/inverse` | 3.84 | n/a | **Not allowed.** Use `text/inverse` on dark surfaces (D26) |
| `text/disabled` on `bg/default` | 2.39 | Placeholder | Intentional: placeholders are examples, the label is the field's name |
| `text/disabled` on `bg/disabled` | 1.70 | Disabled CTA | Intentional: disabled is "not available", and VoiceOver says "dimmed" |

---

## 10. Not on iOS

| Token | Why |
|---|---|
| `bg/brand/hover`, `bg/brand/accent/hover`, `bg/critical/hover`, `text/brand/hover` | No hover on iPhone |
| Keyboard focus ring (component radius + 2 pt, outside) | Not an iPhone idiom; `*/focus` strokes are used only as state borders |
| `bg/surface` (#FFFFFF, Figma only) | Not on Android; not used (IOS_DECISIONS Q3) |
| Paint style `Brand/Bold` #4A1434 (Figma only) | Probably stale; not used |
| Old iOS blue info ramp (#1461CC family), orange warning, yellow caution | Mapped to `info` (purple) and `warning` (gold) families (D22) |


D31 final Warning and rating combinations: [warning-combinations.md](warning-combinations.md). Existing token values are unchanged; usage is finalised.
