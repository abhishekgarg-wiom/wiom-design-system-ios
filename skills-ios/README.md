# Wiom design skills for iOS

Claude Code skills for the **native iOS customer app** (SwiftUI, iPhone only, iOS 16+), built on **Wiom DS V2**. They are the iOS counterpart of the Android skills in `../skills/` and are written so an iOS user and an Android user see **the same app**: same tokens, type, icons (Material Rounded) and component anatomy. iOS differs only where platform behaviour must win (gestures, safe areas, keyboard, VoiceOver, Dynamic Type, Reduce Motion).

Start with [`IOS_DECISIONS.md`](IOS_DECISIONS.md): the parity rule, the 32 decisions every skill follows, the Swift naming rule, and the questions still open for the design team.

## Skills

| Skill | Covers |
|---|---|
| `wiom-ios-foundations` | Tokens with Swift names (colour, type + Dynamic Type, icons, spacing, radius, border, shadow, motion), layout, safe areas, keyboard, accessibility baseline |
| `wiom-ios-layout-rules` | Structural SwiftUI rules and the pre-commit checklist (replaces `wiom-compose-layout-rules`) |
| `wiom-ios-ux` | UX and copy rules: Hindi-first voice, screen patterns, trust on money screens, emotional arc, adoption doctrine, glossary |
| `wiom-ios-motion` | When and how things move; system push/pop; Reduce Motion |
| `wiom-ios-cta` | Buttons (6 types), the one button-group rule, sticky button bar |
| `wiom-ios-input-fields` | Input, Textarea, OTP (one-time-code AutoFill), search, picker trigger, keyboard behaviour |
| `wiom-ios-top-bar` | Top bar S/M/L, status bar, back + swipe-back |
| `wiom-ios-navigation-bar` | Bottom tab bar. Kept for reference; the customer app has no bottom tab bar today (D27) |
| `wiom-ios-bottomsheet` | Custom Wiom sheet, iOS dismissal, and **the** surface-choice table |
| `wiom-ios-dialog` | Wiom dialog (5 types); never the system alert |
| `wiom-ios-toast` | Toast, VoiceOver announcement, position above home indicator / keyboard / CTA bar |
| `wiom-ios-badge` | Dot, count and label status badges |
| `wiom-ios-icon-badge` | Decorative glyph in a tinted circle |
| `wiom-ios-list-item` | List rows, one VoiceOver element per row |
| `wiom-ios-selection-controls` | Checkbox, radio, switch (iOS toggle behaviour) |
| `wiom-ios-tabs-filters` | Pill tabs, underline filters, chips |
| `wiom-ios-loader` | Spinner, linear, dots, skeleton, brand loader |
| `wiom-ios-progress-indicator` | Linear, completion, milestones, circular |
| `wiom-ios-pagination` | Dots, bars, counter, scroll indicator |
| `wiom-ios-rating` | 5-star rating (the only gold use, D36) |

Not included (not loaded by the iOS UI agent): `wiom-design-ui` (Figma plugin catalog), `design-run`, `persona-brief`, `problem-diagnosis`, and the workflow inventory files of the UX skill.

## Install

```bash
for skill in skills-ios/wiom-ios-*; do
    [ "$(basename "$skill")" = "wiom-ios-navigation-bar" ] && continue
    cp -R "$skill" ~/.claude/skills/
done
cp skills-ios/IOS_DECISIONS.md ~/.claude/skills/   # skills link to ../IOS_DECISIONS.md
```

The navigation-bar folder remains in this package for explicit reference and is excluded from normal installation (D27). This task does not install skills globally.

Install the iOS skills **instead of** the Android ones in an iOS session: the names don't collide, but loading both gives an agent two answers.

## Source and sync

Draft created 19 Nov 2026; corrected and audited 22 Nov 2026 against the source `abhishekgarg-wiom/wiom-design-system` and Android library `abhishekgarg-wiom/wiom-ds-android`. The source repository owns design rules. Only the accepted builder corrections in the task context apply; vendored copies are not authoritative. Each component skill lists, under **Open questions**, every place where the Android skill and the Android code disagreed and which one iOS follows.

When an Android skill changes a **visual** rule, reconcile the matching iOS skill against the explicit owner decisions and the named baseline before updating it. An upstream change does not supersede an owner lock. Behaviour sections (`## iOS (SwiftUI, iOS 16+)`) are iOS-only.


Governance: Abhishek Garg owns the design system. Make design changes in the source repository with the owner’s authorisation, never in downstream vendored copies. The final iOS package is versioned in the dedicated public wiom-design-system-ios repository; the shared Android design-system repository was not committed or pushed by this task. Keep unused skills and reference files; mark them not in use. No bottom tab bar is loaded for customer screens (D27).

Audit baseline: source remote HEAD `2fa260f`, Android remote HEAD `1ce3c31` (`v2.0.1`), checked 22 Nov 2026. The checkout was behind when the initial audit began; the user subsequently pulled it to `2fa260f` on 23 Nov. That was the round 2 baseline. Round 3 uses `origin/main b480a46` (Android skills PR #18) without editing Android skills.

The illustrative Swift snippets describe design-system APIs to implement; they are not a compiled module. The switch thumb uses `icon/inverse` (D34). Runtime verification on iOS 16 and current iOS, including VoiceOver and layout screenshots, is required when these skills are used to build the app.

Feedback correction, 23 Nov 2026: owner locks in `23f67f9` take precedence over differing Android code. The four PODS-1 calls are decided. List secondary/meta uses 12 pt; Dialog Alert uses the neutral circle with `icon/action`. D29-D31 now settle toast clearance, pill count and the Warning-icon placement direction. D31 now finalises dark-on-yellow Warning icons globally and gold rating stars only; icon-container geometry, input boundary contrast and switch-thumb mapping remain open.


UX source provenance: the six original `wiom-ios-ux/references/` files were adapted from the builder repo `wiom-builder-documents`’s `wiom-design-ux` material. They are not present in the DS source repository. Only owner-approved recharge rules are active; draft ideas and partner-only vocabulary remain in explicitly unused archive files and must never be loaded for screen or copy work. Ownership of the UX/copy source is still open.


HTML source rule: the canonical Wiom iOS design-system HTML reference is generated from these iOS skills and their active foundation/UX references. Its palette, token values, use-case guidance and component rules are not a separate design authority. `wiom-ios-foundations/references/colour-usage.md` indexes existing colour recipes; it defines no new token. Derived RGB/HSL values are documentation equivalents only. Unused draft/partner archives stay excluded from active HTML guidance.


## Implementation readiness

All 20 skills are documented; that is not a native implementation or release claim. Track evidence using [native validation](wiom-ios-foundations/references/native-validation.md): specified, implemented, native-tested and parity-reviewed are separate statuses. Native status is **not assessed in this package** until linked build/device evidence exists. The HTML is a reference and preview, not a simulator. Selection transitions are shared by iOS and Android skills under D28, aligned in design-system PR #18 (`b480a46`). Only the `wiom-ds-android` library implementation remains pending with the dev team; this task does not modify Android skills or code.


## Finalised iOS skill package, 23 Nov 2026

All 20 skills are included and validated as documentation. D31 is final across components: gold icon/warning is rating-stars-only; Warning indicators use dark icon/action on bg/warning/subtle or bg/warning. See the foundation warning-combinations reference. Existing token values are unchanged. D29 keeps toast clearance at 8 pt and D30 keeps 2–4 pill tabs.

Finalised documentation does not mean every implementation question is closed: remaining border/brand-text contrast and native/device validation remain explicit. Android source and app implementation have not been changed by this package.


Typography (D32): use **Noto Sans only for both Hindi and English**, with the four named weights in foundations. No separate Noto Sans Devanagari font family is used. Script-specific Hindi shaping checks do not introduce another font family.
