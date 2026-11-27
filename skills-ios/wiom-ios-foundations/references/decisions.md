# iOS decisions: the contract every `wiom-ios-*` skill follows

**Owner:** Abhishek Garg (design) · **Applies to:** the native iOS customer app (SwiftUI, iPhone only, iOS 16+, light mode).

These are the rules the iOS skills are written against. Every `wiom-ios-*` skill must agree with them. When a skill and this file disagree, this file wins and the skill is the bug.

---

## 0. The parity principle and explicit owner overrides

**An iOS user and an Android user see the same app.** Same colours, type, spacing, radius, shadows, icons, component anatomy and copy. iOS differs only where the platform's *behaviour* must win: gestures, safe areas, keyboard, VoiceOver, Dynamic Type, Reduce Motion, system share and permission prompts.

**Precedence:** an explicit locked owner decision wins over Android code. This includes PODS-1 (`23f67f9`) and the iOS decisions below. Parity applies where the owner has not locked an override.

So, when a question comes up:

| Question | Answer |
|---|---|
| Is it how something **looks** (colour, size, radius, glyph, shape, type)? | Apply an explicit owner ruling first. Otherwise match the named Android implementation baseline; if the Android skill differs from that baseline, retain the recorded component default and flag the mismatch. |
| Is it how something **behaves** (navigation gesture, dismissal, keyboard, accessibility)? | Follow iOS. Never port an Android behaviour (hardware back, ripple, status-bar colour). |
| Do Android and Figma disagree on a look? | Apply an explicit owner ruling first. Otherwise iOS follows **what Android ships** at the named baseline. Record the mismatch for design review (§3); do not silently replace an owner lock. |

---

## 1. Decisions (locked for the iOS skills)

| # | Topic | Decision | Why |
|---|---|---|---|
| D1 | `text/subtle` / `Neutral/700` | **#5C5570** | Android ships #5C5570; Figma’s #665E75 is stale. Figma gets fixed. The values are also recorded in `wiom-ios-foundations/references/tokens.md`. Component skills cite the token name only, never the hex. |
| D2 | Letter spacing | **Use the skill/Android tracking** (display −0.02em; heading/title.lg −0.01em; label +0.01em; meta +0.02em; others 0) | Android ships these values. Figma's 0 % gets fixed. On Devanagari runs, see `wiom-ios-foundations/references/typography.md` §4. |
| D3 | Corner style | **Circular** (`RoundedRectangle(cornerRadius:style: .circular)`), never `.continuous` | Android corners are circular; continuous corners would visibly differ. |
| D4 | Icons | **Material Icons Rounded, the same glyphs Android uses** (`Icons.Rounded.*`), exported as SVG from `google/material-design-icons` (`materialiconsround` style) into the asset catalog as template images. **SF Symbols are never used**, including for the back arrow, chevrons, close and share. | Icons must look identical on both platforms. |
| D5 | Back control | Material Rounded `arrow_back` in the Wiom top bar (as Android), **plus** the iOS edge-swipe-back gesture, which must keep working. No hardware back exists. | Look = Android, behaviour = iOS. |
| D6 | Page transitions | **System push/pop** (`NavigationStack`) with interactive swipe-back. The Android cross-fade rule (`wiom-motion` R3.1) is Android-only. | Replacing push/pop breaks a core iOS behaviour. |
| D7 | Top bar | Always the **custom Wiom top bar** (system navigation bar hidden). Small / Medium / Large stay **static** (no iOS large-title collapse), as on Android. Heights are **minimums**; titles may wrap at large text sizes. | Visual parity; Dynamic Type safety. |
| D8 | Status bar | Can't be coloured on iOS. The top bar's background extends under it; status-bar content is **dark** on light surfaces and **light** on `bg/brand/bold`, `bg/inverse` and brand-filled headers. | Platform rule. |
| D9 | Dialogs | Always the **Wiom dialog**, never `.alert` / `.confirmationDialog`. Exception: OS permission prompts and other system-owned sheets. | Visual parity; system alerts can't take Wiom styling. |
| D10 | Bottom sheets | **Custom Wiom sheet** on all iOS 16.x (drawn by the app, not `.sheet` + `presentationDetents`), so the 24 pt radius, handle and scrim match Android on 16.0–16.3 too. iOS dismissal: swipe down, scrim tap, VoiceOver escape (two-finger Z). No back press. | Visual parity across iOS 16 minor versions. |
| D11 | Share | The Wiom Share sheet is drawn as on Android; its "More" target opens the **system share sheet** (`ShareLink` / `UIActivityViewController`). | Visual parity for the Wiom part; the OS owns the rest. |
| D12 | Switch | Wiom switch look; **behaves and announces as an iOS toggle** (`Toggle` + custom `ToggleStyle`; VoiceOver: "switch button, on/off"). | Look = Android, behaviour = iOS. |
| D13 | Pressed states | Use the pressed token where one exists, exactly as Android does: Primary `bg/brand/pressed`, Destructive `bg/critical/pressed`, Pre-booking `bg/brand/accent/pressed`, Secondary and Tertiary `bg/brand/subtle` fill, list rows `bg/subtle`. Where a component has no pressed token, follow that component's Android implementation; if Android has none, there is no pressed visual (flag it, don't invent an overlay). **No ripple, no hover, no focus ring** on iPhone. `*/hover` tokens are unused on iOS. | Android uses `indication = null` with these fills; iOS matches it. |
| D14 | Touch targets | Visible sizes stay as designed (icons 16/20/24, controls 20–32). **Hit area is always ≥ 44 × 44 pt; default 48 × 48** (`.frame(minWidth: 48, minHeight: 48)` + `.contentShape`). The Navigation (32) and Info (24) tiers are visible sizes only on iOS. | Apple HIG minimum 44 pt; no visual change. |
| D15 | Units and widths | 1 dp = 1 pt. Every width is "fill the width minus the surface gutter", never 360/328/312. Checked from iPhone SE (375 × 667) to Pro Max (440 × 956). Dialog: max width 312, with ≥ 24 pt side margins. | iPhone widths vary. |
| D16 | Heights | Anything that holds text has a **minimum** height, never a fixed one. Fixed sizes only for non-text glyph shapes (dot badge 8, switch track, radio ring, checkbox box, loader glyphs). | Dynamic Type and two-line Hindi. |
| D17 | Dynamic Type | Every type token scales with a named iOS text style (anchors in `wiom-ios-foundations/references/typography.md` §3). Line height scales with it. Fully usable through **xxxLarge**; no clipping or overlap through **accessibility3**, which is the cap (`.dynamicTypeSize(...DynamicTypeSize.accessibility3)` at the app root). | iOS users set text size system-wide. **Final.** |
| D18 | `type/meta/xs` (10 pt) | Kept (parity), **restricted to Western-digit timestamps and badge counts**. Never Devanagari text. Scales with Caption 2. | Same restriction as the Android skill. |
| D19 | Safe areas | Surfaces (top bar, sticky CTA bar, sheet) extend their background into the safe area; their content stays inside it. **Last bottom CTA:** `space/16` above the home indicator on Face ID iPhones, and `space/16` above the screen edge on Home-button iPhones (SE). **Keyboard up:** the sticky CTA bar rides on the keyboard with `space/12` below the button. | Same 16 as Android. |
| D20 | Reduce Motion | Every motion token has a reduced form: slides and scales become a `motion/micro` cross-fade; draw-on and count-up jump to the end value; loops (spinner excepted) stop at a static frame. The spinner keeps rotating (it is the only signal that work is happening). | iOS accessibility setting. |
| D21 | Haptics | **None by default**, on taps or otherwise. Allowed only where a component skill names one. | Android ships none; keep parity until the design team defines a vocabulary. |
| D22 | Blue info / orange warning (current iOS, server-driven) | Mapped to DS V2: blue info → `info` family (purple), orange warning and yellow caution → `warning` family (gold). No blue or orange tokens on iOS. | Android V2 has neither. Pending confirmation (§3 Q12). |
| D23 | Dark mode | **Light only.** The app root sets `.preferredColorScheme(.light)`. Colours are still defined as asset-catalog colour sets (one appearance) so a dark mode can be added without touching call sites. | Figma has one mode. |
| D24 | Gaps | When no token fits: **don't invent, don't eyedrop.** Report the gap to the design team and the iOS lead. In code, only `// TODO(IOS-123): …` with a ticket, per the iOS code rules. | Replaces the Android `// GAP:` comment. |
| D25 | Copy | All copy in skills is **illustrative**. Real copy comes from the string catalog (Hindi first, English written separately, sentence case). Character limits are counted in **grapheme clusters** (`String.count` in Swift; "क्षि" is one). | Agents copy examples verbatim. |
| D27 | Bottom navigation bar | **None.** The customer app has no bottom tab bar, Top-level destinations are reached from screens. `wiom-ios-navigation-bar` is kept for reference but not used on any screen. | No tab bar in the customer app. |
| D26 | Text/subtle on dark, brand on dark | No new tokens yet. On `bg/inverse` and `bg/brand/bold` use `text/inverse` only; never `text/brand` (3.84:1) or `text/subtle`. | Pending design-team decision (§3 Q5). |
| D28 | Shared selection transitions | Selection colour fades use `motion/micro` + `ease/standard` (200 ms) in both directions on iOS and Android. Values commit on tap. Pressed feedback stays instant. Switch thumb movement is 200 ms on both. Includes checkbox, radio, switch stroke, chips, pill tabs, underline filters and selected list-row backgrounds together with their indicators. Transparent fade endpoints keep the same colour at opacity 0, never `.clear`. iOS Reduce Motion keeps colour/opacity fades and removes movement; Android follows the system "Remove animations" setting. | Same rule in the Android skills. The platform accessibility difference is allowed. |
| D29 | Toast vertical clearance | `space/16` above the highest safe-area / CTA-bar / keyboard boundary. Horizontal margin stays `space/8`. | Shared Wiom spacing choice, not an Apple-prescribed toast measurement. |
| D30 | Pill-tab count | 2 to 4 pills on both platforms. | Retain the existing implementation range; supersedes the older 1..3 source rule. |
| D31 | Final Warning icon combinations | Only three combinations apply: gold `icon/warning` for rating stars in the rating component; dark `icon/action` on `bg/warning/subtle`; dark `icon/action` on `bg/warning`. Gold `icon/warning` is never a Warning indicator, including inside a tinted badge. Toasts and inputs retain their neutral outer surfaces and use a tinted icon container. | Applies to toast, input, icon badge and every Warning indicator. `icon/action` names the colour, not interactivity; decorative glyphs remain non-tappable. No new token. Toast defaults to the subtle background. Container geometry and unrelated contrast questions stay explicit. |
| D32 | Font family | Noto Sans only for both Hindi and English. Use NotoSans-Regular, NotoSans-Medium, NotoSans-SemiBold and NotoSans-Bold; do not add the separate Noto Sans Devanagari family. | The supplied Noto Sans files contain the tested Hindi characters. Devanagari shaping checks refer to the script. Existing typography tokens, weights and sizes stay unchanged. |
| D33 | Long toast messages | Copy fits 2 lines at the default text size (about 80 Hindi grapheme clusters). At larger text sizes the toast grows and shows the whole message; never truncated. Height caps at 40 % of the screen, then the message scrolls inside the toast. | Text is never lost; copy stays short by guideline. |
| D34 | Switch thumb colour | `icon/inverse` (#FAF9FC). No new token. | Visually identical to Android's raw white; Android library to adopt the token. |
| D35 | Warning icon container (toast, input) | Icon Badge Sm: 24 pt circle, 16 pt glyph, `bg/warning/subtle` + `icon/action`. The smaller Warning glyph is intentional; the 24 pt footprint matches the other toast icons. | Reuses an existing size; no new geometry. |
| D36 | Rating component | New `wiom-ios-rating`: 5 Material Rounded stars, 32 pt, `space/8` apart, 48 pt tap area; filled `icon/warning`, empty `icon/nonAction`. | Gives D31's "rating component" a spec. Figma to follow. |
| D37 | Brand loader animation | The shipped `loader_infinity.json` is the brand loader, played at 200 × 200 pt as in the app; Spinner lg only if it fails to load. | Both apps already ship it. Design to correct loop, pink and track later. |
| D38 | App animations | The nine other shipped Lottie files stay as they are and are listed in `wiom-ios-motion` §5.8. | Documents what ships; nothing new. |
| D39 | Copy approval | Abhishek Garg approves new or changed copy. The AI never changes existing copy; it only suggests. | The AI never rewrites existing copy. |
| D40 | Confirmation and dialog easing | The confirmation check segment uses `ease/enter`; the dialog fade uses `ease/standard`. | Arrival vs neutral change. |
| D41 | Bottom sheet copy | Title about 40, body about 120 Hindi grapheme clusters at the default text size. At larger sizes the sheet grows and scrolls; text is never cut off. | Same approach as D33. |

---

## 2. Naming: DS V2 token → Swift

The skills cite tokens in **DS V2 Figma form** (`bg/brand/subtle`). Swift names are generated by rule; the skills never invent others.

| DS V2 | Swift | Rule |
|---|---|---|
| `bg/brand/subtle` | `Wiom.Colors.bgBrandSubtle` | drop slashes, lowerCamelCase |
| `text/onWarning` | `Wiom.Colors.textOnWarning` | |
| `overlay/scrim` | `Wiom.Colors.overlayScrim` | |
| `type/body/lg` | `Wiom.Typography.bodyLg` | drop the `type/` prefix |
| `space/16` | `Wiom.Spacing.s16` | value-named, as in Figma |
| `radius/large` | `Wiom.Radius.large` | **16**, not the old iOS `WiomRadius.large` (24) |
| `stroke/small` (width) | `Wiom.BorderWidth.small` | width collection, kept apart from `stroke/*` colours |
| `icon/md` (size) | `Wiom.IconSize.md` | size collection, kept apart from `icon/*` colours |
| `shadow/md` | `Wiom.Shadow.md` | applied with `.wiomShadow(.md)` |
| `motion/surface`, `ease/standard` | `Wiom.Motion.surface`, `Wiom.Easing.standard` | |
| Icon `Icons.Rounded.ArrowBack` | asset `ic_rounded_arrow_back` → `Wiom.Icon.arrowBack` | Material snake_case name, `ic_rounded_` prefix |

If the iOS design-system module names a token differently, the **DS V2 name** is the truth and the module is renamed.

---

## 3. Questions still open for the design team

The skills carry the default shown until the design team answers.

| # | Question | Default in the skills |
|---|---|---|
| Q1–Q2 | Fix Figma from #665E75 to #5C5570 and the Android tracking? | Skills follow Android (D1, D2). Figma to be updated. |
| Q3 | `bg/surface` #FFFFFF and paint style `Brand/Bold` #4A1434 in Figma: stale or unused? | Neither is used on iOS (Android has neither). |
| Q4 | Motion as Figma variables? | Motion tokens live in `wiom-ios-foundations/references/motion.md` as cubic-Bézier values until Figma has them. |
| Q5 | Contrast failures: `stroke/subtle` input border 1.40:1, `text/brand` on `bg/brand/subtle` 4.10:1, on-dark brand text | **Accepted exceptions: build with the current tokens; review with Android later.** Skills avoid the on-dark pairs (D26). |
| Q12 | Blue info / orange warning from server-driven screens | D22 mapping. |
| Q13 | May iOS write `codeSyntax.iOS` into Figma by script? | Naming rule in §2 is fixed either way. Writing to Figma needs the design team's yes. |
| Q14 | Rename the stroke-width and icon-size collections in Figma? | Swift already separates them (§2). |
| n/a | Haptics vocabulary | None (D21). |
| n/a | Brand-loader file fixes (loop 1.3 s, pink #D9008D, track) | Use the shipped `loader_infinity.json` (D37) until design delivers the corrected file. |

---

## 4. What changed from the Android skills, in one list

- Android implementation APIs are removed; platform behaviour is specified in iOS terms.
- Descriptions name the component and SwiftUI / iOS, with specific triggers.
- Every component skill ends with an **iOS (SwiftUI, iOS 16+)** section in one fixed shape: built from, tokens, size, Dynamic Type, VoiceOver, hit area, motion, safe areas and keyboard, haptics, not on iOS.
- Hex values appear only in `wiom-ios-foundations` and this decisions contract. Component skills cite token names.
- These skills cover the customer app only.
- Dependencies resolve within this iOS package or to the named source repositories; retired workflows are not dependencies.


## 5. Owner locks and standing defaults

Owner locks from PODS-1 (commit `23f67f9`) override differing Android visuals:

- Toast fill: `bg/default` for all four types.
- List secondary and meta text: `type/body/sm` (12 pt).
- Toast side margin: `space/8` each side (344 wide on the 360 reference; iPhone width stays flexible).
- Dialog Alert icon: 48 pt neutral circle, `bg/subtle` + `icon/action`.

Standing defaults:

| Topic | Rule |
|---|---|
| Android skill vs library mismatch | Library visuals win unless an owner decision overrides them. |
| Hindi progress text | 12 pt, never 10 (D18). |
| Missing spacing or geometry tokens | Keep the documented value and report the gap (D24); no new tokens. |
