---
name: wiom-ios-pagination
description: >
  Wiom pagination for the iOS customer app (SwiftUI): page dots, step bars,
  the chevron page counter and the horizontal scroll indicator. Use when
  building or reviewing a SwiftUI page indicator under a carousel, a wizard
  step indicator, a tap-paged list counter or a scroll rail indicator.
---

# Wiom pagination (iOS)

Four indicators, three meanings. Pick by the **kind of progress** shown, not
by what fits the space.

| Component | Meaning | Use for (illustrative) | Avoid for |
|---|---|---|---|
| **Dots, Simple** | Which of 2 to 6 swipeable pages | Onboarding intro slides | Long lists |
| **Dots, Expanded** | Same, current page emphasised | Home promo banners | Tight layouts |
| **Bars** | Step n of 2 to 6, progress accumulated | Multi-step flows (recharge, booking) | Carousels, long lists |
| **Counter** | Page n of many, tap to move | Bills or transaction history paged by tap | Step flows, 2 to 6 pages |
| **Scroll indicator** | Position in a continuous horizontal rail | Plans or offers rail | Discrete pages |

Visuals match the Android implementation (`wiom-ds-android`,
`WiomPagination`) per the parity principle in `wiom-ios-foundations/references/decisions.md`. Where
the design skill and Android disagree, this file follows Android and lists
the mismatch under Open questions.

Tokens are DS V2 names (Swift names by `wiom-ios-foundations/references/decisions.md` §2); values live
in `wiom-ios-foundations` (`tokens.md`, `typography.md`, `icons.md`,
`layout.md`). All copy below is illustrative; real copy comes from the
string catalog (Hindi first, English written separately, sentence case).

## 1. Dots

```
          ●  ○  ○  ○            Simple: every slot 8 × 8 pt
          ━━━  ○  ○  ○          Expanded: current slot 24 × 8 pt
             1 / 4              optional counter label
```

| Slot | Value |
|---|---|
| Slot count | 2 to 6 |
| Slot (default) | 8 × 8 pt · `radius/full` · `bg/muted` |
| Slot (current, Simple) | 8 × 8 pt · `radius/full` · `bg/brand` |
| Slot (current, Expanded) | 24 × 8 pt capsule · `radius/full` · `bg/brand` |
| Gap between slots | `space/8` |
| Row alignment | Centred horizontally in the full width |
| Counter label (optional) | `space/8` below the row · `type/label/md` · `text/subtle` · centred |

- Exactly one slot is current.
- Pick one dot style per product surface (Simple for onboarding, Expanded
  for promo banners); don't mix them on one screen.
- Dot sizes are fixed glyph shapes (D16); they don't grow with text.

## 2. Bars

```
 ██████  ██████  ██████  ▒▒▒▒▒▒  ▒▒▒▒▒▒      step 3 of 5
```

| Slot | Value |
|---|---|
| Bar count | 2 to 6 |
| Bar | Equal share of the full width · 4 pt tall · `radius/full` |
| Filled bars | Bars 1 to n (current step and all before it) · `bg/brand` |
| Remaining bars | `bg/muted` |
| Gap between bars | `space/4` |
| Counter label (optional) | `space/8` below · `type/label/md` · `text/subtle` · centred |

- Bars always fill a prefix (1..n); never a gap in the filled run.
- Don't add a counter label under Bars that repeats the bars ("Step 3 of 5");
  the bars already show it. A label is allowed when it carries something
  else (the step's name).
- Bars width never fixes per bar; it always divides the available width.

## 3. Counter

```
   ‹      4 / 10      ›
  48 pt             48 pt cells, 24 pt glyphs
```

| Slot | Value |
|---|---|
| Layout | Back cell · label · Forward cell, centred row, no extra gap |
| Chevron cells | 48 × 48 pt each, glyph centred |
| Glyphs | Material Rounded `chevron_left` / `chevron_right` (`ic_rounded_chevron_left`, `ic_rounded_chevron_right`), `icon/md` (24 pt) |
| Chevron tint, available | `icon/action` |
| Chevron tint, unavailable | `icon/disabled` |
| Label | `type/label/md` · `text/default` (it is the only text, so full contrast) |

- **Both chevrons always render.** On page 1 Back is unavailable; on the
  last page Forward is unavailable. The unavailable chevron stays in place
  (no layout shift) and is a **truly disabled button**: it does nothing,
  takes no tap feedback, and VoiceOver reads it as dimmed.
- **Label format is one translatable string with placeholders**, never
  built by joining numbers and words in code, and never mixed-language
  ("2 of 10 बिल"). Illustrative key: `pagination.counter` =
  "%1$lld / %2$lld". Digits are Western, as on Android.
- Use for 7 or more pages, or any tap-paged content. A single page shows no
  counter (never "1 / 1").

## 4. Scroll indicator

```
 ████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   track + thumb, 4 pt tall
```

| Slot | Value |
|---|---|
| Track | Full width · 4 pt tall · `radius/full` · `bg/muted` |
| Thumb | 4 pt tall · `radius/full` · `bg/brand` |
| Thumb width | Visible width ÷ content width of the rail, never below 10 % of the track; 30 % when no scroll data (static) |
| Thumb position | Scrolled distance ÷ maximum scroll distance, across (track − thumb) |
| Placement | Below the rail, inside the screen gutter, `space/12` from the rail |

- Show only when the rail actually overflows. No indicator on a rail that
  fits, and none for vertical feeds (the system scroll bar covers those).
- It is a passive readout; it is not draggable.

## 5. Rules for all four

1. **One component per meaning.** Swipeable 2 to 6 pages → Dots. Steps →
   Bars. Many pages by tap → Counter. Continuous rail → Scroll indicator.
2. **Max 6 slots** for Dots and Bars; 7 or more → Counter.
3. **Inside the screen body.** Pagination sits within the `space/16`
   gutter (`layout.md`); it is never edge-to-edge chrome.
4. **Fill the width.** Wrapper, Bars and track fill the parent; dots are
   centred. Never a 360 pt width. Check iPhone SE (375 pt) to Pro Max (440 pt).
5. **Active = `bg/brand`, inactive = `bg/muted`.** No other colours, no
   tinting to "theme" the indicator. No shadows.
6. **Never hand-draw** pagination with ad-hoc shapes or "• • •" text; use the
   component.

### Placement (illustrative)

| Pattern | Where |
|---|---|
| Onboarding carousel · Dots Simple | Below the swipeable area, above the CTA |
| Promo banner · Dots Expanded | Below the banner |
| Multi-step flow · Bars | Top of each step screen, just below the top bar |
| Tap-paged list · Counter | Below the list |
| Horizontal rail · Scroll indicator | Below the rail |

## Settled rules

- **Unavailable chevron:** visible and truly disabled (VoiceOver says "dimmed").
- **Chevrons:** Material Rounded `chevron_left` / `chevron_right`, `icon/action` when available, `icon/disabled` when not.
- **Inactive dots and bars:** `bg/muted`.
- **Counter string:** one catalog string with placeholders.

## Open questions

1. **Counter centring.** iOS centres the counter row in its parent. Confirm on Android.
2. **Expanded dot motion.** Neither platform animates the 8 → 24 pt change. If design wants a `motion/micro` width transition, add it on both.

## iOS (SwiftUI, iOS 16+)

- **Built from:**
  - Dots and Bars: `HStack` of `Capsule()` shapes (Bars: each
    `.frame(maxWidth: .infinity)`), optional `Text` label below in a
    `VStack(spacing: space/8)`. The swipeable carousel on iOS 16 is
    `TabView` with `.tabViewStyle(.page(indexDisplayMode: .never))`; the
    system page dots (`UIPageControl`) are never shown, Wiom dots are drawn
    instead. `scrollTargetBehavior(.paging)` and `scrollPosition(id:)` are
    iOS 17+; if used, keep the `TabView` path for 16.
  - Counter: `HStack(spacing: 0)` of `Button` · `Text` · `Button`; each
    chevron button `.frame(width: 48, height: 48)` + `.contentShape(Rectangle())`,
    with `.disabled(current == 1)` / `.disabled(current == total)`. Glyph tint
    follows the enabled state (`icon/action` / `icon/disabled`).
  - Scroll indicator: track `Capsule` with thumb `Capsule` laid out by
    fraction (`GeometryReader` for the track width). Rail offset on iOS 16
    via a named `coordinateSpace` on the `ScrollView` and a `PreferenceKey`
    reading the content frame. (`onScrollGeometryChange` is iOS 18+; don't
    rely on it.)
  - Glyphs from the asset catalog as template images (D4), never SF Symbols.
- **Tokens:** `bg/brand`, `bg/muted`, `text/subtle`, `text/default`,
  `icon/action`, `icon/disabled`, `type/label/md`, `icon/md` (size),
  `radius/full`, `space/4`, `space/8`, `space/12`, `space/16`.
- **Size:** dots 8 × 8 pt (current Expanded 24 × 8), bars and track 4 pt
  tall: fixed glyph shapes (D16). Counter row min height 48 pt; labels have
  minimum, never fixed, heights. Widths fill.
- **Dynamic Type:** the counter label and the optional label under dots and
  bars scale with `type/label/md`'s anchor (`typography.md` §3); dots, bars,
  track and chevron glyphs stay fixed. The counter label never truncates;
  at accessibility sizes the row grows taller. Check Hindi and English.
- **VoiceOver:**
  - Dots and Bars are **one element** (`.accessibilityElement(children: .ignore)`)
    with a label naming what is paged (illustrative: "Offers"), value
    "Page n of N" (Dots) or "Step n of N" (Bars) via `.accessibilityValue`,
    from catalog strings (illustrative keys `pagination.page` =
    "Page %1$lld of %2$lld", `pagination.step` = "Step %1$lld of %2$lld").
    The optional visible label is folded into that element, not read twice.
  - Where the content is swipeable, add `.accessibilityAdjustableAction`:
    swipe up = next page, swipe down = previous, clamped at the ends, and the
    carousel moves with it. Non-swipeable Bars (a step flow advanced by its
    CTA) are not adjustable.
  - Counter: chevrons are buttons labelled "Previous page" / "Next page"
    (catalog strings); the unavailable one is `.disabled(true)` and reads
    "dimmed". The label reads the page in words via
    `.accessibilityLabel` from `pagination.page`, not "4 slash 10".
  - Scroll indicator is `.accessibilityHidden(true)`; the rail itself is
    scrolled with the standard three-finger swipe.
- **Hit area:** Dots, Bars and Scroll indicator are not tappable. Counter
  chevrons are 48 × 48 pt (≥ 44, D14), enabled or disabled.
- **Motion:** state changes are instant, as on Android: dot colour and the
  Expanded capsule width switch with the page, bars fill on step change, the
  thumb tracks the scroll directly. No extra animation (no bouncing dots).
  If a screen cross-fades the change, use `motion/micro` (`motion.md`); Reduce
  Motion removes it. The thumb follows the finger, so Reduce Motion changes
  nothing there.
- **Safe areas and keyboard:** none of these sit in a safe area. A Counter
  at the bottom of a screen sits inside the content, above the home
  indicator per D19; a Bars indicator under the top bar sits below the
  status bar inside the content area.
- **Haptics:** none (D21), including on page change.
- **Not on iOS:** system `UIPageControl` dots, ripple, focus ring, hover,
  a hidden chevron at the bounds, a tap-swallowing "disabled" chevron that
  is still enabled, SF Symbol chevrons, string-concatenated counters.
