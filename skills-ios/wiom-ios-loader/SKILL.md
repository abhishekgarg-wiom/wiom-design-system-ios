---
name: wiom-ios-loader
description: >
  Wiom loader for the SwiftUI iOS customer app: the spinner, the
  short-wait linear bar, the chat typing dots, skeleton placeholders
  and the full-screen brand loader, for activity waits (including the short-wait Linear transfer fraction). Use when a button, field, card, list, chat or whole
  screen in the iOS app must show that work is under way and there is
  no value to report; for determinate progress toward a known target,
  use wiom-ios-progress-indicator instead.
---

# Wiom loader (iOS): five loaders for five kinds of wait

A loader normally says **that** work is happening. For state-coloured completion, percentages toward a goal or step trackers, use `wiom-ios-progress-indicator`. The short-wait Linear loader also supports a determinate transfer fraction (§4); that is the explicit exception.

| Loader | Variants | Use for |
|---|---|---|
| **Spinner** | 3 sizes (sm 20 · md 32 · lg 48) × 3 tones (Brand · Neutral · OnColor) | Inline and section waits where the layout is already on screen |
| **Linear** | Indeterminate · Determinate | A thin 4 pt bar across the top of a surface for a short wait (≤ 5 s) |
| **Dots** | Brand · Neutral · OnColor | Chat: the assistant or an agent is composing a reply |
| **Skeleton** | Line · Card · ListItem, each Shimmer or Static | Content whose layout is known but whose data hasn't arrived |
| **Brand** | Light · OnBrand · Overlay | Cold start / branded splash, or an explicitly specified full-screen branded wait |

Every loader is **indicator-only**: it draws the wait and nothing else. Message text, surface chrome (dialog, toast, card, chat bubble row) and any Cancel action belong to the parent. The one exception is Brand, which has its own message slot.

All values are tokens from `wiom-ios-foundations` (`references/tokens.md`, `typography.md`, `motion.md`). Swift names follow `wiom-ios-foundations/references/decisions.md` §2.

## 1. Loader or progress indicator?

| The app knows… | Use |
|---|---|
| Nothing about how long it will take | **This skill** (Spinner, Linear Indeterminate, Dots, Skeleton, Brand) |
| A fraction for a **short** wait (≤ 5 s, e.g. a receipt downloading) and only needs a thin brand bar | **Linear Determinate** (this skill; brand colour only) |
| A value toward a target the customer cares about (installation stages, recharge steps, profile completion) | **`wiom-ios-progress-indicator`** (state-coloured, with titles, stages and values) |

When in doubt between Linear Determinate and a progress indicator, use the progress indicator.

## 2. Picking the right loader

| Wait | Layout known? | Weight | Use |
|---|---|---|---|
| < 1 s inside a button | n/a | Low | The button's own Loading state (`wiom-ios-cta`). Don't place a spinner yourself. |
| < 1 s inside a field (validating a number) | n/a | Low | **Spinner sm**, Neutral, in the field's trailing slot (`wiom-ios-input-fields`) |
| 1–3 s, a card, section or dialog body | No | Low–mid | **Spinner md**, centred in that surface |
| 1–3 s, a list, card or text block | **Yes** | Low | **Skeleton** (ListItem × N for lists, Card for cards, Line for text) |
| ≤ 5 s, top of a surface | n/a | Low | **Linear** (Indeterminate without a signal, Determinate with one) |
| Chat reply being composed | n/a | n/a | **Dots** (Brand for the assistant, Neutral for a human agent, OnColor inside a brand bubble) |
| Cold start, post-login splash | n/a | n/a | **Brand** Light or OnBrand |
| Blocking foreground work: processing payment, syncing or submitting | n/a | **High** | **Loading dialog** (`wiom-ios-dialog`) with Spinner sm and an error/timeout path; no duration cutoff |

### Don't use a loader when

| Moment | Use instead |
|---|---|
| A list that will never have data | Empty state, not Skeleton |
| A field failed validation | The field's error state (`wiom-ios-input-fields`) |
| A background refresh the customer doesn't need to see | Nothing; show cached data and update in place |
| Progress toward a named target (installation, recharge steps) | `wiom-ios-progress-indicator` |
| Saying a finished wait succeeded ("Saved") | `wiom-ios-toast`; never leave a loader up after the wait ends |

## 3. Spinner

A full-ring **track** plus a **270° arc** with round caps, both on the same circle (inset by half the stroke so nothing clips). The arc starts at 12 o'clock and turns clockwise. Background is transparent.

| Size | Box | Stroke | Typical host |
|---|---|---|---|
| `sm` | 20 × 20 pt | 2 pt | Field trailing slot, compact row |
| `md` | 32 × 32 pt | 3 pt | Card, dialog, section (default) |
| `lg` | 48 × 48 pt | 4 pt | Hero, centre of a screen, Brand loader |

| Tone | Arc | Track | Where |
|---|---|---|---|
| Brand (default) | `bg/brand` | `bg/brand/subtle` | Light surfaces |
| Neutral | `text/subtle` | `stroke/subtle` | De-emphasised waits, field trailing slot |
| OnColor | `icon/inverse` | none | `bg/brand`, `overlay/scrim`, other filled surfaces |

Sizes are fixed glyph shapes (D16). Pick a size; never scale a spinner with `.frame` or `.scaleEffect`. The spinner inside a CTA is owned by `wiom-ios-cta` (24 pt, 2 pt stroke, as the Android button ships); see Open questions.

## 4. Linear

A **4 pt** bar that fills the width of its host (minus the host's gutter).

| Part | Token |
|---|---|
| Track | `bg/brand/subtle`, `Capsule()` |
| Fill | `bg/brand`, drawn as a plain rectangle **inside** the capsule-clipped track, so its leading end is rounded by the track and its trailing end is square (as Android) |
| Indeterminate | A segment 40 % of the track width travels leading → trailing, from −40 % to 100 %, clipped by the track |
| Determinate | Fill width = value × track width; moves to a new value with `motion/surface` · `ease/standard` |

The host owns the surface. Figma shows the bar inside a card only so it's visible on the canvas; the component is the bar alone. Brand colour only: the info / brand / positive ladder belongs to `wiom-ios-progress-indicator`.

## 5. Dots (chat typing)

Three 8 pt dots in a chat bubble.

| Part | Brand | Neutral | OnColor |
|---|---|---|---|
| Bubble fill | `bg/subtle` | `bg/subtle` | `bg/brand` |
| Dot fill | `bg/brand` | `text/subtle` | `icon/inverse` |

| Part | Value |
|---|---|
| Bubble corners | `radius/large` on top-leading, top-trailing, bottom-trailing; `radius/tiny` on bottom-leading (the tail) |
| Bubble padding | `space/12` horizontal; 10 pt vertical (as Android ships; no 10 token, see Open questions) |
| Dots | 8 × 8 pt circles, gap `space/4`, full opacity |
| Bounce | Each dot rises 3 pt and returns within the first 400 ms of a 1.0 s cycle; dots start 150 ms apart |

The bubble hugs its dots (56 × 28 pt as Android draws it). The bounce moves the dots only, never the bubble's size, so the chat list doesn't jump.

## 6. Skeleton

Placeholder blocks in `bg/muted` that mirror the layout about to load.

| Type | Anatomy |
|---|---|
| **Line** | One bar, `radius/tiny`, height 16 pt (a body line; a heading line may be taller). Width comes from the host. A text block is three Lines stacked with `space/8`, at 100 %, 75 % and 50 % of the width. |
| **Card** | `bg/default` container, `radius/large`, padding `space/16`; a 72 × 72 pt thumbnail (`radius/medium`) then, after `space/16`, three Lines (100 / 75 / 50 %, gap `space/8`), vertically centred. No border (as Android). |
| **ListItem** | Padding `space/16` horizontal, `space/12` vertical; a 40 pt circle, then two Lines (75 / 50 %, gap `space/8`), then a trailing 40 pt-wide Line; gaps `space/16`, vertically centred. Fills the width. |

| Animation mode | Look |
|---|---|
| **Shimmer** (default) | A soft band (transparent → `bg/default` at 55 % → transparent, 60 % of the block wide) sweeps leading → trailing across each block, 1.2 s loop |
| **Static** | Plain `bg/muted` blocks. Use on dense skeleton grids where moving shimmer feels noisy, and always under Reduce Motion |

Rules: the skeleton mirrors the real layout (same number of rows the result will most likely have, roughly the same sizes); never Skeleton for an empty state; replace it in one step when data arrives.

## 7. Brand

Full-screen. It covers the screen, swallows every touch, and centres a vertical stack with `space/16` between items.

| Part | Light | OnBrand | Overlay |
|---|---|---|---|
| Background | `bg/default` | `bg/brand` | `overlay/scrim` over the current screen |
| Wordmark "Wiom" | `type/heading/xl`, `text/brand` | `type/heading/xl`, `text/onBrand` | none (the screen behind gives context) |
| Mark | `loader_infinity` animation, 200 × 200 pt (D37) | same, 200 × 200 pt | same, 200 × 200 pt |
| Message (optional) | `type/body/md`, `text/subtle` | `type/body/md`, `text/onBrand` | `type/body/md`, `text/onBrand` |

**The mark is the `loader_infinity` animation (D37), played in a 200 × 200 pt frame**, as the app does. The file is a 1920 × 1080 canvas with wide empty margins, so never squeeze it into the 128 × 53 glyph size or it looks tiny. It is the infinity stroke-dash chase both apps already ship (`loader_infinity.json`, copied from the Android app), played with `lottie-ios` on a loop. Spinner lg is only the fallback if the file fails to load. Known differences for design to correct in the file later: 2.0 s loop (spec 1.3 s), pink #D92B90 (token `icon/brand` #D9008D), a light-grey track.

Brand Overlay is a full-screen branded-wait variant, not the required loader for payment. Blocking foreground work such as payment, syncing and submitting uses the Loading dialog (`wiom-ios-dialog`), without a duration cutoff. Routine inline waits use Spinner or Skeleton. Surface choice and the outcome follow `wiom-ios-bottomsheet` → Choosing a surface.

Message copy: one short sentence that says what is happening, from the string catalog (illustrative: "Processing your payment…"). It may wrap to two lines; it never truncates.

## 8. Motion and Reduce Motion

Loops use `ease/linear` (the only place it's used). Loop periods are component constants matching Android; they are not motion tokens.

| Loader | Normal | Reduce Motion (D20) |
|---|---|---|
| Spinner | Rotates clockwise, 1.0 s per turn | **Keeps rotating.** It is the only sign that work is happening. |
| Linear Indeterminate | Segment travels, 1.5 s loop | Stops: a static 40 % segment centred on the track (30–70 %) |
| Linear Determinate | Fill moves to the new value, `motion/surface` · `ease/standard` | Jumps to the new value |
| Dots | Staggered bounce, 1.0 s cycle | Stops: three dots at rest on the baseline |
| Skeleton | Shimmer sweep, 1.2 s loop | Static mode (no sweep) |
| Brand | `loader_infinity` loops | Paused on its static frame (the full infinity glyph) |
| Brand fallback (file fails to load) | Spinner lg rotates | Spinner keeps rotating |
| Show / hide any loader | Instant, as Android | Instant |

Read the setting with `@Environment(\.accessibilityReduceMotion)`; never cache it, as the customer can change it while the app runs.

## 9. Accessibility rules (every loader)

1. **Every visible loader that isn't inside another control has a spoken label** from the string catalog that names what is loading (illustrative: "Loading payment", "Loading plans"). Never a bare "Loading" when the screen has more than one thing that could be loading. Add `.updatesFrequently` to spinners, Linear and Brand so VoiceOver treats them as live.
2. **Spinners inside a host** (button, field trailing slot) are `.accessibilityHidden(true)`; the host speaks the state (`wiom-ios-cta`, `wiom-ios-input-fields`).
3. **Linear Determinate** reports its value: `.accessibilityValue` with the percentage from the catalog's percent format (illustrative: "40 percent").
4. **Skeleton**: the whole placeholder region is **one** VoiceOver element labelled "Loading" plus what is loading (illustrative: "Loading transactions"). Individual blocks are never focusable.
5. **Brand (all styles) and any full-screen or overlay wait block VoiceOver focus behind them**: the overlay is one element with `.accessibilityAddTraits(.isModal)`, the content behind is `.accessibilityHidden(true)` while the overlay shows, and VoiceOver focus moves to the overlay when it appears (post `.screenChanged`).
6. **Announce the end** when the screen does not change on completion (illustrative: "Payment received"); post `.announcement`. If the app navigates or shows an outcome sheet, that surface's own focus change is enough; don't announce twice.
7. **Dots**: one element on the chat row (illustrative label: "Wiom is typing"). Don't re-announce on every bounce.
8. **Not a control.** No loader has a tap action, a button trait, or a hit area. A Cancel action, if any, is a `wiom-ios-cta` on the parent.

## 10. Rules

1. Indicator-only. No message parameter except Brand; no background, border or shadow of its own except the Dots bubble and the Skeleton Card container, which are part of the indicator.
2. Fixed sizes. Spinner and Dots never resize; Linear and Skeleton fill the host's width.
3. One indicator per surface. Never a Spinner and a Linear in the same wait.
4. OnColor only on filled or dark surfaces (`bg/brand`, `overlay/scrim`). OnColor on `bg/default` is invisible.
5. Brand Light / OnBrand are for launch and branded splash. Brand Overlay is used only when the flow explicitly calls for a full-screen branded wait; processing payment can use the Loading dialog.
6. Never keep a loader past the wait. Remove it and route to the outcome.
7. Skeleton mirrors the post-load layout and row count.
8. Tokens only, by DS V2 name. No hex, no system colours, no `ProgressView` default look, no `UIActivityIndicatorView`.

### Anti-patterns

- System `ProgressView()` or `UIActivityIndicatorView` with its own look (wrong colours and stroke; looks different from Android).
- Scaling a spinner to an off-ladder size (28 pt) instead of picking sm / md / lg.
- A Skeleton assembled from loose `RoundedRectangle`s per screen (misses the shimmer, the Reduce Motion fallback and the single VoiceOver element).
- Brand Overlay for a routine list load.
- An overlay that blocks touches but leaves VoiceOver free to wander the screen behind it.
- Linear Determinate for installation or recharge steps: use `wiom-ios-progress-indicator`.

## 11. Customer-app examples (illustrative)

All copy below is illustrative; real strings come from the catalog (Hindi first, English written separately, sentence case).

| Moment | Loader |
|---|---|
| Customer taps "Pay" | The CTA's Loading state, or a Loading dialog "Processing your payment…" when foreground interaction must be blocked |
| Plans screen opening | Skeleton Card × 3 |
| Recharge history opening | Skeleton ListItem × the usual result count |
| Checking a mobile number typed into a field | Spinner sm, Neutral, trailing slot |
| Support chat: agent replying | Dots, Neutral |
| App cold start | Brand Light (no message, or "Getting things ready…") |
| Receipt PDF downloading | Linear Determinate at the top of the sheet |

## Open questions

1. **DECIDED (D37): brand-loader animation.** Use the shipped `loader_infinity.json` (both apps). Design to correct loop (2.0 s vs 1.3 s), pink (#D92B90 vs #D9008D) and the grey track in a later file; the Android library should bundle the same file.
2. **Dots vertical padding:** source and Android use 10 vertically (`WiomLoader.kt:473`) and 12 horizontally. The rejected builder copy changed vertical padding to 12. iOS keeps 12 × 10; there is no 10 token (gap per D24). Figma's bubble is 104 × 32; Android's hugs at 56 × 28.
3. **Skeleton shimmer:** Android 1.2 s with a `bg/default` 55 % band (`WiomLoader.kt:532`, `:551`); skill says 1.5 s, "`bg/muted` 10 % lighter". iOS follows Android.
4. **Skeleton Card border:** skill has 1 pt `stroke/subtle`; Android draws none (`WiomLoader.kt:200-205`). iOS follows Android.
5. **Skeleton ListItem trailing block:** skill 60 pt, Android 40 pt (`WiomLoader.kt:274-277`). Line widths: skill fixed 280 / 200 / 160, Android fractions 100 / 75 / 50 % (`WiomLoader.kt:227-229`, `:271-272`). iOS follows Android. Android's Line is a single bar; the skill's three-line "Line" type is a stack of three.
6. **Linear Determinate easing:** Android tweens 300 ms with linear easing (`WiomLoader.kt:399`); foundations keep `ease/linear` for loops, so iOS uses `motion/surface` · `ease/standard`. Confirm, or allow `ease/linear` here.
7. **Loop periods** (spinner 1.0 s, Linear 1.5 s, Dots 1.0 s / 150 ms stagger, shimmer 1.2 s) are not motion tokens. Should `motion.md` define loop tokens?
8. **Reduce Motion still for Linear Indeterminate:** a centred 40 % segment was chosen so it can't be read as "40 % done". Confirm.
9. **In-button spinner:** `wiom-ios-cta` uses 24 pt / 2 pt (as `WiomButton.kt` ships); this skill's sm is 20 pt. Same open point as `wiom-ios-cta` Open question 1.
10. **Brand message alignment:** Android doesn't centre-align the message text (`WiomLoader.kt:365-369`), so a two-line message is leading-aligned inside a centred column. The skill says centred. iOS follows Android; recommend both apps centre it.
11. **Two indeterminate bars on Android:** the loader's Linear (40 %, 1.5 s, `bg/brand/subtle` track) and `WiomLinearProgressIndeterminate` in the progress package (25 %, 1.4 s, `bg/muted` track; `WiomProgressIndicator.kt:115-159`). iOS ships only the loader's. Retire the other?
12. **Status loader** (wait → success / error ring): in old drafts, not shipped on Android. Not on iOS; outcomes use the outcome surface.

## iOS (SwiftUI, iOS 16+)

- **Built from:** `Circle().inset(by:).trim(from:to:).stroke(_:style:)` (spinner), `Capsule` + `Rectangle` (Linear), a small custom `Shape` for the Dots bubble (per-corner radii; `UnevenRoundedRectangle` is iOS 17), `RoundedRectangle(cornerRadius:style: .circular)` / `Circle` blocks with a `LinearGradient` overlay (Skeleton), `ZStack` + `.ignoresSafeArea()` (Brand). Loops are driven by `TimelineView(.animation)` so they never drift or stop on view reuse. Lottie, when it ships, via `lottie-ios` (`LottieView`). Accessibility (label, value, traits) is set explicitly so VoiceOver gets `ProgressView`-equivalent semantics.
- **Tokens:** `bg/brand`, `bg/brand/subtle`, `bg/subtle`, `bg/muted`, `bg/default`, `text/subtle`, `text/brand`, `text/onBrand`, `stroke/subtle`, `icon/inverse`, `overlay/scrim`, `type/heading/xl`, `type/body/md`, `space/4`, `space/8`, `space/12`, `space/16`, `radius/tiny`, `radius/medium`, `radius/large`, `motion/surface`, `ease/standard`, `ease/linear`.
- **Size:** Spinner 20 / 32 / 48 pt and Dots 8 pt are fixed glyph shapes (D16). Linear is 4 pt tall and fills the width. Skeleton fills the width; Card and ListItem heights are intrinsic. Brand fills the screen.
- **Dynamic Type:** only Brand holds text: the wordmark and message scale with their anchors in `typography.md` §3 and the message wraps (no line limit, never truncates). Check Hindi and English at xxxLarge and accessibility3. Skeleton line heights and row padding may use `@ScaledMetric(relativeTo: .body)` so the placeholder grows like the text it stands for; at the default size they equal the values above.
- **VoiceOver:** per §9: a catalog label on every free-standing loader; `.updatesFrequently` on Spinner, Linear and Brand; Linear Determinate value in percent; one element for a whole Skeleton region; Brand and overlays `.isModal` with the content behind hidden; announce completion when the screen doesn't change.
- **Hit area:** none; loaders are not tappable. Brand swallows all touches with its full-screen background (`.contentShape(Rectangle())`), so nothing behind it can be tapped.
- **Motion:** §8. Loops `ease/linear`; Linear Determinate `motion/surface` · `ease/standard`. Reduce Motion: Spinner keeps rotating; Linear, Dots, Skeleton and Lottie stop at a static frame; value changes jump.
- **Safe areas and keyboard:** Brand's background ignores all safe areas (it covers the status bar and home indicator); its content stays inside them. Dismiss the keyboard before showing Brand Overlay (it can't cover the keyboard). Status-bar content: dark on Light, light on OnBrand and Overlay (D8). Linear sits inside its host's safe area.
- **Haptics:** none (D21).
- **Not on iOS:** system `ProgressView` / `UIActivityIndicatorView` styling, Material progress indicators, ripple, touch-consuming tricks from Android, hardware back cancelling a wait, coloured status bar, SF Symbols in any loader (D4).

```swift
enum WiomSpinnerSize { case sm, md, lg
    var diameter: CGFloat { switch self { case .sm: 20; case .md: 32; case .lg: 48 } }
    var stroke: CGFloat   { switch self { case .sm: 2;  case .md: 3;  case .lg: 4 } }
}

struct WiomSpinner: View {
    var size: WiomSpinnerSize = .md
    var tone: WiomSpinnerTone = .brand            // .brand / .neutral / .onColor (§3)

    var body: some View {
        // Spinner ignores Reduce Motion on purpose (D20).
        TimelineView(.animation) { context in
            let t = context.date.timeIntervalSinceReferenceDate
            let turn = t.truncatingRemainder(dividingBy: 1.0)   // 1.0 s per turn, linear
            ZStack {
                if let track = tone.track {
                    Circle().inset(by: size.stroke / 2).stroke(track, lineWidth: size.stroke)
                }
                Circle().inset(by: size.stroke / 2)
                    .trim(from: 0, to: 0.75)
                    .stroke(tone.arc, style: StrokeStyle(lineWidth: size.stroke, lineCap: .round))
                    .rotationEffect(.degrees(-90 + turn * 360))  // starts at 12 o'clock
            }
        }
        .frame(width: size.diameter, height: size.diameter)
    }
}

// Free-standing spinner: labelled and live.
WiomSpinner(size: .md)
    .accessibilityElement()
    .accessibilityLabel(Text("a11y.loading.plans"))   // catalog key; illustrative
    .accessibilityAddTraits(.updatesFrequently)
```

```swift
// Loops other than the spinner stop under Reduce Motion.
struct WiomSkeletonShimmer: ViewModifier {
    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    var enabled: Bool                               // false = Static mode
    func body(content: Content) -> some View {
        if enabled && !reduceMotion { content.overlay(ShimmerBand()) } // 1.2 s sweep
        else { content }
    }
}

// One VoiceOver element for the whole placeholder region.
VStack(spacing: 0) { ForEach(0..<4, id: \.self) { _ in WiomSkeletonListItem() } }
    .accessibilityElement(children: .ignore)
    .accessibilityLabel(Text("a11y.loading.transactions"))
```

```swift
// Explicit branded wait: blocks touches and VoiceOver behind it and takes focus.
// Payment foreground loading uses wiom-ios-dialog instead.
ZStack {
    screen.accessibilityHidden(isLoadingBrand)
    if isLoadingBrand {
        WiomBrandLoader(style: .overlay, message: Text("brand.preparing"))
            .accessibilityElement(children: .ignore)
            .accessibilityLabel(Text("brand.preparing"))
            .accessibilityAddTraits([.isModal, .updatesFrequently])
            .onAppear { UIAccessibility.post(notification: .screenChanged, argument: nil) }
    }
}
// If the screen stays put after success:
UIAccessibility.post(notification: .announcement,
                     argument: String(localized: "a11y.brand.ready"))
```
