---
name: wiom-ios-icon-badge
description: "Wiom icon badge for the iOS customer app in SwiftUI: one glyph in a tinted circle, 3 sizes and 6 tones, used as a decorative leading or hero badge. Use when building or reviewing a list-row leading badge, status-card badge or empty-state hero glyph in SwiftUI; not for avatars or round icon buttons."
---

# Wiom Icon Badge (iOS)

A single Material Rounded glyph centred in a filled circle. **3 sizes × 6 tones = 18 combinations.** Always circular, always filled, no border, no shadow. **Decorative only:** it is never a tap target and never a VoiceOver element; the parent row, card or dialog carries the meaning and the tap.

Contract: `../IOS_DECISIONS.md`. Tokens: `wiom-ios-foundations` (`references/tokens.md`, `icons.md`, `layout.md`, `accessibility.md`).

### Is this the right component?

| You want | Use |
|---|---|
| A glyph in a tinted circle, leading a row, heading a status card or dialog, or as an empty-state hero | **This skill** |
| A count, dot or text chip ("5+", "Active") | `wiom-ios-badge` |
| A person's photo or initials | An avatar, not this (no Wiom avatar component yet) |
| A round tappable icon (close, call, share) | An icon button in its host (`wiom-ios-top-bar`, etc.), not this |
| A multi-colour picture, or anything bigger than 96 pt | An illustration asset |

## 1. Sizes

| Size | Container | Glyph | Padding (all sides) | Use for |
|---|---|---|---|---|
| `sm` | 24 × 24 pt | 16 pt (`icon/xs`) | 4 pt (`space/4`) | Compact list-row leading; inline in toast, chat or completion meter |
| `md` | 48 × 48 pt | 24 pt (`icon/md`) | 12 pt (`space/12`) | Comfortable list-row leading, settings entry, status summary card |
| `lg` | 96 × 96 pt | 48 pt (`icon/lg`) | 24 pt (`space/24`) | Empty-state hero, onboarding step |

Container = glyph + 2 × padding. Corner `radius/full` (a circle). These are fixed, non-text glyph shapes (D16): the size enum is the contract, never a call-site frame. No 32 pt, 40 pt or 64 pt badges.

The dialog Alert header is the owner-locked exception to the generic Neutral tint: it uses `bg/subtle` + `icon/action` in a 48 pt circle (`wiom-ios-dialog`, commit `23f67f9`). Do not apply its tint to every Neutral badge.

## 2. Tones

Fill and glyph use the same status family except Warning: D31 requires dark `icon/action` on the Warning background. Gold `icon/warning` is ratings-only.

| Tone | Container fill | Glyph tint | Means |
|---|---|---|---|
| `neutral` (default) | `bg/subtle` | `icon/nonAction` | Decorative, settings, neutral info |
| `brand` | `bg/brand/subtle` | `icon/brand` | Featured, promoted, Wiom-flagged |
| `positive` | `bg/positive/subtle` | `icon/positive` | Success, step done, all clear |
| `warning` | `bg/warning/subtle` | `icon/action` | Attention needed, expiring soon |
| `critical` | `bg/critical/subtle` | `icon/critical` | Failed, error, critical alert |
| `info` | `bg/info/subtle` | `icon/info` | Tip, help, neutral system message |

- **DECIDED (D31):** Warning tone uses dark `icon/action` on `bg/warning/subtle` (10.85:1). Dark `icon/action` on `bg/warning` is the other approved Warning pairing where a solid Warning surface is specified. Keep the existing badge geometry; do not add a solid variant without a component specification. Gold `icon/warning` is for rating stars only, never a Warning badge.
- The `info` family is themed (purple in the current theme). Use the tokens; never substitute a literal blue.
- Server-driven "blue info" or "orange warning" maps to `info` and `warning` (D22).

## 3. Choosing size and tone

```
Row leading slot, compact row            → sm
Row leading slot, comfortable row        → md
Settings / category row                  → md
Status summary card ("Plan active")      → md
Dialog Alert header                      → wiom-ios-dialog owns the neutral-circle icon/action override (23f67f9)
Empty-state hero, onboarding step        → lg
Inline in toast / chat / meter           → sm
```

Tone follows the meaning of the parent's text (table above). If the status is the point of the row, the **text** must say it too ("Payment failed"), because the badge is invisible to VoiceOver and colour alone is not enough.

## 4. Hosts and who owns the tap

| Host | Badge role | Tap and label owned by |
|---|---|---|
| `wiom-ios-list-item` (primary host) | Leading slot | The row: one VoiceOver element, ≥ 44 pt tall |
| `wiom-ios-dialog` Alert header | Status cue above the title | Nothing to tap; the title and body carry the meaning |
| Status summary card | Leading the card's title | The card, if tappable |
| Empty-state hero | Above heading and body | The page CTA below (`wiom-ios-cta`) |
| `wiom-ios-toast` | Inline leading | The toast |

If a design wants the badge itself to be tappable, it is the wrong component: make the parent (row, card) the button, or use an icon button.

## 5. Universal rules

1. Always a circle. A rounded-square container is a different component: flag it.
2. Always filled. No border, no shadow.
3. One glyph only. No text, no count overlay (place a `wiom-ios-badge` as a sibling if both are needed), no multi-colour artwork.
4. Decorative only: no tap handler, hidden from VoiceOver.
5. Fill and glyph from the same tone family, except the D31 dark-icon Warning recipe.
6. Size from the enum, never from a frame at the call site.
7. Glyphs are Material Icons Rounded, the same glyph Android uses, as template images from the asset catalog (D4). Wiom brand glyphs come from the same catalog as template images. Never SF Symbols.
8. Tokens by DS V2 name only.

### Do / Don't

| Do | Don't |
|---|---|
| `md`, `positive`, check glyph, beside "Plan active" | A green check badge as the only signal that something succeeded |
| Let the settings row own the tap and the label | Wrap the badge in its own `Button` |
| Pick `sm` or `md` | Resize to 32 pt "because it looks better" |
| Warning tint with dark `icon/action` glyph | Gold `icon/warning` glyph used as a Warning indicator |

## Open questions

| # | Question | Default in this skill |
|---|---|---|
| 1 | A `neutral` badge (`bg/subtle`) inside a pressed list row (pressed fill `bg/subtle`, D13) disappears into the row while pressed. Android behaves the same. Intended? | Keep parity; no change. |
| 3 | **DECIDED (D31):** dark Warning glyph on subtle or solid Warning background; gold glyph is ratings-only. | 10.85:1 on subtle; 6.60:1 on solid. The old gold-on-tint exception is superseded. |
| 2 | Figma ships only the Neutral tone; the other five are built from tokens (Android does the same, `WiomIconBadge.kt:158-167`). Will Figma add tone variants? | Tones as in §2. |

The original baseline matched badge sizes/padding. D31 now overrides the old Warning tone pair; shared source and Android library alignment are separate follow-up work, not edits authorised here.

## iOS (SwiftUI, iOS 16+)

- **Built from:** a template `Image` from the asset catalog (`Wiom.Icon.*`), framed to the glyph size, on a `Circle()` fill, framed to the container size. Not `Label`, not `Image(systemName:)`.
- **Tokens:** `bg/subtle`, `bg/brand/subtle`, `bg/positive/subtle`, `bg/warning/subtle`, `bg/critical/subtle`, `bg/info/subtle`, `icon/nonAction`, `icon/brand`, `icon/positive`, `icon/action`, `icon/critical`, `icon/info`, `icon/xs`, `icon/md`, `icon/lg`, `space/4`, `space/12`, `space/24`.
- **Size:** fixed 24 / 48 / 96 pt container (D16, non-text glyph shape). The badge never stretches; the host aligns it (rows: per `wiom-ios-list-item`; heroes: centred).
- **Dynamic Type:** the badge does not scale. The parent's text does, and the host keeps the badge aligned as the text grows (rows align it to the top of a wrapped text block per the list-item skill).
- **VoiceOver:** always `.accessibilityHidden(true)`. The parent carries the full label, including any meaning the glyph or tone suggests ("Wiom Pro", "Payment failed").
- **Hit area:** none on the badge. The parent row or card is the target, ≥ 44 × 44 pt (D14); list rows are 48 pt minimum.
- **Motion:** none. The badge does not animate; tone changes are instant.
- **Safe areas and keyboard:** not applicable; the host surface handles them.
- **Haptics:** none (D21).
- **Not on iOS:** SF Symbols, `.symbolRenderingMode`, a `contentDescription`-style label on the badge, border (`strokeBorder`) or shadow, pressed visual on the badge itself.

```swift
enum WiomIconBadgeSize { case sm, md, lg }        // container 24 / 48 / 96, glyph icon/xs / md / lg
enum WiomIconBadgeTone { case neutral, brand, positive, warning, critical, info }

struct WiomIconBadge: View {
    let icon: Image                                // e.g. Wiom.Icon.settings (template)
    var size: WiomIconBadgeSize = .md
    var tone: WiomIconBadgeTone = .neutral

    var body: some View {
        icon.renderingMode(.template).resizable().scaledToFit()
            .frame(width: size.glyph, height: size.glyph)
            .foregroundColor(tone.glyph)           // §2 tone recipe; Warning uses icon/action under D31
            .frame(width: size.container, height: size.container)
            .background(Circle().fill(tone.fill))
            .accessibilityHidden(true)
    }
}

// The row is the element and the target; the badge is decoration.
Button(action: openProfile) {
    HStack(spacing: Wiom.Spacing.s12) {
        WiomIconBadge(icon: Wiom.Icon.person, size: .md)
        Text("Profile")                             // illustrative copy
        Spacer()
    }
    .frame(minHeight: 48)
    .contentShape(Rectangle())
}
```
