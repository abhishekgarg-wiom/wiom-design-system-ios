---
name: wiom-ios-dialog
description: "Wiom dialog for the iOS customer app in SwiftUI: a centered card over a scrim with 5 types (Alert, Input, Selection, Illustration, Loading), drawn by the app in place of system alerts. Use when building or reviewing a Wiom dialog in SwiftUI: Alert, Input, Selection, Illustration or Loading dialog."
---

# Wiom dialog (iOS)

A centered, blocking card over a scrim. The user stops, reads one thought, and acts through an explicit button.

**Which surface?** Dialog vs toast vs sheet vs full screen is decided in **`wiom-ios-bottomsheet` → `## Choosing a surface`**. This skill does not repeat that table. In short, dialogs carry: short stop-and-decide questions, destructive confirmations, celebrations, one-field capture, 2 to 4 option choices, and blocking foreground loading.

**Always the Wiom dialog, never `.alert` or `.confirmationDialog`** (D9). The only system alerts allowed are ones the OS owns: permission prompts and other system sheets.

Contract: `wiom-ios-foundations/references/decisions.md` (D3, D9, D14 to D21, D25). Tokens: `wiom-ios-foundations` (`tokens.md`, `typography.md`, `icons.md`, `layout.md`, `accessibility.md`, `motion.md`).

## 1. Types

| Type | Header | Text alignment | Body content | Use for |
|---|---|---|---|---|
| `Alert` | 48 neutral circle (optional) | Leading | Title + body | Stop-and-decide question, destructive confirmation, status that needs acknowledging |
| `Input` | None | Leading | Title + body + 1 field | Capture one value (referral code, name) |
| `Selection` | None | Leading | Title + body + 2 to 4 radio rows | Short one-off choice |
| `Illustration` | 144 tall illustration panel | Centered | Title + body | Celebration or emphasised acknowledgement |
| `Loading` | 40 spinner frame | Centered | Title and/or message | Blocking foreground loading: processing payment, syncing, submitting |

## 2. Anatomy

```
          overlay/scrim over the whole screen
     ┌──────── width: min(312, screen − 48) ────────┐
     │  space/24 padding on all sides                │
     │  [Header: icon tile / panel / spinner]        │
     │        ↓ space/16                              │
     │  Title   type/heading/md · text/default        │
     │        ↓ space/8                               │
     │  Body    type/body/md · text/subtle            │
     │        ↓ space/16 (Input, Selection)           │
     │  [Field / radio rows]                          │
     │        ↓ space/48                              │
     │  [Button group: wiom-ios-cta §6]               │
     └────────────────────────────────────────────────┘
       bg/default · radius/xlarge · shadow/xl · no border
```

| Slot | Value |
|---|---|
| Width | **Max 312, with at least `space/24` side margins** (D15): `min(312, container width − 48)`. On iPhone SE (375) that is 312; it never touches the edges. |
| Height | Fits content, **at most** the safe-area height minus `space/24` top and bottom (and above the keyboard). Over that, the main block scrolls; the button group stays pinned. |
| Position | Centered in the safe area (above the keyboard when it is up) |
| Padding | `space/24` all sides |
| Shape | `radius/xlarge`, circular (D3) |
| Fill | `bg/default` |
| Shadow | `shadow/xl` (always paired with `overlay/scrim`) |
| Border | None (shadow or border, never both) |
| Scrim | `overlay/scrim`, full screen including safe areas |
| Header → title | `space/16` |
| Title → body | `space/8` |
| Text → field or rows | `space/16` |
| Main block → button group | `space/48`, all types |

### Title style

**One title style for every type: `type/heading/md`, `text/default`.** This is what ships for all five types. The foundations typography note (`wiom-ios-foundations` `typography.md`) defers to this skill, so the default dialog header is `heading/md`, not `heading/lg`. Never `type/heading/lg` in a dialog.

Body: `type/body/md`, `text/subtle`. Both wrap with no line limit and never truncate.

### Header per type

| Type | Header |
|---|---|
| `Alert` | Optional 48 × 48 circular icon badge, `radius/full`, `bg/subtle`, with an `icon/md` (24) `icon/action` Material Rounded glyph, leading-aligned. The dialog-specific tint overrides the general icon-badge Neutral tint. Omit it for text-only alerts. |
| `Input`, `Selection` | None; the title is first. |
| `Illustration` | Full-width panel, **144 tall**, `radius/large`, `bg/brand/subtle`, with an `icon/lg` (48) `icon/brand` glyph (or an illustration asset) centered. |
| `Loading` | 40 × 40 frame with a `wiom-ios-loader` Spinner, small, brand, centered. |

### Body content

- **Input:** exactly **one** `wiom-ios-input-fields` field, full content width. Two or more fields go to a sheet Form or a screen.
- **Selection:** 2 to 4 `wiom-ios-list-item` radio rows, `space/8` between rows. Rows own their padding and 48 min height. **Never** 5+ rows, and never a scrolling list by design (at large text the main block may scroll, see Height). More options go to a sheet picker.
- **Alert, Illustration, Loading:** title and body only.

### Buttons

The button group follows **`wiom-ios-cta` §6, the one button-group rule** (layout, pairing, order). This skill does not restate it. Limits specific to dialogs:

- Alert, Input, Selection, Illustration: 1 or 2 CTAs.
- Loading: **no buttons**.
- Max 1 Primary or 1 Destructive; a destructive confirmation always has an escape.

## 3. Behaviour per type

There is no back press on iOS. The two dismissal paths are scrim tap and the VoiceOver escape gesture (two-finger Z).

| Type | Scrim tap | VoiceOver escape | Notes |
|---|---|---|---|
| `Alert` | Does nothing | Closes, runs the **dismiss** action (the Cancel / escape CTA, or `onDismiss` when there is one CTA) | Escape never runs the confirm or Destructive action. |
| `Input` | Does nothing | Closes as cancel; typed text is discarded | Protects half-typed input from a stray tap. |
| `Selection` | Does nothing | Closes as cancel; previous choice kept | |
| `Illustration` | Does nothing | Closes, runs the dismiss action | |
| `Loading` | Does nothing | Does nothing | Blocks all interaction until the work ends. |

Rules:

1. **Scrim tap never closes a dialog.** The user leaves through a button.
2. **One dialog at a time.** Close the first before showing a second.
3. A dialog may sit above a bottom sheet; the sheet dims behind the dialog's scrim.
4. **Loading always has a way out:** when the work fails or times out, the Loading dialog is replaced by an Alert (or the flow's error surface) the user can act on. Never leave a Loading dialog up indefinitely.
5. Loading dialogs handle blocking foreground work, including processing payment, syncing and submitting. There is no 3-second cutoff. Keep the error/timeout recovery path in rule 4.

## 4. Rules

1. Max 312 wide, ≥ 24 side margins. Never full width, never a fixed 312 on a narrower screen.
2. `shadow/xl`, no border.
3. One title style: `type/heading/md`.
4. Child components are instances: field from `wiom-ios-input-fields`, rows from `wiom-ios-list-item`, spinner from `wiom-ios-loader`. Never re-draw them.
5. Selection: 2 to 4 options. Input: one field.
6. Buttons follow `wiom-ios-cta` §6.
7. Tokens by DS V2 name only; icons Material Rounded (D4), never SF Symbols.
8. Copy is illustrative; real copy comes from the string catalog (D25). Guide: title up to 40 grapheme clusters (about two lines), body up to 120.

## 5. Examples (illustrative copy)

| Moment | Type | Title / body | Buttons (layout per `wiom-ios-cta`) |
|---|---|---|---|
| Delete a saved address | Alert, icon `delete` | "Delete this address?" / "You can add it again later." | Destructive "Delete" + escape "Cancel" |
| Leave a half-filled form | Alert | "Discard changes?" / "Your edits won't be saved." | Destructive "Discard" + escape "Keep editing" |
| Enter a referral code | Input | "Enter referral code" / "Ask your friend for their code." | Primary "Apply" + escape "Cancel" |
| Choose app language | Selection, 3 rows | "Choose language" / "You can change this later in Settings." | Primary "Confirm" + escape "Cancel" |
| Onboarding finished | Illustration, icon `celebration` | "You're all set" / "Your home internet setup is complete." | Primary "Go to home" |
| Processing payment | Loading | "Processing payment" / "This takes a moment." | None |

## Settled rules

- **Alert icon:** 48 pt neutral circle, `bg/subtle` + `icon/action` (owner lock, PODS-1). Generic Neutral icon badges keep `icon/nonAction`; the dialog owns this override.
- **Loading:** no button, never dismissable (escape does nothing).
- **Illustration panel:** full-width 144 pt panel, `bg/brand/subtle` only.
- **Type:** title `type/heading/md`, body `type/body/md`.

## Open questions

1. **Escape on money Alerts.** VoiceOver escape closes Alert and Illustration. Should a money-related Alert ever be escape-proof? Default: escape closes; money commits belong on a non-dismissable sheet.
2. **Copy limits** (40 / 120 grapheme clusters) are guidance, not from Figma (§4 rule 8).

## iOS (SwiftUI, iOS 16+)

- **Built from:** a custom `WiomDialog` view presented by the same **root-level overlay host** as the bottom sheet (`wiom-ios-bottomsheet`, iOS section), in the dialog layer above the sheet layer. Never `.alert`, `.confirmationDialog`, or `.sheet` (D9). Shape: `RoundedRectangle(cornerRadius: Wiom.Radius.xlarge, style: .circular)`. Main block: `ScrollView` only when it overflows (`ViewThatFits(in: .vertical)`, iOS 16). Buttons from `wiom-ios-cta`, field from `wiom-ios-input-fields`, rows from `wiom-ios-list-item`, spinner from `wiom-ios-loader`.
  ```swift
  GeometryReader { proxy in
      WiomDialogCard(model)
          .frame(maxWidth: min(312, proxy.size.width - 2 * Wiom.Spacing.s24))
          .frame(maxWidth: .infinity, maxHeight: .infinity)      // centered in the safe area
  }
  ```
- **Tokens:** `bg/default`, `overlay/scrim`, `shadow/xl`, `radius/xlarge`, `radius/large`, `radius/medium`, `radius/full`, `bg/subtle`, `bg/brand/subtle`, `icon/action`, `icon/brand`, `text/default`, `text/subtle`, `type/heading/md`, `type/body/md`, `icon/md`, `icon/lg`, `space/8`, `space/16`, `space/24`, `space/48`.
- **Size:** width `min(312, container − 48)`. Height fits content up to the safe area minus `space/24` each end. Text-holding parts have minimum heights only; fixed shapes are the 48 icon circle, the 144 illustration panel and the 40 spinner frame (D16).
- **Dynamic Type:** title and body scale (`typography.md` §3) and wrap with no line limit. When the dialog would exceed its max height (accessibility sizes, two-line Hindi), the main block scrolls and the button group stays pinned and visible; side-by-side buttons stack per `wiom-ios-cta` §6. Check Hindi and English at xxxLarge and accessibility3 on iPhone SE (D17).
- **VoiceOver:** the card gets `.accessibilityAddTraits(.isModal)`; the host hides everything beneath with `.accessibilityHidden(true)`. On appear, focus moves to the **title** first (`@AccessibilityFocusState`), which carries `.isHeader`; then body, content, buttons in order. Header icon and illustration are decorative (`.accessibilityHidden(true)`) unless the asset carries meaning, then it gets a label. Escape per §3:
  ```swift
  .accessibilityAction(.escape) { if model.type != .loading { model.onDismiss() } }
  ```
  **Loading** announces on appear (`UIAccessibility.post(notification: .screenChanged, argument: title)`) and posts an announcement when the work ends; the spinner is labelled from its title, not "spinner". When the dialog closes, focus returns to the control that opened it.
- **Hit area:** buttons and radio rows ≥ 44 × 44, default 48 (D14). The scrim has no hit action.
- **Motion:** per `wiom-ios-motion` §4: card and scrim fade in and out together on `motion/micro` `ease/standard`, one `withAnimation` transaction. No scale or slide. **Reduce Motion:** the same fade (already the reduced form, D20). The Loading spinner keeps rotating under Reduce Motion.
- **Safe areas and keyboard:** centered in the safe area; the scrim covers safe areas too. **Input:** when the keyboard is up, the dialog re-centers in the space above it (the host respects the keyboard safe area) and keeps `space/24` clear above the keyboard; if it no longer fits, the main block scrolls with the field kept visible. The field takes focus on appear. Status bar content stays dark over the scrim.
- **Haptics:** none (D21).
- **Not on iOS:** back press, `DialogProperties`, `.alert`, `.confirmationDialog`, system tint buttons, scrim-tap dismissal, a fixed 312 width on narrow screens, SF Symbols, `.continuous` corners, scale-in animation.
