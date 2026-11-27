---
name: wiom-ios-ux
description: "Wiom UX and copy rules for the SwiftUI iOS customer app: Hindi-first voice, screen patterns, button and input copy, sentence case, grapheme-cluster length limits, trust on money screens, the emotional arc (no celebration before the net works), the access-adoption doctrine, chat copy, and the glossary. Use when deciding a screen's flow, structure or copy for the Wiom customer app on iPhone, or reviewing one."
---

# Wiom UX for the iOS customer app

**The iPhone app is the Android app.** Same flows, same screens, same components, same copy (one shared string catalog). This skill holds the UX and copy rules both apps follow; the `wiom-ios-*` component skills say how each part looks; [`../IOS_DECISIONS.md`](../IOS_DECISIONS.md) says where iOS behaviour differs (gestures, keyboard, accessibility). Adapted on 19 Nov 2026 from the builder repo’s `wiom-design-ux` reference material, with the iOS review’s fixes applied.


**UX provenance:** the six original UX reference files were adapted from the `wiom-design-ux` material supplied from `wiom-builder-documents`, not from `abhishekgarg-wiom/wiom-design-system`. The source DS repository governs component/foundation design; **copy owner (D39): Abhishek Garg** approves new or changed copy. The AI never changes existing app copy; it may only suggest. Builder material is read-only reference for this task.

## Reference files

| File | What | Status of its source |
|---|---|---|
| [`references/customer-adoption-doctrine.md`](references/customer-adoption-doctrine.md) | Product Doctrine v1.0, the Access Adoption frame (Risk / Commitment / Outflow / Effort), Journey Architecture v2.0, no-pressure visual doctrine. **Load for every screen.** | LOCKED product principles; workflow dependencies removed |
| [`references/recharge-belief-model.md`](references/recharge-belief-model.md) | What the customer must believe about recharge, and when it is taught | Approved rows only; unapproved recharge rows moved to unused archive |
| [`references/chat-copy-guidelines.md`](references/chat-copy-guidelines.md) | Chat thread copy: belief, not sales | Retained chat guidance; three draft state extensions excluded |
| [`references/glossary.md`](references/glossary.md) | English → Hindi terms; iOS fixes marked ⟨iOS⟩ | LOCKED + marked changes pending lock |
| [`references/writing-playbook.md`](references/writing-playbook.md) | Voice, screen patterns, buttons, casing, limits, inputs, words to avoid | Rewritten for iOS |
| [`references/drafts-not-in-use.md`](references/drafts-not-in-use.md) | Unapproved recharge ideas and chat-state extensions, preserved verbatim | Not in use: owner approval needed |
| [`references/glossary-partner-not-in-use.md`](references/glossary-partner-not-in-use.md) | Partner vocabulary and original rules, preserved verbatim | Not in use for iOS |
| [`references/design-rules.md`](references/design-rules.md) | Screen-level rules (buttons, top bar, dialogs, inputs, sheets, errors, empty states) | Rewritten for iOS |

**Loading boundary:** agents must never load `references/drafts-not-in-use.md` or `references/glossary-partner-not-in-use.md` for screen or copy work. They are historical review archives, not default guidance.

Not carried over: the workflow inventory and funnel doctrine files (2.5 MB, partner-app and prototype-app data, a QA host URL and mock personal data) and the glossary overlay proposal (its नेट term is applied in the glossary).

## 1. Who we design for

A Bharat household member who reads Hindi first, gives a screen about 10 seconds, may be paying online for the first time, needs to feel safe and in control, and decides for the whole family. The customer already believes in home internet; what they don't yet understand is **Wiom's commercial model**. Every screen removes one of four barriers (**Risk, Commitment, Outflow, Effort**); a screen that removes none probably shouldn't exist (adoption doctrine §1).

## 2. The 12 principles

1. **Hindi first.** Hindi is the default for all UI text, in Noto Sans. Terms come from the glossary; no invented translations. Speak the user's model: घर का नेट, रिचार्ज, पढ़ाई, काम, TV; never Mbps, broadband, FUP.
2. **No negative framing** unless it's needed: "भुगतान नहीं हो पाया" not "भुगतान विफल" (illustrative).
3. **Audience before content:** who reads it, what they need, what our goal is.
4. **Buttons** say the next step, are 2 to 3 words (max 5), never questions; disabled until ready, never hidden (`references/design-rules.md` §2).
5. **Casing:** English is sentence case everywhere; Hindi has no case (`references/writing-playbook.md` §4).
6. **Scan path:** the most important thing goes top-left and first.
7. **Warm, casual tone:** friendly, respectful, never commanding or robotic.
8. **Family brand:** clear to kids and grandparents; respects the household's decision-maker.
9. **Benefit first, action later:** "नेट यहीं लगाया जाएगा", then "अपना पता बताइए" (illustrative).
10. **Short and simple:** one primary action per screen; every word earns its place.
11. **Errors never blame:** say what happened, reassure (only with true facts), give a next step.
12. **Hierarchy:** headline → support → benefit → button.

## 3. Trust on money screens

| The user's fear | The screen answers it with |
|---|---|
| "पैसे कट गए?" | Check mark + exact amount |
| "सही जगह गए?" | Booking ID + company name |
| "धोखा तो नहीं?" | The product's **real** refund terms, stated plainly |
| "सबूत कहाँ?" | Receipt, copyable and shareable |
| "अब क्या करूँ?" | Numbered next steps |
| "मदद मिलेगी?" | "हमसे बात करें" always visible |

**Never promise a refund the product doesn't give.** The booking fee is **not** returned when a booking is cancelled (the live app says so); copy, badges and examples must match the real terms. "Refundable" appears only on money that truly is refundable, and a refundable deposit is called जमा राशि. Status colours: green for confirmed, purple (info) for in progress, never red for processing.

## 4. Emotional arc (T-01, locked 8 Sep 2026)

> **No celebration until the service works.** Payment and commit moments get the calm confirmation motif; celebration is earned when the customer's net is live.

| Journey | Arc |
|---|---|
| Onboarding | Curiosity → confidence → (excitement only when the net is live) |
| Payment | Clarity → trust → relief. Calm confirmation, nothing more |
| Net live | The journey's **one** delight moment, as a visual/motion state (`wiom-ios-motion`), never a "बधाई" string |
| Error | Concern → reassurance → resolution |

## 5. Teaching boundary (T-02, locked)

Before payment, teach only **what I pay today, what I get, what is refundable and what isn't, and that there are no hidden charges**. How the recharge cycle works is taught after the net is live (Welcome Internet), before it matters. First Recharge is a pure decision: no new concepts (`references/recharge-belief-model.md`).

## 6. No pressure

No "limited time", countdowns, flashing buttons, red urgency, or fake scarcity. Urgency only when a real operational limit exists, said honestly (adoption doctrine §7, doctrine 5).

## 7. Confidence

- The user always knows how many steps remain (`wiom-ios-progress-indicator`).
- Waits say how long they usually take.
- No dead ends: every screen has a way forward and a way out.

## Open questions

1. The glossary changes marked ⟨iOS⟩ (नेट and घर का नेट) need the design lead's lock.
2. The live app copy still uses कृपया (15 times) and mixes "Cancel booking" / "Cancel Booking"; fix in the shared catalog.
3. Should the forward-only screen's Wiom logo replace back on Android too, or is it already there? (Parity check.)

## iOS (SwiftUI, iOS 16+)

- **Built from:** the `wiom-ios-*` components only; screens match the Android screens one to one.
- **Tokens:** `type/body/lg`, `type/label/lg`, `text/default`, `text/subtle`; component skills define the visual token sets.
- **Size:** text containers use minimum heights in pt, fill available width and grow with real catalog copy.
- **Hit area:** interactive copy is inside a ≥ 44 × 44 pt target, default 48 × 48.
- **Motion:** `wiom-ios-motion` owns usage; Reduce Motion keeps every state meaningful without movement.
- **Safe areas and keyboard:** surfaces own device-safe layout and field visibility; the sticky CTA follows D19.
- **Haptics:** none.
- **Copy:** from the shared string catalog (`Localizable.xcstrings`), same keys and text as Android. No hard-coded strings; no iOS-only rewording. Fixes to copy are made in the catalog so both apps change together.
- **Dynamic Type:** Hindi copy is longer and taller; every screen is checked in Hindi and English at default, xxxLarge and accessibility3 (`wiom-ios-foundations/references/typography.md`).
- **VoiceOver:** copy is written to be heard as well as read: button labels make sense alone; errors are announced; "9+" style text has a spoken form in the catalog.
- **Length:** limits are grapheme clusters (`String.count`).
- **Behaviour iOS owns:** swipe-back (except on forward-only screens), keyboard, system share sheet, permission prompts. Their system text is iOS's; the permission *purpose strings* in `Info.plist` follow this skill's voice and come from the catalog.
- **Not on iOS:** picture-in-picture flows from the old Android rules (iPhone PiP is for video only), hardware back, bottom tab bar (D27).
