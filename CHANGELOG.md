# Changelog

History of the Wiom iOS design skills. The skills state only the current rules; provenance, baselines, audit rounds, Android code references and earlier open questions live here. Moved text is kept word for word.

## 27 Nov 2026

- **iOS team review applied** (Akshit Verma, 26 Nov 2026):
  - `IOS_DECISIONS.md` moved to `skills-ios/wiom-ios-foundations/references/decisions.md` (stub left at the old path).
  - Swift code taken out of the skills; short "Built from" notes instead. Two illustrative blocks kept (CTA pair fit, toast timer). The Swift API lives in the app repo.
  - History moved to this file; Open questions keep only open items; settled items became rules.
  - One overlay host at the app root for sheet, dialog and toast.
  - D17 Dynamic Type final. D40 confirmation and dialog easing. D41 bottom sheet copy guide. Contrast exceptions (Q5) stay as accepted exceptions: build with current tokens, review with Android later.
  - New skills: `wiom-ios-card`, `wiom-ios-page-states`, `wiom-ios-inline-banner`, `wiom-ios-screen-scaffold`.
  - `tokens.json` generated from `tokens.md`; accessibility string keys listed per component; duplicate `icon/action` removed from the toast token list; navigation-bar marked not in use at the top.
- **Answers to the iOS team** (PR #1, #2): D33 long toasts grow (cap 40 % of the screen), D34 switch thumb `icon/inverse`, D35 Warning box = Icon Badge Sm, D36 `wiom-ios-rating`, D37 `loader_infinity.json` at 200 pt, D38 app animations listed, D39 copy approval. D29 corrected to a 16 pt toast bottom gap.
- **Preview script** (PR #3): `scripts/update_preview.py`.

## 26 Nov 2026

- Android skills in `abhishekgarg-wiom/wiom-design-system` aligned with these iOS skills: PR #21 (pill tabs 2 to 4, dark Warning icons), PR #22 (brand text contrast 4.62:1), PR #23 (skill values aligned with the shipped Android library and iOS choices). Many earlier "Android vs skill" open questions below were settled by PR #23.

## 23 Nov 2026 and earlier: moved text

### From `IOS_DECISIONS.md` (header and §5, as of 27 Nov 2026)

**Owner:** Abhishek Garg (design) · **Date:** 22 Nov 2026 · **Applies to:** the native iOS customer app (SwiftUI, iPhone only, iOS 16+, light mode).

This file answers the iOS team's review ("Wiom design skills: review for the iOS app", 19 Nov 2026) and fixes the rules the iOS skills are written against. Every `wiom-ios-*` skill must agree with it. When a skill and this file disagree, this file wins and the skill is the bug.

## 5. Owner decision status: locked rulings and remaining questions

The 22 Nov context was stale for the four PODS-1 rulings. Owner commit `23f67f971e2a5187dbc07344a9041090aa494fb2` (20 Nov 2026, “Lock PODS-1”) is authoritative. These owner rulings override differing Android visuals. Other rows retain explicit defaults or open status; no new approval is inferred.

| Question | Default until ruled |
|---|---|
| Figma subtle text and tracking | Follow Android; values and live Figma difference are recorded in foundations. |
| Contrast exceptions | Retain documented pairs for parity; no unapproved recolouring. |
| Android skill vs library mismatches | Library visuals win unless an explicit owner correction in the context overrides them; update Android skills separately. |
| Brand animation | Plain Spinner lg on both apps; final asset absent. |
| Hindi progress text at 10 | iOS uses 12; Android should align. |
| Figma-only surface and paint style | Not in use. |
| Motion tokens in Figma | Keep in foundations; add to Figma later. |
| नेट and घर का नेट | Use as the recommended customer-copy defaults. |
| String-catalog courtesy wording and casing | Recommended shared-catalog correction; no catalog changed by this skills task. |
| Warning toast fill | **DECIDED · `23f67f9`:** `bg/default` for all four types. D31 uses a dark icon on a pale-yellow icon container; whole-toast fill stays neutral. |
| List secondary/meta text | **DECIDED · `23f67f9`:** `type/body/sm` (12). iOS follows the owner; Android app must change. |
| Toast side margin | **DECIDED · `23f67f9`:** `space/8` each side, 344 wide on the 360 reference; iPhone width remains flexible. |
| Alert icon | **DECIDED · `23f67f9`:** 48 pt neutral circle, `bg/subtle` + `icon/action`. Dialog rule overrides the generic Neutral badge tint; Android app must change. |
| Toast bottom clearance | **DECIDED (D29):** `space/16` above the highest safe-area / CTA-bar / keyboard boundary. |
| Tabs pill count | **DECIDED (D30):** 2 to 4 on both platforms; supersedes 1..3. |
| Warning icon combinations | **DECIDED (D31):** gold is ratings-only; Warning indicators use dark `icon/action` on subtle or solid Warning backgrounds. Toast/input outer surfaces stay neutral. |
| Dynamic Type anchors and cap | D17 and foundations anchors. |
| Figma code syntax and collection renames | Naming rule fixed locally; no Figma writes authorised by this task. |
| Selection transition refinement | **DECIDED (D28):** shared selection fades and switch timing are approved on both platforms; Android skills are aligned by PR #18 (`b480a46`). Only the Android library code implementation remains pending with the dev team. |
| Switch white-thumb semantic token | **DECIDED (D34):** `icon/inverse`. |
| Missing spacing/geometry tokens | Preserve documented visual values and report gaps; no new tokens created. |

Source baseline checked 22 Nov 2026: design-system remote HEAD `2fa260fd374ec908ea51d2ce01f34ec69c730644`; Android remote HEAD `1ce3c313ca12273afb387bb7b18086028bc3211a` (tag `v2.0.1`). The older context calls the Android library v0.3.0; the audit uses the actual current code and retains that historical version only in the required tabs implementor note.


Round 3 baseline, 23 Nov 2026: design-system `origin/main` and local HEAD are `b480a46`, including Android skills PR #18. Earlier source/library hashes above are historical audit references; the Android library implementation has not been re-baselined by this skills-only change.


Owner decision session, 23 Nov 2026: D29-D31 are recorded above. Switch-thumb token was later decided as `icon/inverse` (D34, 27 Nov 2026). Contrast comparisons are requested for review only, not adoption.


D31 finalisation supersedes the earlier toast-only scope: the same three combinations now govern every iOS Warning indicator. Gold-on-tint is prohibited, not an accepted Warning exception. Ratings retain their documented gold-star exception.

Removed from decision rows: D17 "Pending design-team confirmation (§3 Q11)."; D19 "Decided 19 Nov 2026 (replaces the 8 pt the iOS app ships today)."; D27 "Decided 19 Nov 2026."; D28 "Android skills updated in design-system PR #18 (`b480a46`). The platform accessibility difference is allowed. Only `wiom-ds-android` library implementation remains pending with the dev team."; D29 "Replaces the old source 16 vs implementation 8 question."; the "DECIDED, owner … 2026" prefixes on D28 to D39. §3 rows removed: Q11 (Dynamic Type, now final), UX1 (closed by D39), "Brand-loader Lottie: final file? Plain Spinner lg on both apps." (closed by D37).

### From `skills-ios/README.md`

Not included (not loaded by the iOS UI agent): `wiom-design-ui` (Figma plugin catalog), `design-run`, `persona-brief`, `problem-diagnosis`, and the workflow inventory files of the UX skill.

The navigation-bar folder remains in this package for explicit reference and is excluded from normal installation (D27). This task does not install skills globally.

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

### From `README.md`

## Package status

All 20 skills are documented and validated; 19 are active and bottom navigation remains an unused reference (D27). This repository is design guidance and an HTML reference, not a compiled SwiftUI SDK. Existing native-app code has not been changed here.

Open implementation/review items remain explicit: input-border and pressed-brand-text contrast, Dynamic Type policy and native device validation. No unapproved contrast proposal is an agent default.

## Provenance and parity

Derived from Wiom’s shared design-system repository, with owner decisions recorded through 23 Nov 2026. The inspected shared checkout was 3e6780c; D28 selection transitions were aligned in Android skills PR #18 at b480a46. Explicit owner decisions override older source/implementation mismatches. Android source/library alignment is separate work: this repository does not change Android skills, the builder, Figma or customer-app-ios.

D29 records the 16 pt toast bottom gap (sides 8 pt), same as the Android skill. D30 records 2–4 pills. D31 records the final Warning colour rule above. These differences need coordinated downstream alignment, not silent edits by an iOS agent.

Public reference publication was requested by the design-system owner. See [NOTICE](NOTICE.md) for ownership and reuse terms. No global skill installation was performed.

### From `FINALISATION.md`

# Finalised Wiom iOS design skills

23 Nov 2026. All 19 skill documents are finalised and validated as an iOS design-guidance package. Eighteen are active; the navigation-bar reference remains unused under D27.

## Final Warning rule (D31)

Only three combinations apply:

1. Gold icon/warning for rating stars in the rating component only.
2. Dark icon/action on bg/warning/subtle for Warning indicators (10.85:1).
3. Dark icon/action on bg/warning for Warning indicators where the solid surface is specified (6.60:1).

Applied across foundations, tokens, iconography, colour usage, toast, input and icon-badge guidance. Generic same-family and decorative-icon rules now explain this explicit colour-role reuse. No new token was introduced. The main HTML includes a three-combination visual reference and the updated component examples. The review marks both dark Warning pairings approved globally and gold Warning glyphs prohibited.

D29 sets the toast bottom gap to 16 pt (sides 8 pt). D30 keeps 2–4 pill tabs. 27 Nov 2026 answers to the iOS team (D33 to D39): long toasts grow, switch thumb `icon/inverse`, Warning box = Icon Badge Sm, new `wiom-ios-rating`, `loader_infinity` is the brand loader, app animations listed, copy approved by Abhishek Garg. Existing reference files and the old walkthrough HTML were retained.

## Validation

All 19 metadata/contracts passed; 27 published contrast pairs were recomputed. Targeted browser checks verified the three approved combinations, gold rating stars, dark Warning icon badges and input examples, plus 6.60:1 for the solid pairing. All 19 HTML chapters passed with zero browser errors or HTTP requests. Selection, modal/search accessibility, walkthrough, responsive layout, shortlist/language and print checks passed. All 122 protected source/reference files stayed unchanged and no original files were removed.

Finalised documentation is not a native SDK or native accessibility certification. Warning toast/input container geometry, remaining input-border and pressed-brand-text contrast, Dynamic Type policy, switch-thumb mapping and native/device validation remain explicitly listed.

## Delivery

Refreshed outputs/skills-ios, wiom-ios-skills-revised.zip, wiom-ios-design-system.html and wiom-ios-contrast-review.html. The user authorised a new private GitHub repository named wiom-design-system-ios and explicitly requested the HTML inside it. That repository contains the iOS skills and offline HTML documents. No commit is made to the existing shared design-system repo. Android skills, builder, Figma and customer-app-ios remain untouched.


## Publication update

The owner subsequently requested this repository be public and its HTML be hosted. The repo is now public, with GitHub Pages configured from main /docs. Live preview: https://abhishekgarg-wiom.github.io/wiom-design-system-ios/

### From `wiom-ios-ux/SKILL.md`

**UX provenance:** the six original UX reference files were adapted from the `wiom-design-ux` material supplied from `wiom-builder-documents`, not from `abhishekgarg-wiom/wiom-design-system`. The source DS repository governs component/foundation design; **copy owner (D39): Abhishek Garg** approves new or changed copy. The AI never changes existing app copy; it may only suggest. Builder material is read-only reference for this task.

(`wiom-ios-ux/SKILL.md` also said: "Adapted on 19 Nov 2026 from the builder repo’s `wiom-design-ux` reference material, with the iOS review’s fixes applied.")

## Open questions as they stood before 27 Nov 2026

Each skill's Open questions section, word for word (Android code references already removed; they are listed in the next section).

### wiom-ios-badge

1. **Brand Filled: Android vs skill.** The source skill lists Brand as a
   Filled tone (`bg/brand` + `text/onBrand`, a shipped Figma variant);
   Android has no Brand Filled and falls back to Brand Tinted. iOS
   follows Android, so iOS has 23 variants, not 24. Design team to
   confirm whether Android should add Brand Filled.
2. **Label overflow: Android vs skill.** The skill says one line with
   `overflow = Visible` ("rewrite shorter"); Android ships `maxLines = 1`
   with the default clip. iOS uses one line
   with tail truncation (an ellipsis is safer at large text sizes).
   Confirm, and ask Android to match.
3. **Count nudge.** The skill nudges the overlay Count 4 pt outward
   (x +4, y −4); the Android library only documents top-end alignment and leaves the nudge to callers. iOS follows
   the skill's 4 pt; confirm against the shipped Android bell.
4. **Count display: source vs Android.** Source rule 6 renders 1–9 as
   digits, 10–99 as "9+", and 100+ as "99+" in every placement. Android
   exposes `cap` (default 99), which can render raw 10–99. The owner
   explicitly selected the source rule for iOS. This visual exception
   remains open for Android alignment.
5. **Small Filled.** The skill crashes on Small Filled; Android silently
   gives Small Tinted. iOS follows Android.
6. **Western digits in Hindi.** Default: counts always use Western
   digits, in both languages. Design team to confirm Devanagari digits
   are never wanted.
7. **Label grapheme limit.** The source sets none. iOS uses 10 Hindi /
   14 English grapheme clusters (the chip limits) until the design team
   sets badge limits.
8. **Count minimum under Dynamic Type.** Scaling the 20 pt minimum with
   Caption 2 is an iOS choice (Android's 20 dp is not scaled, though sp
   text is). Confirm.

### wiom-ios-bottomsheet

| # | Question | Default here |
|---|---|---|
| 1 | Sheet list rows: the source skill says rows are `wiom-list-item` instances with a 16 gutter; Android draws its own sheet row with 24 sides, a 40 brand circle, `label/lg` and an `icon/disabled` chevron. Header padding is 16, so header and rows don't line up. | Follow Android: sheet row for action menus and share; `wiom-ios-list-item` for radio and checkbox pickers. Design team to confirm the 24 vs 16 alignment. |
| 2 | Share layout: source skill says a horizontal row of share targets; Android previews it as header + list rows. | Follow Android (rows). |
| 3 | Size heights: source skill gives min/max ranges and `Full` = 92 % of the screen; Android ships minimums only (240 / 400 / 600) and `Full` hugging content. | Minimum shares (30 / 50 / 75 %) as in Android; `Full` fills to the cap. |
| 4 | Android opens tall non-Full sheets half-expanded (`ModalBottomSheet` default state); the iOS sheet has no detents. | No half-open state on iOS. |
| 5 | Shadow: source skill and `tokens.md` say `shadow/md`; Android sets no explicit shadow on the sheet. | `shadow/md`. |
| 6 | Non-dismissable sheets: Android has no non-dismissable mode (scrim and swipe always dismiss). iOS adds it for money and commit moments. | iOS behaviour as §3; Android to follow. |
| 7 | Non-modal sheets: Figma has `Is Modal` (default false); Android ships only modal sheets. If design ever needs one, the overlay host can skip the scrim and leave the content beneath hit-testable on iOS 16.0 (no 16.4 API), with `.isModal` removed. | Not used. |
| 8 | Destructive confirmation: the source sheet skill listed an Illustration sheet; the source dialog skill and the Android dialog preview ("Alert · destructive") use a dialog. `wiom-ios-cta` §6.1 still has a bottom-sheet destructive row. | Dialog. The cta row applies only when a sheet's own commit is destructive (e.g. a Form that cancels a request). |
| 9 | Swipe-to-dismiss from inside a scrolled list (pull down when at the top) needs scroll-offset tracking that iOS 16 SwiftUI does not expose cleanly. | Drag zone is handle + header (+ action bar). |
| 10 | The Android typography file says sheet and dialog headers default to `heading/lg`; the shipped sheet header uses `heading/md`. | `type/heading/md`; `typography.md` leaves the choice to this skill. |
| 11 | Copy limits (40 / 120 grapheme clusters) are guidance, not from Figma. | As §4 rule 11, pending design. |

### wiom-ios-cta

| # | Question | Default in this skill |
|---|---|---|
| 1 | The CTA loading spinner is 24 pt with a 2 pt stroke on Android, but the loader's own in-button size is Spinner Sm, 20 pt. Which is right? | 24 pt, as Android ships. |
| 2 | Source skill says the spinner *replaces* label and icon; Android keeps them laid out at zero opacity, so the button keeps its width. | Follow Android (no size change). |
| 3 | Acknowledge row-to-CTA gap: skill says 16 pt; Android's preview uses 8 pt and the row adds 4 pt vertical padding. | 16 pt (Android's component doesn't own this gap; only its preview differs). |
| 4 | Dialog pairings: skill says Primary + Secondary and Destructive + Secondary; Android dialog previews pair Primary + Tertiary and Destructive + Tertiary. Which is canonical? | Skill table (§6.2). |
| 5 | Is a two-line CTA label acceptable to design at large text sizes, and should copy guidance cap at two lines? | Wrap freely, never truncate; copy aims for one line at default size. |

### wiom-ios-dialog

| # | Question | Default here |
|---|---|---|
| 1 | **DECIDED by owner commit `23f67f9`:** Alert uses a 48 pt neutral circle with `bg/subtle` and `icon/action`. Android still draws a brand rounded square. | iOS follows the locked dialog rule. **Android app must change.** Generic Neutral icon badges retain `icon/nonAction`; the dialog owns this override. |
| 2 | Loading: the source skill has an optional Tertiary "Cancel" and back-press dismissal when cancellable; Android ships no button and is never dismissable. | Follow Android: no button, escape does nothing. |
| 3 | Illustration panel: the source skill allows other subtle tones (`bg/positive/subtle`, `bg/info/subtle`); Android ships `bg/brand/subtle` only. The Android doc comment still describes a 120 circle; the code draws the 144 panel. | Brand only, 144 panel. |
| 4 | Title style: the Android typography file says dialog headers default to `heading/lg`; every dialog type ships `heading/md`. | `type/heading/md`; `typography.md` defers to this skill. |
| 5 | Body style: the Android README says `body/lg`; the code uses `body/md`. | `type/body/md`. |
| 6 | VoiceOver escape on Alert and Illustration closes (mirrors Android's back press). Should a money-related Alert ever be escape-proof? | Escape closes; money commits belong on a non-dismissable sheet anyway. |
| 7 | Copy limits (40 / 120 grapheme clusters) are guidance, not from Figma. | As §4 rule 8. |

### wiom-ios-foundations

Tracked in [`references/decisions.md`](references/decisions.md) §3: Figma alignment for `text/subtle` and tracking (Q1–Q2), `bg/surface` (Q3), motion in Figma (Q4), accepted contrast exceptions (Q5, list in tokens §9), Dynamic Type anchors and cap (Q11), blue/orange mapping for server-driven screens (Q12), `codeSyntax.iOS` (Q13).

### wiom-ios-icon-badge

| # | Question | Default in this skill |
|---|---|---|
| 1 | A `neutral` badge (`bg/subtle`) inside a pressed list row (pressed fill `bg/subtle`, D13) disappears into the row while pressed. Android behaves the same. Intended? | Keep parity; no change. |
| 3 | **DECIDED (D31):** dark Warning glyph on subtle or solid Warning background; gold glyph is ratings-only. | 10.85:1 on subtle; 6.60:1 on solid. The old gold-on-tint exception is superseded. |
| 2 | Figma ships only the Neutral tone; the other five are built from tokens (Android does the same). Will Figma add tone variants? | Tones as in §2. |

The original baseline matched badge sizes/padding. D31 now overrides the old Warning tone pair; shared source and Android library alignment are separate follow-up work, not edits authorised here.

### wiom-ios-input-fields

1. **Label weight.** Android and the source skill keep the title at `type/label/lg` and change colour only. An earlier design note described the label as Bold when empty and Regular when focused or filled. This skill follows what Android ships; design team to confirm, then Figma and Android change together.
2. **`+91` prefix vs phone icon.** This skill draws `+91` as a non-editable prefix (source skill). The Android README says not to prepend `+91` and to use a leading phone icon instead (`component/input/README.md:111-125`). Which one does the customer app ship on both platforms?
3. **Read-only title colour.** Source skill says `text/default`; Android ships `text/subtle`. This skill follows Android.
4. **Leading icon tint.** Source skill code uses `icon/action`; Android ships `icon/nonAction`. This skill follows Android.
5. **OTP status borders.** Android draws every resting box in the status colour on Error/Success and shows the active box only while editing; the source skill's code draws only active/inactive and an active box whenever enabled. This skill follows Android.
6. **Warning border.** Android code uses `stroke/warning`; the Android README table says `stroke.brandFocus` (`README.md:81`). This skill follows the code; README to be fixed.
7. **Textarea states.** Design draws six states; Android's `WiomTextarea` also accepts Warning and read-only. Are those allowed in customer screens?
8. **DECIDED (D31): Warning status colour.** Dark `icon/action` on `bg/warning/subtle`, inside the neutral field. Gold `icon/warning` is ratings-only. The Warning status glyph remains non-tappable. Container: Icon Badge Sm, 24 pt circle, 16 pt glyph (D35). The separate Warning border contrast remains open; do not change helper text, field fill or border tokens under this icon ruling.
9. **Number-pad "Next".** Number pads have no Return key. This skill relies on the CTA riding the keyboard; if a form needs a "Next" between two numeric fields, does design want a keyboard accessory bar (system-styled)?

### wiom-ios-layout-rules

No separate visual values are defined here. Component mismatches remain in the component Open questions lists; shared unresolved decisions are in `../wiom-ios-foundations/references/decisions.md` §3 and §5.

### wiom-ios-list-item

0. **DECIDED: secondary/meta text.** Owner commit `23f67f9` locks `type/body/sm` (12 pt). Android still ships `type/body/md` (14). iOS follows the owner’s locked source rule; **Android app must change**. This is a known implementation mismatch, not an unanswered design choice.

1. **Disabled icon-with-bg row.** Android draws a `bg/disabled` circle *behind* a Neutral-tone `WiomIconBadge` of the same size, so the visible result is the Neutral badge (`bg/subtle` fill, `icon/nonAction` glyph), not the skill's `bg/disabled` fill + `icon/disabled` glyph. iOS follows Android for parity. Design team: confirm the intended look; if it is `bg/disabled` + `icon/disabled`, Android and iOS both change.
2. **Text wrapping.** The older skill code set one-line limits on primary, secondary and meta; Android sets none, so text wraps. iOS follows Android (wraps). Confirm wrapping is the intended rule for meta too.
3. **Trailing meta at accessibility text sizes** moving under the text column is an iOS-only layout adaptation (Android has no equivalent breakpoint). Confirm with the design team.
4. **Dialog selection body `space/8` between rows** comes from the skill (Figma dialog selection); Android's list item has no such spacing itself, the host adds it. Confirm with `wiom-ios-dialog`.
5. **Row press timing.** SwiftUI delays the pressed state of a `Button` inside a `ScrollView` slightly so a scroll doesn't flash rows; Android shows it on touch-down. Accepted as platform behaviour unless the design team objects.

### wiom-ios-loader

1. **DECIDED (D37): brand-loader animation.** Use the shipped `loader_infinity.json` (both apps). Design to correct loop (2.0 s vs 1.3 s), pink (#D92B90 vs #D9008D) and the grey track in a later file; the Android library should bundle the same file.
2. **Dots vertical padding:** source and Android use 10 vertically and 12 horizontally. The rejected builder copy changed vertical padding to 12. iOS keeps 12 × 10; there is no 10 token (gap per D24). Figma's bubble is 104 × 32; Android's hugs at 56 × 28.
3. **Skeleton shimmer:** Android 1.2 s with a `bg/default` 55 % band; skill says 1.5 s, "`bg/muted` 10 % lighter". iOS follows Android.
4. **Skeleton Card border:** skill has 1 pt `stroke/subtle`; Android draws none. iOS follows Android.
5. **Skeleton ListItem trailing block:** skill 60 pt, Android 40 pt. Line widths: skill fixed 280 / 200 / 160, Android fractions 100 / 75 / 50 %. iOS follows Android. Android's Line is a single bar; the skill's three-line "Line" type is a stack of three.
6. **Linear Determinate easing:** Android tweens 300 ms with linear easing; foundations keep `ease/linear` for loops, so iOS uses `motion/surface` · `ease/standard`. Confirm, or allow `ease/linear` here.
7. **Loop periods** (spinner 1.0 s, Linear 1.5 s, Dots 1.0 s / 150 ms stagger, shimmer 1.2 s) are not motion tokens. Should `motion.md` define loop tokens?
8. **Reduce Motion still for Linear Indeterminate:** a centred 40 % segment was chosen so it can't be read as "40 % done". Confirm.
9. **In-button spinner:** `wiom-ios-cta` uses 24 pt / 2 pt (as Android ships); this skill's sm is 20 pt. Same open point as `wiom-ios-cta` Open question 1.
10. **Brand message alignment:** Android doesn't centre-align the message text, so a two-line message is leading-aligned inside a centred column. The skill says centred. iOS follows Android; recommend both apps centre it.
11. **Two indeterminate bars on Android:** the loader's Linear (40 %, 1.5 s, `bg/brand/subtle` track) and `WiomLinearProgressIndeterminate` in the progress package (25 %, 1.4 s, `bg/muted` track). iOS ships only the loader's. Retire the other?
12. **Status loader** (wait → success / error ring): in old drafts, not shipped on Android. Not on iOS; outcomes use the outcome surface.

### wiom-ios-motion

| # | Question | Until answered |
|---|---|---|
| Q4 | Will motion tokens become Figma variables? | Tokens live in `wiom-ios-foundations/references/motion.md` as cubic-Bézier values; this skill cites names only. |
| M1 | Does the iOS DS module ship the composed `Animation` wrappers (`Wiom.Motion.surfaceStandard`, `Wiom.Motion.settle`, …) or only durations and curves? | Treat §7 as the required set; wrapper names follow `wiom-ios-foundations/references/decisions.md` §2. |
| M2 | Does any customer-app moment need the celebration motif? | Unused (§5.5); raise a customer-app motion gap. |
| M3 | Easing for the confirmation check segment and the dialog fade is not stated in the locked rulings. | Check uses `ease/enter` (arrival), dialog uses `ease/standard`, pending design confirmation. |

### wiom-ios-navigation-bar

1. **Closed by D27:** the customer app has no bottom navigation bar.
   The remaining questions concern this unused reference only.
2. **Glyph fill: accepted correction.** Default is Rounded fill off; Selected uses the filled pair in source commit `2fa260f`. Android defaults to its supplied glyph; exact state-pair assets need verification before this unused reference is activated. Do not source substitute glyphs from another family.
3. **Label wrapping.** Android shows 1 line and truncates. iOS wraps to 2 lines at larger text sizes
   and follows the app-wide accessibility3 cap.
   Confirm, and consider the same for Android with two-line Hindi.
4. **Pressed visual.** Android nav items use the default `clickable`
   indication, the Material ripple. D13 bans
   ripple and there is no pressed token, so iOS shows none. Design team:
   define one or confirm none.
5. **Badge type.** The source skill allows swapping the dot for a count badge
   "when the count is meaningful"; Android supports only the critical dot. This skill allows the dot only.
6. **Bottom padding on Face ID iPhones.** `space/12` above the
   home-indicator inset makes the bar
   about 114 pt tall including the 34 pt inset, against 83 pt for a system tab
   bar. Confirm, or use the D19 value (`space/16`) as for the last bottom CTA.
7. **Tab re-tap.** Scroll-to-top on re-tapping the selected tab is iOS
   behaviour; Android doesn't specify one. Confirm.

### wiom-ios-pagination

1. **Disabled chevron.** The skill says the unavailable chevron "consumes
   taps as a no-op"; Android disables the click and drops its spoken label.
   Android's README says chevrons hide at bounds, but the code keeps them
   visible and disabled. iOS uses a visible, truly disabled button
   (VoiceOver "dimmed"). Confirm the README is stale.
2. **Counter string.** Android builds the label as `"$current / $total"` in
   code, not from a string resource, and the skill's example "2 of 10 बिल"
   mixes languages. iOS uses one catalog string with placeholders. Android
   to move to a string resource with the same key.
3. **Chevron glyph style.** The skill asks for an "outline (line)" chevron;
   Android uses Material Rounded `chevron_left` / `chevron_right`. iOS
   follows Android (Material Rounded assets).
4. **Inactive token.** Android's README lists `stroke/subtle` for inactive
   dots and bars; the code and the skill use `bg/muted`. iOS uses `bg/muted`.
5. **Chevron tint.** Android's README says `icon/nonAction`; the code and
   the skill use `icon/action` (available) and `icon/disabled`
   (unavailable). iOS follows the code.
6. **Counter centring.** The skill centres the counter row; Android's row
   has no centring of its own (the parent places it). iOS centres the row in
   its parent; confirm on Android.
7. **Accessibility parity.** Android dots and bars expose no "page n of N"
   value or adjustable action. iOS adds both (behaviour, not look); Android
   should add the Android accessibility equivalent.
8. **Expanded dot motion.** Neither platform animates the 8 → 24 pt change.
   If design wants a `motion/micro` width transition, add it on both.

### wiom-ios-progress-indicator

1. **Milestones gap:** Android 20 dp; the skill says both `space/24` and "20 dp". iOS uses 20 pt for parity. No `space/20` exists: add the token, or change both apps to `space/16` or `space/24`?
2. **Ladder automation:** the skill says Linear and Circular pick the tone from the value; Android does not (caller passes `tone`, default Brand). iOS follows Android, with one shared ladder helper. Confirm that's intended.
3. **Circular:** skill = one 48 pt ring with a centre `type/label/sm` percentage; Android = sm 24 / 3 and lg 48 / 4, no centre label. iOS follows Android. Is a centre label wanted on lg?
4. **Draw-on, count-up and colour cross-fades:** in the skill (600 ms fill / arc, 300 ms colour), not shipped on Android. iOS is instant. Adopt on both, with `motion/emphasis` / `motion/surface` and the Reduce Motion jump?
5. **Pill and stage-label type:** Android uses `type/meta/xs` (10 pt) for the Completion pill and the Milestones stage labels. D18 forbids `type/meta/xs` for Devanagari, and both carry Hindi. iOS uses the skill's `type/label/sm` (pill) and `type/body/sm` (stage labels). Android should change to match.
6. **Stage-label position:** Android centres each label in an equal-width column, so the first and last labels don't sit under their circles; the skill says centred under each circle. iOS follows Android.
7. **Untokened values:** pill vertical padding 2 pt (`space/2` isn't an iOS token) and the 6 pt pill dot. Gaps per D24.
8. **Linear default size:** Android defaults to sm 4; the skill's examples default to md 8. iOS follows Android; Completion always uses md.
9. **Stage-label limit and fallback:** ≤ 8 grapheme clusters is taken from the longest source example. Confirm, and confirm hiding the label row (subtitle carries the stage) when labels need more than 2 lines at large text sizes.
10. **Stage glyph source:** Android takes only an `ImageVector`; the skill allows a brand drawable fallback. iOS uses Material Rounded assets only (D4); a non-Material glyph needs a design-team asset.
11. **Indeterminate bars and rings in Android's progress package** (`WiomLinearProgressIndeterminate`, `WiomCircularProgressIndeterminate`) are not part of this iOS skill; indeterminate waits use `wiom-ios-loader`.

### wiom-ios-rating

1. Star size 32 pt has no icon token (D24). Add `icon/xl` 32 or keep as a component constant.
2. Figma has no rating component yet; design to draw it from this spec.

### wiom-ios-selection-controls

1. **DECIDED (D34): thumb token.** `icon/inverse`. Android library to switch from raw `Color.White` to the same token.
2. **DECIDED (D28): switch animation.** Switch thumb movement uses `motion/micro` + `ease/standard` on both platforms, not the previously recorded Android default spring. Android skills were updated in PR #18 (`b480a46`). Applying the rule to the `wiom-ds-android` library code remains a dev-team implementation task.
3. **Indicator size.** The Android README says checkbox and radio are 20 × 20 (`selectioncontrol/README.md:16-17`, rule 2 at line 69); the Android code and the skill ship 24 × 24. iOS follows the code (24). The README should be fixed.
4. **Checkbox/radio pressed.** Standalone Android checkbox and radio use the default indication (ripple) via `toggleable` / `selectable`; there is no pressed token. iOS shows no pressed visual (D13). Design team: is a pressed look wanted?
5. **Error announcement.** The skill defines Error visuals only. iOS puts the error text next to the control (in the label). Should the error also be posted as a VoiceOver announcement when it appears (as for input fields)?
6. **Switch semantics.** Verify the native accessibility representation on iOS 16 through current versions; ensure the value is spoken once.
7. **Switch thumb implementation.** Use `Wiom.Colors.iconInverse` (D34).

### wiom-ios-tabs-filters

1. **DECIDED (D30): pill count.** 2 to 4 on both platforms. Historical implementor note: **Android v0.3.0 caps at 2..4 and should tighten to 1..3**. That older instruction is superseded by D30; do not tighten the implementation to 1..3. The shared source documentation needs the new owner ruling.

2. **Pill item height: skill 32 pt vs Android 36 pt.** The source base minimum is
   32 (track 40); Android pads `space/8` vertically around a 20 pt
   line, giving 36 (track 44). iOS follows Android.
3. **Pill and filter disabled state, badges, icon-only More filter.** The
   skill defines a disabled pill (`bg/disabled`), a disabled filter
   (`text/disabled`), count badges in pills and filters, and a trailing
   `filter_list` "more" item. Android ships none of these. iOS keeps badges and disabled variants
   unexposed for parity, but implements the accepted More overflow rule
   at 7+ (§2.3); Android needs to add that behaviour.
4. **Fixed-mode filter width: skill "always hug" vs Android "equal width".**
   iOS follows Android (equal width in Fixed mode, hug when scrolling).
5. **Underline indicator position.** The skill puts the indicator at the
   item's bottom edge, full item width. Android draws it at the bottom of
   the label's padded content box (12 pt above the bar border; label width
   when scrolling, item width minus 32 pt when fixed). iOS follows Android;
   this looks unintended and needs a design ruling.
6. **Chip unselected border: skill `stroke/default` vs Android
   `stroke/subtle`.** iOS follows Android.
7. **Chip close glyph as its own target.** Android makes the 16 pt close
   glyph separately tappable ("Remove …"). On iOS it can't reach 44 pt
   inside a 36 pt chip, so the whole chip toggles. Confirm no separate
   remove action is needed.
8. **Chip row wrapping.** The skill says chips wrap; Android's `WiomChipRow`
   is a single non-wrapping row and leaves wrapping to a `FlowRow` parent.
   iOS wraps (skill rule), which matches Android only when the screen uses
   `FlowRow`. Confirm wrapping is the rule on both.
9. **Pressed states.** No pressed token exists for pill, filter or chip and
   Android relies on ripple. iOS shows no pressed visual (D13). Design team
   to say whether a pressed fill (e.g. `bg/subtle`) is wanted on both.
10. **Pill label wrapping at large text.** Android truncates pill and filter
    labels to one line; iOS wraps pill labels (Dynamic Type safety) and
    switches the filter bar to scrolling. Confirm.

### wiom-ios-toast

1. **DECIDED (D31): Warning fill and icon colours.** Whole toast stays `bg/default`. Use dark `icon/action` on `bg/warning/subtle`, measured 10.85:1, and preserve the Material Rounded Warning glyph as decorative. This is the global Warning recipe, not a toast-only exception: inputs and Warning icon badges also use dark glyphs on the approved Warning backgrounds. Gold `icon/warning` is ratings-only. **Container (D35):** Icon Badge Sm, a 24 pt circle with a 16 pt glyph (`wiom-ios-icon-badge`). The Warning glyph is intentionally smaller than the 24 pt Critical / Info / Positive glyphs; the circle keeps the same 24 pt footprint so the row height and alignment match.
2. **DECIDED: horizontal and bottom margins.** Owner commit `23f67f9` locks `space/8` horizontally (flexible width). D29 locks `space/16` above the highest safe-area / CTA-bar / keyboard boundary, matching the Android skill.
3. **Easing: Android vs skill.** The skill (§11) and the motion
   doctrine (D-3 ruling) specify 300 ms `EaseOut` in / `EaseIn` out;
   Android ships `tween(300)` with the default standard curve, plus a
   fade, both ways. iOS follows Android
   (`motion/surface`, `ease/standard`). Confirm whether Android will be
   moved to EaseOut / EaseIn; iOS will follow.
4. **Hit area of action and ✕.** The skill wraps both in a ≥ 48 pt
   interactive box; Android ships only `space/8` × `space/4` padding on
   the action and none on ✕. iOS uses the
   44/48 pt hit area (D14), which changes no visual. Android should add
   the minimum interactive size.
5. **Toast while a modal is open.** Android's toast lives in the
   screen's `Scaffold`, so a modal sheet or dialog covers it. iOS
   queues toasts until the modal closes (§5). Confirm, or name the
   cases (for example "Copied" from inside a sheet) where the toast
   should show above the modal.
6. **Message length guide.** The source gives no grapheme number for
   the message; "about 40 Hindi grapheme clusters per line on iPhone
   SE" and "action ≤ 12" are iOS defaults. The design team to confirm
   or replace.
7. **VoiceOver ✕ on Actionable toasts.** Showing ✕ on Actionable toasts
   only while VoiceOver runs is a behaviour-only addition (it adds a
   visible glyph for VoiceOver users). Confirm this is acceptable, or
   rely on the escape gesture alone.

### wiom-ios-top-bar

1. **Hamburger on the Android home tab.** The Android README lists "Home tab:
   Large · Default · `Menu` leading" (`wiom-ds-android/.../topbar/README.md`,
   "Wiom use cases"). The customer iOS app has no hamburger; root screens have
   no leading item. Design team: confirm Android drops it too, or say where
   its menu content lives on iOS.
2. **Pressed visual.** Android's `WiomTopBarIconAction` and
   `WiomTopBarTextAction` use the default `clickable` indication, which is the
   Material ripple. D13 bans ripple and there is
   no pressed token, so iOS shows no pressed visual. Design team: define one
   (for example a `bg/subtle` circle) or confirm none.
3. **Centered state: skill vs Android.** The source skill says Centered is for
   branded / no-back screens with no leading item and no subtitle. Android
   ships it as the modal header with a close leading, a subtitle allowed and
   max 1 trailing action.
   This skill follows Android. The title centres in the space between leading
   and trailing, not on the screen; confirm that's intended.
4. **Search pill details: skill vs Android.** Android tints the search glyph
   `icon/nonAction` (skill: `icon/action`), uses a `text/default` insertion
   point (skill: `text/brand`), adds `space/8` horizontal margin around the
   pill, and passes the trailing slot through, so icons are possible there
   (skill: text action only). This
   skill follows Android for the visuals and keeps "text action only" as the
   usage rule.
5. **Medium / Large action row.** Android pins the action row at 48 with
   `space/8` vertical padding, leaving 32 pt for
   48 pt icon cells. iOS draws a 48 pt row with full 48 pt cells and no extra
   vertical padding. Confirm against the rendered Android build.
6. **Large two-line title.** Android allows 2 lines in a fixed 152 dp bar; the title area has 60 dp for 88 dp of text,
   so a two-line title clips on Android. iOS grows the bar instead.
7. **Line limits for Small / Medium titles.** Android is 1 line with
   ellipsis. iOS allows 2 lines at
   larger text sizes. Confirm for Android too, so two-line Hindi doesn't clip.
8. **Back-button VoiceOver string key.** Needs a shared string-catalog entry
   ("Back") used by every screen.

### wiom-ios-ux

1. The glossary changes marked ⟨iOS⟩ (नेट and घर का नेट) need the design lead's lock.
2. The live app copy still uses कृपया (15 times) and mixes "Cancel booking" / "Cancel Booking"; fix in the shared catalog.
3. Should the forward-only screen's Wiom logo replace back on Android too, or is it already there? (Parity check.)

## Android code references

Kept for parity checks against `wiom-ds-android` (v2.0.1, `1ce3c31`). Each row is the skill line as it read before the references were removed.

| File | Line | Text |
|---|---|---|
| `wiom-ios-badge/SKILL.md` | 252 | (`WiomBadge.kt:214-215`; KDoc at `WiomBadge.kt:128` and `:150`). iOS |
| `wiom-ios-badge/SKILL.md` | 257 | with the default clip (`WiomBadge.kt:191-196`). iOS uses one line |
| `wiom-ios-badge/SKILL.md` | 262 | (`WiomBadge.kt:70-71`) and leaves the nudge to callers. iOS follows |
| `wiom-ios-badge/SKILL.md` | 270 | gives Small Tinted (`WiomBadge.kt:169`). iOS follows Android. |
| `wiom-ios-bottomsheet/SKILL.md` | 194 | \| 1 \| Sheet list rows: the source skill says rows are `wiom-list-item` instances with a 16 gutter; Android draws its own sheet row with 24 sides, a 40 brand circle, `label/lg` and an `icon/disabled` chevron (`WiomBottomSheet.kt:254-318`). Header padding is 16 (`WiomBottomSheet.kt:196-200`), so header and rows don't line up. \| Follow Android: sheet row for action menus and share; `wiom-ios-list-item` for radio and checkbox pickers. Design team to confirm the 24 vs 16 alignment. \| |
| `wiom-ios-bottomsheet/SKILL.md` | 195 | \| 2 \| Share layout: source skill says a horizontal row of share targets; Android previews it as header + list rows (`WiomBottomSheet.kt:561-577`). \| Follow Android (rows). \| |
| `wiom-ios-bottomsheet/SKILL.md` | 196 | \| 3 \| Size heights: source skill gives min/max ranges and `Full` = 92 % of the screen; Android ships minimums only (240 / 400 / 600) and `Full` hugging content (`WiomBottomSheet.kt:128-141`). \| Minimum shares (30 / 50 / 75 %) as in Android; `Full` fills to the cap. \| |
| `wiom-ios-bottomsheet/SKILL.md` | 197 | \| 4 \| Android opens tall non-Full sheets half-expanded (`ModalBottomSheet` default state, `WiomBottomSheet.kt:73-75`); the iOS sheet has no detents. \| No half-open state on iOS. \| |
| `wiom-ios-bottomsheet/SKILL.md` | 198 | \| 5 \| Shadow: source skill and `tokens.md` say `shadow/md`; Android sets no explicit shadow on the sheet (`WiomBottomSheet.kt:81-99`). \| `shadow/md`. \| |
| `wiom-ios-bottomsheet/SKILL.md` | 199 | \| 6 \| Non-dismissable sheets: Android has no non-dismissable mode (scrim and swipe always dismiss, `WiomBottomSheet.kt:81-87`). iOS adds it for money and commit moments. \| iOS behaviour as §3; Android to follow. \| |
| `wiom-ios-bottomsheet/SKILL.md` | 200 | \| 7 \| Non-modal sheets: Figma has `Is Modal` (default false); Android ships only modal sheets (`WiomBottomSheet.kt:87`). If design ever needs one, the overlay host can skip the scrim and leave the content beneath hit-testable on iOS 16.0 (no 16.4 API), with `.isModal` removed. \| Not used. \| |
| `wiom-ios-bottomsheet/SKILL.md` | 201 | \| 8 \| Destructive confirmation: the source sheet skill listed an Illustration sheet; the source dialog skill and Android (`WiomDialog.kt` preview "Alert · destructive") use a dialog. `wiom-ios-cta` §6.1 still has a bottom-sheet destructive row. \| Dialog. The cta row applies only when a sheet's own commit is destructive (e.g. a Form that cancels a request). \| |
| `wiom-ios-bottomsheet/SKILL.md` | 203 | \| 10 \| `WiomTypography.kt:18` says sheet and dialog headers default to `heading/lg`; the shipped sheet header uses `heading/md` (`WiomBottomSheet.kt:219`). \| `type/heading/md`; `typography.md` leaves the choice to this skill. \| |
| `wiom-ios-cta/SKILL.md` | 219 | \| 1 \| The CTA loading spinner is 24 pt with a 2 pt stroke on Android (`WiomButton.kt:167-174`), but the loader's own in-button size is Spinner Sm, 20 pt (`WiomLoader.kt:58-59`). Which is right? \| 24 pt, as Android ships. \| |
| `wiom-ios-cta/SKILL.md` | 220 | \| 2 \| Source skill says the spinner *replaces* label and icon; Android keeps them laid out at zero opacity (`WiomButton.kt:139-155`), so the button keeps its width. \| Follow Android (no size change). \| |
| `wiom-ios-cta/SKILL.md` | 221 | \| 3 \| Acknowledge row-to-CTA gap: skill says 16 pt; Android's preview uses 8 pt (`WiomButton.kt:517`) and the row adds 4 pt vertical padding (`WiomButton.kt:208`). \| 16 pt (Android's component doesn't own this gap; only its preview differs). \| |
| `wiom-ios-cta/SKILL.md` | 222 | \| 4 \| Dialog pairings: skill says Primary + Secondary and Destructive + Secondary; Android dialog previews pair Primary + Tertiary and Destructive + Tertiary (`WiomDialog.kt:509-510, 525-526`). Which is canonical? \| Skill table (§6.2). \| |
| `wiom-ios-dialog/SKILL.md` | 136 | \| 1 \| **DECIDED by owner commit `23f67f9`:** Alert uses a 48 pt neutral circle with `bg/subtle` and `icon/action`. Android still draws a brand rounded square (`WiomDialog.kt:143-159`). \| iOS follows the locked dialog rule. **Android app must change.** Generic Neutral icon badges retain `icon/nonAction`; the dialog owns this override. \| |
| `wiom-ios-dialog/SKILL.md` | 137 | \| 2 \| Loading: the source skill has an optional Tertiary "Cancel" and back-press dismissal when cancellable; Android ships no button and is never dismissable (`WiomDialog.kt:366-381`). \| Follow Android: no button, escape does nothing. \| |
| `wiom-ios-dialog/SKILL.md` | 138 | \| 3 \| Illustration panel: the source skill allows other subtle tones (`bg/positive/subtle`, `bg/info/subtle`); Android ships `bg/brand/subtle` only (`WiomDialog.kt:318-333`). The Android doc comment still describes a 120 circle (`WiomDialog.kt:290-292`); the code draws the 144 panel. \| Brand only, 144 panel. \| |
| `wiom-ios-dialog/SKILL.md` | 139 | \| 4 \| Title style: `WiomTypography.kt:18` says dialog headers default to `heading/lg`; every dialog type ships `heading/md` (`WiomDialog.kt:164, 208, 261, 340, 404`). \| `type/heading/md`; `typography.md` defers to this skill. \| |
| `wiom-ios-dialog/SKILL.md` | 140 | \| 5 \| Body style: the Android README says `body/lg`; the code uses `body/md` (`WiomDialog.kt:169`). \| `type/body/md`. \| |
| `wiom-ios-dialog/SKILL.md` | 141 | \| 6 \| VoiceOver escape on Alert and Illustration closes (mirrors Android's back press, `WiomDialog.kt:82`). Should a money-related Alert ever be escape-proof? \| Escape closes; money commits belong on a non-dismissable sheet anyway. \| |
| `wiom-ios-icon-badge/SKILL.md` | 103 | \| 2 \| Figma ships only the Neutral tone; the other five are built from tokens (Android does the same, `WiomIconBadge.kt:158-167`). Will Figma add tone variants? \| Tones as in §2. \| |
| `wiom-ios-input-fields/SKILL.md` | 240 | 1. **Label weight.** Android (`WiomInput.kt:224-228, 261`) and the source skill keep the title at `type/label/lg` and change colour only. An earlier design note described the label as Bold when empty and Regular when focused or filled. This skill follows what Android ships; design team to confirm, then Figma and Android change together. |
| `wiom-ios-input-fields/SKILL.md` | 242 | 3. **Read-only title colour.** Source skill says `text/default`; Android ships `text/subtle` (`WiomInput.kt:226`). This skill follows Android. |
| `wiom-ios-input-fields/SKILL.md` | 243 | 4. **Leading icon tint.** Source skill code uses `icon/action`; Android ships `icon/nonAction` (`WiomInput.kt:254`). This skill follows Android. |
| `wiom-ios-input-fields/SKILL.md` | 244 | 5. **OTP status borders.** Android draws every resting box in the status colour on Error/Success and shows the active box only while editing (`WiomOtp.kt:95-113, 141-142`); the source skill's code draws only active/inactive and an active box whenever enabled. This skill follows Android. |
| `wiom-ios-input-fields/SKILL.md` | 245 | 6. **Warning border.** Android code uses `stroke/warning` (`WiomInput.kt:219`); the Android README table says `stroke.brandFocus` (`README.md:81`). This skill follows the code; README to be fixed. |
| `wiom-ios-input-fields/SKILL.md` | 246 | 7. **Textarea states.** Design draws six states; Android's `WiomTextarea` also accepts Warning and read-only (`WiomInput.kt:144-146`). Are those allowed in customer screens? |
| `wiom-ios-list-item/SKILL.md` | 154 | 1. **Disabled icon-with-bg row.** Android (`WiomListItem.kt:257-271`) draws a `bg/disabled` circle *behind* a Neutral-tone `WiomIconBadge` of the same size, so the visible result is the Neutral badge (`bg/subtle` fill, `icon/nonAction` glyph), not the skill's `bg/disabled` fill + `icon/disabled` glyph. iOS follows Android for parity. Design team: confirm the intended look; if it is `bg/disabled` + `icon/disabled`, Android and iOS both change. |
| `wiom-ios-list-item/SKILL.md` | 155 | 2. **Text wrapping.** The older skill code set one-line limits on primary, secondary and meta; Android (`WiomListItem.kt:133-150`) sets none, so text wraps. iOS follows Android (wraps). Confirm wrapping is the intended rule for meta too. |
| `wiom-ios-loader/SKILL.md` | 209 | 2. **Dots vertical padding:** source and Android use 10 vertically (`WiomLoader.kt:473`) and 12 horizontally. The rejected builder copy changed vertical padding to 12. iOS keeps 12 × 10; there is no 10 token (gap per D24). Figma's bubble is 104 × 32; Android's hugs at 56 × 28. |
| `wiom-ios-loader/SKILL.md` | 210 | 3. **Skeleton shimmer:** Android 1.2 s with a `bg/default` 55 % band (`WiomLoader.kt:532`, `:551`); skill says 1.5 s, "`bg/muted` 10 % lighter". iOS follows Android. |
| `wiom-ios-loader/SKILL.md` | 211 | 4. **Skeleton Card border:** skill has 1 pt `stroke/subtle`; Android draws none (`WiomLoader.kt:200-205`). iOS follows Android. |
| `wiom-ios-loader/SKILL.md` | 212 | 5. **Skeleton ListItem trailing block:** skill 60 pt, Android 40 pt (`WiomLoader.kt:274-277`). Line widths: skill fixed 280 / 200 / 160, Android fractions 100 / 75 / 50 % (`WiomLoader.kt:227-229`, `:271-272`). iOS follows Android. Android's Line is a single bar; the skill's three-line "Line" type is a stack of three. |
| `wiom-ios-loader/SKILL.md` | 213 | 6. **Linear Determinate easing:** Android tweens 300 ms with linear easing (`WiomLoader.kt:399`); foundations keep `ease/linear` for loops, so iOS uses `motion/surface` · `ease/standard`. Confirm, or allow `ease/linear` here. |
| `wiom-ios-loader/SKILL.md` | 216 | 9. **In-button spinner:** `wiom-ios-cta` uses 24 pt / 2 pt (as `WiomButton.kt` ships); this skill's sm is 20 pt. Same open point as `wiom-ios-cta` Open question 1. |
| `wiom-ios-loader/SKILL.md` | 217 | 10. **Brand message alignment:** Android doesn't centre-align the message text (`WiomLoader.kt:365-369`), so a two-line message is leading-aligned inside a centred column. The skill says centred. iOS follows Android; recommend both apps centre it. |
| `wiom-ios-loader/SKILL.md` | 218 | 11. **Two indeterminate bars on Android:** the loader's Linear (40 %, 1.5 s, `bg/brand/subtle` track) and `WiomLinearProgressIndeterminate` in the progress package (25 %, 1.4 s, `bg/muted` track; `WiomProgressIndicator.kt:115-159`). iOS ships only the loader's. Retire the other? |
| `wiom-ios-navigation-bar/SKILL.md` | 173 | (`WiomNavigationBar.kt:163-164`). iOS wraps to 2 lines at larger text sizes |
| `wiom-ios-navigation-bar/SKILL.md` | 177 | indication, the Material ripple (`WiomNavigationBar.kt:122`). D13 bans |
| `wiom-ios-navigation-bar/SKILL.md` | 182 | (`WiomNavigationBar.kt:48`, `:148-155`). This skill allows the dot only. |
| `wiom-ios-navigation-bar/SKILL.md` | 184 | home-indicator inset (Android: `WiomNavigationBar.kt:94-95`) makes the bar |
| `wiom-ios-progress-indicator/SKILL.md` | 118 | **Gap note (stated once):** the source skill says `space/24` in its anatomy and "20 dp" in its token table. Android ships **20** for both gaps (`WiomProgressIndicator.kt:454`), so iOS uses 20 pt for parity. There is no `space/20` token: this is a token gap reported to the design team (D24); in code it carries a `// TODO(IOS-123): …` with the ticket. |
| `wiom-ios-progress-indicator/SKILL.md` | 169 | Android draws each new value **at once**: no tween on the fill or arc, no colour cross-fade, no count-up (`WiomProgressIndicator.kt:85-100`, `:196-222`). iOS matches this: value, tone, stage and pill changes are instant. |
| `wiom-ios-progress-indicator/SKILL.md` | 196 | 1. **Milestones gap:** Android 20 dp (`WiomProgressIndicator.kt:454`); the skill says both `space/24` and "20 dp". iOS uses 20 pt for parity. No `space/20` exists: add the token, or change both apps to `space/16` or `space/24`? |
| `wiom-ios-progress-indicator/SKILL.md` | 197 | 2. **Ladder automation:** the skill says Linear and Circular pick the tone from the value; Android does not (caller passes `tone`, default Brand; `WiomProgressIndicator.kt:39-48`, `:77`, `:188`). iOS follows Android, with one shared ladder helper. Confirm that's intended. |
| `wiom-ios-progress-indicator/SKILL.md` | 198 | 3. **Circular:** skill = one 48 pt ring with a centre `type/label/sm` percentage; Android = sm 24 / 3 and lg 48 / 4, no centre label (`WiomProgressIndicator.kt:167-223`). iOS follows Android. Is a centre label wanted on lg? |
| `wiom-ios-progress-indicator/SKILL.md` | 199 | 4. **Draw-on, count-up and colour cross-fades:** in the skill (600 ms fill / arc, 300 ms colour), not shipped on Android (`WiomProgressIndicator.kt:85-100`, `:196-222`). iOS is instant. Adopt on both, with `motion/emphasis` / `motion/surface` and the Reduce Motion jump? |
| `wiom-ios-progress-indicator/SKILL.md` | 200 | 5. **Pill and stage-label type:** Android uses `type/meta/xs` (10 pt) for the Completion pill (`WiomProgressIndicator.kt:391`) and the Milestones stage labels (`:511`). D18 forbids `type/meta/xs` for Devanagari, and both carry Hindi. iOS uses the skill's `type/label/sm` (pill) and `type/body/sm` (stage labels). Android should change to match. |
| `wiom-ios-progress-indicator/SKILL.md` | 201 | 6. **Stage-label position:** Android centres each label in an equal-width column (`WiomProgressIndicator.kt:505-507`), so the first and last labels don't sit under their circles; the skill says centred under each circle. iOS follows Android. |
| `wiom-ios-progress-indicator/SKILL.md` | 202 | 7. **Untokened values:** pill vertical padding 2 pt (`WiomProgressIndicator.kt:380`; `space/2` isn't an iOS token) and the 6 pt pill dot (`:386`). Gaps per D24. |
| `wiom-ios-progress-indicator/SKILL.md` | 203 | 8. **Linear default size:** Android defaults to sm 4 (`WiomProgressIndicator.kt:78`); the skill's examples default to md 8. iOS follows Android; Completion always uses md. |
| `wiom-ios-progress-indicator/SKILL.md` | 205 | 10. **Stage glyph source:** Android takes only an `ImageVector` (`WiomProgressIndicator.kt:413`); the skill allows a brand drawable fallback. iOS uses Material Rounded assets only (D4); a non-Material glyph needs a design-team asset. |
| `wiom-ios-progress-indicator/SKILL.md` | 206 | 11. **Indeterminate bars and rings in Android's progress package** (`WiomLinearProgressIndeterminate`, `WiomCircularProgressIndeterminate`; `WiomProgressIndicator.kt:115-271`) are not part of this iOS skill; indeterminate waits use `wiom-ios-loader`. |
| `wiom-ios-selection-controls/SKILL.md` | 149 | 3. **Indicator size.** The Android README says checkbox and radio are 20 × 20 (`selectioncontrol/README.md:16-17`, rule 2 at line 69); the Android code and the skill ship 24 × 24 (`WiomSelectionControl.kt:87`, `:192`). iOS follows the code (24). The README should be fixed. |
| `wiom-ios-selection-controls/SKILL.md` | 150 | 4. **Checkbox/radio pressed.** Standalone Android checkbox and radio use the default indication (ripple) via `toggleable` / `selectable` (`WiomSelectionControl.kt:78-82`, `:183-187`); there is no pressed token. iOS shows no pressed visual (D13). Design team: is a pressed look wanted? |
| `wiom-ios-toast/SKILL.md` | 224 | fade, both ways (`WiomToast.kt:256-263`). iOS follows Android |
| `wiom-ios-toast/SKILL.md` | 229 | the action and none on ✕ (`WiomToast.kt:133-148`). iOS uses the |
| `wiom-ios-top-bar/SKILL.md` | 256 | Material ripple (`WiomTopBar.kt:190`, `:217`). D13 bans ripple and there is |
| `wiom-ios-top-bar/SKILL.md` | 262 | max 1 trailing action (`WiomTopBar.kt:50`, `:276-310`; preview `:521-537`). |
| `wiom-ios-top-bar/SKILL.md` | 269 | (skill: text action only) (`WiomTopBar.kt:262-274`, `:365-379`). This |
| `wiom-ios-top-bar/SKILL.md` | 273 | `space/8` vertical padding (`WiomTopBar.kt:470-474`), leaving 32 pt for |
| `wiom-ios-top-bar/SKILL.md` | 277 | (`WiomTopBar.kt:439`, `:457`); the title area has 60 dp for 88 dp of text, |
| `wiom-ios-top-bar/SKILL.md` | 280 | ellipsis (`WiomTopBar.kt:288`, `:322`, `:419`). iOS allows 2 lines at |
| `wiom-ios-foundations/references/decisions.md` | 30 | \| D2 \| Letter spacing \| **Use the skill/Android tracking** (display −0.02em; heading/title.lg −0.01em; label +0.01em; meta +0.02em; others 0) \| Android ships these values (`WiomTypography.kt:62-74`). Figma's 0 % gets fixed. On Devanagari runs, see `wiom-ios-foundations/references/typography.md` §4. \| |
| `wiom-ios-foundations/references/typography.md` | 24 | Same values as Android (`WiomTypography.kt`). Sizes and line heights in pt at the default text size. |
