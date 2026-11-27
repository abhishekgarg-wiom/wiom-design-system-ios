---
name: wiom-ios-page-states
description: "Wiom full-screen page states for the iOS customer app in SwiftUI: loading, empty and error with retry, shown in a screen's content area when the whole page has nothing else to show. Use when a screen is waiting for its first data, has no data, or its main call failed; not for inline waits (wiom-ios-loader) or partial failures (wiom-ios-inline-banner)."
---

# Wiom Page States (iOS)

What a screen shows in its content area when the whole page is loading, empty, or failed. The top bar stays, so the user can always go back.

Contract: `../wiom-ios-foundations/references/decisions.md` (D14, D16, D17, D20). Uses `wiom-ios-loader`, `wiom-ios-icon-badge`, `wiom-ios-cta`.

## 1. Which state

| Situation | State |
|---|---|
| First load, layout known | **Loading**: Skeleton of that layout (`wiom-ios-loader`) |
| First load, layout unknown or very short wait | **Loading**: Spinner lg, centred |
| App launch or an explicit branded wait | Brand loader (`wiom-ios-loader`, D37) |
| Data loaded but there is nothing to show | **Empty** |
| The page's main call failed | **Error with retry** |
| One section failed, the rest is fine | Inline banner in that section (`wiom-ios-inline-banner`) |
| Offline, cached data still visible | Persistent Warning toast (`wiom-ios-toast`) |

## 2. Anatomy (empty and error)

A centred column in the content area, inside the `space/16` gutter.

| Slot | Value | Token |
|---|---|---|
| Badge | Icon Badge Lg (96 pt circle, 48 pt glyph) | `wiom-ios-icon-badge`; Neutral for empty, Critical for error |
| Badge → text | | `space/24` |
| Title | Centred, wraps | `type/heading/md` · `text/default` |
| Title → body | | `space/8` |
| Body | Centred, wraps | `type/body/md` · `text/subtle` |
| Text → CTA | | `space/32` |
| CTA | Empty: optional Primary that fixes the emptiness. Error: Primary "दोबारा कोशिश करें / Try again" | `wiom-ios-cta` |

## 3. Rules

1. **Keep the top bar.** Never replace the whole screen; back must work.
2. **Skeleton first** when the layout is known; a spinner only when it isn't.
3. **Error always has a way forward:** Try again, plus back. Phone offline uses the app's line: "इंटरनेट से कनेक्ट करके दोबारा कोशिश करें" / "No internet connection on your phone." Say what failed in plain words; no error codes.
4. **Try again** re-runs the same call and shows Loading again; it never navigates.
5. **Empty is not an error.** Neutral tone, and a next step when there is one.
6. Copy is illustrative and comes from the catalog (D25); text wraps and never truncates.

## Settled rules

- **Auto-retry (D45):** none; the user taps Try again.
- **Illustrations (D61):** empty and error show an Icon Badge Lg (96 pt circle, Material Rounded glyph) until design supplies illustrations.

## Open questions

1. **Figma.** No page-state component in Figma; this recipe comes from the loader, icon-badge and CTA skills.

## Accessibility strings

| Key | English meaning |
|---|---|
| `common.loading` | "Loading" |
| `common.retry` | "दोबारा कोशिश करें" / "Try again" |

Hindi text comes from the catalog; new strings need approval (D39).

## iOS (SwiftUI, iOS 16+)

- **Built from:** the screen's content area switches on its load state (loading, content, empty, error). Empty and error are a centred `VStack` inside a `ScrollView`, so large text can scroll.
- **Tokens:** `type/heading/md`, `type/body/md`, `text/default`, `text/subtle`, `space/8`, `space/16`, `space/24`, `space/32`, plus the loader, icon-badge and CTA tokens.
- **Size:** fills the content area between the top bar and the bottom safe area.
- **Dynamic Type:** text scales and wraps; the column scrolls when it no longer fits.
- **VoiceOver:** when the state changes, post `.screenChanged` with the title so focus moves to it. Loading is one element labelled "Loading" with `.updatesFrequently`.
- **Hit area:** the CTA (≥ 44 pt, default 48).
- **Motion:** state changes cross-fade on `motion/micro`; Reduce Motion keeps the fade (D20).
- **Safe areas and keyboard:** content stays inside the safe area; no keyboard.
- **Haptics:** none (D21).
