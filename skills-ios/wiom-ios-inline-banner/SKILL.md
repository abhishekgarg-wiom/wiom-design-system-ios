---
name: wiom-ios-inline-banner
description: "Wiom inline banner for the iOS customer app in SwiftUI: a status callout inside the page (info, positive, warning, critical) with an icon, text and an optional link action. Use when a screen must explain a state in place, such as account on hold, partial failure or an expiring plan; not for transient messages (wiom-ios-toast) or field errors (wiom-ios-input-fields)."
---

# Wiom Inline Banner (iOS)

A status callout that sits in the page flow. It explains a state that stays true while the screen is open. It does not float, time out or block.

Contract: `../wiom-ios-foundations/references/decisions.md` (D13, D14, D16, D31). Tokens: `wiom-ios-foundations` (`tokens.md`, `colour-usage.md`, `warning-combinations.md`).

## 1. Anatomy

| Slot | Value | Token |
|---|---|---|
| Fill | Status subtle background | `bg/{info,positive,warning,critical}/subtle` |
| Corner | 16 pt, circular | `radius/large` |
| Border | None | |
| Padding | All sides | `space/16` |
| Row | Icon top-aligned with the first text line; gap | `space/8` |
| Icon | 24 pt Material Rounded filled glyph | `icon/md` (size) |
| Title (optional) | One short line | `type/title/sm` |
| Body | Wraps | `type/body/md` |
| Action (optional) | Text link below the body | Tertiary CTA (`wiom-ios-cta`) |

## 2. Tones

| Tone | Fill | Icon | Title | Body |
|---|---|---|---|---|
| Info | `bg/info/subtle` | `info` · `icon/info` | `text/info` | `text/default` |
| Positive | `bg/positive/subtle` | `check_circle` · `icon/positive` | `text/positive` | `text/default` |
| Warning | `bg/warning/subtle` | `warning` · `icon/action` (D31) | `text/onWarning` | `text/onWarning` |
| Critical | `bg/critical/subtle` | `error` · `icon/critical` | `text/critical` | `text/default` |

Body text on critical and positive is `text/default`; their status text colours are for the title only (contrast, `tokens.md`).

## 3. Rules

1. **In place, not floating.** Full width inside the screen gutter, in the content flow, usually at the top of the section it explains.
2. **One banner per section.** Several issues go in one banner as a short list.
3. **Never gold** for Warning glyphs (D31).
4. **Not a toast.** If the message is about a single tap that just happened, use a toast (`wiom-ios-bottomsheet` → Choosing a surface).
5. Copy is illustrative and comes from the catalog (D25); text wraps and never truncates.

## Settled rules

- **Dismissable (D45):** not dismissable by default. If one ever is, add a close button (`icon/action`, 48 pt hit area).

## Open questions

1. **Corner radius.** Uses `radius/large` like cards; the source has no banner component. Confirm.
2. **Figma.** No banner component in Figma; this recipe comes from the foundations error-surface rule.

## Accessibility strings

| Key | English meaning |
|---|---|
| `banner.tone.info` / `.positive` / `.warning` / `.critical` | "Information" / "Success" / "Warning" / "Error" (spoken before the text) |

Hindi text comes from the catalog; new strings need approval (D39).

## iOS (SwiftUI, iOS 16+)

- **Built from:** an `HStack(alignment: .firstTextBaseline)` of the template glyph and a text `VStack`, on a filled `RoundedRectangle`. The optional action is a Tertiary button from `wiom-ios-cta`.
- **Tokens:** as §1 and §2, plus `space/8`, `space/16`.
- **Size:** fills the width; height from content (minimum only, D16).
- **Dynamic Type:** text scales and wraps; the glyph stays 24 pt (D16).
- **VoiceOver:** icon hidden; tone word + title + body read as one element; the action stays a separate button. A banner that appears after the screen loads posts one announcement.
- **Hit area:** only the action (≥ 44 pt, default 48).
- **Motion:** appears and disappears instantly, or with a `motion/micro` fade when it changes in place.
- **Safe areas and keyboard:** none of its own.
- **Haptics:** none (D21).
