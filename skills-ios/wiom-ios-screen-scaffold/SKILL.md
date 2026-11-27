---
name: wiom-ios-screen-scaffold
description: "Wiom screen scaffold for the iOS customer app in SwiftUI: the template every screen starts from, with the top bar, scrolling content, optional sticky CTA bar, the app-root overlay host and keyboard handling. Use when creating or reviewing any new screen, before placing components."
---

# Wiom Screen Scaffold (iOS)

The one structure every screen uses. It puts the shared rules from foundations and the bar skills in one place, so screens don't re-solve safe areas, keyboard or presentation.

Contract: `../wiom-ios-foundations/references/decisions.md` (D5 to D10, D17, D19, D27). Uses `wiom-ios-top-bar`, `wiom-ios-cta`, `wiom-ios-page-states`, `wiom-ios-bottomsheet`.

## 1. Structure (top to bottom)

| Part | Rule | Owner |
|---|---|---|
| Top bar | Always the custom Wiom top bar; system navigation bar hidden; status bar per D8 | `wiom-ios-top-bar` |
| Content | One vertical scroll view; `space/16` side gutter; `space/16` from the top bar to the first content; sections `space/32` apart | `layout.md` |
| Page state | Loading, empty or error replaces the content area only | `wiom-ios-page-states` |
| Sticky CTA bar (optional) | Only when the screen's purpose can't be finished without it; last CTA `space/16` above the home indicator (D19) | `wiom-ios-cta` §7 |
| Overlay host | **Not per screen.** Sheets, dialogs and toasts are layers of the one host at the app root; the screen binds them to its own state | `wiom-ios-bottomsheet` (iOS section) |

Root screens have no back control and no bottom tab bar (D27). Pushed screens use system push/pop with edge-swipe back (D5, D6).

## 2. Keyboard

- The focused field and its helper or error line stay visible above the keyboard and the sticky CTA bar (`wiom-ios-input-fields` §7).
- The sticky CTA bar rides on the keyboard with `space/12` below the button.
- Scrolling dismisses the keyboard interactively.

## 3. Rules

1. **Start every screen from this scaffold.** Don't re-implement top-bar insets, bottom spacing or keyboard handling per screen.
2. **One scroll view** per screen; no nested vertical scrolls.
3. **Gutters belong to the surface**, not the components (`layout.md` §2).
4. **No system presentation** (`.sheet`, `.alert`, `.confirmationDialog`); use the overlay host (D9, D10).
5. Light mode only (D23).

## Open questions

1. **Scroll-under shadow** on the top bar and CTA bar follows each bar's skill; confirm both show it together on long pages.

## Accessibility strings

| Key | English meaning |
|---|---|
| `common.back` | "Back" |

Hindi text comes from the catalog; new strings need approval (D39).

## iOS (SwiftUI, iOS 16+)

- **Built from:** a `NavigationStack` destination whose content is a `ScrollView`; the top bar attaches with `.safeAreaInset(edge: .top, spacing: 0)` and the sticky CTA bar with `.safeAreaInset(edge: .bottom)`; `.toolbar(.hidden, for: .navigationBar)`; `.scrollDismissesKeyboard(.interactively)`.
- **Tokens:** `space/12`, `space/16`, `space/32`, plus the bar skills' tokens.
- **Size:** full screen, portrait only; widths from iPhone SE (375) to Pro Max (440) (D15).
- **Dynamic Type:** content scrolls; bars follow their skills (minimum heights) through accessibility3 (D17).
- **VoiceOver:** reading order top bar → content → CTA bar; the screen title in the top bar carries `.isHeader`.
- **Hit area:** per component (≥ 44 pt, default 48).
- **Motion:** system push/pop (D6); content changes per `wiom-ios-motion`.
- **Safe areas and keyboard:** bars paint into the safe areas; content stays inside them (`layout.md` §5, §6).
- **Haptics:** none (D21).
