# Warning icons: the three approved combinations

**Owner-finalised: D31, 23 Nov 2026.** Applies to every iOS component. These are the only permitted uses of the Warning gold/icon pairing vocabulary; this does not restrict unrelated text, border or status-family tokens.

| Use | Foreground | Background | Rule |
|---|---|---|---|
| Rating stars only | `icon/warning` | The rating component’s documented surface | Gold is a rating colour only. The recognisable star and spoken rating value carry its meaning. Never use this gold colour for a Warning triangle, alert or input status glyph. |
| Warning indicator, subtle surface | `icon/action` | `bg/warning/subtle` | Dark glyph on pale yellow. Applies to toast, input status and Warning icon badges. |
| Warning indicator, solid surface | `icon/action` | `bg/warning` | Dark glyph on solid gold. Use only when the component specifies a solid Warning surface; this is not permission to recolour the whole toast or input. |

## Values and measured contrast

| Pair | Values | Ratio |
|---|---|---|
| Dark on subtle Warning | `icon/action` #352D42 on `bg/warning/subtle` #FFE9A1 | 10.85:1 |
| Dark on solid Warning | `icon/action` #352D42 on `bg/warning` #E2B203 | 6.60:1 |
| Rating gold on neutral | `icon/warning` #E2B203 on `bg/default` #FAF9FC | 1.89:1; rating-specific exception, not an icon contrast pass |

Ratios are foreground/background comparisons, not whole-component certification. Do not rely on colour alone: Warning meaning is also stated in readable text and accessibility semantics. Rating stars expose the rating through their host, not as separate unlabeled icons.

## Component application

- **Toast:** neutral `bg/default` outer surface, dark Warning glyph on `bg/warning/subtle` inside the leading icon container. Message stays `text/onWarning`. Existing spacing, motion and two-line rules remain unchanged.
- **Input:** neutral `bg/default` field, dark Warning glyph on `bg/warning/subtle` inside the status-icon container. Helper stays `text/onWarning`; the Warning border is a separate token and contrast question. The status glyph is not an action.
- **Icon badge:** Warning tone is `bg/warning/subtle` plus `icon/action`, preserving the badge’s documented sizes and glyph sizes. A solid surface is allowed only where specified; it does not add an unapproved badge variant.
- **Rating:** gold `icon/warning` remains available for stars only. Component spec: `wiom-ios-rating` (D36). Do not import a Warning triangle into a rating or use a gold star as a Warning indicator.

`icon/action` is a colour-role reuse for Warning status, not a command to make the icon tappable. Decorative badges and embedded indicators remain hidden from VoiceOver individually; the host carries the meaning.

## Superseded and open

Gold Warning glyphs on neutral, subtle-yellow or solid-yellow backgrounds are prohibited. The previous gold-on-tint contrast exception no longer applies to Warning indicators. Generic same-family rules yield to D31’s dark-icon recipe.

**Toast/input container (D35):** Icon Badge Sm, a 24 pt circle with a 16 pt glyph on `bg/warning/subtle`. No new size. Other open issues, including input boundary contrast, pressed brand text, Dynamic Type policy and the switch-thumb semantic mapping, are not closed by this colour ruling.
