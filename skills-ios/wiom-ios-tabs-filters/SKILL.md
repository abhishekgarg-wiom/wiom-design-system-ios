---
name: wiom-ios-tabs-filters
description: >
  Wiom tabs and filters for the iOS customer app (SwiftUI): Pill Tabs (context
  switch between datasets), Underline Filter (single-select slice of one
  dataset) and Chips (multi-select attribute toggles). Use when building or
  reviewing a SwiftUI pill tab track, underline filter bar or filter chip row.
  Status, count and dot badges are wiom-ios-badge, not chips.
---

# Wiom tabs and filters (iOS)

Three components that narrow what the user sees. They solve different
problems and are not interchangeable.

| Component | Question it answers | Selection model |
|---|---|---|
| **Pill Tabs** | "Whose / which data am I looking at?" | Exactly one; swaps the **whole dataset** below |
| **Underline Filter** | "Which slice of this data do I want?" | Exactly one; narrows the **loaded** dataset |
| **Chip** | "Which attributes do I want to combine?" | Zero to many; each chip is independent |

Unsure? Ask what a tap changes: *which data is loaded* (Pill Tabs), *which
one slice of it is shown* (Underline Filter), or *which attributes are
combined* (Chips). A tap that opens another screen is none of these: use a
list row (`wiom-ios-list-item`).

A chip is always a **tappable filter toggle**. A passive status, count or
dot ("Paid", "3", unread dot) is `wiom-ios-badge`, never a chip.

Visuals match the Android implementation (`wiom-ds-android`,
`WiomTabsFilters`) per the parity principle in `wiom-ios-foundations/references/decisions.md`.
Where the design skill and Android disagree, this file follows Android and
lists the mismatch under Open questions.

Tokens are DS V2 names (Swift names by the rule in `wiom-ios-foundations/references/decisions.md` §2);
values live in `wiom-ios-foundations` (`tokens.md`, `typography.md`,
`layout.md`). All copy below is illustrative; real copy comes from the
string catalog (Hindi first, English written separately, sentence case).

## 1. Pill Tabs: context switch

A muted rounded track holding 2 to 4 equal-width pills. The selected pill
is raised (light fill + small shadow).

```
Track: bg/muted · radius/medium · space/4 padding all sides
┌────────────────────────────────────────────────┐
│ ┌───────────────┐                              │
│ │  Tab A (sel)  │    Tab B         Tab C       │
│ └───────────────┘                              │
└────────────────────────────────────────────────┘
  items split the track interior equally, no gap between them
```

### 1.1 Anatomy

| Slot | Value |
|---|---|
| Track width | Fills the parent; the surface owns the gutter |
| Track fill / radius | `bg/muted` · `radius/medium` |
| Track padding | `space/4` all sides |
| Item width | Track interior ÷ item count (equal widths, no gap) |
| Item padding | `space/12` horizontal · `space/8` vertical |
| Item min height | 36 pt (`space/8` + 20 pt label line + `space/8`); grows with text |
| Track min height | 44 pt (consequence of the above, never set) |
| Item radius | `radius/small` |
| Label | `type/label/md`, centred both axes |

### 1.2 States

| State | Fill | Shadow | Label |
|---|---|---|---|
| **Selected** | `bg/default` | `shadow/sm` | `text/selected` |
| **Unselected** | none (track shows through) | none | `text/subtle` |
| **Pressed** | No pressed token; Android shows only the platform ripple, which iOS does not port. No pressed visual (D13). | | |

Exactly one pill is selected at all times, including first load.

### 1.3 Count

- **2 to 4 pills** (D30; shared owner decision, Android ships `2..4`). Two is the common case.
- A single pill is not shown: one dataset means no Pill Tabs.
- More than 4 is the wrong component: slices of one dataset go to the
  Underline Filter; separate destinations go to list rows or separate screens.
- Never a scrolling pill track.

### 1.4 Use

- **Use for** a top-level switch between 2 to 4 datasets or scopes
  (illustrative: "My plan" / "Family plan", "Today" / "This week" / "This month").
- **Don't use for** narrowing one dataset (Underline Filter), multi-select
  (Chips), or navigation to other screens.
- **Where** directly under the top bar (`wiom-ios-top-bar`), inside the
  screen gutter. Never inside list rows.

## 2. Underline Filter: single-select slice

A flat bar of text filters with a 1 pt bottom border. The selected filter is
shown by brand-coloured text plus a 2 pt brand indicator line.

```
┌──────────────────────────────────────────────────┐
│    All        Pending       Closed      Expired   │
│    ───                                            │
└──────────────────────────────────────────────────┘  ← 1 pt stroke/subtle
```

### 2.1 Anatomy

| Slot | Value |
|---|---|
| Bar width | Fills the parent |
| Bar background | None (sits on the screen's `bg/default`) |
| Bar bottom border | `stroke/small` width · `stroke/subtle` colour, full bar width |
| Item padding | `space/16` horizontal · `space/12` vertical |
| Item min height | 48 pt; content centred vertically; grows with text |
| Label | `type/label/md`, centred |
| Indicator | `stroke/medium` (2 pt) tall · `bg/brand` fill · round caps (`radius/full`) |
| Indicator position | Bottom edge of the label's content box (inside the item padding), as Android draws it; see Open questions |
| Indicator width | Width of the item's content box: item width minus `space/16` each side (fixed mode), label width (scrolling mode) |

The indicator is a **filled shape** in `bg/brand`, not a stroke token.

### 2.2 States

| State | Label | Indicator |
|---|---|---|
| **Selected** | `text/brand` | Visible, `bg/brand` |
| **Unselected** | `text/subtle` | Hidden |
| **Pressed** | No pressed visual (no token; Android shows only ripple; D13) | |

Exactly one filter is selected at all times.

### 2.3 Layout modes

Use count and fit together; never combine horizontal scroll with a More affordance.

| Count / fit | Mechanism |
|---|---|
| 1–6, all labels fit | All visible, no scroll, no More |
| 1–6, labels do not fit at the current Dynamic Type size | Horizontal scroll, no More |
| 7+ | Fit as many filters as possible beside a trailing Material Rounded `filter_list` More icon; no horizontal scroll |

The More icon has a ≥ 44 × 44 pt target and a catalog label. It opens a radio list of **all** filters in a Wiom sheet. The active filter always remains inline; choosing a hidden filter replaces the rightmost non-active inline filter. When large text leaves no space beside More, expose the selected filter as wrapping text above the full-width More control. Labels never truncate.

Android currently ships fixed equal-width and scrolling modes without the More control. The accepted source overflow rule above applies on iOS; record the Android gap (Open question 3). Fixed-mode equal widths and indicator geometry otherwise follow Android.

### 2.4 Use

- **Use for** single-select narrowing of one list or feed: status, type or
  period (illustrative: "All" / "Recharges" / "Refunds").
- **Don't use for** multi-select (Chips), free-text search (top bar search,
  `wiom-ios-top-bar`), switching datasets (Pill Tabs), or inside a dialog or
  sheet (use a radio list, `wiom-ios-list-item` + `wiom-ios-selection-controls`).
- **Where** directly under the top bar, or directly under Pill Tabs when both
  exist.

## 3. Chip: multi-select toggle

Independent toggles. Tapping a chip flips it on or off; any number can be on,
including none.

```
┌──────────────┐  ┌──────────────────┐  ┌──────────┐
│  Fiber       │  │  WiFi 6     ✕   │  │  Mesh    │
└──────────────┘  └──────────────────┘  └──────────┘
  unselected         selected              unselected
```

### 3.1 Anatomy

| Slot | Value |
|---|---|
| Width | Hugs label (+ close glyph when selected) |
| Padding | `space/12` horizontal · `space/8` vertical |
| Min height | 36 pt (`space/8` + 20 pt label line + `space/8`); grows with text |
| Radius | `radius/small` |
| Label | `type/label/md` in every state |
| Label to close gap | `space/4` |
| Close glyph (Selected only) | Material Rounded `close` (`ic_rounded_close`), `icon/xs` (16 pt), `icon/brand` |
| Border width | `stroke/small` |
| Shadow | None |

### 3.2 States

| State | Fill | Border | Label | Close glyph |
|---|---|---|---|---|
| **Unselected** | none | `stroke/subtle` | `text/default` | none |
| **Selected** | `bg/selected` | `stroke/selected` | `text/selected` | shown, `icon/brand` |
| **Disabled** | `bg/disabled` | none | `text/disabled` | none (even if selected) |
| **Pressed** | No pressed visual (no token; Android shows only ripple; D13) | | | |

Disabled uses the fill and text tokens, never opacity.

### 3.3 Chip row

| Slot | Value |
|---|---|
| Width | Fills the parent; the surface owns the gutter |
| Gap between chips | `space/8` horizontal |
| Gap between lines | `space/8` vertical |
| Overflow | **Wraps to a new line.** A chip row never scrolls horizontally |

Chips wrap at every text size; at large Dynamic Type they simply take more
lines. A single chip whose label is wider than the row wraps its label onto
a second line inside the chip (the chip grows taller).

### 3.4 Behaviour

- Tapping anywhere on a chip, including the close glyph, toggles it. The
  close glyph is a visual cue, not a separate button.
- Zero selected is valid ("no attribute filter").
- "Clear all" is not part of the component; add a Tertiary button
  (`wiom-ios-cta`) beside or above the row when the design asks for it.

### 3.5 Use

- **Use for** additive attribute filters (illustrative: connection type,
  speed tier, plan features) where several values combine.
- **Don't use for** mutually exclusive choices (Underline Filter), switching
  datasets (Pill Tabs), status display (`wiom-ios-badge`), or inside the top
  bar.
- **Where** inline above content, or inside a filter sheet
  (`wiom-ios-bottomsheet`).

## 4. Rules for all three

1. **Fill the width; never fix it.** Track, bar and chip row fill the
   parent; the screen, sheet or card owns the `space/16` gutter
   (`layout.md`). Check from iPhone SE (375 pt) to Pro Max (440 pt).
2. **Heights are minimums.** Pill 36 pt, filter item 48 pt, chip 36 pt;
   all grow with Dynamic Type and two-line Hindi (D16).
3. **Pill items split evenly; scrolling filter items hug.** Never the reverse.
4. **One selection visual per component.** Pill = raised fill + shadow;
   Underline = brand text + indicator; Chip = fill + border. Never mix them
   (no underline inside a pill track, no raised pill in a filter bar).
5. **Unselected stays readable:** `text/subtle` (pill, filter) or
   `text/default` (chip). No lighter greys.
6. **Disabled is tokens, not opacity**, and a disabled item is a truly
   disabled control (see the iOS section).
7. **Labels name the data, not the action:** "Active", not "Show active".
   Keep them short: aim for ≤ 10 grapheme clusters Hindi, ≤ 14 English, so
   3 to 4 filters fit in Fixed mode on a 375 pt screen.
8. **Selection is instant.** No confirmation, no spinner on the control. If
   data must load, show a skeleton in the content (`wiom-ios-loader`).
9. **No icons in pills or ordinary filter items, no badges** until supported on both apps. The trailing More icon at 7+ is the accepted exception (see Open questions).

## Screen behaviour guidance

These are screen-level rules. The components hold no state rules; the
screen owns the selected index / set and applies these.

- **Stacking order:** top bar → Pill Tabs → Underline Filter → content.
  Never Underline above Pill.
- **Max two filter levels** per screen. Allowed: Pill alone, Underline
  alone, Chip row alone, Pill + Underline, Pill + Chips, Underline + Chips
  (Chips in content or in a filter sheet, never as a second row under the
  top bar). Not allowed: two Pill tracks, two Underline bars, two Chip rows,
  Pill + Underline + Chips.
- **Pill flip resets the filter.** When the Pill Tab changes, set the
  Underline Filter back to its first item ("All"). Don't carry a slice
  across datasets.
- **Sticky header:** when content scrolls, Pill Tabs and Underline Filter
  stay pinned together under the top bar; content scrolls beneath.
- **7+ filters:** use the fit-N plus More mechanism in §2.3. Keep the selected filter inline. The More sheet lists all filters; never mix More with horizontal scroll.

## Settled rules

- **Pill count (D30):** 2 to 4 pills.
- **Pill item height:** 36 pt (`space/8` around a 20 pt line), track 44 pt.
- **Underline filter width:** equal width in fixed mode, hug content when scrolling.
- **Chip unselected border:** `stroke/subtle`.

## Open questions

1. **Disabled pills and filters, badges, More filter.** iOS keeps badges and disabled variants unexposed for parity, and implements the More overflow rule at 7+ (§2.3). Confirm.
2. **Underline indicator position.** Drawn at the bottom of the label's padded content box (12 pt above the bar border). Looks unintended; needs a design ruling.
3. **Chip close glyph as its own target.** On iOS it can't reach 44 pt inside a 36 pt chip, so the whole chip toggles. Confirm no separate remove action is needed.
4. **Chip row wrapping.** iOS wraps chips (skill rule). Confirm wrapping is the rule on both platforms.
5. **Pressed states.** No pressed token for pill, filter or chip; iOS shows none (D13). Is a pressed fill (for example `bg/subtle`) wanted on both?
6. **Pill label wrapping at large text.** iOS wraps pill labels and switches the filter bar to scrolling. Confirm.

## iOS (SwiftUI, iOS 16+)

- **Built from:**
  - Pill Tabs: `HStack(spacing: 0)` of `Button`s with a custom `ButtonStyle`,
    each `.frame(maxWidth: .infinity)`, inside a `RoundedRectangle(cornerRadius:style: .circular)`
    track. Not `Picker(.segmented)` (cannot take Wiom styling).
  - Underline Filter: `ViewThatFits(in: .horizontal)` for 1–6 choosing between the
    fixed `HStack` (equal widths) and a `ScrollView(.horizontal, showsIndicators: false)`
    + `ScrollViewReader` (`proxy.scrollTo(selectedID)` on change). Bottom
    border as an overlay `Rectangle` of `stroke/small` height. At 7+,
    use the measured inline filter group plus a More `Button` opening the sheet (§2.3).
  - Chip: `Button` + custom `ButtonStyle`; chip row is a custom flow
    `Layout` (the `Layout` protocol is iOS 16) with `space/8` gaps.
  - `scrollPosition(id:)` is iOS 17+; on 16 use `ScrollViewReader` only.
  - Corners `.circular` (D3); shadow `.wiomShadow(.sm)`; icons from the asset
    catalog as template images (D4), never SF Symbols.
- **Tokens:** `bg/muted`, `bg/default`, `bg/brand`, `bg/selected`,
  `bg/disabled`, `text/selected`, `text/brand`, `text/subtle`,
  `text/default`, `text/disabled`, `stroke/subtle`, `stroke/selected`,
  `icon/brand`, `type/label/md`, `space/4`, `space/8`, `space/12`,
  `space/16`, `radius/small`, `radius/medium`, `radius/full`,
  `stroke/small`, `stroke/medium` (widths), `icon/xs` (size), `shadow/sm`.
- **Size:** minimum heights only: pill 36 pt (track 44 pt), filter item
  48 pt, chip 36 pt. Widths fill or hug as above; never 360/328.
- **Dynamic Type:** `type/label/md` scales with its anchor text style
  (`typography.md` §3), line height with it; check through xxxLarge, no
  clipping through accessibility3 (D17).
  - Pill labels wrap onto more lines rather than truncate; all pills in the
    track take the height of the tallest.
  - Underline Filter labels stay on one line; at 1–6, when the fixed bar no longer
    fits, it becomes the scrolling bar (`ViewThatFits`); 7+ keeps More (§2.3).
  - Chips wrap to new lines in the row; an over-long label wraps inside its
    chip. Check Hindi and English both.
- **VoiceOver:**
  - Each pill and each filter item is one element: label = its text, trait
    `.isButton`, plus `.isSelected` when selected (announced "selected"),
    value "Tab n of N" from the string catalog (illustrative key
    `tabs.position` = "Tab %1$lld of %2$lld"; Hindi translated separately).
    Group the track/bar with `.accessibilityElement(children: .contain)`.
  - Each chip is one element: label = chip text, `.isButton`, `.isSelected`
    when on. The close glyph is `.accessibilityHidden(true)`; no "n of N".
  - Disabled chip: `.disabled(true)` so VoiceOver says "dimmed".
  - In a scrolling bar, VoiceOver focus moving to an off-screen filter
    scrolls it into view (the system does this).
- **Hit area:** ≥ 44 × 44 pt, default 48 (D14). Pills: the 36 pt item gets
  `.contentShape` covering the full track height (44 pt). Filter items are
  48 pt tall already. Chips: `.contentShape` expanded to 44 pt minimum height
  and width in the flow layout. Reserve these frames before computing
  the parent gaps; `.contentShape` alone does not enlarge layout.
- **Motion:** selection takes effect immediately. Its fill, border and label colour ease in both directions using `Wiom.Motion.microStandard` (`motion/micro` + `ease/standard`). Keep the same control identity and bind animation to the selected value; replacing the entire control prevents interpolation. The chip close glyph fades in/out on the same token. Do not slide the pill background or underline between controls, bounce, scale or animate chip width/row layout. Reduce Motion retains colour/opacity fades and removes spatial motion. Programmatic scroll-into-view uses the same token; Reduce Motion jumps to its destination (D28). Transparent selection endpoints use the same fill/stroke/underline colour at opacity 0, never `.clear`; this introduces no confirmation delay.
- **Safe areas and keyboard:** none of the three touches a safe area; the
  host surface handles it. In a filter sheet the chip row scrolls with the
  sheet body and stays above the keyboard if a field is present.
- **Haptics:** none (D21), including on selection.
- **Not on iOS:** ripple, hover tokens, focus ring, Android TabRow/FilterChip
  conventions, system `Picker(.segmented)` look, SF Symbols.
