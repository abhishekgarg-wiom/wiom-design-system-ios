# Accessibility on iOS: what every Wiom screen and component does

**Contents:** 1 VoiceOver · 2 Dynamic Type · 3 Hit areas · 4 Reduce Motion · 5 Colour and contrast · 6 Per-component summary · 7 Test pass

Every component skill has an iOS section that applies these rules to that component. This file is the shared baseline.

---

## 1. VoiceOver

| Rule | How |
|---|---|
| Every tappable element has a label | `accessibilityLabel` from the string catalog, in the user's language. Icon-only buttons included ("Back", "Close", "Share": illustrative) |
| Labels say what, not how | "Recharge" not "Recharge button" (the trait says "button") |
| Traits match the role | `.isButton`, `.isHeader` (screen and section titles), `.isSelected` (tabs, chips, selected rows), `.isModal` (dialogs, sheets, full-screen loaders), `.updatesFrequently` (live timers, progress) |
| Values for state | Switch "on/off", checkbox "checked / not checked / mixed", progress "40 percent", pager "page 2 of 5" via `accessibilityValue` |
| Disabled is truly disabled | `.disabled(true)`, so VoiceOver says "dimmed". Never a button that swallows taps silently |
| One row, one element | A list row, card or tile that is tapped as one unit is one element: `.accessibilityElement(children: .combine)` or an explicit label. Embedded checkbox/radio/switch/icon badge indicators are hidden individually when the row owns that one action. A separate trailing action keeps its own accessible target; do not combine unrelated actions into a single row element |
| Decorative = hidden | Icon badges, illustrations, dividers, decorative icons: `.accessibilityHidden(true)` |
| Announcements | For relevant changes that appear without focus moving (toast, inline error, "copied", load finished), post `UIAccessibility.post(notification: .announcement, argument: text)`. Announce the changed result once, not on every render or animation frame. Do not announce the same modal title again after moving focus to it |
| Modals trap focus | Dialogs, sheets and full-screen loaders are `.isModal`; content behind them is not reachable; focus moves to the title on open and returns to the trigger on close |
| Escape | Dismissable dialogs and sheets handle the two-finger scrub (`.accessibilityAction(.escape)`); non-dismissable ones don't |
| Reading order | Matches the visual order; use `.accessibilitySortPriority` only to fix a real mismatch |
| Numbers and money | "₹299" reads correctly by default; don't spell it out. Counts like "9+" have a spoken form ("more than 9") in the string catalog |

## 2. Dynamic Type

- Every text style scales (`typography.md` §3); the app caps at `accessibility3`.
- Nothing holding text has a fixed height (D16); rows, buttons, chips, badges and bars grow.
- At large sizes: text wraps first; side-by-side layouts stack (button groups, title + trailing meta); screens scroll. Truncate only where a component skill allows it.
- CTA labels wrap as needed, never truncate (`wiom-ios-cta`).
- Icons don't scale (they keep 16/20/24/48) unless a component skill says otherwise.
- Check Hindi and English: Hindi is usually longer and taller.

## 3. Hit areas

≥ 44 × 44 pt, default 48 × 48, for every tappable element, independent of its visible size (`layout.md` §4).

## 4. Reduce Motion

Every animation has its reduced form (`motion.md` §5). Meaning must survive with all motion removed: a sheet that fades in still reads as a sheet because of its scrim and position.

## 5. Colour and contrast

- Never use colour alone for meaning: errors have text, selected chips have `.isSelected`, status badges have words or a spoken value.
- Known sub-AA pairs and their mitigations: `tokens.md` §9. Don't introduce new pairs outside the contrast table without a check.
- Light mode only (D23); "Increase Contrast" and "Smart Invert" are not specially handled yet: note any screen that breaks under them.

## 6. Per-component summary

| Component | VoiceOver shape |
|---|---|
| Button (CTA) | Button; label = text; loading adds value "loading"; disabled = dimmed |
| Top bar | Title `.isHeader`; back = button "Back" |
| Input | Label + value + helper/error in the value; error announced when it appears |
| OTP | One field: "verification code, 4 of 6 digits entered" (illustrative) |
| Switch | "switch button, on/off" (iOS toggle) |
| Checkbox / Radio | Button with value checked/not checked; radio group items `.isSelected` |
| List row | One element; trait button if tappable; state in the value |
| Pill tabs / underline filters | Button + `.isSelected`; position/count follows the component skill |
| Chips | One button per chip + `.isSelected` when on; label is chip text, close glyph hidden; no tab position/count |
| Badge | Hidden; host's label carries it ("Notifications, 3 new") |
| Toast | Announced; action toasts stay while VoiceOver runs |
| Dialog / sheet | `.isModal`; title first; escape if dismissable |
| Loader | Spoken label; full-screen ones are modal |
| Progress | Value "40 percent" / "step 2 of 4" |
| Pagination | "page n of N"; adjustable where swipeable |

## 7. Test pass (every screen)

- [ ] VoiceOver: every element reachable, labelled, in order; no unlabelled icon buttons.
- [ ] Dynamic Type at `xxxLarge` and `accessibility3`: no clipping, no overlap.
- [ ] Reduce Motion on: no slides or loops except the spinner.
- [ ] Hit areas: every tappable element ≥ 44 pt (Accessibility Inspector).
- [ ] Hindi and English.


## 8. Native evidence and reusable hosts

Use [native validation](native-validation.md) when implementing or reviewing a screen. It lists the keyboard, reflow, modal-focus and navigation checks that cannot be proved by HTML. The current Dynamic Type cap and icon-size policy remain unchanged; their open questions are not resolved by this checklist.
