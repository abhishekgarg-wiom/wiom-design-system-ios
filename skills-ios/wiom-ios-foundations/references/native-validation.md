# Native iOS validation and implementation readiness

Use when implementing the app shell, reviewing a component or signing off a screen. This makes the existing iOS contract testable; it adds no visual tokens or new product behaviour. Component skills and IOS_DECISIONS remain authoritative. HTML examples and Swift snippets are not native test evidence.

**Contents:** 1 shared host responsibilities · 2 keyboard and text reflow · 3 interaction tests · 4 readiness evidence.

## 1. Implement shared hosts once

| Shared responsibility | Existing contract to preserve | Acceptance case |
|---|---|---|
| Navigation host | Custom Wiom top bar plus system push/pop and interactive swipe-back; top-bar skill and decisions D5-D7 | Push two destinations. Back button and edge swipe both work. Cancel an interactive swipe; the current screen remains usable and its state is retained. Verify after a sheet is dismissed too. |
| Overlay host | Root-level custom sheet/dialog layers; bottomsheet and dialog skills own sizes, z-order and dismissibility | Install the host in each presentation context as the sheet skill requires. A dialog over a sheet isolates the top dialog. Closing it restores access and focus to the sheet, rather than the screen beneath. System-owned share and permission surfaces remain system-owned. |
| Modal accessibility | Focus enters the title, underlying content is hidden from VoiceOver and untappable; escape only when dismissible | Navigate every element with VoiceOver. No background control is reachable. Dismiss using an allowed path; focus returns to the initiating control if it still exists, otherwise a logical visible control in the same task. Non-dismissible loading exposes no false escape action. |
| Keyboard-aware surface | Existing safe-area rules and component-specific CTA gaps; backgrounds extend into insets, content respects them | Focus the last field with the keyboard open. The field and its error remain reachable. The CTA stays above the keyboard; sheet body scrolls within its cap. Do not apply a second manual keyboard-height inset over the system keyboard safe area. |
| State and animation ownership | Component state updates immediately; motion rules specify the visual interpolation | Keep selection identity stable. Rapid reversal does not restart from a stale value, lose focus or require waiting for animation. Disable interaction according to the component state, not merely through visual opacity. |

Use these shared hosts in features; do not recreate their focus, gesture and keyboard logic per screen. These are implementation responsibilities, not claims that a compiled host ships in this package.

## 2. Keyboard and text reflow

| Scenario | Pass condition |
|---|---|
| Hindi and English; default, xxxLarge and accessibility3 | Text wraps before truncating, except where the component explicitly permits truncation. No overlap, clipped matras, hidden actions or fixed-height text container. Preserve the existing Dynamic Type cap pending its open owner question. |
| CTA pairs or title plus trailing value no longer fit | Use the component's existing stacking rule. Keep reading and action order consistent after reflow; do not shrink fonts or icons to force a row to fit. |
| Chips wrap at large text sizes | Hit frames occupy layout space and do not overlap. Selection/deselection remains usable; close glyph stays decorative. Do not animate the entire wrapping layout. |
| Sheet at accessibility sizes | Follow the sheet skill: header may scroll with body, action bar stays pinned and its group stacks. Last content can scroll into view above the action bar and keyboard. |
| Text entry, paste and focus changes | Preserve entered text and caret across validation and unrelated state updates. OTP remains one semantic field with one-time-code support; visual boxes do not become separate inputs. Test paste and AutoFill on a native build. |
| Keyboard appears, changes height and dismisses | Focused content stays reachable without double insets or abrupt screen jumps. Bottom spacing follows the CTA and surface skills; this checklist does not settle the separate toast vertical-gap question. |

Keep the shared default appearance. Reflow is the response to available space and accessibility size, not a new iOS visual variant.

## 3. Interaction and accessibility tests

- Check a compact iPhone and a large iPhone on iOS 16 and the current supported iOS version. Record build, OS, device and language with evidence.
- Verify actual hit frames meet the existing minimum without overlap. An invisible content shape alone does not reserve layout space.
- VoiceOver reads one action once, preserves reading order after reflow, announces selection immediately, and announces each relevant error/result once. Verify a row with a separate trailing action does not hide that action.
- On modal open, move focus to the heading rather than defaulting to a destructive button. Test allowed scrim/drag/escape paths and focus restoration. Dismissibility comes from the component skill.
- Turn Reduce Motion on. Spatial motion uses the reduced form; selection colour/opacity changes remain. Progress and confirmation use their documented final states; non-spinner loops stop; spinner remains active.
- Interrupt and reverse a selection transition with repeated taps. Final visible and accessible state matches the latest input. Navigating away during dismissal leaves no delayed overlay, stale focus or blocked background interaction.
- Inspect Increase Contrast and Smart Invert for breakage and record issues. Do not invent alternate colours or claim those modes are supported without validation.
- Compare the same fixture content and component states with Android at default text sizes. Record approved platform behaviour differences separately from unexplained visual differences.

## 4. Readiness evidence

| Status | Evidence required | Current package |
|---|---|---|
| Specified | Active skill, decision links, explicit gaps and unused states | 19 skill documents exist; the navigation-bar skill is retained but unused (D27) |
| Implemented | Native component/API and consuming build or code reference | Not assessed; snippets describe APIs to implement |
| Native-tested | Build/device/OS/language details plus results for applicable cases above | Not assessed; HTML and static validation do not qualify |
| Parity-reviewed | Android/iOS fixtures at named versions, reviewed differences and decision links | Not assessed; a documentation baseline does not prove rendered parity |

When reporting a component, use these statuses independently and attach evidence to the claim. Do not mark it native-tested because an HTML test passed, or parity-reviewed because both platforms use the same token names. Record unavailable evidence as not assessed, not passed. Keep unresolved owner decisions visible rather than treating a provisional default as approved.
