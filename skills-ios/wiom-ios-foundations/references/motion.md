# Motion tokens (iOS)

The values below are the **single definition** of Wiom motion tokens on iOS. They are the Android values (`wiom-motion` §2) written as cubic Bézier curves and spring numbers, so the same token moves the same way on both platforms. Figma has no motion variables yet (decisions Q4); when it does, Figma becomes the source and this table follows it.

When to use which token, and the idioms built from them: `wiom-ios-motion`.

---

## 1. Durations

| Token | Swift (`TimeInterval`) | Value | Use |
|---|---|---|---|
| `motion/instant` | `Wiom.Motion.instant` | 0 s | Deliberate no-motion (data refresh in place, skeleton entry) |
| `motion/micro` | `Wiom.Motion.micro` | 0.2 s | Chevron rotation, icon state, colour/opacity ticks, dialog fade |
| `motion/surface` | `Wiom.Motion.surface` | 0.3 s | Sheet and overlay enter/exit, skeleton → content, colour cross-fades |
| `motion/emphasis` | `Wiom.Motion.emphasis` | 0.45 s (ring draw-on) · 0.6 s (progress fill) | Per segment on the dominant stroke |

The Android token `motion.page` (300 ms page cross-fade) **does not exist on iOS**: page changes use system push/pop (D6).

## 2. Easing curves

| Token | Swift | Cubic Bézier (x1, y1, x2, y2) | Compose name |
|---|---|---|---|
| `ease/standard` | `Wiom.Easing.standard` | 0.4, 0, 0.2, 1 | FastOutSlowIn |
| `ease/enter` | `Wiom.Easing.enter` | 0, 0, 0.2, 1 | LinearOutSlowIn |
| `ease/exit` | `Wiom.Easing.exit` | 0.4, 0, 1, 1 | FastOutLinearIn |
| `ease/linear` | `Wiom.Easing.linear` | 0, 0, 1, 1 | Linear (**loops only**) |

## 3. Spring

| Token | Swift | Value | Compose equivalent |
|---|---|---|---|
| `spring/settle` | `Wiom.Motion.settle` | `.interpolatingSpring(mass: 1, stiffness: 400, damping: 40, initialVelocity: 0)` | `spring(stiffness = StiffnessMediumLow)`, damping ratio 1.0 |

Critically damped: no overshoot. `.spring(duration:bounce:)` is iOS 17+ and not used while the floor is iOS 16.

## 4. Composed animations (call these, never the numbers)

| Swift | = |
|---|---|
| `Wiom.Motion.microStandard` | `.timingCurve(0.4, 0, 0.2, 1, duration: 0.2)` |
| `Wiom.Motion.surfaceStandard` | `.timingCurve(0.4, 0, 0.2, 1, duration: 0.3)` |
| `Wiom.Motion.surfaceEnter` | `.timingCurve(0, 0, 0.2, 1, duration: 0.3)` |
| `Wiom.Motion.surfaceExit` | `.timingCurve(0.4, 0, 1, 1, duration: 0.3)` |
| `Wiom.Motion.emphasisEnter` | `.timingCurve(0, 0, 0.2, 1, duration: 0.45)` |
| `Wiom.Motion.fill` | `.timingCurve(0.4, 0, 0.2, 1, duration: 0.6)` |
| `Wiom.Motion.settle` | spring above |

Component-owned timings (toast slide and timers, loader loops) are defined in their component skills, not here.

## 5. Reduce Motion form of each token (D20)

Read `@Environment(\.accessibilityReduceMotion)`.

| Motion | Reduced form |
|---|---|
| Slide, move, scale (sheet, toast, step change, reveal) | Cross-fade on `Wiom.Motion.microStandard`, opacity only |
| `spring/settle` reveal | `microStandard` fade; layout jumps to the end state |
| Draw-on ring, progress fill, count-up | Jump to the end value (`motion/instant`) |
| Colour and opacity changes | Unchanged (they are not motion) |
| Loops: shimmer, dots, brand loader, pulses | Stop on a static frame |
| Spinner | Keeps rotating: it is the only "working" signal |
| System push/pop, system sheets | iOS handles them; don't override |
