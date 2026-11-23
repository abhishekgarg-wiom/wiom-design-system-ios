---
name: wiom-ios-progress-indicator
description: >
  Wiom progress indicator for the SwiftUI iOS customer app: the linear
  bar, the completion meter, the named-stage milestones tracker and the
  circular ring, all showing determinate progress toward a known
  target. Use when the iOS app shows the customer how far along
  something is, such as installation stages after booking, recharge
  steps or profile completion; for short indeterminate waits with no
  value, use wiom-ios-loader instead.
---

# Wiom progress indicator (iOS): four ways to show forward motion

A progress indicator says **how far along** something is, toward a target the customer wants. If there is no value to show, it isn't progress: use `wiom-ios-loader`.

| Component | What it shows | Use for |
|---|---|---|
| **Linear** | A plain bar, 2 sizes (sm 4 pt, md 8 pt) × 3 tones | A percentage next to other content; a download with a known size |
| **Completion** | Title + status pill + value + md bar, 4 states | A "how complete is this" card, e.g. profile completion |
| **Milestones** | Title + subtitle + 2–5 named stages on a bar | Where the customer is in a multi-stage process, e.g. installation after booking |
| **Circular** | A ring, 2 sizes (sm 24 pt, lg 48 pt) × 3 tones | A compact percentage in a row or tile |

**Reversed semantics: more is better.** Wiom is an unlimited-data ISP; there is no usage meter where "full" is bad. Every progress visual shows movement toward something good.

All values are tokens from `wiom-ios-foundations` (`references/tokens.md`, `typography.md`, `motion.md`). Swift names follow `IOS_DECISIONS.md` §2.

## 1. Progress indicator or loader?

| The app knows… | Use |
|---|---|
| A value toward a target (stage 2 of 4, 60 %, 3 of 5 details) | **This skill** |
| Nothing about how long it will take | `wiom-ios-loader` (Spinner, Skeleton, Linear Indeterminate) |
| A fraction for a short (≤ 5 s) technical wait where a thin brand bar is enough | `wiom-ios-loader` Linear Determinate |
| Blocking foreground loading (processing payment, syncing, submitting) | `wiom-ios-dialog` Loading, with an error/timeout fallback; no duration cutoff |

## 2. Colour ladder

Fill colour follows the value. It is the same ladder everywhere in the app:

| Value | Tone | Fill | Mood |
|---|---|---|---|
| < 35 % | Info | `bg/info` | Just started: calm, not worrying |
| 35–80 % | Brand | `bg/brand` | Under way |
| > 80 % | Positive | `bg/positive` | Almost there / done |

- **Never `bg/warning` or `bg/critical` on a fill.** A stuck or failed process is shown by the outcome surface (`wiom-ios-bottomsheet` Illustration) or a status badge next to the progress, never by a red bar.
- As on Android, **Linear and Circular take the tone as a parameter** (default Brand); they don't pick it from the value themselves. A screen that shows a moving value picks the tone with the ladder (one shared helper, so every screen uses the same thresholds). **Completion** has the ladder built into its states (§4).

## 3. Linear

| Part | Value |
|---|---|
| Track | `bg/muted`, `Capsule()`, fills the host width |
| Height | sm 4 pt (default, as Android) · md 8 pt |
| Fill | Tone colour (§2), its own `Capsule()` (both ends rounded), width = value × track width. No fill at 0. |
| Border, shadow | None |

Value is clamped to 0…1. Display-only: no tap action.

## 4. Completion

```
┌───────────────────────────── fills host width ──────────────────────────┐
│ Profile completion                                       3 of 5 details │  title · value
│  ● In progress                                                          │  pill  (space/4 below title)
│                                                                         │  space/12
│ ██████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░                  │  Linear md, state tone
└─────────────────────────────────────────────────────────────────────────┘
```

| Part | Token |
|---|---|
| Title | `type/label/md`, `text/default`; wraps, never truncates |
| Value (trailing) | `type/body/sm`, `text/subtle`; gap to the title column `space/8` |
| Title → pill | `space/4` |
| Pill | `Capsule()`; padding `space/8` horizontal, 2 pt vertical; a 6 pt dot then the label, gap `space/4`; label `type/label/sm` |
| Header → bar | `space/12` |
| Bar | Linear md (8 pt), tone from the state |

The state drives fill, tone, pill colours and pill copy together:

| State | Fill | Tone | Pill fill / text | Pill copy (illustrative) |
|---|---|---|---|---|
| Just started | 20 % | Info | `bg/info/subtle` / `text/info` | "Just started" |
| In progress | 60 % | Brand | `bg/brand/subtle` / `text/brand` | "In progress" |
| Almost there | 88 % | Positive | `bg/positive/subtle` / `text/positive` | "Almost there" |
| Complete | 100 % | Positive | `bg/positive/subtle` / `text/positive` | "Complete" |

The pill dot is the pill's text colour. Title, value and pill copy come from the string catalog.

## 5. Milestones

```
┌───────────────────────────── fills host width ──────────────────────────┐
│ Your installation                                                       │  title
│ Step 2 of 4 · Visit set                                                 │  subtitle (space/4)
│                                                                         │  20 pt
│  ●━━━━━━━━━━━━━━━━●━━━━━━━━━━━━━━━━○──────────────────○                │  24 pt circles + 4 pt connectors
│                                                                         │  20 pt
│   Booked        Visit set        Installing          Live               │  stage labels
└─────────────────────────────────────────────────────────────────────────┘
```

| Part | Token |
|---|---|
| Title | `type/label/lg`, `text/default`; wraps |
| Subtitle | `type/body/sm`, `text/subtle`; names the step and the current stage; wraps |
| Title → subtitle | `space/4` |
| Header → bar row, bar row → labels | **20 pt** (see the note below) |
| Stage circle | 24 × 24 pt `Circle()`, glyph `icon/xs` (16 pt) centred |
| Circle, reached (stage ≤ current) | `bg/brand` fill, `icon/inverse` glyph |
| Circle, not reached | `bg/muted` fill, `icon/nonAction` glyph |
| Connector | 4 pt `Capsule()`, flexes to fill the space between circles; `bg/brand` when the stage before it is finished (stage < current), else `bg/muted` |
| Stage label | `type/body/sm`, centred; past `text/default`, current `text/brand`, future `text/subtle` |
| Stage glyphs | Material Rounded icons from the asset catalog (D4) |

**Gap note (stated once):** the source skill says `space/24` in its anatomy and "20 dp" in its token table. Android ships **20** for both gaps (`WiomProgressIndicator.kt:454`), so iOS uses 20 pt for parity. There is no `space/20` token: this is a token gap reported to the design team (D24); in code it carries a `// TODO(IOS-123): …` with the ticket.

**Stage count:** 2, 3, 4 or 5 stages; pick the real count, never pad. More than 5 means per-step screens (see §7). `current` is 1-based and within the stage count.

**Label layout (as Android):** the label row is split into equal columns, one per stage, each label centred in its column.

**Stage labels, Hindi and English:**

- Keep stage labels to **≤ 8 grapheme clusters** (`String.count`; "क्षि" is one). 8 is the longest stage name in the source examples ("Activate").
- A label **wraps to at most 2 lines, centred**. A label of ≤ 8 grapheme clusters is never truncated.
- If, at a large Dynamic Type size, a label still needs more than 2 lines, the whole label row is hidden (use `ViewThatFits`); the subtitle already names the current stage, and VoiceOver reads it in the value. See Open questions.

## 6. Circular

| Part | sm | lg |
|---|---|---|
| Box | 24 × 24 pt | 48 × 48 pt |
| Ring stroke | 3 pt | 4 pt |
| Track | full ring, `bg/muted` | same |
| Arc | tone colour (§2), from 12 o'clock, clockwise, round caps; none at 0 | same |
| Centre label | none (as Android) | none (as Android) |

Sizes are fixed glyph shapes (D16). Put the percentage as text **beside** the ring (e.g. in the list row's trailing meta), not inside it. See Open questions on a centre label.

## 7. Picking the right component

| Need | Use |
|---|---|
| A plain percentage next to a label | **Linear** sm |
| A completion card the customer returns to | **Completion** |
| Where the customer is in a named, multi-stage process they watch but don't drive | **Milestones** |
| A compact percentage in a row or tile | **Circular** |
| Per-step screens where the customer acts at each step (form, OTP, choose a plan) | Build one screen or sheet per step; show position with `wiom-ios-pagination` Bars or a compact Milestones strip. There is no stepper component. |
| Unlabelled "page n of N" dots | `wiom-ios-pagination` |
| No value, just "please wait" | `wiom-ios-loader` |
| A usage or quota meter | None. Wiom has no usage meters; push back on the requirement. |

**Customer-app examples (illustrative; real copy from the catalog, Hindi first):**

| Moment | Component |
|---|---|
| Installation tracker after booking, as the customer sees it | Milestones, 4 stages: "Booked" · "Visit set" · "Installing" · "Live" |
| After paying for a recharge | Milestones, 3 stages: "Paid" · "Activating" · "Active" |
| Profile completion card on Home | Completion, "Profile completion", "3 of 5 details" |
| A profile row with a compact percentage | Circular sm + the percentage as trailing text |
| Downloading a large invoice with a known size | Linear sm |

Don't stack two progress visuals on one card. When the process completes, hide the progress and show the outcome (`wiom-ios-bottomsheet` Illustration, or a toast for small ones); don't leave a full bar on screen as the result.

## 8. Motion and Reduce Motion

Android draws each new value **at once**: no tween on the fill or arc, no colour cross-fade, no count-up (`WiomProgressIndicator.kt:85-100`, `:196-222`). iOS matches this: value, tone, stage and pill changes are instant.

The source skill also describes a draw-on (fill and arc growing to the new value), a count-up of a centre percentage and colour cross-fades. These are not shipped on Android and are an Open question. If they are adopted, they use `motion/emphasis` · `ease/standard` for draw-on and count-up and `motion/surface` · `ease/standard` for colour changes, and under **Reduce Motion they jump straight to the final value and colour** (D20). Code should already route value changes through one place that checks `accessibilityReduceMotion`, so adding the tween later can't skip the Reduce Motion path.

Progress never loops. A determinate indicator must not look busy when nothing is changing.

## 9. Rules

1. More is better. No warning / critical fills; no usage meters.
2. One ladder (§2) for every value-driven tone.
3. Display-only. No tap action, no button trait; the hosting row or card owns the tap (`wiom-ios-list-item`), and any action is a `wiom-ios-cta` next to the progress.
4. Linear, Completion and Milestones fill the host's width; Circular and the stage circles are fixed shapes.
5. Every bar, ring and tracker reports its value to VoiceOver (§iOS).
6. Real stage count, 2–5.
7. Tokens only, by DS V2 name. No hex, no system tint, no default `ProgressView` look.

### Anti-patterns

- System `ProgressView(value:)` with its default styling (wrong height, colour and track).
- A red or amber bar for "stuck". Use the outcome surface or a status badge.
- A hand-built row of circles and rectangles instead of Milestones (misses the connector rule, label colours and the single VoiceOver element).
- Five stages for a three-stage flow.
- A tap gesture on the bar itself.
- Truncating a stage label to "Instal…".

## Open questions

1. **Milestones gap:** Android 20 dp (`WiomProgressIndicator.kt:454`); the skill says both `space/24` and "20 dp". iOS uses 20 pt for parity. No `space/20` exists: add the token, or change both apps to `space/16` or `space/24`?
2. **Ladder automation:** the skill says Linear and Circular pick the tone from the value; Android does not (caller passes `tone`, default Brand; `WiomProgressIndicator.kt:39-48`, `:77`, `:188`). iOS follows Android, with one shared ladder helper. Confirm that's intended.
3. **Circular:** skill = one 48 pt ring with a centre `type/label/sm` percentage; Android = sm 24 / 3 and lg 48 / 4, no centre label (`WiomProgressIndicator.kt:167-223`). iOS follows Android. Is a centre label wanted on lg?
4. **Draw-on, count-up and colour cross-fades:** in the skill (600 ms fill / arc, 300 ms colour), not shipped on Android (`WiomProgressIndicator.kt:85-100`, `:196-222`). iOS is instant. Adopt on both, with `motion/emphasis` / `motion/surface` and the Reduce Motion jump?
5. **Pill and stage-label type:** Android uses `type/meta/xs` (10 pt) for the Completion pill (`WiomProgressIndicator.kt:391`) and the Milestones stage labels (`:511`). D18 forbids `type/meta/xs` for Devanagari, and both carry Hindi. iOS uses the skill's `type/label/sm` (pill) and `type/body/sm` (stage labels). Android should change to match.
6. **Stage-label position:** Android centres each label in an equal-width column (`WiomProgressIndicator.kt:505-507`), so the first and last labels don't sit under their circles; the skill says centred under each circle. iOS follows Android.
7. **Untokened values:** pill vertical padding 2 pt (`WiomProgressIndicator.kt:380`; `space/2` isn't an iOS token) and the 6 pt pill dot (`:386`). Gaps per D24.
8. **Linear default size:** Android defaults to sm 4 (`WiomProgressIndicator.kt:78`); the skill's examples default to md 8. iOS follows Android; Completion always uses md.
9. **Stage-label limit and fallback:** ≤ 8 grapheme clusters is taken from the longest source example. Confirm, and confirm hiding the label row (subtitle carries the stage) when labels need more than 2 lines at large text sizes.
10. **Stage glyph source:** Android takes only an `ImageVector` (`WiomProgressIndicator.kt:413`); the skill allows a brand drawable fallback. iOS uses Material Rounded assets only (D4); a non-Material glyph needs a design-team asset.
11. **Indeterminate bars and rings in Android's progress package** (`WiomLinearProgressIndeterminate`, `WiomCircularProgressIndeterminate`; `WiomProgressIndicator.kt:115-271`) are not part of this iOS skill; indeterminate waits use `wiom-ios-loader`.

## iOS (SwiftUI, iOS 16+)

- **Built from:** a `Capsule` track with a `Capsule` fill in `.overlay(alignment: .leading)`, sized from the track width, for Linear; `VStack` / `HStack` for Completion (`ViewThatFits` or `dynamicTypeSize` for the stacked header); an `HStack` of `Circle`s and flexible `Capsule` connectors, plus an equal-column `HStack` of labels (each `.frame(maxWidth: .infinity)`), for Milestones; `Circle().inset(by:).trim(from:to:).stroke(_:style:)` rotated −90° for Circular. Accessibility is set explicitly so VoiceOver gets `ProgressView`-equivalent semantics.
- **Tokens:** `bg/muted`, `bg/info`, `bg/brand`, `bg/positive`, `bg/info/subtle`, `bg/brand/subtle`, `bg/positive/subtle`, `text/info`, `text/brand`, `text/positive`, `text/default`, `text/subtle`, `icon/inverse`, `icon/nonAction`, `type/label/lg`, `type/label/md`, `type/label/sm`, `type/body/sm`, `space/4`, `space/8`, `space/12`, `icon/xs`, `motion/instant`, `motion/surface`, `motion/emphasis`, `ease/standard`.
- **Size:** bar heights 4 / 8 pt, connector 4 pt, circles 24 pt, rings 24 / 48 pt are fixed non-text shapes (D16). Everything that holds text (Completion header, Milestones header and labels) has no fixed height and grows. Widths fill the host minus its gutter; check iPhone SE (375 pt) to Pro Max (440 pt).
- **Dynamic Type:** titles, values, subtitles and pill labels scale with their anchors in `typography.md` §3 and wrap. Completion: when `dynamicTypeSize.isAccessibilitySize`, the value moves under the title instead of beside it. Milestones: stage labels `lineLimit(2)`, `.multilineTextAlignment(.center)`, never truncated at ≤ 8 grapheme clusters; the label-row fallback in §5. Check Hindi and English at xxxLarge and accessibility3.
- **VoiceOver:** each indicator is **one element** (`.accessibilityElement(children: .ignore)`) with a label and a value. Linear and Circular: label = what is progressing (from the host, e.g. "Profile completion"), value = percent (illustrative "40 percent", from the catalog's percent format). Completion: label = title, value = the value string plus the pill copy (illustrative "3 of 5 details, in progress"); don't speak the state's fixed fill percent. Milestones: label = title, value = "step 2 of 4, <stage name>" (catalog format string). Add `.updatesFrequently` while a value is changing live (a download). When a stage or state changes while the customer is on the screen, post one `.announcement` with the new value.
- **Hit area:** none; indicators are not tappable. The hosting row or card has the ≥ 44 pt target.
- **Motion:** §8. Today all changes are instant on both platforms. If draw-on / count-up / cross-fades are adopted: `motion/emphasis` / `motion/surface` with `ease/standard`, and under Reduce Motion they jump to the final value. Nothing loops.
- **Safe areas and keyboard:** no special handling; indicators live inside their host's safe area. A Milestones strip pinned under the top bar sits below the status bar with the top bar (D8).
- **Haptics:** none, including on completion (D21).
- **Not on iOS:** default `ProgressView` / `UIProgressView` styling, Material progress indicators, ripple on hosting cards, SF Symbols for stage glyphs (D4), `minimumScaleFactor` on stage labels.

```swift
enum WiomProgressTone { case info, brand, positive
    // The one ladder (§2). Screens with a value-driven tone call this.
    init(ladderFor value: Double) {
        self = value < 0.35 ? .info : (value > 0.80 ? .positive : .brand)
    }
    var fill: Color {
        switch self { case .info: Wiom.Colors.bgInfo; case .brand: Wiom.Colors.bgBrand
                      case .positive: Wiom.Colors.bgPositive }
    }
}

struct WiomLinearProgress: View {
    let value: Double                       // 0...1, clamped
    var tone: WiomProgressTone = .brand     // as Android: caller picks
    var size: WiomLinearProgressSize = .sm  // 4 pt; .md = 8 pt
    var body: some View {
        let v = min(max(value, 0), 1)
        Capsule().fill(Wiom.Colors.bgMuted)
            .frame(maxWidth: .infinity)
            .frame(height: size.height)
            .overlay(alignment: .leading) {
                if v > 0 {
                    GeometryReader { g in
                        Capsule().fill(tone.fill).frame(width: g.size.width * v)
                    }
                }
            }
            .accessibilityElement(children: .ignore)
            .accessibilityValue(Text(v, format: .percent.precision(.fractionLength(0))))
    }
}

// Call site: label from the host, tone from the ladder.
WiomLinearProgress(value: p, tone: .init(ladderFor: p))
    .accessibilityLabel(Text("profile.completion.title"))   // catalog key; illustrative
```

```swift
// Milestones: one element, "step n of N, stage".
WiomMilestones(title: title, subtitle: subtitle, stages: stages, current: current)
    .accessibilityElement(children: .ignore)
    .accessibilityLabel(title)
    .accessibilityValue(Text("a11y.progress.step \(current) \(stages.count) \(stages[current - 1].label)"))

// Value changes go through one place, so a future tween can't bypass Reduce Motion.
@Environment(\.accessibilityReduceMotion) private var reduceMotion
func show(_ newValue: Double) {
    shown = newValue        // today: instant, as Android
    // If draw-on is adopted (Open question 4): animate only when !reduceMotion,
    // with motion/emphasis + ease/standard; under Reduce Motion keep the jump.
}
```
