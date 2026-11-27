---
name: wiom-ios-navigation-bar
description: >
  Wiom navigation bar for the iOS customer app (SwiftUI): the bottom tab
  bar of 2 to 5 items that switches between top-level destinations, each
  item an icon pill plus a label with a selected state and optional dot
  badge. Use only when explicitly inspecting this retained reference; do not
  add a bottom tab bar to the customer app (D27). Not for the sticky button bar at the
  bottom of a screen (that is wiom-ios-cta).
---

# Wiom navigation bar (iOS)

> **Status: not in use (D27).** The customer app has no bottom tab bar.
> Keep this skill as reference only. Do not load it to build customer screens.

**2 parts (Nav item · Navigation bar) · 2 item states (Default · Selected) ·
4 bar configurations (2 / 3 / 4 / 5 tabs) · edge to edge.**

The bar owns the bottom of a root screen: it runs the full width with no
screen gutter, and its background continues down under the home indicator.
Its items sit above the home indicator (D19).

It is **not** the sticky button bar that holds a screen's primary CTA. That
belongs to `wiom-ios-cta`. The bar holds destinations only.

## 1. Configurations

| Tabs | Use for |
|---|---|
| 2 | Rare. Exactly two peer destinations. |
| 3 | The target for most apps: Home plus two key destinations. |
| 4 | When a fourth top-level destination is genuinely needed. |
| 5 | Hard cap. Only if every tab is used weekly by most users. |

- Tab 1 and Tab 2 are always present. Put the highest-traffic destination
  first.
- No sixth tab and no "More" tab. Needing six is a scope problem.
- Illustrative customer set: Home · Plans · Bills · Profile.

## 2. Anatomy

### Navigation bar

```
┌──────────────────────── full width (edge to edge) ─────────────────────────┐
├─ stroke/small · stroke/subtle top border ──────────────────────────────────┤
│  ●Nav item   ●Nav item   ●Nav item   ●Nav item   ●Nav item                 │
│  equal share equal share equal share equal share equal share               │
└──────────────────────────── space/12 bottom ───────────────────────────────┘
                 ↓  bg/default continues under the home indicator
```

| Slot | Value |
|---|---|
| Width | Fills the screen width |
| Height | Hugs its items (≈ 80 pt at the default text size) plus the home-indicator inset |
| Fill | `bg/default` |
| Top border | `stroke/small` width, `stroke/subtle` colour, top edge only |
| Top padding | none (each item carries its own) |
| Bottom padding | `space/12` above the home-indicator inset (above the screen edge on Home-button iPhones) |
| Items | Equal width: every item takes an equal share of the bar, so 2 and 5 tabs use the same component |
| Shadow | none |

### Nav item (min 68 pt at the default text size)

```
          ┌───────────────────────────┐
          │      space/8 top          │
          │   ┌─── icon pill ───┐     │   pill: space/16 H, space/4 V
          │   │   ●  24 pt      │     │   → 32 pt tall at rest
          │   └─────────────────┘     │
          │      space/4 gap          │
          │         Home              │   type/label/sm
          │      space/8 bottom       │
          └───────────────────────────┘
               space/4 horizontal
```

| Slot | Value |
|---|---|
| Width | Equal share of the bar |
| Padding | `space/4` horizontal · `space/8` vertical |
| Layout | Column, centred, `space/4` between pill and label |
| Icon pill | `space/16` horizontal · `space/4` vertical padding · `radius/full`. Its width stays fixed; it does not grow with the label. |
| Icon | `icon/md` (24 pt) Material Rounded glyph |
| Label | `type/label/sm`, centred |
| Badge | `wiom-ios-badge` Dot, critical tone, at the icon's top-trailing corner, 2 pt outside it on both axes |

## 3. Item states

| State | Pill | Icon | Label |
|---|---|---|---|
| Default | transparent | Rounded glyph, fill off, `icon/nonAction` | `text/subtle` |
| Selected | `bg/selected` | Filled pair of the same Rounded glyph, `icon/brand` | `text/selected` |

- **Exactly one item is Selected**, and it reflects where the user is, not a
  preference.
- **Approved Rounded state pair.** Default is fill off; Selected uses its filled pair, per the current source. Do not borrow another icon family.
- Default icons use `icon/nonAction`, not `icon/action`: the label carries the
  affordance and the Selected pill carries the active signal.
- **No Disabled state.** A destination that can't open right now is not in
  the bar; gate at navigation time.
- **No pressed visual.** There is no pressed token for nav items (D13; see
  Open questions). No hover, no focus ring, no ripple.

## 4. When the bar is shown

The bar belongs to **root screens only** (the first screen of each tab). It
is removed, not dimmed or disabled, on:

1. **Pushed screens**: anything pushed onto a tab (detail, edit, form,
   picker). The top bar's back arrow takes over (`wiom-ios-top-bar`).
2. **Flows**: onboarding, OTP, payment, installation scheduling. A linear flow
   doesn't allow tab switching mid-way.
3. **Immersive media**: video, full-screen image viewer, camera.
4. **Sheets and dialogs**: a Wiom bottom sheet or dialog covers the bar with
   its scrim; the bar is not drawn above it.
5. **Keyboard up on a root screen**: the keyboard covers the bar; the bar
   never rides on top of the keyboard.

A dimmed bar on a non-root screen invites mis-taps and breaks "where am I".

## 5. Rules

1. **Edge to edge.** Never wrap the bar in the screen gutter. The only inset
   inside it is each item's own `space/4`.
2. **One Selected item, always.**
3. **Labels always on.** Never an icon-only bar.
4. **One word per label**, a noun ("Home", "Plans", "Bills"), not a verb
   ("Pay"). Rename the destination rather than shrinking the type.
5. **Default is Rounded with fill off; Selected uses the filled pair.**
6. **Badges are rare**: unread or actionable state only, never decoration.
   Avoid badging more than one tab at a time.
7. **No CTA in the bar.** No "Add" tab, no plus button merged into a slot.
8. **Same order everywhere.** Tabs never reorder; a role-gated destination
   keeps its slot or is absent.
9. **Flat.** No shadow on the bar, no border on the pill. Only the top border
   separates the bar from content.
10. **Tokens only.** No raw values.

## 6. Copy (illustrative)

Labels come from the string catalog (Hindi first, English written separately,
sentence case, D25). Keep each label short enough to sit on **one line** at
the default text size in a 5-tab bar on a 375 pt iPhone SE (about 8 grapheme
clusters, counted with `String.count`). Illustrative: "Home", "Plans",
"Bills", "Profile".

The "Tab n of N" phrase read by VoiceOver is also a catalog string with
placeholders, not concatenated in code.

## 7. Related skills

- `wiom-ios-foundations` → `tokens.md`, `typography.md` (Dynamic Type
  anchors), `icons.md` (approved Material Rounded assets),
  `layout.md` (surface padding, safe areas), `accessibility.md`, `motion.md`.
- `wiom-ios-top-bar`: the paired surface at the top; same edge-to-edge
  contract. Tab roots use it with no leading item.
- `wiom-ios-badge`: the dot on a nav item, and how its meaning is spoken.
- `wiom-ios-cta`: the sticky button bar at the bottom of a screen. Never
  combined with the navigation bar on the same screen.
- `wiom-ios-tabs-filters`: switching sections **inside** one screen. The
  navigation bar switches top-level destinations.
- `wiom-ios-bottomsheet`, `wiom-ios-dialog`: surfaces that cover the bar.

## Open questions

1. **Closed by D27:** the customer app has no bottom navigation bar. The questions below concern this unused reference only.
2. **Glyph fill.** Default is Rounded fill off; Selected uses the filled pair. Verify the exact state-pair assets before this reference is ever activated. Do not source substitute glyphs from another family.
3. **Label wrapping.** iOS wraps to 2 lines at larger text sizes and follows the accessibility3 cap. Confirm, and consider the same for Android with two-line Hindi.
4. **Pressed visual.** No pressed token; iOS shows none (D13). Design team: define one or confirm none.
5. **Badge type.** Dot only (the source allows a count badge "when the count is meaningful").
6. **Bottom padding on Face ID iPhones.** `space/12` above the home-indicator inset makes the bar about 114 pt tall including the 34 pt inset, against 83 pt for a system tab bar. Confirm, or use the D19 value (`space/16`).
7. **Tab re-tap.** Scroll-to-top on re-tapping the selected tab is iOS behaviour. Confirm.

## iOS (SwiftUI, iOS 16+)

- **Built from:** a custom `WiomNavigationBar` view (`HStack` of equal-width
  item `Button`s, each with `.frame(maxWidth: .infinity)` and a plain custom
  `ButtonStyle`), **not** `TabView`'s system tab bar. Why: `UITabBar` can't
  draw the `bg/selected` pill, the Noto Sans `type/label/sm` label with its
  tracking, two-line labels or the `stroke/subtle` border, and its look
  changes between iOS versions (iOS 26 restyles it), so it could never match
  Android. How tab state is kept:
  - One app-level `@State var selectedTab` (or a router object) owns the
    selection; each tab has **its own `NavigationStack`** with its own
    `NavigationPath`, held in the same router so a tab's stack survives
    switching away and back.
  - All visited tabs stay alive in a `ZStack`; only the selected one is shown,
    so scroll position and stack are preserved. A tab is created the first
    time it is opened.
  - The bar is attached to each **root screen** with
    `.safeAreaInset(edge: .bottom, spacing: 0)`, so it is part of the root:
    it slides away with the root on push and returns on swipe-back, and
    pushed screens never draw it.

  ```swift
  ZStack {
      ForEach(router.visitedTabs) { tab in
          NavigationStack(path: $router.paths[tab]) {
              tab.rootView
                  .safeAreaInset(edge: .bottom, spacing: 0) {
                      WiomNavigationBar(items: tabs, selected: $router.selectedTab)
                  }
          }
          .opacity(tab == router.selectedTab ? 1 : 0)
          .allowsHitTesting(tab == router.selectedTab)
          .accessibilityHidden(tab != router.selectedTab)
      }
  }
  ```

  Tapping the already-selected item scrolls its root to the top
  (`ScrollViewReader`). Since the bar is only on root screens, there is no
  stack to pop.

- **Tokens:** `bg/default`, `stroke/subtle`, `stroke/small`
  (`Wiom.BorderWidth.small`), `bg/selected`, `icon/brand`, `icon/nonAction`,
  `text/selected`, `text/subtle`, `type/label/sm`, `space/4`, `space/8`,
  `space/12`, `space/16`, `radius/full`, `icon/md`; badge tokens via
  `wiom-ios-badge`. Swift names per `wiom-ios-foundations/references/decisions.md` §2. Corners circular
  (D3).

- **Size:** width fills the screen; items share it equally (≥ 75 pt each with
  5 tabs on a 375 pt iPhone SE). Item min height 68 pt, pill 32 pt at rest
  (`.frame(minHeight:)`, never fixed). The 24 pt glyph and the pill's
  horizontal padding stay the same at every text size (D14).

- **Dynamic Type:** the label scales with its anchor (`typography.md` §3).
  Decision: at the default size a label is one line. At larger sizes it
  **wraps to max 2 lines, centred, then truncates at the end**
  (`.lineLimit(2)`, `.multilineTextAlignment(.center)`); the bar grows. The
  bar follows the app cap at **accessibility3**, without a lower local cap.
  It grows with wrapped labels; a Large Content Viewer may supplement the
  text but never replaces support for the app’s Dynamic Type range. Check Hindi and English, 5 tabs, on iPhone SE.

- **VoiceOver:**
  - The bar is one container (`.accessibilityElement(children: .contain)`);
    each item is one element: button trait, label = the tab label, value =
    the catalog string for "Tab n of N", and `.accessibilityAddTraits(.isSelected)`
    on the selected item. Reads as "Bills, selected, Tab 3 of 4, button".
  - A badge's meaning is spoken on the item (for example "1 new bill"), as
    `wiom-ios-badge` describes; the dot itself is hidden.
  - The glyph is decorative (`.accessibilityHidden(true)`); the label speaks.
  - After a tab switch, VoiceOver focus moves to the new root's top-bar title
    (`@AccessibilityFocusState`).

- **Hit area:** each item's whole cell (equal share of the width × the item
  height, ≥ 68 pt) is tappable (`.contentShape(Rectangle())`), well over
  44 × 44 pt. Cells don't overlap and there are no gaps between them.

- **Motion:** none. Selection changes instantly (pill, glyph, colours), and
  switching tabs shows the new root without a transition, as Android. The bar
  leaves and returns with the root screen's system push and pop (D6). Reduce
  Motion: nothing to reduce.

- **Safe areas and keyboard:**
  - Background extends under the home indicator:
    `.background(Wiom.Colors.bgDefault.ignoresSafeArea(edges: .bottom))`.
    Items stay inside the safe area, with `space/12` between the label and the
    home-indicator inset (Home-button iPhones: `space/12` above the screen
    edge).
  - The root screen's content ends above the bar (`safeAreaInset` handles it);
    nothing scrolls behind the bar's items unseen.
  - Keyboard: the bar must not ride on the keyboard. Put
    `.ignoresSafeArea(.keyboard, edges: .bottom)` on the bar's host so the
    keyboard covers it.

- **Haptics:** none (D21), on selection or otherwise.

- **Not on iOS:** `TabView` system chrome or `UITabBar` appearance styling;
  ripple or pressed overlays; hover; focus ring; hardware back; navigation-bar
  inset padding; SF Symbols; showing the bar on pushed screens (reference only; D27).
