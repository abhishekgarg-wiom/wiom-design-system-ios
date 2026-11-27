---
name: wiom-ios-input-fields
description: >
  Wiom input fields for the iOS customer app in SwiftUI: single-line Input,
  multi-line Textarea and the boxed OTP code field, plus the Input
  configurations for search bar, password, amount and the read-only picker
  trigger. Use when building or reviewing a SwiftUI text field, OTP or
  verification-code entry, search bar or picker trigger on iOS.
---

# Wiom input fields (iOS)

Three text-entry components for the customer app. They look exactly like the
Android components (`wiom-ios-foundations/references/decisions.md` §0); keyboard, focus, AutoFill,
VoiceOver and Dynamic Type behave the iOS way.

| Component | States drawn in design | Notes |
|---|---|---|
| Input | Default · Focused · Filled · Error · Success · Warning · Disabled · Read-only | Search, password, amount, phone and picker trigger are configurations of Input |
| Textarea | Default · Focused · Filled · Error · Success · Disabled | Grows with content. No icon, prefix or suffix slots |
| OTP | Default · Focused · Filled · Error · Success · Disabled | 4 boxes (default) or 6. One text field underneath, drawn as boxes |

- **Search bar is an Input**: leading `search` icon, trailing `cancel` icon only while there is a query.
- **Picker trigger is an Input** in Read-only with a trailing `keyboard_arrow_down` chevron. Tapping it opens a **`wiom-ios-bottomsheet` picker** (rows from `wiom-ios-list-item`). There is no separate dropdown component.

Tokens are cited by DS V2 name; values live in `wiom-ios-foundations` (`tokens.md`, `typography.md`). Swift names follow `wiom-ios-foundations/references/decisions.md` §2.

## 1. Anatomy

All three share one column: **Title → field → helper row**, `space/8` between rows.

### Input

```
Title                                         type/label/lg
   space/8
┌── wrap: radius/medium · padding space/16 H, space/12 V ─────────┐
│ [lead 20]  prefix  value / placeholder  suffix  [trail 20]      │
└── space/12 between adjacent slots ──────────────────────────────┘
   space/8
Helper text (wraps)                                  0 / 100      type/body/md
```

| Part | Token |
|---|---|
| Width | Fills the surface width minus its gutter (never a fixed number) |
| Wrap radius | `radius/medium` (circular corners, D3) |
| Wrap padding | `space/16` horizontal, `space/12` vertical |
| Slot gap | `space/12` |
| Row gap (title, wrap, helper) | `space/8` |
| Title | `type/label/lg` |
| Value, placeholder, prefix, suffix | `type/body/lg` |
| Value line minimum | one `type/body/lg` line (24 pt at default size) |
| Helper and counter | `type/body/md`, helper ↔ counter gap `space/12` |
| Leading and trailing icon | `icon/sm` (20 pt), Material Rounded (D4) |

Wrap height = `space/12` + value line + `space/12`: **48 pt minimum** at the default text size, growing with Dynamic Type. Never fixed.

Helper row renders only when there is helper or counter text. Counter is right-aligned, single line; helper takes the remaining width and wraps.

### Textarea

Same as Input without icon, prefix and suffix slots. Value aligns to the **top** of the wrap so the placeholder sits on the first line, not the vertical middle. Minimum three lines (Android `minLines = 3`); grows with content.

### OTP

```
Title                                         type/label/lg
   space/8
┌──┐ space/8 ┌──┐ ┌──┐ ┌──┐                    4 boxes (default), or 6
│ 4│         │ 8│ │  │ │  │                    digits type/label/lg, centred
└──┘         └──┘ └──┘ └──┘
   space/8
Sent to your number                    00:24   type/body/md, timer optional
```

| Part | Token |
|---|---|
| Box width | Equal share of the row width after `space/8` gaps (flex, never 76/48) |
| Box padding | `space/12` all sides; height 48 pt minimum |
| Box radius | `radius/medium` |
| Digit | `type/label/lg` (SemiBold, so each digit reads as a discrete token) |
| Active box border | `stroke/medium` · `stroke/brand/focus` |
| Resting box border | `stroke/small` · `stroke/subtle` |
| Helper and timer | `type/body/md`; timer right-aligned in the helper row |

The resend timer lives in the OTP helper row. Never add a counter or a separate chip for it.

## 2. Pick the right component

```
Single line (text, phone, amount, password, name)?   → Input
Search across a list or screen?                       → Input + leading search, trailing cancel while query present
Multi-line (address, reason, feedback)?               → Textarea
4- or 6-digit verification code?                      → OTP
Choose from a list?                                   → Input, Read-only + chevron, opens a wiom-ios-bottomsheet picker
Value to show and copy, not edit (customer ID)?       → Input, Read-only, no chevron
```

Never draw a custom field. Never fake OTP with an Input holding spaced digits.

## 3. States and tokens

Status (none / error / success / warning), enabled and read-only are **three independent axes**: a read-only field can also be in error.

| State | Wrap fill | Border | Title | Value | Helper | Trailing |
|---|---|---|---|---|---|---|
| Default (empty, not editing) | `bg/default` | `stroke/small` · `stroke/subtle` | `text/default` | placeholder `text/disabled` | `text/subtle` | caller's icon |
| Focused (editing) | `bg/default` | `stroke/medium` · `stroke/brand/focus` | `text/subtle` | `text/default` | `text/subtle` | caller's icon |
| Filled (has value, not editing) | `bg/default` | `stroke/small` · `stroke/subtle` | `text/subtle` | `text/default` | `text/subtle` | caller's icon |
| Error | `bg/default` | `stroke/medium` · `stroke/critical/focus` | `text/subtle`* | `text/default` | `text/critical` | `error` · `icon/critical` |
| Success | `bg/default` | `stroke/medium` · `stroke/positive/focus` | `text/subtle`* | `text/default` | `text/positive` | `check_circle` · `icon/positive` |
| Warning (Input) | `bg/default` | `stroke/medium` · `stroke/warning` | `text/subtle`* | `text/default` | `text/onWarning` | `warning` · `icon/action` in an Icon Badge Sm (24 pt circle, 16 pt glyph, `bg/warning/subtle`; D31, D35) |
| Disabled | `bg/disabled` | `stroke/small` · `stroke/subtle` | `text/disabled` | `text/disabled` | `text/disabled` | `icon/disabled` |
| Read-only | `bg/subtle` | `stroke/small` · `stroke/subtle` | `text/subtle` | `text/default` | `text/subtle` | chevron `icon/action` for a picker |

\* Title follows the label ramp below; with a status it is normally filled, so `text/subtle`.

Other tokens: prefix and suffix `text/subtle` (`text/disabled` when disabled); counter `text/subtle`; leading icon `icon/nonAction`; caller's trailing icon `icon/action`; cursor `text/default`.

**Border priority:** disabled > error > success > warning > focused > rest. A focused field in error keeps the critical border.

**Label ramp (as Android ships it).** The title is always `type/label/lg`; only its colour changes: `text/default` while the field is empty and not being edited, `text/subtle` once it is focused, filled or read-only, `text/disabled` when disabled. The border darkens at the same moment (rest → `stroke/brand/focus`). Weight does not change (see Open questions).

**Status icons win the trailing slot.** In Error, Success and Warning the status icon replaces the caller's trailing icon (including clear and show-password) and is not tappable.

**Warning** helper uses `text/onWarning`; there is no `text/warning`. Warning is a nudge, never a substitute for Error.

### OTP states

| State | Resting boxes | Active box (only while editing) | Helper |
|---|---|---|---|
| Default / Filled | `stroke/small` · `stroke/subtle` on `bg/default` | `stroke/medium` · `stroke/brand/focus` | `text/subtle` |
| Error | `stroke/medium` · `stroke/critical/focus` | `stroke/medium` · `stroke/brand/focus` | `text/critical` |
| Success | `stroke/medium` · `stroke/positive/focus` | `stroke/medium` · `stroke/brand/focus` | `text/positive` |
| Disabled | `stroke/small` · `stroke/subtle` on `bg/disabled`, digits `text/disabled` | none | `text/disabled` |

Active box = the next empty position (`code.count`), clamped to the last box once full. No box is active when the field is not being edited. OTP has no Warning or Read-only.

## 4. Surface contract

Fields fill the width; the surface owns the gutter (`wiom-ios-foundations` `layout.md`).

| Host | Gutter owned by host |
|---|---|
| Screen content | `space/16` |
| Wiom dialog (`wiom-ios-dialog`) | `space/24` |
| Wiom bottom sheet, Form size (`wiom-ios-bottomsheet`) | `space/24` inside the form body; action bar keeps `space/16` |

Check every form from iPhone SE (375 pt) to Pro Max (440 pt), in Hindi and English.

## 5. Rules

1. **Affixes go in the prefix / suffix slot**, never typed into the value. `+91`, `₹`, `.00` are non-editable text beside the value; the bound string holds only what the user typed.
2. **Error helper must say what is wrong and how to fix it.** Error with no helper is not allowed.
3. **Read-only ≠ Disabled.** Read-only is readable and copyable (`text/default` value, `bg/subtle`). Disabled is inactive (`text/disabled`, `bg/disabled`) and cannot be copied.
4. **One trailing icon at a time.** Status icons take over the slot.
5. **Keep the title.** Hide it only when a section header directly above already labels the field. A placeholder is not a label: it disappears on the first keystroke.
6. **Counter only where a limit helps** (Textarea, long free text). Count in grapheme clusters (`String.count`), so "क्षि" is 1. Never on OTP.
7. **Don't recolour the title per instance.** The ramp is state-driven.
8. **No fixed heights.** Wraps, boxes and rows have minimums; text wraps or the field grows.
9. **Tokens only.** No hex, no eyedropped colours. Missing token: report it (D24).
10. Copy in this file is illustrative. Real copy comes from the string catalog (Hindi first, English sentence case).

## 6. Keyboard per field

Every editable field is bound to a `@FocusState` owned by the screen. "Next" moves focus to the next field in reading order; the last field's Return submits (same action as the primary CTA) or dismisses the keyboard.

| Field | `keyboardType` | `textContentType` | Return (`.submitLabel`) | Next field | Autocorrect / autocapitalisation |
|---|---|---|---|---|---|
| Phone (`+91` prefix) | `.numberPad` | `.telephoneNumber` | No Return key on a number pad: the CTA riding the keyboard is the action | Focus moves on CTA tap, never on reaching 10 digits | Off / `.never` |
| OTP | `.numberPad` | `.oneTimeCode` | None; the screen may verify as soon as all digits are in | n/a | Off / `.never` |
| Name | `.default` | `.name` (or `.givenName` / `.familyName`) | `.next`, `.done` on the last field | Yes | Off / `.words` |
| Amount (`₹` prefix, `.00` suffix) | `.numberPad` | none | None (number pad); CTA is the action | Via CTA | Off / `.never` |
| Address (Textarea) | `.default` | `.fullStreetAddress` (or `.streetAddressLine1`, `.postalCode` for split fields) | Return inserts a new line | Tap next field or CTA | On / `.sentences` |
| Pincode | `.numberPad` | `.postalCode` | None; CTA | Via CTA | Off / `.never` |
| Search | `.default` | none | `.search` | n/a | Off / `.never` |
| Password | `.default` (`.asciiCapable` if Latin-only) | `.password` (`.newPassword` when creating) | `.go` or `.done` | Last field | Off / `.never` |

- **Phone:** filter to digits and keep the **last 10** so AutoFill of "+91 98765 43210" lands as 10 digits; the `+91` prefix stays drawn, never inserted.
- **Digits:** accept any script's digits (`Character.wholeNumberValue`) and store ASCII, so a Devanagari number pad still works.
- **Amount:** digits only (the `.00` suffix means whole rupees). If paise are ever needed, use `.decimalPad` and drop the suffix.
- Don't use the UIKit system clear button (`clearButtonMode`); the Wiom `cancel` icon is the clear control.

## 7. Keyboard avoidance and scrolling

- Forms live in a `ScrollView`. The sticky CTA bar (`wiom-ios-cta`) sits in `.safeAreaInset(edge: .bottom)` so it rides on the keyboard with `space/12` below the button (D19).
- When a field gains focus, scroll so the **whole field, including its helper / error row**, sits above the keyboard plus the CTA bar. SwiftUI only guarantees the caret; tag the whole field column with an `id` and scroll to it.
- When an error appears under a focused field, scroll again so the error is visible.
- `.scrollDismissesKeyboard(.interactively)` (iOS 16) on the form; tapping outside a field does not need to dismiss.

```swift
// Read @Environment(\.accessibilityReduceMotion) var reduceMotion in the host.
ScrollViewReader { proxy in
    ScrollView {
        VStack(spacing: Wiom.Spacing.s16) {
            WiomInput(title: titlePhone, text: $phone, prefix: "+91", helper: phoneHelper,
                      status: phoneStatus, focus: $focus, equals: .phone)
                .id(Field.phone)               // id covers title + wrap + helper
            // ...
        }
        .padding(.horizontal, Wiom.Spacing.s16)
    }
    .scrollDismissesKeyboard(.interactively)
    .onChange(of: focus) { field in            // iOS 16 one-argument form
        guard let field else { return }
        if reduceMotion { proxy.scrollTo(field, anchor: .bottom) }
        else { withAnimation(Wiom.Motion.microStandard) { proxy.scrollTo(field, anchor: .bottom) } }
    }
    .safeAreaInset(edge: .bottom) { stickyCTABar }
}
```

## 8. Configurations

Swift shapes are illustrative; the module API may differ, the behaviour must not.

```swift
enum WiomInputStatus { case none, error, success, warning }
```

**Phone.** Input · prefix `+91` · `.numberPad` · `.telephoneNumber` · helper (illustrative) "We'll send a code to this number". Error helper: "Enter a 10-digit mobile number".

**Search.** Input · no title (the screen title labels it) · leading `search` (`icon/nonAction`) · trailing `cancel` only while the query is non-empty; tapping it clears the query and keeps focus. `.submitLabel(.search)`.

**Password.** Input · trailing `visibility` / `visibility_off` toggle. Keep a `SecureField` and a `TextField` stacked and switch which is visible, both bound to the same `@FocusState`, so toggling does not drop the keyboard. Preserve the bound value and caret when switching visibility; do not intentionally clear the password. Verify focus and AutoFill on device.

**Amount.** Input · prefix `₹` · suffix `.00` · `.numberPad` · helper "Includes 18% GST" (illustrative).

**Address.** Textarea · `TextField(_, text:, axis: .vertical)` with `.lineLimit(3...)` (iOS 16) · counter `n / 200` when a limit exists.

**Picker trigger.** Input · Read-only · trailing `keyboard_arrow_down` · the whole wrap is a `Button` (not a text field) that opens a `wiom-ios-bottomsheet` picker. Single-select: radio rows, selection closes the sheet. Multi-select: checkbox rows with a primary "Done" CTA; the trigger shows the selected values, truncating extra ones as "+N". Value `text/default`, placeholder `text/disabled`.

**Read-only copyable value** (customer ID, account number). Input · Read-only · no chevron · value rendered as `Text(value).textSelection(.enabled)` so long-press offers Copy. Never use Disabled for this.

### OTP: one hidden field, drawn as boxes

Never N separate fields. One `TextField` owns the whole code; the boxes are drawing only.

```swift
struct WiomOtp: View {
    let title: String
    @Binding var code: String
    var length = 4                                  // 4 or 6
    var status: WiomInputStatus = .none
    var helper: String? = nil
    var timer: String? = nil
    @FocusState private var editing: Bool
    @Environment(\.isEnabled) private var isEnabled

    var body: some View {
        VStack(alignment: .leading, spacing: Wiom.Spacing.s8) {
            Text(title)                             // type/label/lg, label ramp colour
            ZStack {
                HStack(spacing: Wiom.Spacing.s8) {
                    ForEach(0..<length, id: \.self) { i in box(i) }
                }
                .accessibilityHidden(true)
                TextField("", text: $code)
                    .keyboardType(.numberPad)
                    .textContentType(.oneTimeCode)
                    .focused($editing)
                    .foregroundColor(.clear).tint(.clear)   // no visible text or caret
                    .accessibilityLabel(title)
                    .accessibilityValue(otpValue)           // "2 of 6 digits entered"
            }
            .contentShape(Rectangle())
            .onTapGesture { editing = true }
            .onChange(of: code) { new in            // paste, AutoFill, typing, delete
                let digits = new.compactMap(\.wholeNumberValue).map(String.init).joined()
                let clamped = String(digits.prefix(length))
                if clamped != new { code = clamped }
            }
            // helper row: helper (wraps) + timer, see §1
        }
    }
}
```

- **SMS AutoFill** shows the code above the number pad; one tap fills every box. **Paste** fills every box. Normalise pasted digits and spaces before applying the length limit. Verify AutoFill replaces the complete code; prefix-clamping alone does not guarantee duplicate-insertion handling.
- **Delete** removes the last digit and the active box moves back one. Tapping any box focuses the one field. If the flow requires append/delete-at-end only, implement caret control in a `UITextField` wrapper; the illustrative SwiftUI field below does not enforce selection position. Never split into multiple fields.
- Box `i` is active when `editing && isEnabled && i == min(code.count, length - 1)`.
- On Error, keep the digits and the error helper; clearing for re-entry is the screen's choice. Move focus back to the field.
- Timer: `Text` in the helper row, updated by the screen. VoiceOver label is spoken form ("Resend in 24 seconds", illustrative); ticks are never announced.

## 9. Anti-patterns

- A custom `TextField` with a hand-drawn border instead of the component.
- OTP as N `TextField`s with focus chaining (breaks AutoFill, paste and delete), or as one Input with spaced digits.
- `+91` or `₹` concatenated into the bound string.
- Error shown by colour only, or Error with no helper.
- `text/warning` (doesn't exist) or a hand-picked orange.
- Placeholder used as the only label.
- Disabled used for a value the user should copy.
- A trailing icon with a 20 pt hit area.
- A fixed `.frame(height:)` on the wrap, the OTP boxes or the helper row.

## Open questions

1. **Label weight.** Android (`WiomInput.kt:224-228, 261`) and the source skill keep the title at `type/label/lg` and change colour only. An earlier design note described the label as Bold when empty and Regular when focused or filled. This skill follows what Android ships; design team to confirm, then Figma and Android change together.
2. **`+91` prefix vs phone icon.** This skill draws `+91` as a non-editable prefix (source skill). The Android README says not to prepend `+91` and to use a leading phone icon instead (`component/input/README.md:111-125`). Which one does the customer app ship on both platforms?
3. **Read-only title colour.** Source skill says `text/default`; Android ships `text/subtle` (`WiomInput.kt:226`). This skill follows Android.
4. **Leading icon tint.** Source skill code uses `icon/action`; Android ships `icon/nonAction` (`WiomInput.kt:254`). This skill follows Android.
5. **OTP status borders.** Android draws every resting box in the status colour on Error/Success and shows the active box only while editing (`WiomOtp.kt:95-113, 141-142`); the source skill's code draws only active/inactive and an active box whenever enabled. This skill follows Android.
6. **Warning border.** Android code uses `stroke/warning` (`WiomInput.kt:219`); the Android README table says `stroke.brandFocus` (`README.md:81`). This skill follows the code; README to be fixed.
7. **Textarea states.** Design draws six states; Android's `WiomTextarea` also accepts Warning and read-only (`WiomInput.kt:144-146`). Are those allowed in customer screens?
8. **DECIDED (D31): Warning status colour.** Dark `icon/action` on `bg/warning/subtle`, inside the neutral field. Gold `icon/warning` is ratings-only. The Warning status glyph remains non-tappable. Container: Icon Badge Sm, 24 pt circle, 16 pt glyph (D35). The separate Warning border contrast remains open; do not change helper text, field fill or border tokens under this icon ruling.
9. **Number-pad "Next".** Number pads have no Return key. This skill relies on the CTA riding the keyboard; if a form needs a "Next" between two numeric fields, does design want a keyboard accessory bar (system-styled)?

## iOS (SwiftUI, iOS 16+)

- **Built from:** Input = `TextField` (or `SecureField` for password) inside an `HStack` wrap drawn with `RoundedRectangle(cornerRadius:style: .circular)` fill + `strokeBorder`; editing state from `@FocusState`. Textarea = `TextField(axis: .vertical)` + `.lineLimit(3...)`. OTP = one hidden `TextField` (`.oneTimeCode`, `.numberPad`) under N drawn boxes. Picker trigger = `Button` with a custom `ButtonStyle` drawing the Read-only wrap. Read-only value = `Text` + `.textSelection(.enabled)`. Disabled = `.disabled(true)`.
- **Tokens:** `bg/default`, `bg/subtle`, `bg/disabled`; `stroke/subtle`, `stroke/brand/focus`, `stroke/critical/focus`, `stroke/positive/focus`, `stroke/warning`; `stroke/small`, `stroke/medium` (widths); `text/default`, `text/subtle`, `text/disabled`, `text/critical`, `text/positive`, `text/onWarning`; `icon/action`, `icon/nonAction`, `icon/critical`, `icon/positive`, `icon/disabled`; `icon/sm`; `radius/medium`; `space/8`, `space/12`, `space/16`; `type/label/lg`, `type/body/lg`, `type/body/md`. Swift: `Wiom.Colors.strokeBrandFocus`, `Wiom.BorderWidth.medium`, `Wiom.Typography.labelLg`, etc. (§2 naming).
- **Size:** wrap and OTP box 48 pt **minimum** at default text size (`space/12` + one line + `space/12`); Textarea min three lines; widths fill the host minus its gutter. Border is drawn inside (`strokeBorder`), so 1 → 2 pt does not shift layout.
- **Dynamic Type:** all three type tokens scale with their anchors in `wiom-ios-foundations` `typography.md` §3, line height included. Title and helper wrap (no truncation); counter and timer stay one line. Prefix and suffix never truncate; a long single-line value scrolls inside the field. The wrap and OTP boxes grow taller. At accessibility sizes the helper row may stack the counter under the helper. Six OTP boxes must still fit on iPhone SE at accessibility3 (cap, D17); check it. Icon sizes follow `icons.md`.
- **VoiceOver:**
  - Input: label = title (plus prefix, e.g. "Mobile number, plus 91"); value = text or placeholder; helper as hint. Status icons are decorative (`.accessibilityHidden(true)`); the status is spoken through the helper.
  - **Error is announced when it appears**: `UIAccessibility.post(notification: .announcement, argument: helper)` on the change into Error, and the field's `accessibilityValue` carries "Error: <helper>" while it lasts, so it is never colour-only. (iOS 17 `AccessibilityNotification.Announcement` is the newer API; on 16 use `UIAccessibility.post`.) Success may announce; Warning is in the value only.
  - OTP: **one element**, label = title, value = "4 of 6 digits entered" (illustrative, from the string catalog); boxes hidden.
  - Picker trigger: button trait, label = title, value = selection or placeholder, hint "Opens a list" (illustrative).
  - Disabled reads "dimmed" (system). Read-only value reads as static text with Copy in the rotor/long-press menu.
- **Hit area:** the whole wrap focuses the field. Trailing controls reserve an actual ≥ 44 × 44 pt layout slot, default 48 × 48, around the `icon/sm` glyph. The field grows or the text slot shrinks to fit that slot. Never negative padding or overlapping hit areas to preserve a 20 pt layout slot. Each trailing `Button` has a catalog label (illustrative: "Clear text", "Show password").

  ```swift
  Button(action: clear) {
      Wiom.Icon.cancel.resizable()
          .frame(width: Wiom.IconSize.sm, height: Wiom.IconSize.sm)
          .frame(minWidth: 48, minHeight: 48)
          .contentShape(Rectangle())
  }
  .accessibilityLabel(clearLabel)
  ```
- **Motion:** none. Border, label colour and status changes are instant, as on Android. Scrolling to the focused field follows the keyboard animation. Reduce Motion: nothing to reduce; `withAnimation` on the scroll may be dropped when `accessibilityReduceMotion` is on.
- **Safe areas and keyboard:** forms scroll; the focused field and its helper/error stay above the keyboard plus the sticky CTA bar (§7); CTA bar rides the keyboard with `space/12` below the button (D19); `.scrollDismissesKeyboard(.interactively)`. Per-field keyboard, content type and Return key in §6.
- **Haptics:** none (D21), including on OTP error or success.
- **Not on iOS:** hover, keyboard focus ring (the `stroke/brand/focus` border is the editing state, not a focus ring), ripple, Android IME action names and `NumberPassword` keyboard, hardware back to close a picker, `clearButtonMode` system clear button, `.alert` for validation errors.
