---
name: wiom-ios-toast
description: >
  Wiom toast for the iOS customer app (SwiftUI): the short, passive
  message that floats at the bottom of the screen after a tap, server
  response or system event, in 4 types (Critical, Warning, Info,
  Positive) and 3 behaviours (Informational, Actionable, Persistent).
  Use when building, reviewing or placing a WiomToast or WiomToastHost
  in SwiftUI on iOS.
---

# Wiom toast (iOS)

**4 types · 3 behaviours · 1 component.**

A toast is a passive, transient message shown at the **bottom of the
screen** after a single user action or system event. It auto-dismisses,
or, when Persistent, waits for an explicit close. A toast is a feedback
layer, not a content layer: it never replaces an inline field error, an
required in-page explanation or a result screen. Offline with cached data
is the explicit Persistent / Warning case (§1).

This skill follows `IOS_DECISIONS.md` (parity principle: the toast looks
exactly as the Android app ships it; only behaviour follows iOS). Tokens
are cited by DS V2 name; values live in `wiom-ios-foundations`.

## 1. Is a toast the right surface?

The single surface-choice table (Toast vs Dialog vs Bottom sheet vs Full
screen) lives in **`wiom-ios-bottomsheet` § "Choosing a surface"**. Use
it; this skill does not repeat it. The toast-specific checks:

| Moment | Surface |
|---|---|
| Quick feedback to one tap: request rejected, call failed, copied, undoable delete | **Toast** |
| Form or input validation error | Inline error on the field (`wiom-ios-input-fields`) |
| Whole screen failed to load | Empty / error state on the screen |
| Offline while cached data remains visible | **Persistent / Warning toast**, until dismissed or connectivity returns |
| End of a multi-step flow | Result screen |
| Small money acknowledgement (illustrative: "Nikaasi safal rahi") | **Positive toast** when no decision or receipt is required; otherwise follow the surface-choice table |

> **One-liner.** Toast = quick feedback to a single action, no
> explanation needed, the user can carry on or retry at once. Anything
> more gets a bigger surface.

## 2. Anatomy

```
┌──────────────────── screen (any iPhone width) ───────────────────┐
│                                                                   │
│                            content                                │
│                                                                   │
│ ←8→ ┌─────────────────────────────────────────────────────┐ ←8→  │
│     │ (icon)  Message text, up to 2 lines        Action  ✕ │      │
│     └─────────────────────────────────────────────────────┘      │
│                         ↕ space/16                                │
│ ─────── sticky CTA bar / keyboard / home-indicator safe area ──── │
└───────────────────────────────────────────────────────────────────┘
```

| Slot | Value | Token |
|---|---|---|
| Container width | Fills the screen width minus **8 pt each side** (the host owns the margin) | `space/8` |
| Container height | **Minimum**, from padding + content: 12 + 24 + 12 = 48 pt for one line at default text size. Grows with a second line and with Dynamic Type | n/a |
| Container radius | 8 pt, circular corners (D3) | `radius/small` |
| Container fill | Same for all 4 types | `bg/default` |
| Container shadow | Drop shadow, no border | `shadow/lg` |
| Horizontal padding | 16 pt | `space/16` |
| Vertical padding | 12 pt | `space/12` |
| Row | Items centred vertically; gap between every adjacent item | `space/8` |
| Leading icon | 24 pt, Material Rounded filled glyph (D4) | `icon/md` (size) |
| Message | Regular, fills the remaining width. **2 lines at default text size; grows at large text sizes** (never cut off, D33). Toast height caps at **40 % of the screen**; beyond that the message scrolls inside the toast | `type/body/lg` |
| Action label (optional) | SemiBold, 1 line, text only (never a filled button) | `type/label/lg` |
| Action label padding (visible) | 8 pt horizontal, 4 pt vertical | `space/8` · `space/4` |
| Close ✕ (Persistent) | 24 pt glyph `close` | `icon/md` (size) · `icon/action` |

**No fixed width or height on the toast.** Width comes from the host's
margin; height comes from padding + content.

**Why 8 pt and not the 16 pt screen gutter.** The toast floats: it is a
deliberately wider card (344 pt on a 360-wide Android reference) with an
8 pt margin on each side, as Android ships it (`WiomToastHost` is placed
with `space/8` padding). Do not "standardise" it to the 16 pt gutter used
by list rows, the top bar and sheet content.

## 3. The 4 types

All four share the `bg/default` container. Only the leading icon (and,
for Warning, the message colour) carries the status.

| Type (Figma name) | Icon glyph (Material Rounded) | Icon colour | Message colour |
|---|---|---|---|
| **Critical** (Error) | `error` | `icon/critical` | `text/default` |
| **Warning** | `warning`, in an Icon Badge **Sm** (24 pt circle, 16 pt glyph, `bg/warning/subtle`; D31, D35) | `icon/action` (dark; decorative) | `text/onWarning` |
| **Info** | `info` | `icon/info` | `text/default` |
| **Positive** (Success) | `check_circle` | `icon/positive` | `text/default` |

- **Action label is always `text/brand`**, whatever the type: Undo /
  Retry / View is the screen's brand action, not the toast's status.
- **Warning is the only type whose message is not `text/default`.** It
  uses `text/onWarning`, the one text token of the warning family.
- The icon is decorative; the message carries the meaning (so the
  message must be specific, see §6).

Sample copy (illustrative only; real copy comes from the string catalog,
Hindi first, English written separately, sentence case):

| Type | Hindi (illustrative) | English (illustrative) |
|---|---|---|
| Critical | "अनुरोध पूरा नहीं हो सका" | "Couldn't send your request" |
| Warning | "Offline: purana data dikh raha hai" | "Offline: showing saved data" |
| Info | "शिकायत अपडेट हो गई" | "Complaint updated" |
| Positive | "Nikaasi safal rahi" | "Withdrawal successful" |

## 4. The 3 behaviours

Behaviour is not a visual variant; it is the action / close slots plus
the timer.

| Behaviour | Action | Close ✕ | Duration | Use for |
|---|---|---|---|---|
| **Informational** | No | No | **2 s** auto | Fire-and-forget: request rejected, status changed, copied |
| **Actionable** | Yes | No | **8 s** auto | The user just did something undoable or retryable: delete + Undo, failed call + Retry |
| **Persistent** | Optional | **Yes** | None: until ✕ or the state that caused it clears | An ongoing state, including offline while cached data remains visible |

- **2 s**: a fast read, the user moves on. Shorter feels skipped.
- **8 s**: the floor for something the user must read *and* tap.
- **No auto-dismiss** only when a state clears it or the user taps ✕.
- Tapping the action runs it **and dismisses the toast**.
- **With VoiceOver running, a toast with an action never auto-dismisses**
  (§8, VoiceOver). Informational toasts keep their 2 s timer.

## 5. Placement and stacking

**Bottom only.** Never top, never middle.

**Decided bottom clearance (D29):** the toast's bottom edge sits `space/16` above the highest bottom element
that is showing, in this order. Sides stay `space/8`. Same as the Android skill:

| Bottom of the screen has… | Toast sits `space/16` above… |
|---|---|
| Keyboard open | the top of the keyboard (and above the sticky CTA bar riding on it) |
| Sticky CTA bar (`wiom-ios-cta`) | the top edge of the CTA bar |
| Navigation bar (`wiom-ios-navigation-bar`, if used) | the top edge of the navigation bar |
| Nothing | the bottom safe-area edge (the home indicator on Face ID iPhones; the screen edge on Home-button iPhones) |

**Stacking order (back to front):** screen content → sticky CTA bar →
**toast** → scrim → dialog or bottom sheet. The toast
never covers the CTA bar's buttons and never sits under them. Do not
show a toast while a dialog or modal sheet is up; queue it until the
modal closes (§7 rule 1).

## 6. Copy

- **Specific over generic.** "Couldn't send your request" beats "Error";
  "Complaint deleted" beats "Success" (illustrative).
- **No congratulatory copy.** No "Great!", "Awesome!", "Done!".
- **Positive sparingly**: only when the user genuinely needs the
  confirmation. Small money acknowledgements are allowed (§1).
- **1 line target, 2 lines max at the default text size** (about
  **80 Hindi grapheme clusters**). At larger text sizes the toast grows
  so the whole message shows; it is never cut off (D33). The toast
  never grows past 40 % of the screen height; the message scrolls
  inside it beyond that, so the CTA bar and content stay usable.
  Check both Hindi and English at the default text size: aim for about
  **40 grapheme clusters** of Hindi so one line holds on iPhone SE
  (counted with `String.count`; "क्षि" is one). Treat this number as a
  guide, not a hard limit (see Open questions).
- **Action label: one word where possible** ("Undo", "Retry", "View",
  illustrative), max **12 grapheme clusters**. It never truncates the
  message's room to zero; shorten the label instead.
- All copy above is illustrative. Real strings come from the string
  catalog.

## 7. Rules

1. **One toast at a time.** Never stack. A new toast queues (first in,
   first out) and shows only after the current one dismisses.
2. **Bottom only**, positioned per §5.
3. **No fixed width or height** on the toast. Width = screen minus
   `space/8` each side; height = minimum, from padding + content.
4. **The toast body is passive.** Only the action label and the ✕ are
   interactive. Never make the whole toast a button.
5. **Action is text only**, `type/label/lg` in `text/brand`. No filled
   button inside a toast.
6. **No retry loops.** One attempt, revert the state, show the toast;
   the user retries by tapping the action or the original control.
7. **Message fits 2 lines at default size** (about 80 Hindi grapheme clusters); at large text sizes the toast grows, never truncates (D33).
8. **Tokens only**, by DS V2 name. No raw colours.
9. **All four types use `bg/default`.** Never a solid status fill
   (`bg/critical`, `bg/warning`, …) or a tinted fill.
10. **Persistent toasts always show ✕.** A toast with no timer and no ✕
    is a stuck toast.
11. **No congratulatory copy.**

### Anti-patterns

- ❌ Toast replacing field validation, a required decision, or a receipt/result screen (§1).
- ❌ Auto-dismissing a Persistent toast.
- ❌ An Actionable toast that disappears while VoiceOver is running.
- ❌ A Positive toast after every action: it reads as noise.
- ❌ Two toasts on screen at once.
- ❌ Hard-coding a 344 pt (or any) width: iPhones range from 375 to
  440 pt wide.

## See also

- `wiom-ios-foundations`: `tokens.md`, `typography.md`, `icons.md`,
  `layout.md`, `accessibility.md`, `motion.md`.
- `wiom-ios-bottomsheet` § "Choosing a surface": the one surface-choice
  table.
- `wiom-ios-cta`: sticky CTA bar the toast stacks above; the toast's
  action borrows the brand colour but is text only.
- `wiom-ios-dialog`: modal halts; toasts wait until it closes.
- `wiom-ios-navigation-bar`: bottom bar the toast stacks above, if used.

## Open questions

1. **DECIDED (D31): Warning fill and icon colours.** Whole toast stays `bg/default`. Use dark `icon/action` on `bg/warning/subtle`, measured 10.85:1, and preserve the Material Rounded Warning glyph as decorative. This is the global Warning recipe, not a toast-only exception: inputs and Warning icon badges also use dark glyphs on the approved Warning backgrounds. Gold `icon/warning` is ratings-only. **Container (D35):** Icon Badge Sm, a 24 pt circle with a 16 pt glyph (`wiom-ios-icon-badge`). The Warning glyph is intentionally smaller than the 24 pt Critical / Info / Positive glyphs; the circle keeps the same 24 pt footprint so the row height and alignment match.
2. **DECIDED: horizontal and bottom margins.** Owner commit `23f67f9` locks `space/8` horizontally (flexible width). D29 locks `space/16` above the highest safe-area / CTA-bar / keyboard boundary, matching the Android skill.
3. **Easing: Android vs skill.** The skill (§11) and the motion
   doctrine (D-3 ruling) specify 300 ms `EaseOut` in / `EaseIn` out;
   Android ships `tween(300)` with the default standard curve, plus a
   fade, both ways (`WiomToast.kt:256-263`). iOS follows Android
   (`motion/surface`, `ease/standard`). Confirm whether Android will be
   moved to EaseOut / EaseIn; iOS will follow.
4. **Hit area of action and ✕.** The skill wraps both in a ≥ 48 pt
   interactive box; Android ships only `space/8` × `space/4` padding on
   the action and none on ✕ (`WiomToast.kt:133-148`). iOS uses the
   44/48 pt hit area (D14), which changes no visual. Android should add
   the minimum interactive size.
5. **Toast while a modal is open.** Android's toast lives in the
   screen's `Scaffold`, so a modal sheet or dialog covers it. iOS
   queues toasts until the modal closes (§5). Confirm, or name the
   cases (for example "Copied" from inside a sheet) where the toast
   should show above the modal.
6. **Message length guide.** The source gives no grapheme number for
   the message; "about 40 Hindi grapheme clusters per line on iPhone
   SE" and "action ≤ 12" are iOS defaults. The design team to confirm
   or replace.
7. **VoiceOver ✕ on Actionable toasts.** Showing ✕ on Actionable toasts
   only while VoiceOver runs is a behaviour-only addition (it adds a
   visible glyph for VoiceOver users). Confirm this is acceptable, or
   rely on the escape gesture alone.

## iOS (SwiftUI, iOS 16+)

- **Built from:** `WiomToast` is an `HStack(alignment: .center,
  spacing: space/8)` of icon `Image` (template, asset
  `ic_rounded_error` / `ic_rounded_warning` / `ic_rounded_info` /
  `ic_rounded_check_circle`), message `Text`, optional action `Button`
  (plain style, text label), optional close `Button`. Background is a
  `RoundedRectangle(cornerRadius: radius/small, style: .circular)`
  filled `bg/default` with `.wiomShadow(.lg)`. `WiomToastHost` is an
  `ObservableObject` queue plus an overlay view that the screen (or the
  app root) attaches once with `.overlay(alignment: .bottom)`.
- **Tokens:** `bg/default`, `bg/warning/subtle`, `icon/action`, `icon/critical`,
  `icon/info`, `icon/positive`, `icon/action`, `text/default`,
  `text/onWarning`, `text/brand`, `type/body/lg`, `type/label/lg`,
  `radius/small`, `shadow/lg`, `space/4`, `space/8`, `space/12`,
  `space/16`, `icon/md` (size), `motion/surface`, `motion/micro`,
  `ease/standard`. Swift names per `IOS_DECISIONS.md` §2
  (`Wiom.Colors.textOnWarning`, `Wiom.Typography.bodyLg`, …).
- **Size:** width = container width minus `space/8` each side (never a
  number). Height is a minimum: 48 pt at default size with one line.
  Icon and ✕ glyphs are fixed 24 pt (non-text glyphs, D16).
- **Dynamic Type:** message and action scale with their type tokens
  (anchors in `wiom-ios-foundations` `typography.md` §3). The toast
  grows taller and the message wraps fully (no line limit, D33); keep
  copy within the 2-line default-size guide so large sizes stay compact. Through the
  accessibility3 cap, the action label keeps its full width
  (`.fixedSize()` + `.layoutPriority(1)`) and the message gives way.
  Glyphs do not scale. Check Hindi and English.
- **VoiceOver:**
  - **Announced on appear:** post
    `UIAccessibility.post(notification: .announcement, argument: text)`
    where `text` is the message, plus the action label for Actionable
    ("Complaint deleted. Undo available", illustrative, from the string
    catalog). Post it a moment after the toast is on screen
    (`DispatchQueue.main.asyncAfter(deadline: .now() + 0.1)`), because
    announcements made during a screen change can be dropped.
  - Icon and message are **one element**
    (`.accessibilityElement(children: .combine)` on the icon + message
    group; icon `.accessibilityHidden(true)`). The action and ✕ are
    separate buttons (`.accessibilityAddTraits(.isButton)` comes with
    `Button`). ✕ label: "Close" from the string catalog.
  - **When `UIAccessibility.isVoiceOverRunning` is true, toasts with an
    action do not auto-dismiss.** They stay until the user taps the
    action, taps ✕, or uses the escape gesture (two-finger Z,
    `.accessibilityAction(.escape)`). Show the ✕ on these toasts so a
    VoiceOver user always has a visible way out. Re-check the flag when
    `UIAccessibility.voiceOverStatusDidChangeNotification` fires.
  - Focus is not moved to the toast (announcement only), so the user's
    place on the screen is kept.
- **Hit area:** the action label and ✕ each get a hit area of at least
  44 × 44 pt, default 48 × 48 (`.frame(minWidth: 48, minHeight: 48)` +
  `.contentShape(Rectangle())`, D14), while their visible size stays as
  in §2. The hit areas may extend into the toast's padding, never past
  the toast's edge. Pressed state: Android has no pressed visual on the
  action or ✕, so iOS has none either (D13); use a `ButtonStyle` that
  ignores `isPressed`.
- **Motion:** enter = slide up from below its own height + fade in;
  exit = slide down + fade out; `motion/surface` (300 ms) with
  `ease/standard`, matching what Android ships. **Reduce Motion**
  (`@Environment(\.accessibilityReduceMotion)`): no slide; a
  `motion/micro` cross-fade in and out (D20). Timers are unchanged by
  Reduce Motion.
- **Safe areas and keyboard:** the host respects the bottom safe area
  and the keyboard safe area (do not apply `.ignoresSafeArea(.keyboard)`
  to it), so the toast rides `space/16` above the keyboard when it is
  open and `space/16` above the home-indicator safe area otherwise. On a
  screen with a sticky CTA bar, the host is attached
  above that bar (or pads by its height) so the toast sits `space/16`
  above it (§5). The toast's shadow may spill into the margin; the
  toast itself never enters the home-indicator area.
- **Haptics:** none (D21). Android plays none on toasts, including
  Critical and Positive.
- **Not on iOS:** a platform snackbar slot, system back to
  dismiss, ripple, swipe-to-dismiss (Android does not ship it either),
  top-of-screen placement, `UIAlertController` or system banners as a
  substitute.

### Snippets

Host: one at a time, FIFO, timer rules including VoiceOver. Timer cancellation and delayed announcements are scoped to a presentation identity, not the copy string: an old callback must never dismiss or announce a replacement, including one with identical text. Hiding or dismissing invalidates that identity; timers follow the existing behaviour policy, not a new lifecycle duration.

```swift
@MainActor
final class WiomToastHost: ObservableObject {
    @Published private(set) var current: WiomToastMessage?
    private var queue: [WiomToastMessage] = []
    private var timer: Task<Void, Never>?
    private var modalPresented = false
    private var presentationID = UUID()

    // Call from the overlay presenter before a modal appears.
    func modalWillPresent() {
        modalPresented = true
        presentationID = UUID() // Invalidate callbacks for the hidden presentation.
        timer?.cancel()
        if let message = current { queue.insert(message, at: 0) }
        current = nil
    }

    func modalDidDismiss() {
        modalPresented = false
        showNext()
    }

    // Connect to UIAccessibility.voiceOverStatusDidChangeNotification
    // on the main actor. Turning VoiceOver on cancels action-toast expiry.
    func voiceOverStatusChanged() {
        timer?.cancel()
        guard let message = current else { return }
        armTimer(for: message)
    }

    func show(_ message: WiomToastMessage) {
        queue.append(message)
        if current == nil { showNext() }
    }

    func dismiss() {
        presentationID = UUID()
        timer?.cancel()
        current = nil
        showNext()
    }

    private func showNext() {
        guard !modalPresented, current == nil, !queue.isEmpty else { return }
        let next = queue.removeFirst()
        presentationID = UUID()
        current = next
        announce(next, id: presentationID)
        armTimer(for: next)
    }

    private func armTimer(for message: WiomToastMessage) {
        guard let seconds = message.autoDismissSeconds(
            voiceOverRunning: UIAccessibility.isVoiceOverRunning
        ) else { return }                       // Persistent, or action + VoiceOver
        let id = presentationID
        timer = Task { [weak self] in
            do { try await Task.sleep(nanoseconds: UInt64(seconds * 1_000_000_000)) }
            catch { return }
            guard !Task.isCancelled, let self, self.presentationID == id else { return }
            self.dismiss()
        }
    }

    private func announce(_ message: WiomToastMessage, id: UUID) {
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) { [weak self] in
            guard let self, self.presentationID == id, self.current != nil,
                  !self.modalPresented else { return }
            UIAccessibility.post(notification: .announcement,
                                 argument: message.spokenText)
        }
    }
}

extension WiomToastMessage {
    /// 2 s Informational · 8 s Actionable · nil Persistent.
    /// With VoiceOver running, any toast with an action stays.
    func autoDismissSeconds(voiceOverRunning: Bool) -> Double? {
        if action != nil && voiceOverRunning { return nil }
        switch behavior {
        case .informational: return 2
        case .actionable:    return voiceOverRunning ? nil : 8
        case .persistent:    return nil
        }
    }
}
```

Placement and motion, Reduce Motion aware:

```swift
struct WiomToastOverlay: View {
    @ObservedObject var host: WiomToastHost
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        VStack {
            Spacer()
            if let message = host.current {
                WiomToast(message: message,
                          onAction: { message.action?.run(); host.dismiss() },
                          onClose: { host.dismiss() })
                    .padding(.horizontal, Wiom.Spacing.s8)
                    .padding(.bottom, Wiom.Spacing.s16)
                    .transition(reduceMotion
                        ? .opacity
                        : .move(edge: .bottom).combined(with: .opacity))
                    .id(message.id)
            }
        }
        .animation(reduceMotion ? Wiom.Motion.microStandard : Wiom.Motion.surfaceStandard,
                   value: host.current?.id)
    }
}
```

`Wiom.Motion.microStandard` and `Wiom.Motion.surfaceStandard` stand for the
`Animation` values built from `motion/micro` and `motion/surface` +
`ease/standard` in `wiom-ios-foundations` `motion.md`; use whatever that
file names them.
