---
name: wiom-ios-card
description: "Wiom card for the iOS customer app in SwiftUI: a rounded container that groups related content, flat or elevated, static, tappable or selectable. Use when building or reviewing a plan card, summary card, settings group or any grouped block on an iOS screen; not for list rows (wiom-ios-list-item) or status callouts (wiom-ios-inline-banner)."
---

# Wiom Card (iOS)

A rounded container that groups related content on a screen. **Flat** (border) or **elevated** (shadow), never both. A card is either static, tapped as one unit, or one choice in a selectable set.

Contract: `../wiom-ios-foundations/references/decisions.md` (D3, D13, D14, D16). Tokens: `wiom-ios-foundations` (`tokens.md`, `typography.md`, `layout.md`, `accessibility.md`).

## 1. Anatomy

| Slot | Value | Token |
|---|---|---|
| Fill | Page-coloured surface | `bg/default` |
| Fill (section card) | Grouped settings or section background | `bg/subtle` |
| Corner | 16 pt, circular (D3) | `radius/large` |
| Border (flat) | 1 pt, inside the shape | `stroke/small` · `stroke/subtle` |
| Shadow (elevated) | Instead of the border | `shadow/md` |
| Padding | All sides | `space/16` |
| Title | Optional | `type/title/sm` · `text/default` |
| Body | Optional | `type/body/md` · `text/subtle` |
| Divider | Inset to the card padding | `stroke/small` · `stroke/default` |
| Gaps | Sections `space/16`; title → subtitle `space/8`; content → CTA `space/32` | |

Cards that host list rows have **0 padding**: the rows own it (`wiom-ios-list-item` rule 9).

## 2. States

| State | Visual |
|---|---|
| Default | As anatomy |
| Selected (selectable cards only) | Border `stroke/medium` width · `stroke/selected`; fill unchanged |
| Disabled | Content tokens swap to `text/disabled` / `icon/disabled`; never opacity |

Pressed: no pressed visual (D13); no pressed token exists for cards.

## 3. Rules

1. **Shadow or border, never both.**
2. **Full width** inside the screen gutter (`space/16`); cards stack `space/16` apart (`layout.md` §3).
3. **One tap target per card.** A tappable card is one element; it holds no other buttons. If it needs a button, the card is static and the button is the target.
4. **Status meaning** goes in an inline banner (`wiom-ios-inline-banner`), not in a tinted card.
5. Text has minimum heights only and wraps (D16).

## Settled rules

- Values follow the Android foundations "Card (interactive, flat)" recipe.
- **Pressed (D46):** no pressed fill for now (D13).

## Open questions

1. **Figma.** There is no Card component in Figma; the recipe comes from the foundations.

## Accessibility strings

None of its own. A tappable card's label and value come from its content (catalog strings).

## iOS (SwiftUI, iOS 16+)

- **Built from:** a `VStack` inside a `RoundedRectangle(cornerRadius: radius/large, style: .circular)` background (`.strokeBorder` for flat, `.wiomShadow(.md)` for elevated). Tappable cards are a `Button` with a no-op `ButtonStyle` and a full content shape.
- **Tokens:** `bg/default`, `bg/subtle`, `stroke/subtle`, `stroke/default`, `stroke/selected`, `stroke/small`, `stroke/medium` (widths), `shadow/md`, `radius/large`, `type/title/sm`, `type/body/md`, `text/default`, `text/subtle`, `text/disabled`, `icon/disabled`, `space/8`, `space/16`, `space/32`.
- **Size:** fills the width minus the surface gutter; height from content (minimum only).
- **Dynamic Type:** all text scales and wraps; the card grows.
- **VoiceOver:** a tappable or selectable card is one element (`.accessibilityElement(children: .combine)`), button trait, `.isSelected` when selected. A static card is not an element; its content reads in order.
- **Hit area:** the whole card (≥ 48 pt tall).
- **Motion:** selection border and colour fade on `motion/micro` + `ease/standard` (D28); nothing moves.
- **Safe areas and keyboard:** none of its own; the screen handles them.
- **Haptics:** none (D21).
