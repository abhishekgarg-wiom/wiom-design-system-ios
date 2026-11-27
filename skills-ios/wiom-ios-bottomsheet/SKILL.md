---
name: wiom-ios-bottomsheet
description: "Wiom bottom sheet for the iOS customer app in SwiftUI: a custom bottom-anchored sheet with 8 sizes (list, picker, illustration, share, form), plus the surface-choice table for toast, dialog, sheet and full screen. Use when building or reviewing a bottom sheet, sheet picker, action menu, share sheet or sheet form in SwiftUI, or when deciding which surface a moment belongs on."
---

# Wiom bottom sheet (iOS)

A bottom-anchored panel drawn by the app over the current screen, behind a scrim. It hosts pickers, action menus, confirmations with an illustration, share targets and short forms.

The sheet **owns the surface**: full width, top corners, scrim, handle, header and divider, action-bar gutter, safe areas, keyboard. It hosts but never re-draws its children: picker rows come from `wiom-ios-list-item`, buttons from `wiom-ios-cta`, the illustration badge from `wiom-ios-icon-badge`, fields from `wiom-ios-input-fields`.

This skill also **owns the surface-choice table** (`## Choosing a surface`). `wiom-ios-dialog` and `wiom-ios-toast` point here.

Contract: `wiom-ios-foundations/references/decisions.md` (D3, D9, D10, D11, D14 to D21). Tokens: `wiom-ios-foundations` (`tokens.md`, `typography.md`, `icons.md`, `layout.md`, `accessibility.md`, `motion.md`).

## Choosing a surface

One table for the whole app. If a moment is not listed, pick the lightest surface that still lets the user act safely.

**Modality.** Every dialog and every bottom sheet is **modal**: scrim, background inert, VoiceOver confined. There is **no non-modal sheet** in the customer app. The toast is the only surface that leaves the screen usable.

| Moment | Surface | Notes |
|---|---|---|
| Acknowledge a single tap that harms no one if missed ("Saved", "Copied") | **Toast** (`wiom-ios-toast`) | Non-blocking; small money acknowledgements are allowed. |
| A single tap failed and can be retried right away | **Toast**, Error, with action | Anything needing explanation goes to a dialog or sheet. |
| A field value is wrong | **Inline**: field error (`wiom-ios-input-fields`) | Next to the cause. |
| A setting that applies instantly | **Inline**: list-row switch (`wiom-ios-list-item`) | No confirmation. |
| Offline while cached data remains visible | **Toast**, Persistent / Warning | Illustrative: "Offline: purana data dikh raha hai". |
| Account on hold, or a state needing explanation or action | **Inline** message or a dedicated screen | Choose for the required task. |
| A short stop-and-decide question, text only, 1 or 2 actions | **Dialog**, Alert | |
| **Destructive confirmation** (delete, remove, sign out) | **Dialog**, Alert, Destructive CTA | **Always a dialog**, never a sheet. Matches what ships. |
| **Celebration** or emphasised acknowledgement (milestone, onboarding done) | **Dialog**, Illustration | Never a sheet, never a toast. |
| Capture one value not tied to a field on the screen (referral code) | **Dialog**, Input | One field only. |
| A one-off choice of 2 to 4 options, not opened from a field | **Dialog**, Selection | No scrolling inside a dialog. |
| A picker opened from a field or dropdown trigger (any count), or any choice of 5+ options | **Sheet**: Compact, Half, Expanded or Full | Pickers **are** bottom-sheet pickers; there is no dropdown menu. |
| Multi-select with Apply, filter or sort | **Sheet**, Expanded (Full if it scrolls) | Draft state reverts on dismiss. |
| Menu of contextual actions | **Sheet**, Compact or Half | |
| **Money commit**: confirm a payment, set up auto-pay | **Sheet**, Illustration, **non-dismissable** | Explicit buttons only (see Dismissal). |
| Money outcome requiring acknowledgement or recovery mid-flow | **Dialog**, Alert/Illustration, or **Sheet**, Illustration | Use the content and action needs; a sheet handling a commit is non-dismissable. |
| Small money acknowledgement requiring no decision | **Toast**, Positive | Illustrative: "Nikaasi safal rahi". No receipt or next step may depend on seeing it. |
| Money outcome at the end of a flow (receipt) | **Full screen** result | |
| Explain a permission before the OS prompt | **Sheet**, Illustration, Warning tone | Then the system prompt (system-owned, D9). |
| 2 to 3 fields tied to the current context | **Sheet**, Form | 1 field: Dialog Input. 4+ fields: full screen. |
| Share | **Sheet**, Share | "More" opens the system share sheet (D11). |
| Blocking foreground loading, including processing payment, syncing or submitting | **Dialog**, Loading | No 3-second cutoff; always an error/timeout fallback. |
| Long form, multi-step flow, T&C, plan details, FAQ, search with many results | **Full screen** (pushed) | System push/pop and swipe-back (D6). |

**Stacking.** A dialog may sit above a sheet. Never a sheet above a sheet (dismiss the first, then present the second). Never a dialog above a dialog. Avoid a toast while a dialog or sheet is up.

## 1. Sizes

Sizes are **content-fitted** or a **share of the screen height**, never fixed points (iPhones run 667 to 956 pt tall). "Screen height" means the height of the presenting container including safe areas.

**Cap (all sizes):** the sheet's top edge never rises above the top safe-area inset (status bar, Dynamic Island). Content taller than the cap **scrolls** inside the sheet; the handle, header and action bar do not scroll (but see Dynamic Type).

| Size | Height | Body | Use for |
|---|---|---|---|
| `Compact` | Fits content, **at least 30 %** of screen height | Header + about 2 rows | Short action menu, quick choice |
| `Half` | Fits content, **at least 50 %** | Header + about 4 rows | Option menu, short picker, filter |
| `Expanded` | Fits content, **at least 75 %** | Header + up to 7 rows | Standard picker, multi-select |
| `Full` | **Fills to the cap** | Header + 7+ rows, scrolls | Long picker, searchable picker |
| `Illustration` | Fits content | Badge + heading + subtext, centered | Money commit and outcome, permission explainer |
| `Illustration Left` | Fits content | Badge left, text right | Compact feedback |
| `Share` | Fits content | Header + share-target rows | Share |
| `Form` | Fits content | Header + 1 to 3 fields | Short in-context input |

The minimum shares come from the shipped minimums (240 / 400 / 600 on an 800-tall reference screen). There are **no intermediate detents**: a sheet opens at its fitted height and is never half-open.

Picker row count is a guide: 7 or fewer rows use `Expanded` without scrolling; more rows use `Full`.

## 2. Anatomy

```
 overlay/scrim over the whole screen (safe areas included)
┌──────── bg/default · radius/xlarge top corners · bottom corners square ────────┐
│                  ▬▬▬  Handle: 32 × 4, stroke/strong, radius/full             │  space/8 above and below
│  [space/16 top space]                                                        │
│  (icon)  Title                                             Trailing action   │  Header
│          Subtitle                                                            │  padding 8 top · 16 sides · 16 bottom
│ ──────────────────────────── divider ─────────────────────────────────────── │  stroke/small, stroke/subtle
│  Body: rows / illustration / share targets / fields                          │  scrolls when over the cap
│  [space/48 gap]                                                              │
│  [space/16]  Button group (wiom-ios-cta)  [space/16]                          │  Action bar
│  [bottom: see Safe areas]                                                    │
└──────────────────────────────────────────────────────────────────────────────┘
```

| Slot | Value |
|---|---|
| Width | Fill the screen width. No side margin. |
| Shape | Top corners `radius/xlarge`, circular (D3). Bottom corners square: the sheet sits flush on the bottom edge. |
| Fill | `bg/default`, extended under the home indicator |
| Shadow | `shadow/md`, no border |
| Scrim | `overlay/scrim`, full screen, flat (no shadow, no radius) |
| Handle | 32 × 4 glyph, `stroke/strong`, `radius/full`, `space/8` above and below, centered |
| Top space | `space/16` between handle and header or content |
| Header padding | `space/8` top, `space/16` leading and trailing, `space/16` bottom; slot gap `space/12` |
| Divider | `stroke/small` thick, `stroke/subtle`, full width, only when a header is shown |
| Content to action bar | `space/48` |
| Action bar | `space/16` leading and trailing, no top padding, **no top border**; bottom per Safe areas |

### Header

| Slot | Style |
|---|---|
| Leading icon (optional) | `icon/md` (24), `icon/nonAction`, Material Rounded (D4) |
| Title | `type/heading/md`, `text/default`, leading-aligned, wraps, never truncates |
| Subtitle (optional) | `type/body/sm`, `text/subtle`, `space/4` below title |
| Trailing action (optional, e.g. "Clear all") | `type/label/md`, `text/brand`; a text link, hit area ≥ 44 × 44 |

**No close (X) button.** Dismissal is the handle, the scrim and the VoiceOver escape (see Dismissal). A non-dismissable sheet uses its own explicit buttons.

### Body by size

- **Compact / Half / Expanded / Full, picker** (radio or checkbox): `wiom-ios-list-item` rows, end to end. A picker opened from a field ticks the current value.
- **Compact / Half, action menu**: the sheet's own **sheet row**: `space/24` leading and trailing, `space/12` top and bottom, min height 48; optional leading 40 circle in `bg/brand/subtle` with an `icon/sm` (20) `icon/brand` glyph; label `type/label/lg` `text/default`; optional description `type/body/md` `text/subtle` with `space/4` gap; trailing `chevron_right` `icon/sm` `icon/disabled`; `space/12` slot gap. Pressed fill per D13 (`bg/subtle` as list rows).
- **Full, searchable**: header, then a search field (`wiom-ios-input-fields`) with `space/16` sides and `space/8` top and bottom, then radio rows that filter as the user types.
- **Illustration**: block padding `space/16` top and sides, `space/48` bottom; `wiom-ios-icon-badge` Lg (96) centered; `space/24` badge to text; heading `type/heading/md` `text/default` centered; `space/12`; subtext `type/body/md` `text/subtle` centered. No header, no divider.
- **Illustration Left**: same block as a row: badge leading, text trailing and leading-aligned, `space/24` gap, vertically centered.
- **Share**: header, then share-target rows (sheet rows). The last target is "More", which opens the system share sheet (D11).
- **Form**: header, then 1 to 3 `wiom-ios-input-fields` fields with `space/24` sides, `space/16` top and bottom, `space/12` between fields; then the action bar.

### Illustration tones

Tone comes from `wiom-ios-icon-badge` (`bg/{tone}/subtle` + `icon/{tone}`). Match the message:

| Tone | Use for |
|---|---|
| Brand (default) | Neutral announcement, tip |
| Positive | Payment succeeded, activation done |
| Critical | Payment failed, network error |
| Warning | Permission needed, plan expiring |
| Info | How something works |

A Positive tone on a failure, or Critical on a welcome, is a bug.

### Action bar

Buttons come from `wiom-ios-cta`. **Layout, pairing and count follow `wiom-ios-cta` §6 (the one button-group rule)**; this skill does not restate it. Never hand-roll buttons in the action bar. Pickers that commit on row tap (single-select) have no action bar.

## 3. Dismissal

iOS ways to close a dismissable sheet (D10). **There is no back press.**

| Path | Behaviour |
|---|---|
| Swipe down | Drag on the handle, header or action bar. Release past **one third of the sheet height**, or a fast downward flick (predicted end beyond half the sheet height), and the sheet closes; otherwise it springs back. Dragging up rubber-bands; the sheet never grows. |
| Scrim tap | Closes. |
| VoiceOver escape (two-finger Z) | Closes. |
| VoiceOver scrim element | The scrim is exposed as a "Close" button, read last. |

Closing a dismissable sheet means **cancel**: a picker keeps its old value; multi-select and filter drafts revert to the state before the sheet opened.

### Non-dismissable sheets

Money and commit moments close **only through an explicit button** in the action bar:

- confirm a payment or auto-pay; a payment outcome (success or failure) mid-flow; consent or terms acceptance; a Form while it is submitting.

In a non-dismissable sheet: the **handle is hidden** (top space stays), swipe-down does nothing, scrim tap does nothing, VoiceOver escape does nothing, and the scrim is not exposed to VoiceOver. The action bar always has a way out ("Cancel", "Done", "Try again"); a non-dismissable sheet with no exit is a bug.

## 4. Rules

1. Full width, top corners only. Bottom corners square.
2. `shadow/md` only, never a border.
3. No close (X) button. Dismissal per §3.
4. No top border on the action bar; the `space/48` gap separates it.
5. Buttons follow `wiom-ios-cta` §6. Max 1 Primary, max 1 Destructive.
6. Picker rows are `wiom-ios-list-item`; never re-draw them.
7. The illustration badge is `wiom-ios-icon-badge` Lg; never draw a circle and a glyph by hand.
8. Never a sheet over a sheet. Dismiss, then present.
9. Destructive confirmations and celebrations are dialogs, not sheets (`## Choosing a surface`).
10. Tokens by DS V2 name only. Icons are Material Rounded (D4); never SF Symbols.
11. Copy is illustrative; real copy comes from the string catalog (D25). Guide: heading and title up to 40 grapheme clusters, subtitle and subtext up to 120. Text wraps; it never truncates.

## 5. Examples (illustrative copy)

| Moment | Size | Content | Buttons (layout per `wiom-ios-cta`) | Dismissable |
|---|---|---|---|---|
| Choose language from a field | Half | Header "Choose language", radio rows | None (row tap commits and closes) | Yes |
| Filter plans | Expanded | Header "Filter plans", subtitle "2 selected", trailing "Clear all", checkbox rows | Secondary "Cancel" + Primary "Apply" | Yes (reverts) |
| Choose city | Full | Header, search field, radio rows | None | Yes |
| Plan actions | Compact | Header "Plan options", sheet rows "View details", "Get help" | None | Yes |
| Confirm payment | Illustration, Brand | Heading "Confirm payment", subtext "Check your plan before you pay." | Primary "Pay now" + Secondary "Cancel" | **No** |
| Payment failed | Illustration, Critical | Heading "Payment didn't go through", subtext "You can try again or pick another method." | Primary "Try again" + Secondary "Cancel" | **No** |
| Allow location | Illustration, Warning | Heading "Allow location?", subtext "We use it to check service at your address." | Primary "Continue" + Tertiary "Not now" | Yes |
| Share plan | Share | Header "Share", rows "WhatsApp", "Copy link", "More" | None | Yes |
| Edit name | Form | Header "Edit name", 1 field | Primary "Save" | Yes, **No** while saving |

## Open questions

| # | Question | Default here |
|---|---|---|
| 1 | Sheet list rows: the source skill says rows are `wiom-list-item` instances with a 16 gutter; Android draws its own sheet row with 24 sides, a 40 brand circle, `label/lg` and an `icon/disabled` chevron (`WiomBottomSheet.kt:254-318`). Header padding is 16 (`WiomBottomSheet.kt:196-200`), so header and rows don't line up. | Follow Android: sheet row for action menus and share; `wiom-ios-list-item` for radio and checkbox pickers. Design team to confirm the 24 vs 16 alignment. |
| 2 | Share layout: source skill says a horizontal row of share targets; Android previews it as header + list rows (`WiomBottomSheet.kt:561-577`). | Follow Android (rows). |
| 3 | Size heights: source skill gives min/max ranges and `Full` = 92 % of the screen; Android ships minimums only (240 / 400 / 600) and `Full` hugging content (`WiomBottomSheet.kt:128-141`). | Minimum shares (30 / 50 / 75 %) as in Android; `Full` fills to the cap. |
| 4 | Android opens tall non-Full sheets half-expanded (`ModalBottomSheet` default state, `WiomBottomSheet.kt:73-75`); the iOS sheet has no detents. | No half-open state on iOS. |
| 5 | Shadow: source skill and `tokens.md` say `shadow/md`; Android sets no explicit shadow on the sheet (`WiomBottomSheet.kt:81-99`). | `shadow/md`. |
| 6 | Non-dismissable sheets: Android has no non-dismissable mode (scrim and swipe always dismiss, `WiomBottomSheet.kt:81-87`). iOS adds it for money and commit moments. | iOS behaviour as §3; Android to follow. |
| 7 | Non-modal sheets: Figma has `Is Modal` (default false); Android ships only modal sheets (`WiomBottomSheet.kt:87`). If design ever needs one, the overlay host can skip the scrim and leave the content beneath hit-testable on iOS 16.0 (no 16.4 API), with `.isModal` removed. | Not used. |
| 8 | Destructive confirmation: the source sheet skill listed an Illustration sheet; the source dialog skill and Android (`WiomDialog.kt` preview "Alert · destructive") use a dialog. `wiom-ios-cta` §6.1 still has a bottom-sheet destructive row. | Dialog. The cta row applies only when a sheet's own commit is destructive (e.g. a Form that cancels a request). |
| 9 | Swipe-to-dismiss from inside a scrolled list (pull down when at the top) needs scroll-offset tracking that iOS 16 SwiftUI does not expose cleanly. | Drag zone is handle + header (+ action bar). |
| 10 | `WiomTypography.kt:18` says sheet and dialog headers default to `heading/lg`; the shipped sheet header uses `heading/md` (`WiomBottomSheet.kt:219`). | `type/heading/md`; `typography.md` leaves the choice to this skill. |
| 11 | Copy limits (40 / 120 grapheme clusters) are guidance, not from Figma. | As §4 rule 11, pending design. |

## iOS (SwiftUI, iOS 16+)

- **Built from:** a custom sheet view presented by a **root-level overlay host** (below). Never `.sheet` + `presentationDetents` (D10). Top-corner shape: a custom `Shape` rounding only the top corners with circular arcs (`UIBezierPath(roundedRect:byRoundingCorners: [.topLeft, .topRight], cornerRadii:)`); `UnevenRoundedRectangle` is iOS 17+, so not used. Body scroll: `ScrollView` inside a `ViewThatFits(in: .vertical)` (iOS 16) or a measured height. Drag: `DragGesture` with `predictedEndTranslation`. Rows, buttons, badge and fields from the `wiom-ios-*` skills named above.
- **Presentation approach (iOS 16):**

  | Approach | Pros | Cons |
  |---|---|---|
  | **Overlay host (chosen).** A `.wiomOverlayHost()` modifier at the app root, and again at the root of each `fullScreenCover`, draws a `ZStack`: app content, then the sheet layer (scrim + sheet), then the dialog layer. Screens present through an environment presenter (`@EnvironmentObject WiomOverlayPresenter`). | Pure SwiftUI on 16.0+. Full control of scrim, animation, keyboard and accessibility. Sheet and dialog share one host, so "dialog above sheet" is just z-order. | Must be installed in every presentation context. It cannot sit above system-presented UI (it lives inside the window). The host must hide the content beneath from VoiceOver itself. |
  | `fullScreenCover` with a clear background + the custom sheet inside | Sits above everything in the app. | Clear background needs `presentationBackground(.clear)` (16.4+) or a UIKit superview hack on 16.0 to 16.3. The system cover slide must be disabled (`Transaction.disablesAnimations`) and re-done, and the scrim fade lags. |

  ```swift
  // App root (and the root of each fullScreenCover)
  RootView().wiomOverlayHost()

  // Inside the host, sheet layer:
  ZStack(alignment: .bottom) {
      Wiom.Colors.overlayScrim.ignoresSafeArea()
          .onTapGesture { if sheet.isDismissable { presenter.dismissSheet() } }
          .accessibilityElement().accessibilityLabel("Close")     // string catalog
          .accessibilityAddTraits(.isButton)
          .accessibilityHidden(!sheet.isDismissable)
      WiomSheetSurface(sheet)                                   // handle, header, body, action bar
  }
  ```
- **Tokens:** `bg/default`, `overlay/scrim`, `shadow/md`, `radius/xlarge`, `radius/full`, `stroke/strong`, `stroke/subtle`, `stroke/small` (width), `text/default`, `text/subtle`, `text/brand`, `icon/nonAction`, `icon/brand`, `icon/disabled`, `bg/brand/subtle`, `bg/subtle`, `type/heading/md`, `type/body/md`, `type/body/sm`, `type/label/md`, `type/label/lg`, `icon/sm`, `icon/md`, `space/4`, `space/8`, `space/12`, `space/16`, `space/24`, `space/48`.
- **Size:** width fills. Heights per §1 (minimum share of screen height or content-fitted, capped below the top safe area). Header, rows and buttons have **minimum** heights (rows 48); only the handle glyph (32 × 4) and badge are fixed shapes (D16).
- **Dynamic Type:** all text scales (`typography.md` §3); titles, subtitles, row labels and subtext wrap with no line limit. A sheet that grows past the cap scrolls its body. At accessibility sizes (accessibility1 and up) the header scrolls with the body so the list keeps room; the action bar stays pinned, and its group stacks per `wiom-ios-cta` §6. Check Hindi and English at xxxLarge and accessibility3 (D17).
- **VoiceOver:** the sheet container gets `.accessibilityAddTraits(.isModal)`, and the host sets `.accessibilityHidden(true)` on the content beneath while a sheet is up. On appear, focus moves to the **title** (or the illustration heading) via `@AccessibilityFocusState`, which carries `.isHeader`. Dismissable sheets add `.accessibilityAction(.escape) { dismiss() }`; non-dismissable sheets add none. Handle and divider are `.accessibilityHidden(true)`. Picker rows announce selected state (`wiom-ios-list-item`). When the sheet closes, focus returns to the control that opened it.
- **Hit area:** every tappable element ≥ 44 × 44, default 48 (D14): header trailing action, rows, buttons. The drag zone (handle + header) is at least 44 tall.
- **Motion:** per `wiom-ios-motion` §4: the sheet slides up from the bottom edge and the scrim fades in, both `motion/surface` `ease/standard`, in one `withAnimation` transaction; exit mirrors it. During a drag the sheet follows the finger with no animation; on release it completes or snaps back on `motion/surface` `ease/standard`. **Reduce Motion** (`@Environment(\.accessibilityReduceMotion)`): the slide becomes a `motion/micro` cross-fade; drag-to-dismiss still works (it follows the finger) but the release closes with a fade (D20).
  ```swift
  .transition(reduceMotion ? .opacity : .move(edge: .bottom))
  ```
- **Safe areas and keyboard:** the fill extends under the home indicator (`.ignoresSafeArea(.container, edges: .bottom)` on the background only); content stays inside. Last CTA: `space/16` above the home indicator on Face ID iPhones, `space/16` above the screen edge on Home-button iPhones (D19); with no action bar, the last row ends at the safe-area edge. **Form:** the sheet rides on the keyboard (content respects the keyboard safe area) with `space/12` between the last button and the keyboard; the focused field stays visible (`ScrollViewReader` scroll-to on focus). If sheet plus keyboard exceed the cap, the body scrolls. Status bar content stays dark over the scrim.
- **Haptics:** none (D21).
- **Not on iOS:** back press, Android `ModalBottomSheet` half-expanded state, ripple, `.sheet` / `presentationDetents`, `presentationBackgroundInteraction` (16.4+, and non-modal sheets are not used), SF Symbols, a close (X) button, `UnevenRoundedRectangle` (17+), `.continuous` corners.
