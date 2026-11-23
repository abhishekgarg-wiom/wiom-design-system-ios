# Wiom Customer Adoption Doctrine : canon reference

**Source of truth:** Ashish's Google Doc "Customer App Design Philosophy" (ID `112_IA9WEaSAAd2WXYOWG0X1nxT50qFv1B9jI62U6kaw`), captured Aug 31 2026 via the owner's session. The doc contains five documents; the OPERATIVE frame is the NEW one (Access Adoption) : the old "category teacher" philosophy is kept there as history with a written comparison recording the pivot. This file carries the complete rule content; the Google Doc remains the living SoT.

**The pivot, in one line:** the app is no longer a *category teacher* ("why should I get home internet?") : it is an **Access Adoption Engine** ("why should I get home internet *this way*?"). Customers already believe in home internet; they don't yet understand Wiom's commercial model. *Experience changes behavior, not information.* Owner's margin notes preserved: "RWGKN works"; "not about how our install process works : those are secondary"; "you're not teaching what GKN is, you're teaching what RW is"; "the commercial model IS the product ← most important"; "the app owns expectation management : cost of failure has increased"; OPEN THREAD: "we'll need to think about if reliability is more important than speed (of getting install)".

## 1. The four Access barriers (the design doctrine)

Every screen must remove one or more of: **Risk** ("will I lose my money?") · **Commitment** ("will I get trapped?") · **Outflow** ("can I comfortably pay this today?") · **Effort** ("how difficult is this going to be?"). *If a screen removes none of these, it probably should not exist.*

## 2. Wiom Product Doctrine v1.0 : ten doctrines, ALL LOCKED (per the doc's register)

Hierarchy: **Paradigm Integrity** is the parent; the rest are its consequences. *"If a proposal violates a doctrine, the proposal should change : not the doctrine."*

| # | Doctrine | Rule | Decision test |
|---|---|---|---|
| 1 | **Paradigm Integrity** (parent) | Every interaction teaches customers what Wiom is; no interaction is neutral. Wiom teaches: Flexible, Safe, Honest, Recharge-shaped. Anything teaching cheap/discount/lock-in/pressure/hidden terms weakens the category | What does this teach the customer about Wiom? |
| 2 | **Price Integrity** | Increasing value, never decreasing price. Never discount the category. ✓ extra recharge days, Welcome Internet, referral rewards · ✗ percentage discounts, reduced prices, "today only" pricing | Does this strengthen or weaken the commercial model's perceived value? |
| 3 | **Recharge Doctrine** | Recharge is part of the product, not a payment mechanism. Every promotional benefit requires a recharge action. ✓ "14 days + 2 extra days", redeem via recharge · ✗ auto-extending validity, auto-crediting promotional days | Does this strengthen recharge behaviour, or bypass it? |
| 4 | **Promise Integrity** | Every promise must already be operationally true before it enters communication. Marketing follows operations. A company capability measured across Product/Ops/Finance | Can this promise be honoured consistently? |
| 5 | **Operational Honesty** | Urgency only when it reflects a real operational constraint. ✓ locality launch, genuine capacity · ✗ fake countdowns, manufactured scarcity | Would this constraint exist if we never marketed it? If yes, communicate honestly; if no, don't communicate it |
| 6 | **Adaptive Journey** | Friction adapts to earned trust: new = max reassurance; returning = max convenience; existing = max speed. Same destination, different journey | Has this customer already earned the right to skip this step? |
| 7 | **Flexibility Doctrine** | Whenever operationally feasible, choose the option that increases customer flexibility. The customer constantly feels "I remain in control" | Does this increase or reduce customer flexibility? |
| 8 | **Experience Before Revenue** | Onboarding's objective is adoption, not revenue. Welcome Internet exists to teach flexibility. **First Recharge is the acquisition event**; retention begins after it | Does this improve first recharge, or merely Day-0 revenue? |
| 9 | **Simplicity Doctrine** | The commercial model gets simpler over time, never more sophisticated | Can a customer explain this to a neighbour after seeing it once? |
| 10 | **Trust Through Transparency** | Trust = eliminating surprises. Transparency is the product, not customer support | Does this reduce uncertainty? |

**Decision checklist (verbatim intent, all ten):** what mental model does this teach · strengthens flexibility? · preserves price integrity? · reinforces recharge behaviour? · can ops keep the promise? · genuine urgency? · journey adapts to trust? · improves first recharge? · simplifies the model? · reduces uncertainty? *Multiple "No" → redesign the proposal.*

## 3. Experience Philosophy (the operative purpose doc)

- The product being built is **Flexibility** (the defining experience, à la Uber = convenient rides, UPI = instant payments); home internet is the medium.
- The app does NOT teach: why home internet matters, broadband tech, Mbps, router features. It MUST teach the commercial model : what I pay today, what I receive, what's refundable, hidden charges (none), what happens after Welcome Internet : **before payment is requested**, and it **verifies understanding through observable behaviour** ("commercial-model understanding is a measurable milestone, not an assumption").
- Design principles: (1) Reassure before explaining. (2) The commercial model is part of the product. (3) Every decision feels reversible. (4) Experience deepens belief (Welcome Internet's purpose = experiencing flexibility, not free internet : "make the first recharge feel inevitable"). (5) One psychological job at a time. (6) Every screen answers one customer question.
- Marketing: creates interest / removes hesitation; the product converts trial into adoption and proves flexibility. Operations: **the app is the primary promise-keeping surface** : it proactively communicates reality (installation status, next steps, changes); the app owns expectation management, not the call center.
- One line: *"Reassure first. Explain the commercial model clearly. Prove continuously. Let the first recharge close itself."*

## 4. Customer Journey Architecture v2.0 : ten stages

Entry Router first: New (reassurance + model + guided trial) / Returning (convenience, quick reconnect, relationship acknowledged) / Existing (speed, continuity) / future: referral, assisted, WhatsApp, locality. Same destination; only the starting point changes.

| Stage | Customer question | Barrier | Success event |
|---|---|---|---|
| 1 Reassurance | Can I trust this? | Risk | Customer continues (trust badges, neighbourhood proof, promise indicators : facts not marketing) |
| 2 Serviceability | Will this work at my home? | Effort+Risk | Certainty either way : not-serviceable captures location/phone/interest, explains next steps, **never a dead end** |
| 3 Commercial Model | Exactly what happens if I continue? | Risk | Model understood (dominant visual: the commercial-model timeline : understand before reading paragraphs) |
| 4 Model Confirmation | Did I understand correctly? | Risk | Understanding VERIFIED (clarify and continue on misunderstanding : never test intelligence, never block) |
| 5 Identity | What information do you need? | Effort | Minimum info collected, nothing more |
| 6 Payment | Is my money still safe? | Commitment | Payment : Commercial Truth Pack stays visible; **no new information at payment** |
| 7 Welcome Internet | Is Wiom actually different? | : (creates belief) | Active usage : reinforce remaining days, recharge rhythm, control, next steps |
| 8 Guided Adoption | What happens after Welcome Internet? | Commitment | Recharge readiness : nothing at First Recharge may feel surprising |
| 9 First Recharge | Do I want to continue? | : | **First Recharge = the acquisition event.** No new concepts, no education, only decision |
| 10 Habit | How does Wiom fit into my life? | : | Recharge continuity; product gets quieter; family usage/value expands |

**Cross-cutting rules (all seven):** every screen removes one barrier · answers one customer question · every visual has one job · understand by looking before reading · recognition before instruction (borrow familiar patterns; teach new commercial behaviour) · rich journey, simple screens, one dominant visual · every stage leaves "the next step is obvious."

**Screen review checklist:** which question does it answer? · which barrier does it reduce? · the one dominant visual? · understandable without reading every word? · what observable behaviour proves success? · does the customer know exactly what to do next? Unclear → redesign.

**Stage success metrics (verbatim):** Reassurance→continue · Serviceability→resolved-or-waitlist · Model→understood · Confirmation→confirmed · Identity→completion · Payment→payment · Welcome→active usage · Guided→recharge readiness · First Recharge→first recharge · Habit→recharge continuity.

## 5. Capability Roadmap v1.0 (build shape, for reference)

Nine capabilities, phased: **Phase 1 launch-critical** : Adaptive Entry, Commercial Model (Truth Pack, timeline, confirmation), Trust (local proof, promise indicators, tracking), Trial Experience (Welcome meter, guidance). **Phase 2 adoption** : First Recharge (recharge cards, user-applied rewards, reminders), Promise Keeping (install/refund trackers, delay comms, compensation). **Phase 3 scale** : Habit, Supply Awareness (serviceability, waitlist, outage, slots), Measurement (funnel events, comprehension measurement, experiments : "the product should never assume psychological progress without evidence"). Weekly planning question: *which capability are we strengthening?* : never *which feature are we building?*

## 6. Language philosophy

Avoid telecom vocabulary (broadband, Mbps, FUP, latency). Speak the user's mental model: घर का नेट, recharge, पढ़ाई, काम, TV, phone. (Feeds the glossary's audience-scoped rules : customer surfaces speak the customer's words.)

## 7. Visual doctrine for early-journey customer screens

Trust before brand (white dominates, brand colours sparing, branding understated : brand emerges from a trustworthy experience). Calm before excitement (generous whitespace, minimal noise, restrained type : "closer to opening a bank account than an e-commerce sale"). Information before offers. Commercials introduced late. **No pressure**: no "Limited Time", no "Only Today", no flashing CTAs, no countdown timers, no aggressive pop-ups. Teacher, not salesperson: patient, factual, transparent, respectful : the user leaves thinking "I understand this better", never "I am being sold to." Action before exploration.

