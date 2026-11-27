# App design rules (iOS customer app)

**Contents:** 1 Parity · 2 Buttons · 3 Pages and top bar · 4 Dialogs · 5 Inputs · 6 Bottom sheets · 7 Icons and graphics · 8 Loading · 9 Errors and no-internet · 10 Empty states · 11 General

Screen-level rules: what a screen contains and how it behaves. The component skills (`wiom-ios-*`) own how each part looks. When this file and a component skill disagree on a visual, the component skill wins.

---

## 1. Parity with Android

- **The iPhone app looks exactly like the Android app.** Same screens, same layout, same components, same icons (Material Rounded), same copy. A screen is designed once and built twice.
- Copy is **shared**: both apps read the same string catalog keys. iOS never rewrites a string for "iOS style".
- iOS changes only behaviour the platform owns: swipe-back, keyboard, safe areas, VoiceOver, Dynamic Type, Reduce Motion, system share and permission prompts ([decisions.md](../../wiom-ios-foundations/references/decisions.md) §0).
- If an Android screen and this file disagree, raise it with the design team; don't make the iOS screen different.

## 2. Buttons (CTAs)

| Rule | Detail |
|---|---|
| Statements, not questions | No "?" in a button |
| Disabled until ready | The main button is **shown disabled** until every required input is valid, then enabled. It is never hidden (both apps do this) |
| Name the next step | The label says what happens next ("पता बताइए", illustrative) |
| Short | 2 to 3 words ideal, 5 at most; at large text sizes the label wraps, never truncates (`wiom-ios-cta`) |
| Button count, pairing and layout | Follow `wiom-ios-cta` §6; dialog-specific maximums follow `wiom-ios-dialog` |
| Text buttons | Tertiary for soft actions, dismissals or acknowledgement as defined by `wiom-ios-cta` |
| Sticky at the bottom | The screen's main action sits in the sticky button bar (`wiom-ios-cta` §7): flat, 1 pt top border, no shadow |
| Keyboard | The sticky bar rides on the keyboard; inline secondary buttons stay in place |
| Design system only | Every button is a `wiom-ios-cta` type |

## 3. Pages and top bar

| Rule | Detail |
|---|---|
| Every screen has a top bar | `wiom-ios-top-bar`; the title may be empty |
| Top-bar actions | Back (if the user can go back), Help (if available), overflow menu, language switch |
| Back | The Material Rounded back arrow **and** iOS swipe-back, both always working when back is allowed |
| Forward-only screens | No back: the Wiom logo sits where back would be, and swipe-back is disabled (e.g. after a payment is confirmed) |
| No bottom tab bar | The customer app has none (D27) |

## 4. Dialogs

| Rule | Detail |
|---|---|
| Blocking or optional | A blocking dialog can only be left through its buttons |
| At most 2 buttons | One is fine when there is one action |
| Actions | CTA types and dismissal follow `wiom-ios-dialog`; no separate action whitelist |
| Component | `wiom-ios-dialog`; which surface to use: `wiom-ios-bottomsheet` § Choosing a surface |

## 5. Inputs

| Rule | Detail |
|---|---|
| Placeholder = an example | "राम कुमार", "110001" (illustrative). **Never an instruction** like "अपना नाम लिखें" |
| Label states | As `wiom-ios-input-fields` defines (it follows Android) |
| Errors | A line of error text under the field, announced to VoiceOver; never colour alone |
| Leading icon | Optional slot as defined by `wiom-ios-input-fields` |
| Phone | Number pad; `+91` as a fixed prefix; the button enables at 10 digits; wrong numbers are explained, not blocked silently |
| Name | Default keyboard, no autocorrect. If it's the only required field, the button enables after the first character |
| WiFi name (SSID) | Letters, digits and the allowed special characters |
| Device ID | Letters and digits |
| Keyboard behaviour | Per field type in `wiom-ios-input-fields` §6 |

## 6. Bottom sheets

| Rule | Detail |
|---|---|
| Purpose | Context for an action the user just took, on top of that screen |
| Size | Fits its content; grows up to the cap and then scrolls (`wiom-ios-bottomsheet`) |
| Content | Picker rows or Form content as defined by `wiom-ios-bottomsheet`; 2–3 fields may use Form, 4+ use a screen |
| Header | As the sheet size specifies; Illustration variants omit it |
| Buttons | Per `wiom-ios-cta` §6; row-commit pickers need none |

## 7. Icons and graphics

| Type | Size | Token / component |
|---|---|---|
| Decorative row badge | As `wiom-ios-icon-badge` specifies | Parent owns label and tap |
| Dialog header or illustration | As `wiom-ios-dialog` specifies | Do not substitute a hero badge recipe |
| Page illustration, empty state | 240 pt | Supplied by the design team (same file as Android) |

All icons are Material Rounded (`wiom-ios-foundations/references/icons.md`). Illustrations are never drawn by an agent.

## 8. Loading

- Skeletons mirror the final layout (`wiom-ios-loader`).
- Waits that take longer than a moment say what is happening and, where known, how long ("आमतौर पर 30 सेकंड लगते हैं", illustrative).

## 9. Errors and no-internet

| Case | Treatment |
|---|---|
| Offline with cached content | Persistent Warning toast; keep cached content visible |
| No usable content can load | Full-screen error with illustration and retry |
| Server failure | Full-screen error with illustration and a retry |
| A specific known error | Show its error code on screen so support can find it |

Always a way forward (retry) and a way out (back or help). Supportive tone; never blame the user.

## 10. Empty states

- Don't send users to an empty screen if it can be avoided.
- When one is needed: illustration + a line saying what will appear here and how to get it.

## 11. General

1. One primary action per screen.
2. Reveal complexity step by step.
3. Same component, same behaviour, everywhere.
4. Design-system components only.
5. Designed for every iPhone width (375 to 440 pt), from the same layout as Android.
