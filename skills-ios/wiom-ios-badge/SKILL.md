---
name: wiom-ios-badge
description: >
  Wiom badge for the iOS customer app (SwiftUI): the passive, non-tappable
  Dot, Count and Label badges (WiomBadgeDot, WiomBadgeCount,
  WiomBadgeLabel) that mark unread items, show a number on an icon or
  tab, or show a state in a row or card. Use when building, reviewing or
  placing a Wiom Dot, Count or Label badge in SwiftUI on iOS.
---

# Wiom badge (iOS)

**3 types · 23 iOS variants (Dot 3 · Count 3 · Label 17) · passive.**

| Type | Variants on iOS |
|---|---|
| Dot | Tone: Brand · Critical · Neutral |
| Count | Tone: Brand · Critical · Neutral |
| Label | Default Filled × 5 tones (Positive · Warning · Critical · Info · Neutral) · Default Tinted × 6 tones (+ Brand) · Small Tinted × 6 tones |

Badges are **passive**: never tappable, never a button. If it needs a
tap, it is a chip (`wiom-ios-tabs-filters`), not a badge. A glyph inside
a coloured circle is `wiom-ios-icon-badge`, not this component.

This skill follows `wiom-ios-foundations/references/decisions.md` (parity principle: badges look
as Android ships them, except the owner-selected count display rule in §5). Tokens are cited by DS V2 name; values
live in `wiom-ios-foundations`.

## 1. Anatomy

### Dot

| Slot | Value | Token |
|---|---|---|
| Size | **Fixed 8 × 8 pt** (no content; does not scale with Dynamic Type) | n/a |
| Shape | Circle | `radius/full` |

### Count

| Slot | Value | Token |
|---|---|---|
| Width | Hugs the number; **minimum** 20 pt, grows for "9+" / "99+" | n/a |
| Height | **Minimum** 20 pt; grows with Dynamic Type | n/a |
| Shape | Full pill | `radius/full` |
| Horizontal padding | 4 pt | `space/4` |
| Number | Regular 10 / 16 | `type/meta/xs` |
| Alignment | Centred both axes | n/a |

`type/meta/xs` is allowed here only because a count is Western digits
(D18). Never put Devanagari text in a Count.

### Label

| Slot | Default | Small | Token |
|---|---|---|---|
| Width | Hugs content | Hugs content | n/a |
| Height | **Minimum** 28 pt (4 + 20 + 4) | **Minimum** 24 pt (4 + 16 + 4) | n/a |
| Radius | 4 pt, circular corners (D3) | 4 pt | `radius/tiny` |
| Horizontal padding | 12 pt | 8 pt | `space/12` / `space/8` |
| Vertical padding | 4 pt | 4 pt | `space/4` |
| Text | SemiBold 14 / 20 | SemiBold 12 / 16 | `type/label/md` / `type/label/sm` |
| Lines | **1**, tail truncation | **1**, tail truncation | n/a |

**No fixed width or height on Count or Label.** Size comes from padding +
content; the 20 / 28 / 24 pt values are minimums. The Dot is the only
fixed size.

## 2. The 3 types

| Type | Purpose | Where it sits | Don't use for |
|---|---|---|---|
| **Dot** | "Something new here", no number or text needed: unread, new | **Overlay only**: top-trailing corner of an icon or avatar | Numbers (Count), explained state (Label), inline in a row |
| **Count** | A number attached to an icon, tab or row | **Overlay** on an icon (bell + number) or **inline** after a tab or row label | Zero (hide the badge), non-numeric content, state |
| **Label** | A text state or role | **Inline** in a list row, card or header | Anything tappable, long copy, several stacked states |

Customer-app examples (illustrative only; real copy comes from the
string catalog, Hindi first, English written separately, sentence
case):

| Badge | Example |
|---|---|
| Dot · Critical | On the notification bell in the top bar |
| Count · Critical, overlay | Bell with "3" |
| Count · Neutral, inline | Support tab "टिकट" + "2" |
| Label · Default Filled · Critical | Payment history row: "असफल" / "Failed" |
| Label · Default Filled · Positive | Payment history row: "पूरा हुआ" / "Completed" |
| Label · Default Tinted · Info | Complaint row: "प्रगति में" / "In progress" |
| Label · Small Tinted · Brand | Plan card: "सबसे लोकप्रिय" / "Most popular" |

## 3. Tokens per type and tone

### 3.1 Dot

| Tone | Fill |
|---|---|
| Brand | `bg/brand` |
| Critical | `bg/critical` |
| Neutral | `bg/muted` |

### 3.2 Count

| Tone | Fill | Number |
|---|---|---|
| Brand | `bg/brand` | `text/onBrand` |
| Critical | `bg/critical` | `text/onCritical` |
| Neutral | `bg/muted` | `text/subtle` |

### 3.3 Label, Filled (Default size only)

| Tone | Fill | Text |
|---|---|---|
| Positive | `bg/positive` | `text/onPositive` |
| Warning | `bg/warning` | `text/onWarning` |
| Critical | `bg/critical` | `text/onCritical` |
| Info | `bg/info` | `text/onInfo` |
| Neutral | `bg/muted` | `text/subtle` |
| Brand | **Not available.** Falls back to Brand Tinted (as Android ships) | n/a |

> **Warning is dark on gold.** The warning family's only text token is
> `text/onWarning`; white on `bg/warning` fails contrast. This is a
> foundations rule, not a badge rule.

### 3.4 Label, Tinted (Default and Small)

| Tone | Fill | Text |
|---|---|---|
| Brand | `bg/brand/subtle` | `text/brand` |
| Positive | `bg/positive/subtle` | `text/positive` |
| Warning | `bg/warning/subtle` | `text/onWarning` |
| Critical | `bg/critical/subtle` | `text/critical` |
| Info | `bg/info/subtle` | `text/info` |
| Neutral | `bg/subtle` | `text/subtle` |

- There is **no `text/warning` token**; Warning uses `text/onWarning` in
  both styles.
- **Two greys:** Filled Neutral is `bg/muted`; Tinted Neutral is
  `bg/subtle` (the lighter one, so it reads as recessed). Easy to swap
  by mistake.
- **Small is Tinted only.** Asking for Small Filled gives Small Tinted.

## 4. Placement

| Type | Position | How |
|---|---|---|
| Dot | Overlay, top-trailing corner of the host icon or avatar | Aligned to the host's top-trailing corner, no nudge: at 8 pt it sits inside the corner of a 24 pt icon |
| Count | Overlay on an icon, or inline | Overlay: aligned top-trailing, then nudged 4 pt outward and 4 pt up so it sits on the icon's corner. Inline: after the tab or row label, gap `space/8` |
| Label | Inline in a row, card or header | Next to its neighbour text, gap `space/8`; hugs content, never fills |

The parent places the badge and owns the gap; the badge has no outer
margin.

**One badge per row.** Never put two badges on one line. If a row has
two status dimensions, the row is doing too much: split it, or move one
into the secondary text.

## 5. Count display rules

1. **Hide at zero.** A count of 0 means no badge. Never show "0".
2. **One rule in every placement.** 1 to 9 render as the digit;
   10 to 99 render as **"9+"**; 100 or more render as **"99+"**.
   Never show a raw count of 10 or more.
3. **Western digits, in Hindi too** (default; see Open questions). The
   badge renders `String(count)` / "9+" / "99+" in Western digits
   regardless of the app language. Do not run it through a
   locale-aware number formatter.
4. **The visible "9+" is not what VoiceOver says.** The spoken form is
   "more than 9" / "more than 99" from the string catalog (§8).

## 6. Label copy and truncation

- **Single line, always.** Never wraps. If the text does not fit, it
  **tail-truncates** with an ellipsis; that is a signal to rewrite.
- **Length limit:** at most **10 grapheme clusters in Hindi** and **14
  in English** (counted with `String.count`; "क्षि" is one). The source
  skill sets no number; these are the chip-label limits from
  `wiom-ios-tabs-filters`, used until the design team sets badge ones
  (Open questions).
- **The badge keeps its full width before its neighbours do.** In a
  row, the primary text wraps or truncates first; the badge truncates
  only when it alone no longer fits (accessibility text sizes, iPhone
  SE).
- **Specific, not generic.** Never "Status", "State", "Active" on its
  own; say what the state is (illustrative: "असफल", "पूरा हुआ").
- English in sentence case ("In progress", not "IN PROGRESS").

## 7. Decision logic

```
Step 1: Type
  "Something new / unread", no number or text      → Dot
  A number (unread, tab counter)                    → Count
  A text state or role                              → Label (Step 2)

Step 2: Label size
  Remove the badge: does the row still do its job?
    Yes, the badge supports other content            → Small
    No, the badge IS the information (payment result) → Default

Step 3: Label style (Default only; Small is Tinted)
  Is the state final?
    Yes: completed, failed, confirmed, expired       → Filled
    No: processing, pending, active, eligible        → Tinted

Step 4: Tone
  Success / confirmed / complete / eligible          → Positive
  Pending / provisional / needs attention            → Warning
  Failed / expired / revoked                         → Critical
  Active / in progress / informational               → Info
  Brand marker ("Most popular", Wiom-managed)        → Brand (Tinted only)
  Default / inactive / muted                         → Neutral
```

## 8. Rules

1. **Passive.** Never a `Button`, never a tap gesture. Need a tap → chip.
2. **No icons inside badges.** Colour + text is enough.
3. **No fixed size on Count or Label;** minimums only. Dot is fixed 8 pt.
4. **Small is Tinted only. Brand is Tinted only.**
5. **Hide Count at zero; use "9+" for 10–99 and "99+" for 100+, everywhere.**
6. **Label: one line, tail truncation, within the grapheme limit.**
7. **One badge per row.**
8. **Tone matches the row's status family.** No Positive badge on a row
   whose other signals are Critical.
9. **Dot is overlay only.** For a tiny inline marker with text, use a
   Small Tinted Label.
10. **Tokens only**, by DS V2 name. No raw colours.

### Anti-patterns

- ❌ Multi-line badge text, or a badge that wraps at large text sizes.
- ❌ `text/warning` (does not exist).
- ❌ Filled Neutral on `bg/subtle`, or Tinted Neutral on `bg/muted`.
- ❌ An icon + text + colour "status indicator" treated as a badge.
- ❌ A Count or Dot that VoiceOver reads on its own ("9 plus") instead of
  the host saying what it means.

## See also

- `wiom-ios-foundations`: `tokens.md`, `typography.md`,
  `accessibility.md`, `layout.md`.
- `wiom-ios-list-item`: rows that host a trailing Label badge.
- `wiom-ios-top-bar`: hosts the bell with a Dot or Count overlay.
- `wiom-ios-tabs-filters`: chips (the tappable relative) and tab counts.
- `wiom-ios-icon-badge`: glyph in a coloured circle; a different
  component.

## Settled rules

- **No Brand Filled.** Brand is Tinted only; 23 variants in total. Small is always Tinted (Small Filled renders Small Tinted).
- **Label overflow:** one line, tail truncation (ellipsis). Rewrite copy that truncates.
- **Count display:** 1 to 9 as digits, 10 to 99 as "9+", 100+ as "99+", in every placement.

## Open questions

1. **Count nudge.** The overlay Count sits 4 pt up and 4 pt out from top-trailing. Confirm against the shipped Android bell.
2. **Western digits in Hindi.** Counts always use Western digits in both languages. Confirm Devanagari digits are never wanted.
3. **Label length.** No source limit; iOS uses 10 Hindi / 14 English grapheme clusters (the chip limits) until design sets one.
4. **Count minimum under Dynamic Type.** The 20 pt minimum scales with Caption 2 on iOS. Confirm.

## Accessibility strings

Catalog keys this component needs (never literals in code):

| Key | English meaning | Used for |
|---|---|---|
| `badge.count.new` | "%d new" | Host value with a Count |
| `badge.count.over9` | "more than 9 new" | Host value at 9+ |
| `badge.count.over99` | "more than 99 new" | Host value at 99+ |

Hindi text comes from the catalog; new strings need approval (D39).

## iOS (SwiftUI, iOS 16+)

- **Built from:** `WiomBadgeDot` = `Circle().fill(...)` in an 8 × 8
  frame. `WiomBadgeCount` = `Text` with `type/meta/xs`, horizontal
  padding `space/4`, a scaled minimum frame, background `Capsule()`.
  `WiomBadgeLabel` = `Text` with `type/label/md` or `type/label/sm`,
  padding, background
  `RoundedRectangle(cornerRadius: radius/tiny, style: .circular)`.
  Overlays attach with `.overlay(alignment: .topTrailing)` on the host
  icon; the Count's 4 pt nudge uses `.alignmentGuide`, not `.offset`.
- **Tokens:** `bg/brand`, `bg/critical`, `bg/muted`, `bg/subtle`,
  `bg/positive`, `bg/warning`, `bg/info`, `bg/brand/subtle`,
  `bg/positive/subtle`, `bg/warning/subtle`, `bg/critical/subtle`,
  `bg/info/subtle`, `text/onBrand`, `text/onCritical`, `text/onPositive`,
  `text/onWarning`, `text/onInfo`, `text/subtle`, `text/brand`,
  `text/positive`, `text/critical`, `text/info`, `type/meta/xs`,
  `type/label/md`, `type/label/sm`, `radius/full`, `radius/tiny`,
  `space/4`, `space/8`, `space/12`. Swift names per `wiom-ios-foundations/references/decisions.md`
  §2 (`Wiom.Colors.bgCriticalSubtle`, `Wiom.Typography.labelMd`, …).
- **Size:** Dot fixed 8 pt. Count minimum 20 × 20 pt. Label minimum
  28 pt (Default) / 24 pt (Small). Never `.frame(height:)` on Count or
  Label.
- **Dynamic Type:** Count and Label text scale with their type tokens
  (`type/meta/xs` with Caption 2, D18; label anchors in
  `wiom-ios-foundations` `typography.md` §3). The Count's 20 pt minimum
  scales with it (`@ScaledMetric(relativeTo: .caption2)`), so the pill
  stays round around a larger digit. Labels grow taller, stay on one
  line and tail-truncate if they run out of room. The Dot does not
  scale. Check Hindi and English up to accessibility3.
- **VoiceOver:**
  - **Dot and Count are hidden** (`.accessibilityHidden(true)`). The
    host carries the meaning in its label or value: bell button
    "Notifications, 3 new" / "सूचनाएं, 3 नई" (illustrative, string
    catalog); with a Dot, "Notifications, new" (illustrative).
  - **Over the cap, say "more than 9"** (or 99): the host's string uses
    a catalog entry such as `badge.count.overflow` = "more than %lld" /
    "%lld से ज़्यादा" (illustrative), never the visible "9+".
  - **A Label is never its own element.** The row or card it sits in is
    one VoiceOver element (`.accessibilityElement(children: .combine)`
    on the row, per `wiom-ios-list-item`), so the label text is read as
    part of the row, in reading order. Never add a "badge" trait or
    hint.
- **Hit area:** none; badges are not interactive. The host (icon button,
  tab, row) owns the ≥ 44 × 44 pt hit area (D14), and the badge overlay
  must not shrink or block it (`.allowsHitTesting(false)` on overlays).
- **Motion:** none. A badge appears, changes and disappears without
  animation (Android ships none). Reduce Motion has nothing to change.
- **Safe areas and keyboard:** not applicable; badges live inside their
  host.
- **Haptics:** none (D21).
- **Not on iOS:** tap, ripple, hover, focus ring, the Android
  `contentDescription` on the icon (iOS puts it on the host's
  accessibility label), the system `.badge()` modifier on `TabView` or
  `List` (it draws iOS styling, not Wiom's).

### Built from

**Built from:** Count is `Text` with Western digits (1 to 9, then 9+, then 99+) in `type/meta/xs`, `space/4` horizontal padding and a minimum of 20 × 20 pt that scales with Caption 2, on a `Capsule` fill; hidden from VoiceOver. Label is `Text` in `type/label/md` (`type/label/sm` for Small), one line with tail truncation, `space/12` (Small: `space/8`) horizontal and `space/4` vertical padding, on a `radius/tiny` circular rectangle. It has layout priority so neighbouring text gives way first. Small is always Tinted.

**Host example (bell):** the Count sits in a top-trailing overlay on the 24 pt glyph, nudged 4 pt up and 4 pt out, and takes no taps. The host `Button` owns the 48 pt hit area and carries the label and value ("Notifications, 3 new") from the string catalog.

The spoken value is a catalog string ("3 new", "more than 9 new", "more than 99 new"; illustrative). Check the 4 pt nudge against Android side by side.
