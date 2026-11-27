---
name: wiom-ios-motion
description: "Wiom motion rules for the iOS customer app in SwiftUI: which motion token and idiom each change uses, system push/pop with swipe-back, sheet, dialog and overlay enter/exit, in-screen idioms (expand/collapse, reveal with its exit pair, step change, confirmation success motif, skeleton resolve), the Reduce Motion form of each, and the SwiftUI Animation mapping. Use when specifying, implementing or reviewing a transition or animation in SwiftUI for Wiom."
---

# Wiom motion (iOS customer app)

**Applies to:** the native iOS customer app (SwiftUI, iPhone only, iOS 16+). Binding contract: [`IOS_DECISIONS.md`](../IOS_DECISIONS.md) (D6 page transitions, D10 custom sheet, D20 Reduce Motion, D21 haptics). When this file and `IOS_DECISIONS.md` disagree, `IOS_DECISIONS.md` wins.

**Rulings:** locked 26 Aug 2026 by the design lead; this iOS doctrine derives from them.

**Tokens are owned by foundations.** Durations, curves and the spring are defined in [`wiom-ios-foundations/references/motion.md`](../wiom-ios-foundations/references/motion.md). This skill cites them by name. Section 2 lists names only; foundations owns every value.

## 1. Principles

1. **Motion states meaning, never decoration.** A transition answers "where did this come from" or "what changed". If removing the motion loses no meaning, remove it.
2. **Calm by default.** Customers are often paying, waiting on an install or fixing a broken connection. Motion never adds urgency: nothing pulses, bounces or celebrates.
3. **Cheap transforms only.** Animate opacity, offset, scale and rotation. Never animate blur or materials, never animate the height of a long list, never drive layout every frame.
4. **One motif per meaning.** Expand, success and loading each move the same way everywhere in the app.
5. **Component-internal motion lives in the component's own skill.** [`wiom-ios-toast`](../wiom-ios-toast/SKILL.md) (enter/exit and its timers), [`wiom-ios-loader`](../wiom-ios-loader/SKILL.md) (spinner, linear, dots, skeleton shimmer, brand loops) and [`wiom-ios-progress-indicator`](../wiom-ios-progress-indicator/SKILL.md) (fills, count-up) are authoritative for their components. Where this file mentions them it is a pointer, not a rule; cite the component skill. This file governs everything else: pages, sheets, dialogs, overlays, steps, in-screen idioms, and how loading states arrive and resolve.

## 2. Tokens

Use the duration, easing, spring and SwiftUI helper definitions in [foundations motion](../wiom-ios-foundations/references/motion.md). Tokens: `motion/instant`, `motion/micro`, `motion/surface`, `motion/emphasis`, `ease/standard`, `ease/enter`, `ease/exit`, `ease/linear`, `spring/settle`. No iOS page token: navigation uses system push/pop. An untokened motion is a gap under D24.

## 3. Page-to-page transitions

- **R3.1 System push/pop.** Every page change inside the app uses `NavigationStack` push and pop with the system slide and the **interactive edge-swipe-back**. Never replace it with a cross-fade, a custom slide or a `matchedGeometryEffect` hero. The Android rule "page transitions are cross-fade only" is Android-only (D6).
- **R3.2 Swipe-back must survive the custom top bar.** The app hides the system navigation bar for the Wiom top bar (D7). Hiding the system back button disables the interactive pop gesture unless the app restores it; the top-bar host must keep it working (see [`wiom-ios-top-bar`](../wiom-ios-top-bar/SKILL.md)). A pushed screen where swipe-back does nothing is a defect.
- **R3.3 Don't fight the system.** No `Transaction(disablesAnimations:)`, `.animation(nil)` or `UIView.setAnimationsEnabled(false)` around navigation. iOS owns push/pop timing and its Reduce Motion form.
- **R3.4 Full-screen covers.** A full-screen surface either uses the system `fullScreenCover` transition (slide up from the bottom, as iOS draws it; do not customise it) or is an app-drawn overlay in a `ZStack` above the `NavigationStack` that fades in and out on `motion/surface` `ease/standard`. Never mount or unmount an overlay instantly.

## 4. Surface enter/exit

| Surface | Motion |
|---|---|
| Bottom sheet (custom Wiom sheet, D10) | Sheet slides up from the bottom edge, scrim fades in, both `motion/surface` `ease/standard`. Exit mirrors it. During a drag-down the sheet follows the finger with no animation; on release it either completes the dismissal or snaps back, `motion/surface` `ease/standard`. |
| Dialog (Wiom dialog, D9) | Fade in/out `motion/micro` `ease/standard`; the scrim fades with it. No scale-up. |
| Toast | Per [`wiom-ios-toast`](../wiom-ios-toast/SKILL.md). Cite that skill, never a copy here. |
| App-drawn full-screen overlay | Fade in/out `motion/surface` `ease/standard` (R3.4). |
| Dialog over sheet (sheet over sheet is prohibited) | The top surface animates per its own row; the surface below does not move. |

Present and dismiss surfaces with `withAnimation(...)` on the state that shows them, so the scrim and the surface share one transaction.

## 5. In-screen idioms

### 5.1 Expand/collapse (accordions, drill-downs)
- Chevron rotates 0° → 180° on `motion/micro` `ease/standard` (`.rotationEffect`).
- The body is inserted/removed under `withAnimation(spring/settle)`: `.transition(.opacity.combined(with: .move(edge: .top)))` inside a `.clipped()` container, so rows below slide with the layout change.
- The most repeated idiom in the app: keep it exactly. Never on a long list (principle 3).

### 5.2 Reveal-on-condition (a CTA or field appears when a gate passes)
- Fade + move on `spring/settle`: `.transition(.move(edge: .bottom).combined(with: .opacity))`.
- **Every reveal defines its exit pair.** The element leaves the same way when the gate closes again (the symmetric transition above, or an explicit `.asymmetric(insertion:removal:)`). An enter-only reveal that vanishes instantly is a defect.

### 5.3 Step change inside one route (steps that are not navigation destinations)
- Directional slide + fade, `motion/surface` `ease/standard`. Forward: new step comes in from one third of the width on the trailing side while the old one leaves one third toward the leading side, both fading. Back: mirrored.
- Implement with the step as the view identity (`.id(step)`) and an `.asymmetric` transition built from `.offset(x: ±width / 3)` + `.opacity`, chosen by direction. Width comes from the container.
- If the step is a real destination (it has its own back-swipe), it is a push (§3), not this idiom. Instant step swaps are a defect.

### 5.4 Value and colour state change (selected, confirmed)
- Colour, fill and opacity changes animate on `motion/micro` `ease/standard`, attached with `.animation(Wiom…, value: state)`.
- Selection commits immediately; the visual interpolation must not delay interaction, accessibility state or data updates. Keep the control identity stable, use an animation bound to the selected value, and allow a new tap to reverse from the current presentation value. Do not rebuild or change `.id` on the selected control. Chips, tabs, filters, checkboxes, radios and selected list-row backgrounds use their component rules (D28); switch thumb movement remains component-owned. Animate only the changed properties, never a blanket animation on the whole screen or row layout.
- Every selection fade (checkbox, radio, switch stroke, chip, pill tab, underline and list row) interpolates between the colour and that same colour at opacity 0, for example `Wiom.Colors.bgSelected.opacity(0)`, never `.clear`; this preserves the colour through the fade.
- Both selection and deselection use the same token. Retain colour/opacity fades with Reduce Motion; remove spatial movement. Pressed CTA feedback and data refresh remain instant under their existing rules.
- Numbers do not roll. Any proposed progress count-up is owned by [`wiom-ios-progress-indicator`](../wiom-ios-progress-indicator/SKILL.md). Adding a count-up anywhere else needs a design ruling.

### 5.5 Success
The doctrine has two scoped success motifs. **On the customer app only the confirmation motif applies.**
- **Confirmation motif** (payment success, recharge done, plan change committed, receipt, step completion): the ring draws on over `motion/emphasis` (450 ms) `ease/enter` (`.trim(from: 0, to: progress)` on the stroke), then the approved Material Rounded check asset is revealed through a mask over `motion/surface`; never draw a custom check path. About 750 ms in total. Never bouncy, never scaled up. The receipt or confirmation text is visible from the start; motion never delays it.
- **Celebration motif** (bouncy spring circle-and-check pop): **unused on the customer app.** It is scoped to partner milestones, and money and commit surfaces always use the confirmation motif. A customer moment that seems to need celebration goes to the design team as a gap.

### 5.6 Loading enter and resolve
- A skeleton **enters instantly** (`motion/instant`): never delay showing that work started.
- Skeleton → content **resolves with a cross-fade** on `motion/surface` `ease/standard`.
- A spinner appears instantly; what replaces it cross-fades on `motion/surface`.
- The loops themselves (spinner rotation, shimmer sweep, brand loop, dots) are owned by [`wiom-ios-loader`](../wiom-ios-loader/SKILL.md); progress fills by [`wiom-ios-progress-indicator`](../wiom-ios-progress-indicator/SKILL.md).

### 5.7 Data changes in place
List reorders, pull-to-refresh results and server re-renders use `motion/instant` by default: no row insertion animation, no shuffle.

### 5.8 App animations (approved, as shipped) (D38)

These Lottie files already ship in the app and stay as they are. Use them only for the moment listed; no new animations without design.

| File | Used for | Plays | Reduce Motion |
|---|---|---|---|
| `loader_infinity` | Brand loader (`wiom-ios-loader`, D37) | loop | static frame |
| `payment_loading` | Payment in progress | loop | static frame |
| `payment_failed` | Payment failed | once | final frame |
| `location_checking_loader` | Checking location / serviceability | loop | static frame |
| `location_marker_pin_loop` | Location pin on the map step | loop | static frame |
| `confetti` | Celebration after a completed milestone | once | skip (no motion) |
| `clapping` | Appreciation moment | once | final frame |
| `thumbs_up_animation` | Positive confirmation | once | final frame |
| `update_success` | App / plan update done | once | final frame |
| `chat_typing_dots` | Chat typing indicator | loop | static dots |

Files are Android's, byte for byte. Decorative: hidden from VoiceOver; the screen text carries the meaning.

## 6. Reduce Motion

Read it with `@Environment(\.accessibilityReduceMotion) private var reduceMotion` and choose the reduced form **at the call site**; never ignore it. Meaning must survive with motion reduced or off.

| Token / idiom | Default | Reduce Motion form |
|---|---|---|
| `motion/instant` | 0 ms | Unchanged |
| `motion/micro` fades and colour ticks | Cross-fade / colour | Unchanged (already a cross-fade) |
| Chevron rotation | Rotate 200 ms | Snaps to the end angle; the body reveal carries the meaning |
| `motion/surface` slides (sheet, step change) | Slide + fade | `motion/micro` cross-fade in place, no offset. A drag-down on the sheet still follows the finger (user-driven, not animation) |
| Dialog, overlay, skeleton resolve fades | Fade | `motion/micro` cross-fade |
| `spring/settle` reveals (expand, reveal-on-condition) | Spring move + fade | `motion/micro` cross-fade, opacity only; layout jumps to its end |
| Scales | Scale | `motion/micro` cross-fade |
| `motion/emphasis` draw-on (confirmation ring, check) | Draw over ~750 ms | Shown at the end value (ring closed, check drawn), optionally faded in on `motion/micro` |
| Progress fill, count-up | Animated | Jump to the end value (per wiom-ios-progress-indicator) |
| `ease/linear` loops (shimmer, brand loop, dots) | Loop | Stop at a static frame (per wiom-ios-loader) |
| Spinner | Rotates | **Keeps rotating**: the only signal that work is happening |
| Toast | Per wiom-ios-toast | Per wiom-ios-toast |
| `NavigationStack` push/pop, swipe-back, `fullScreenCover` | System | System: iOS applies its own reduced form. Do nothing |

```swift
@Environment(\.accessibilityReduceMotion) private var reduceMotion

var revealTransition: AnyTransition {
    reduceMotion ? .opacity : .move(edge: .bottom).combined(with: .opacity)
}
var revealAnimation: Animation {
    reduceMotion ? Wiom.Motion.microStandard : Wiom.Motion.settle   // helpers per §7
}
```

## 7. SwiftUI mapping

Every animation is **explicit**: a Wiom token passed in code. Never rely on a library or system default (`.default`, bare `.easeInOut`, `.spring()` with no arguments, `.animation(_:)` without `value:`), so an OS or library upgrade can't silently change the app's motion.

Use the composed `Wiom.Motion` helpers defined in foundations. Implement each helper once in the design-system module, never repeat curve or spring numbers at call sites. The iOS 16 spring helper is the foundations `interpolatingSpring` mapping.

Patterns:

```swift
// Present a surface: state change and transition share one transaction
withAnimation(Wiom.Motion.surfaceStandard) { isSheetShown = true }

// Reveal-on-condition with its exit pair
if canContinue {
    WiomButton(...)
        .transition(.move(edge: .bottom).combined(with: .opacity))
}
// driven by: withAnimation(Wiom.Motion.settle) { canContinue = gatePassed }

// Value / colour change bound to its state
.animation(Wiom.Motion.microStandard, value: isSelected)
```

## 8. Haptics

**None** (D21): no haptic on taps, success, errors or any transition. Add one only where a component skill names it.

## 9. Anti-patterns

- **A9.1** No per-screen motion invention: tokens and idioms above, or a reported gap. Never an inline duration, curve or spring.
- **A9.2** No implicit or default animations (§7). No `.animation(_:)` without `value:`.
- **A9.3** No custom page transitions, cross-fade navigation or cross-page hero (`matchedGeometryEffect`) transitions; never disable swipe-back (§3).
- **A9.4** No infinite animation on a determinate state; fills are caller-driven (wiom-ios-progress-indicator).
- **A9.5** `ease/linear` only in loops, and loops only in loaders. No content loops: no pulsing dots, badges or CTAs.
- **A9.6** No celebratory motion anywhere on the customer app, and above all on money and commit surfaces; motion never delays a receipt or confirmation.
- **A9.7** No blur, material or shadow-radius animation; no height animation of long lists; no `GeometryReader`-driven per-frame layout.
- **A9.8** No motion on list reorders or feed refreshes by default (§5.7).
- **A9.9** No haptics (§8).
- **A9.10** No animation that ignores Reduce Motion (§6).

## Open questions

| # | Question | Until answered |
|---|---|---|
| Q4 | Will motion tokens become Figma variables? | Tokens live in `wiom-ios-foundations/references/motion.md` as cubic-Bézier values; this skill cites names only. |
| M1 | Does the iOS DS module ship the composed `Animation` wrappers (`Wiom.Motion.surfaceStandard`, `Wiom.Motion.settle`, …) or only durations and curves? | Treat §7 as the required set; wrapper names follow `IOS_DECISIONS.md` §2. |
| M2 | Does any customer-app moment need the celebration motif? | Unused (§5.5); raise a customer-app motion gap. |
| M3 | Easing for the confirmation check segment and the dialog fade is not stated in the locked rulings. | Check uses `ease/enter` (arrival), dialog uses `ease/standard`, pending design confirmation. |

## iOS (SwiftUI, iOS 16+)

- **Built from:** explicit SwiftUI `Animation`, transitions and environment Reduce Motion; `NavigationStack` owns push/pop.
- **Tokens:** `motion/instant`, `motion/micro`, `motion/surface`, `motion/emphasis`, `ease/standard`, `ease/enter`, `ease/exit`, `ease/linear`, `spring/settle`.
- **Size:** animation never imposes fixed text heights or device widths; component minimums remain in pt.
- **Dynamic Type:** evaluate the final layout in Hindi and English through accessibility3 before animating it.
- **VoiceOver:** semantic state changes remain understandable without watching motion; surface skills own focus and announcements.
- **Hit area:** ≥ 44 × 44 pt on interactive hosts; animations must not create overlapping targets.
- **Motion:** foundations defines values; §3–§7 define usage. Reduce Motion replaces slides/scales with `motion/micro` fades, jumps draw-on/count-up to the end and stops loops except spinners.
- **Safe areas and keyboard:** animate within device-safe layout; keyboard transitions remain system owned.
- **Haptics:** none.
- **Not on iOS:** Android page cross-fades, hover, press effects, hardware back, status-bar colour and focus rings.
