---
name: wiom-ios-top-bar
description: >
  Wiom top bar for the iOS customer app (SwiftUI): the custom header at
  the top of every screen, in Small, Medium and Large sizes with back
  arrow, title, optional subtitle, trailing icon and text actions, a
  search state and a scrolled shadow. Use when building, editing or
  reviewing the header of a SwiftUI screen or full-screen sheet in the
  Wiom iOS app.
---

# Wiom top bar (iOS)

**1 component · 3 sizes · 8 ship variants · edge to edge.** Every screen in
the customer app starts with this bar. The system navigation bar is never
shown (`wiom-ios-foundations/references/decisions.md` D7).

| Size | Minimum height | States |
|---|---|---|
| Small | 64 pt | Default · Centered · Scrolled · Search |
| Medium | 112 pt | Default · Scrolled |
| Large | 152 pt | Default · Scrolled |

Heights are **minimums** (D7, D16). At the default text size the bar is
exactly this tall; at larger Dynamic Type sizes, or with a two-line Hindi
title, the bar grows. It never clips its title.

The bar owns the top of the screen: it runs the full width with no screen
gutter, and its background continues up under the status bar so the two
read as one surface (D8, D19).

## 1. Picking a size and state

Size is a design choice. State is partly runtime.

| Size × State | Use for |
|---|---|
| Small × Default | Most screens: back arrow, title, 0–3 trailing actions. The default. |
| Small × Centered | Headers of full-screen sheets and modal flows: close (`close`) leading, centered title, at most one trailing action (often a text action such as "Save"). Never on ordinary pushed screens. |
| Small × Search | Search screens: back arrow, inline search pill, optional trailing text action ("Cancel"). |
| Medium × Default | List roots where the title needs more weight ("Payment history"). |
| Large × Default | Hero or landing surfaces only, at most one per flow (a tab root such as Home). Never on a list, form, detail, settings or modal screen. |
| Any × Scrolled | Same bar plus `shadow/sm`. Not chosen by design: it appears once content scrolls under the bar (§5). |

Rules for picking:

1. **Small is the default.** Use Medium or Large only with a concrete reason.
2. **Medium and Large are static.** No iOS large-title collapse, no shrink
   on scroll (D7). Scrolling only adds the shadow.
3. **Root screens have no leading item.** A tab root shows its title and
   trailing actions only. **The customer app has no hamburger menu**; never
   put a menu glyph in the leading slot.
4. **Pushed screens lead with the back arrow** (Material Rounded
   `arrow_back`, D5). Full-screen sheets and modal flows lead with `close`.

## 2. Anatomy

All sizes share an **action row** (leading cell, title or spacer, trailing
area). Medium and Large add a **title area** below it.

### Small (min 64 pt)

```
┌────────────────────── full width (edge to edge) ──────────────────────┐
│ ●Lead  Title                                    Save  ●T1  ●T2  ●T3   │
│ 48pt   Subtitle (optional)                      text  48pt 48pt 48pt  │
└───────────────────────────────────────────────────────────────────────┘
 ↑ space/4 outer                                          space/4 outer ↑
```

| Slot | Value |
|---|---|
| Width | Fills the screen width |
| Height | Min 64 pt (48 pt row + `space/8` top and bottom) |
| Outer padding | `space/4` horizontal · `space/8` vertical |
| Leading / trailing icon cell | 48 × 48 pt: `icon/md` (24 pt) glyph centred, `space/12` all round |
| Title column | Fills the remaining width · `space/12` horizontal padding · vertically centred |
| Title | `type/title/lg`, `text/default` |
| Subtitle (optional) | `type/body/sm`, `text/subtle`, `space/4` above it |
| Trailing text action | Min height 48 pt · `space/12` horizontal padding · `type/label/md`, `text/brand` |

**Centered:** the title column centres its title (and subtitle) inside the
space between the leading cell and the trailing area. With a 48 pt leading
cell and a wider trailing text action the title sits slightly off the
screen centre; that matches what ships.

### Search (Small only, min 64 pt)

```
┌───────────────────────────────────────────────────────────────────────┐
│ ●Lead  ┌── search pill (bg/subtle, radius/full) ──────────┐  Cancel   │
│ 48pt   │ ●search 20pt   Search plans, bills               │  text     │
│        └──────────────────────────────────────────────────┘           │
└───────────────────────────────────────────────────────────────────────┘
 ↑ space/4                                                    space/16 ↑
```

- Outer padding: `space/4` leading, **`space/16` trailing** (the only
  asymmetric state).
- Pill: fills the width between leading cell and trailing area, with
  `space/8` horizontal margin; fill `bg/subtle`; `radius/full`;
  `space/16` horizontal and `space/8` vertical padding; `space/12` gap
  between glyph and field. Min height 40 pt at the default text size.
- Pill glyph: `search`, `icon/sm` (20 pt), `icon/nonAction`.
- Field text: `type/body/lg`, `text/default`; insertion point `text/default`.
- Placeholder: `type/body/lg`, `text/disabled`.
- The trailing area normally holds only a text action ("Cancel").

### Medium (min 112 pt)

```
┌───────────────────────────────────────────────────────────────────────┐
│ ●Lead                                           Save  ●T1  ●T2  ●T3   │ ← action row, min 48
├───────────────────────────────────────────────────────────────────────┤
│ Title (type/heading/lg)                                                │ ← title area, min 64
└───────────────────────────────────────────────────────────────────────┘
```

- Action row: min 48 pt, `space/4` horizontal padding; leading cell, flexible
  spacer, trailing area. No title in this row.
- Title area: min 64 pt; `space/16` horizontal, `space/8` vertical padding;
  title aligned to the **bottom leading** corner; `type/heading/lg`,
  `text/default`. No subtitle.

### Large (min 152 pt)

- Action row: as Medium.
- Title area: min 104 pt; `space/16` horizontal, `space/12` top, `space/32`
  bottom padding; title bottom leading; `type/heading/xl`, `text/default`.
  No subtitle.

### Title line limits

| Size | At the default text size | At larger Dynamic Type sizes |
|---|---|---|
| Small | 1 line (write copy that fits) | Wraps to **max 2 lines**, then truncates at the end; the bar grows |
| Medium | 1 line | Wraps to max 2 lines, then truncates; the title area grows |
| Large | Max 2 lines | Max 2 lines, then truncates; the title area grows |
| Subtitle (Small) | 1 line | Max 2 lines, then truncates |

Title copy (D44 target): keep it to about 24 grapheme clusters (`String.count`) so it fits
one line on a 375 pt iPhone SE at the default size. A longer idea moves into
the subtitle. Truncated text is still read in full by VoiceOver.

## 3. Variants: light and dark

All 8 variants are light. The **dark** treatment is a token override on the
same component, used sparingly for premium headers.

| Slot | Light (default) | Dark |
|---|---|---|
| Container (and status-bar strip) | `bg/default` | `bg/brand/bold` |
| Title | `text/default` | `text/inverse` |
| Subtitle | `text/subtle` | not supported |
| Trailing text action | `text/brand` | `text/inverse` (never `text/brand` on dark, D26) |
| Leading / trailing icons | `icon/action` | `icon/inverse` |
| Search pill | `bg/subtle` | not supported |
| Scrolled shadow | `shadow/sm` | `shadow/sm` |
| Status-bar content | **dark** | **light** |

The dark treatment supports Small × Default, Centered, Scrolled and Medium /
Large × Default, Scrolled. It does **not** support a subtitle (no dimmed
inverse text token) or the Search state (no inverse pill fill). If a design
needs either, use the light bar or request the tokens from the design team.

## 4. Status bar

iOS can't colour the status bar (D8). The bar's background extends under it,
so the strip shows `bg/default` (light) or `bg/brand/bold` (dark). Only the
status-bar **content style** changes:

| Bar | Status-bar content |
|---|---|
| Light (`bg/default`) | Dark content |
| Dark (`bg/brand/bold`), or a screen headed by `bg/inverse` or a brand-filled hero | Light content |

- Don't half-pair: a light bar with light content (or the reverse) makes the
  clock and battery unreadable.
- Set the style once per screen, never per scroll position. If a screen's
  header changes from dark to light, the style changes with it, but question
  the design first.

## 5. States

| State | Visual | When |
|---|---|---|
| Default | Flat `bg/default`, no shadow | Content at rest (scroll position 0) |
| Centered | Title centred, close leading | Full-screen sheet / modal-flow header |
| Scrolled | Default + **`shadow/sm`** below the bar | **`shadow/sm` appears once content scrolls under the bar** and goes away when it scrolls back to the top. The shadow separates the bar from the content beneath. It is never shown at rest. |
| Search | Search pill replaces the title | Search-first screens, or after the user taps a search action |

The shadow switches on and off without animation (as Android).

**Pressed:** the back arrow, trailing icons and text action have no pressed
token and no pressed fill on iOS (D13, D46). No hover, no
focus ring, no ripple.

## 6. Rules

1. **Width fills the screen; heights are minimums.** Never wrap the bar in
   the screen gutter; never pin its height. The bar owns its own inner
   padding.
2. **Status-bar content style pairs with the bar** (§4).
3. **Trailing area: max 3 icons, or 1 text action.** Never a text action plus
   3 icons. Overflow goes into a `more_vert` action that opens a Wiom bottom
   sheet (`wiom-ios-bottomsheet`).
4. **The text action is never destructive and never a filled button.** It is
   `text/brand` (light) or `text/inverse` (dark). Irreversible actions use a
   button in the screen body (`wiom-ios-cta`) behind a confirmation.
5. **Subtitle: Small, light only.** Medium and Large have no subtitle slot.
6. **Centered: Small only, modal headers only, max 1 trailing action.**
7. **Search and Centered are Small-only states.** There is no Medium or Large
   search bar.
8. **Icons:** Material Icons Rounded only, `icon/md`, tinted `icon/action`
   (D4). No SF Symbols, including the back arrow.
9. **Tokens only.** Every colour, type, space, radius and shadow is a DS V2
   token. No raw values.

## 7. Copy (illustrative)

All strings come from the string catalog (Hindi first, English written
separately, sentence case, D25). Examples here are illustrative only.

| Slot | Guidance | Illustrative |
|---|---|---|
| Title | A noun phrase naming the screen; ≤ ~24 grapheme clusters | "Payment history" |
| Subtitle | Context for the title; one short line | "Updated just now" |
| Text action | One verb | "Save", "Done", "Cancel" |
| Search placeholder | What can be searched | "Search plans, bills" |
| Back button (VoiceOver) | Always the catalog string for "Back" | "Back" |

## 8. Related skills

- `wiom-ios-foundations` → `tokens.md`, `typography.md` (Dynamic Type
  anchors), `icons.md` (Material Rounded assets), `layout.md` (surface
  padding, safe areas), `accessibility.md`, `motion.md`.
- `wiom-ios-navigation-bar`: the bottom tab bar (kept for reference; not used today); same
  edge-to-edge contract at the bottom.
- `wiom-ios-tabs-filters`: pill tabs and filters sit **below** the top bar,
  inside the screen gutter.
- `wiom-ios-input-fields`: for a full search-results screen that needs a real
  input with helper text, use an input field in the body instead of the pill.
- `wiom-ios-bottomsheet`: the overflow menu behind `more_vert`.
- `wiom-ios-cta`: primary actions live in the body or the sticky button bar,
  never in the top bar.

## Settled rules

- **Centered:** the modal header. Close leading and a subtitle are allowed; at most 1 trailing action. The title centres between leading and trailing, not on the screen.
- **Search pill:** glyph `icon/nonAction`, cursor `text/default`, `space/8` horizontal margin around the pill. Trailing slot: text action only.
- **Back button** VoiceOver label is the shared catalog key `common.back`.
- **Pressed (D46):** no pressed visual for now (D13).
- **Large two-line title (D45):** the bar grows instead of clipping.
- **Small / Medium titles (D45):** 2 lines at larger text sizes on iOS. Android follow-up per D51.
- **Hamburger (D51):** root screens have no leading item on iOS. Android follow-up: drop the home-tab hamburger.
- **Medium / Large action row (D51):** a 48 pt row with full 48 pt cells, no extra vertical padding. Android follow-up.
- **Title line limits (D51):** Small / Medium titles wrap to 2 lines at larger text sizes. Android follow-up: move from 1 line + ellipsis to 2 lines.

## Open questions

None.

## Accessibility strings

Catalog keys this component needs (never literals in code):

| Key | English meaning | Used for |
|---|---|---|
| `common.back` | "Back" | Back button on every pushed screen |
| `common.close` | "Close" | Close leading on modal (Centered) headers |
| `input.clear` | "Clear text" | Search pill clear button |

Hindi text comes from the catalog; new strings need approval (D39).

## iOS (SwiftUI, iOS 16+)

- **Built from:** a custom `WiomTopBar` view (`VStack` of an action-row
  `HStack` and, for Medium / Large, a title area), placed with
  `.safeAreaInset(edge: .top, spacing: 0)` on the screen's scroll view so
  content scrolls under it and the shadow draws over content. Icon actions and
  the text action are `Button`s with a plain custom `ButtonStyle` (no pressed
  fill). The system navigation bar is hidden on every screen with
  `.toolbar(.hidden, for: .navigationBar)` (iOS 16). Navigation stays
  `NavigationStack` push/pop (D6). The search field is a `TextField` inside
  the pill.

  Built from: the screen `ScrollView` reports its offset; the bar attaches with `.safeAreaInset(edge: .top, spacing: 0)` and shows its scrolled state when the offset is below zero; the system navigation bar is hidden with `.toolbar(.hidden, for: .navigationBar)`.

  `ScrollOffsetReader` is a zero-height `GeometryReader` at the top of the
  content that reports `frame(in: .named("scroll")).minY` through a
  `PreferenceKey` (iOS 16 has no scroll-geometry API; on iOS 18+
  `onScrollGeometryChange` can replace it). Without a scroll view the bar is
  simply `Default`.

- **Tokens:** `bg/default`, `bg/brand/bold`, `bg/subtle`, `text/default`,
  `text/subtle`, `text/brand`, `text/inverse`, `text/disabled`, `icon/action`,
  `icon/inverse`, `icon/nonAction`, `type/title/lg`, `type/heading/lg`,
  `type/heading/xl`, `type/body/sm`, `type/body/lg`, `type/label/md`,
  `space/4`, `space/8`, `space/12`, `space/16`, `space/32`, `radius/full`,
  `icon/md`, `icon/sm`, `shadow/sm` (`.wiomShadow(.sm)`). Swift names per
  `wiom-ios-foundations/references/decisions.md` §2 (`Wiom.Colors.bgDefault`, `Wiom.Typography.titleLg`).
  Corners circular (D3).

- **Size:** width fills the screen. Minimum heights: Small 64, action row 48,
  Medium title area 64 (bar 112), Large title area 104 (bar 152), search pill
  40. Use `.frame(minHeight:)`, never `.frame(height:)`. Icon glyphs stay
  24 pt (search glyph 20 pt) at every text size (D14).

- **Dynamic Type:** title, subtitle, text action and search text scale with
  their anchors (`typography.md` §3); line height scales with them. Titles
  wrap per the §2 line-limit table (`.lineLimit(2)`), then truncate at the
  end; the bar grows. The text action keeps its full label on one line
  (`.fixedSize()`) and the title column gives up the width. Check Hindi and
  English at xxxLarge and accessibility3 (the app cap, D17) on a 375 pt
  iPhone SE: nothing clips or overlaps.

- **VoiceOver:**
  - Title: `.accessibilityAddTraits(.isHeader)`; title and subtitle combine
    into one element (`.accessibilityElement(children: .combine)`).
  - Back: label from the string catalog for "Back", button trait
    (the back `Button` is labelled with the catalog key `common.back`). Close
    reads "Close".
  - Every trailing icon has a catalog label naming the action
    ("Notifications", "More options"); glyphs alone are never read.
  - Search field: label = a dedicated catalog search label, independent of the placeholder example; when the Search state opens,
    focus moves to the field (`@FocusState`).
  - Reading order: back, title, trailing actions.
  - Also support the escape gesture (two-finger scrub) on pushed screens:
    `.accessibilityAction(.escape) { if canGoBack { dismiss() } }`.

- **Hit area:** back, close and every trailing icon are 48 × 48 pt
  (`.frame(minWidth: 48, minHeight: 48)` + `.contentShape(Rectangle())`). The
  text action is min 48 pt tall and at least 48 pt wide. Cells never overlap.

- **Motion:** no animation of its own. The Scrolled shadow switches on and off
  without a transition. Push/pop and edge-swipe-back are the system's (D6).
  Reduce Motion: nothing to reduce.

- **Safe areas and keyboard:**
  - Background extends under the status bar:
    `.background(Wiom.Colors.bgDefault.ignoresSafeArea(edges: .top))`
    (`bgBrandBold` for dark); content stays below the status bar and inside
    the horizontal safe area.
  - Status-bar content style (D8): SwiftUI on iOS 16 can't set it per view
    while the navigation bar is hidden. The app shell hosts SwiftUI in a
    `UIHostingController` subclass that overrides `preferredStatusBarStyle`
    (`.darkContent` for light bars, `.lightContent` for dark) and calls
    `setNeedsStatusBarAppearanceUpdate()`; each screen's top bar publishes its
    style through a `PreferenceKey` read at the root. Info.plist:
    `UIViewControllerBasedStatusBarAppearance = YES`.
  - **Edge-swipe-back must keep working with the bar hidden.** Hiding the
    navigation bar can leave `interactivePopGestureRecognizer` without a
    working delegate, so the swipe stops. Fix once, app-wide: give each
    `UINavigationController` a gesture delegate that allows the swipe whenever
    the stack has more than one screen.

    Built from: one app-wide gesture delegate allows the pop gesture whenever the stack has more than one screen; a small representable in each stack root finds its navigation controller, keeps a strong reference to the delegate, and sets it on `interactivePopGestureRecognizer` with `isEnabled = true`.

    A screen that must block back (payment in progress) disables both the
    back button and this gesture for that screen.
  - Keyboard: the top bar never moves with the keyboard.

- **Haptics:** none (D21).

- **Not on iOS:** hamburger / menu leading icon; ripple or pressed overlays;
  hover; focus ring; hardware back; status-bar background colour; system
  navigation bar, `.navigationTitle` or large-title collapse; SF Symbols;
  custom cross-fade page transitions.
