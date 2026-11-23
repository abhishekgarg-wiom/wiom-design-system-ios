# Icons on iOS: the same Material Rounded glyphs as Android

**Contents:** 1 Source · 2 Export and naming · 3 Using an icon · 4 Fill rules and categories · 5 Brand and partner icons · 6 Missing icons · 7 Never

---

## 1. Source

Android draws icons from `Icons.Rounded.*` (Compose `material-icons-extended`), which is Google's **Material Icons, Round style**. iOS uses **exactly those glyphs** so both apps look identical (D4).

- Source: `github.com/google/material-design-icons`, path `src/<category>/<icon_name>/materialiconsround/24px.svg`.
- Same name on both platforms: Compose `Icons.Rounded.ArrowBack` ↔ `arrow_back`; `Icons.Rounded.ChevronRight` ↔ `chevron_right`; `Icons.Rounded.BookmarkBorder` ↔ `bookmark_border`.
- Don't use the newer **Material Symbols** (variable font) set: its Rounded glyphs differ slightly from Compose's `Icons.Rounded`. If Android ever moves to Symbols, iOS moves with it.
- **SF Symbols are never used** for Wiom UI, including the back arrow, chevrons, close, share and checkmarks.

---

## 2. Export and naming

| Step | Rule |
|---|---|
| File | The 24 px SVG, unchanged (no hand edits, no re-drawing) |
| Asset name | `ic_rounded_<material_name>`, e.g. `ic_rounded_arrow_back` |
| Asset settings | **Render As: Template Image** · **Preserve Vector Data: on** · Scales: Single Scale |
| Swift | `Wiom.Icon.arrowBack` (lowerCamelCase of the Material name), returning `Image("ic_rounded_arrow_back")` |
| State pairs | Use named Round-family pairs such as `bookmark` / `bookmark_border` where the component specifies them. The unused navigation reference uses Rounded fill off by default and its filled pair on selection. If that approved glyph is unavailable, report the asset gap; do not import another family or fake a fill variant. |
| Mirroring | Directional icons (`arrow_back`, `chevron_right`) are not mirrored: the app is LTR in both Hindi and English |

Only icons the app uses are exported. The list lives next to the asset catalog (`Icons.md`), with the Compose name for each, so Android and iOS can be diffed.

---

## 3. Using an icon

```swift
Wiom.Icon.close
    .renderingMode(.template)
    .resizable()
    .frame(width: Wiom.IconSize.md, height: Wiom.IconSize.md)
    .foregroundColor(Wiom.Colors.iconAction)
```

- Glyph sizes: `icon/xs` 16 · `icon/sm` 20 · `icon/md` 24 (default) · `icon/lg` 48. No other sizes. Icon size does **not** scale with Dynamic Type, except where a component skill says so (icons inside a CTA stay 20).
- Tint with `icon/*` tokens only (never `text/*`, even inside a CTA).
- A tappable icon is a `Button` with a ≥ 44 pt hit area (default 48) and an `accessibilityLabel` from the string catalog (`layout.md` §4, `accessibility.md`).
- A decorative icon is `.accessibilityHidden(true)`.

---

## 4. Fill rules and categories

Round-family glyphs are the default. Use named outline twins only where a toggle explicitly requires them; navigation uses fill off by default and the filled pair on selection.

| Category | Examples (Material name) | Default | Selected / on | Tint |
|---|---|---|---|---|
| Action | `arrow_back`, `search`, `share`, `close`, `edit`, `more_vert` | Filled | n/a | `icon/action` |
| Navigation (not in use, D27) | `home`, `account_balance_wallet`, `account_circle` | Rounded, fill off | Filled pair | `icon/nonAction` → `icon/brand` |
| Status | `check_circle`, `cancel`, `warning`, `info` | Filled | n/a | `icon/positive` / `critical` / `warning` / `info` |
| Toggle | `bookmark` / `bookmark_border`, `favorite` / `favorite_border` | Outlined (off) | Filled (on) | `icon/nonAction` → `icon/brand` |
| Brand | Wiom logo | Original colours | n/a | Not tinted (`renderingMode(.original)`) |
| Partner | WhatsApp, YouTube logos | Original colours | n/a | Not tinted |

---

## 5. Brand and partner icons

`ic_wiom_*` and `ic_partner_*` come from the design team as SVG or PDF (the same files Android uses as vector drawables). Render As: **Original Image**. Never generated, traced or recoloured by an agent.

---

## 6. Missing icons

If the design shows an icon that isn't in Material Icons Round:

1. Don't draw, trace, or substitute an SF Symbol.
2. Ask the design team for the asset (`ic_wiom_<name>`).
3. Report the missing asset and leave only a ticketed `// TODO(IOS-123): …` at the integration point. Do not substitute a help glyph for a meaningful icon.

---

## 7. Never

- SF Symbols (`Image(systemName:)`) in Wiom UI.
- Material Symbols, Sharp, Material Icons Outlined, Two-tone. Named border/outline glyphs within the Round family are allowed.
- Icon sizes outside 16 / 20 / 24 / 48.
- Tinting brand or partner logos.
- A tappable icon with a hit area under 44 pt, or without a label.


## Warning colour versus glyph identity

A Material Rounded Warning glyph uses dark `icon/action` on `bg/warning/subtle` or `bg/warning` (D31). The gold token named `icon/warning` is reserved for rating stars only. Names describe colour roles, not glyph choice or whether a status icon is tappable. Full pairings: [warning-combinations.md](warning-combinations.md).
