# Wiom design skills for iOS

Claude Code skills for the **native iOS customer app** (SwiftUI, iPhone only, iOS 16+), built on **Wiom DS V2**. They are the iOS counterpart of the Android skills in `abhishekgarg-wiom/wiom-design-system` and are written so an iOS user and an Android user see **the same app**: same tokens, type, icons (Material Rounded) and component anatomy. iOS differs only where platform behaviour must win (gestures, safe areas, keyboard, VoiceOver, Dynamic Type, Reduce Motion).

Start with [`wiom-ios-foundations/references/decisions.md`](wiom-ios-foundations/references/decisions.md): the parity rule, the decisions every skill follows, the Swift naming rule, and the questions still open for the design team.

**Skills define design and behaviour; the Swift API lives in the app repo.** Each skill gives anatomy, tokens, states, sizes and iOS behaviour, with short "Built from" notes. The app's design-system module owns component names, parameters and code, and keeps them in line with these skills. The few code blocks left here are marked "Illustrative, not an API".

## Skills

| Skill | Covers |
|---|---|
| `wiom-ios-foundations` | Tokens with Swift names (colour, type + Dynamic Type, icons, spacing, radius, border, shadow, motion), layout, safe areas, keyboard, accessibility baseline, decisions |
| `wiom-ios-layout-rules` | Structural SwiftUI rules and the pre-commit checklist |
| `wiom-ios-screen-scaffold` | The template every screen starts from: top bar, scroll, sticky CTA bar, overlay host, keyboard |
| `wiom-ios-ux` | UX and copy rules for new copy: Hindi-first voice, screen patterns, trust on money screens, glossary |
| `wiom-ios-motion` | When and how things move; system push/pop; Reduce Motion; app animations |
| `wiom-ios-cta` | Buttons (6 types), the one button-group rule, sticky button bar |
| `wiom-ios-input-fields` | Input, Textarea, OTP (one-time-code AutoFill), search, picker trigger, keyboard behaviour |
| `wiom-ios-top-bar` | Top bar S/M/L, status bar, back + swipe-back |
| `wiom-ios-navigation-bar` | **Not in use (D27).** Bottom tab bar reference only; the customer app has no tab bar |
| `wiom-ios-bottomsheet` | Custom Wiom sheet, iOS dismissal, and **the** surface-choice table |
| `wiom-ios-dialog` | Wiom dialog (5 types); never the system alert |
| `wiom-ios-toast` | Toast, VoiceOver announcement, position above home indicator / keyboard / CTA bar |
| `wiom-ios-card` | Card container (flat, interactive or static) |
| `wiom-ios-inline-banner` | Inline status callout (info, positive, warning, critical) |
| `wiom-ios-page-states` | Full-screen loading, empty and error-with-retry states |
| `wiom-ios-badge` | Dot, count and label status badges |
| `wiom-ios-icon-badge` | Decorative glyph in a tinted circle |
| `wiom-ios-list-item` | List rows, one VoiceOver element per row |
| `wiom-ios-selection-controls` | Checkbox, radio, switch (iOS toggle behaviour) |
| `wiom-ios-tabs-filters` | Pill tabs, underline filters, chips |
| `wiom-ios-loader` | Spinner, linear, dots, skeleton, brand loader |
| `wiom-ios-progress-indicator` | Linear, completion, milestones, circular |
| `wiom-ios-pagination` | Dots, bars, counter, scroll indicator |
| `wiom-ios-rating` | 5-star rating (the only gold use, D36) |

**One presentation model.** Sheets, dialogs and toasts are three layers of one overlay host at the app root (sheet, then dialog, then toast on top). Screens bind presentation to their own state with a declarative API (for example `.wiomSheet(item:)`, `.wiomDialog(item:)`, `.wiomToast(item:)`); the app repo owns that API. See `wiom-ios-screen-scaffold`.

## Install

```bash
for skill in skills-ios/wiom-ios-*; do
    [ "$(basename "$skill")" = "wiom-ios-navigation-bar" ] && continue
    cp -R "$skill" ~/.claude/skills/
done
```

The decisions file travels inside `wiom-ios-foundations`. The navigation-bar folder stays in this package as an unused reference and is not installed (D27).

Install the iOS skills **instead of** the Android ones in an iOS session: the names don't collide, but loading both gives an agent two answers.

## Source and sync

Abhishek Garg owns the design system. The source repository (`abhishekgarg-wiom/wiom-design-system`) owns the shared design rules; vendored copies are not authoritative. When an Android skill changes a **visual** rule, reconcile the matching iOS skill against the owner decisions before updating it; an upstream change does not override an owner lock. Behaviour sections (`## iOS (SwiftUI, iOS 16+)`) are iOS-only. Keep unused skills and reference files; mark them not in use.

History (audit rounds, baselines, Android code references, earlier open questions) is in [`../CHANGELOG.md`](../CHANGELOG.md).

The HTML preview is generated from these skills and their active references; it is not a separate design authority. `wiom-ios-foundations/references/colour-usage.md` indexes colour recipes and defines no new token. Unused draft and partner archives stay out of the preview.

## Implementation readiness

Documented skills are not a native implementation or release claim. Track evidence with [native validation](wiom-ios-foundations/references/native-validation.md): specified, implemented, native-tested and parity-reviewed are separate statuses. Runtime checks on iOS 16 and the current iOS, including VoiceOver and layout screenshots, are required when building the app.

Typography (D32): **Noto Sans only for both Hindi and English**, with the four named weights in foundations.

## Later

These are referenced but have no skill yet; until they do, ask the design team rather than inventing them:

- **Wiom share sheet** (D11 says it is drawn as on Android; anatomy pending).
- **Chat bubbles and chat surfaces** (the chat tokens exist in foundations).
- **Server-driven pages**: a table from server component to DS component (D22 maps the colours).
