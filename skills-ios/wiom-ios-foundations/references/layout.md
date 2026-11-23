# Layout on iPhone: frames, gutters, safe areas, keyboard, hit areas

**Contents:** 1 Frames · 2 Surface gutters · 3 Vertical rhythm · 4 Hit areas · 5 Safe areas · 6 Keyboard · 7 Status bar · 8 Checks

---

## 1. Frames

There is no fixed screen size. Layouts fill the width and are checked on:

| Frame | Points | Why |
|---|---|---|
| iPhone SE (3rd gen) | 375 × 667 | Narrowest width, shortest height, no home indicator |
| iPhone 15 / 16 | 393 × 852 | The common case |
| iPhone Pro Max | 440 × 956 | Widest |

Android designs are drawn at 360 × 720. Converting: 1 dp = 1 pt; anything "360 wide" becomes "full width"; anything "328 wide" becomes "full width minus the 16 pt gutters".

---

## 2. Surface gutters

Components are full width (`.frame(maxWidth: .infinity)`). The **surface** they sit on owns the horizontal gutter. Same table as Android:

| Surface | Horizontal gutter |
|---|---|
| Top bar · Navigation bar · Bottom sheet | Edge to edge (the surface fills the width; its own content padding is in its skill) |
| Screen content · Sticky CTA bar · Filter bar | `space/16` |
| Chat screen | `space/12` |
| Dialog | `space/24` inside; dialog max width 312 with ≥ `space/24` to the screen edges |
| Toast | As `wiom-ios-toast` says (don't standardise it to 16) |
| List item | Edge to edge on a bare screen; `space/16` inside a card or grouped background |

A component's own internal padding (CTA pill padding, list-row inner gutter) is part of the component and stays as its skill defines.

**Parents own gaps.** Spacing between siblings is the parent's `VStack(spacing:)` / `HStack(spacing:)`. Children never add outside padding to push siblings away. No `.offset` for layout (offset moves the drawing, not the hit area or the layout).

---

## 3. Vertical rhythm

| Between | Token |
|---|---|
| Top bar → first content | `space/16` |
| Content sections | `space/32` |
| Cards | `space/16` |
| Card padding | `space/16` |
| Last content → sticky CTA bar or keyboard | `space/16` |

---

## 4. Hit areas

**Every tappable element has a hit area of at least 44 × 44 pt; the default is 48 × 48** (D14). The visible element keeps its designed size.

| Android tier | Visible size (unchanged) | iOS hit area |
|---|---|---|
| Action (delete, edit, share, close, back, menu) | 24 glyph | 48 × 48 |
| Navigation (expand, sort, arrows, pagination, filters) | 24 or 20 glyph in a 32 frame | **≥ 44 × 44** (48 when space allows) |
| Info (help, tooltip trigger) | 16–20 glyph in a 24 frame | **≥ 44 × 44** |
| Buttons | 48 tall via 12 + 24 + 12 | Already ≥ 48 tall; Tertiary that hugs text gets `minWidth: 48` |

```swift
Button(action: close) {
    Wiom.Icon.close.wiomIcon(.md, tint: Wiom.Colors.iconAction)
        .frame(minWidth: 48, minHeight: 48)
        .contentShape(Rectangle())
}
.accessibilityLabel(Text("common.close"))   // string-catalog key, illustrative
```

Hit areas of neighbours must not overlap. If two 44 pt areas would overlap, re-layout; don't shrink the hit area.

---

## 5. Safe areas

Read insets from the environment (`GeometryReader` / `safeAreaInsets`); never constants. The status bar is 20–62 pt; the home indicator area is 34 pt on Face ID iPhones and 0 on SE.

| Rule | How |
|---|---|
| Surfaces paint into the safe area | Top bar, navigation bar, sticky CTA bar, bottom sheet: their **background** uses `.ignoresSafeArea(edges:)`; their **content** stays inside |
| Screen content scrolls under bars | Content insets so the last item clears the bar; scrolled-under shadows are each bar's skill |
| **Last bottom CTA** (D19) | Face ID iPhones: the button's bottom edge sits `space/16` above the home indicator. Home-button iPhones (no inset): `space/16` above the screen edge. Never computed per screen: use the **sticky CTA bar** from `wiom-ios-cta`, which encodes it once |
| Landscape | Not supported (iPhone portrait only) |

The sticky CTA bar is the **only** place this bottom rule is implemented; every screen uses that component rather than re-doing the maths.

---

## 6. Keyboard

| Rule | Detail |
|---|---|
| Focused field stays visible | The screen scrolls so the focused field **and its helper or error line** sit above the keyboard plus any sticky CTA bar (`ScrollViewReader` + `@FocusState`; `wiom-ios-input-fields`) |
| Sticky CTA bar rides the keyboard | When the keyboard is up the bar sits on it with `space/12` below the button, and the home-indicator spacing no longer applies (`wiom-ios-cta`) |
| Dialog with an input | Stays fully above the keyboard; it moves up, never under (`wiom-ios-dialog`) |
| Bottom sheet with a form | Grows or scrolls above the keyboard (`wiom-ios-bottomsheet`) |
| Toast | Appears above the keyboard when it is up (`wiom-ios-toast`) |
| Dismissal | Scrolling the form dismisses the keyboard interactively (`.scrollDismissesKeyboard(.interactively)`, iOS 16) |

---

## 7. Status bar

iOS can't colour the status bar (D8). The top bar's background extends under it. Status-bar content:

| Surface under the status bar | Content style |
|---|---|
| `bg/default`, `bg/subtle`, light images | Dark |
| `bg/brand/bold`, `bg/inverse`, `bg/brand`, dark images | Light |

Set per screen through the hosting controller's `preferredStatusBarStyle` (SwiftUI on iOS 16 has no per-view modifier for it without a navigation bar). The top-bar skill gives the pattern.

---

## 8. Checks

- [ ] No width constants (360, 328, 312 only as a **max** for the dialog).
- [ ] No text-holding view with a fixed height.
- [ ] Every tappable element ≥ 44 × 44 pt, with a label.
- [ ] No `.offset` used for layout; no child padding used as a margin.
- [ ] Bottom CTAs use the sticky CTA bar component.
- [ ] Checked on SE and Pro Max, in Hindi and English, at default and `accessibility3`.
