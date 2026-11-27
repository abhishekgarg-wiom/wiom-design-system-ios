---
name: wiom-ios-cta
description: "Wiom button (CTA) for the iOS customer app in SwiftUI: 6 types, states, button groups, sticky button bar. Use when building or reviewing a Wiom CTA, its button group or sticky CTA bar in SwiftUI."
---

# Wiom CTA (iOS)

One button component with **6 types**: Primary, Secondary, Tertiary, Destructive, Pre-booking, Acknowledge (compound). The five standard types have the states Default, Pressed, Disabled, Loading. Acknowledge has Unchecked, Checked, Disabled.

This skill also **owns the button-group rule** (§6) and the **sticky button bar** (§7). `wiom-ios-dialog` and `wiom-ios-bottomsheet` point here for how their buttons are laid out.

Contract: `../wiom-ios-foundations/references/decisions.md`. Tokens: `wiom-ios-foundations` (`references/tokens.md`, `typography.md`, `icons.md`, `layout.md`, `accessibility.md`, `motion.md`).

## 1. Anatomy

| Slot | Value | Token |
|---|---|---|
| Width | Fill the container (the surface owns the gutter). Inline Tertiary may hug its label. | none |
| Height | **Minimum** 48 pt: vertical padding + label line height. Grows when the label wraps. | none |
| Corner radius | 16 pt, circular corners (D3) | `radius/large` |
| Shadow | none | `shadow/none` |
| Horizontal padding | 16 pt | `space/16` |
| Vertical padding | 12 pt | `space/12` |
| Content row | Centred on both axes, 8 pt gap | `space/8` |
| Leading / trailing icon | 20 pt, optional, Material Rounded (D4) | `icon/sm` (size) |
| Label | SemiBold 16 / 24 | `type/label/lg` |
| Border (Secondary only) | 2 pt, drawn **inside** the shape | `stroke/medium` (width) |
| Loading spinner | 24 pt, 2 pt stroke, centred; label and icons stay laid out but invisible, so the button never changes size | `icon/md` (size) |

Never set a fixed width or height on a CTA. Size comes from padding and content.

## 2. The 6 types

| Type | Purpose | Where it sits | Don't use for | Sample copy (illustrative) |
|---|---|---|---|---|
| **Primary** | The main action. Filled brand. Max 1 per screen, sheet or dialog. | Sticky button bar (most common); inline in cards, sheets, dialogs when it is the dominant action. | Cancel, Skip, Dismiss, Maybe later, a generic "Continue". | "Recharge now", "भुगतान करें", "Verify OTP" |
| **Secondary** | Alternate prominent action next to Primary. Outlined brand. | Beside Primary in bottom sheets; under Primary in dialogs; rarely alone. | Destructive actions, throwaway dismiss, the main action. | "Cancel", "Change plan", "वापस जाएं" |
| **Tertiary** | Lightweight dismiss or soft action. Text only. | Under Primary; alone in a dialog for a plain "OK"; inline in cards and rows. | Destructive actions, the main action, side by side with Primary. | "बाद में", "Maybe later", "Skip", "Edit", "ठीक है" |
| **Destructive** | Irreversible loss of data. Filled critical. **Never alone.** | Confirmation sheets and dialogs, always with an escape (Secondary or Tertiary). | Closing a form, Skip, Go back: those lose nothing. | "Delete plan", "Deactivate account" |
| **Pre-booking** | The Primary of the **pre-booking journey**: every forward action from app landing through payment success. Several per journey is expected. | Sticky bar, sheets, dialogs, inline cards on every pre-booking screen until payment success. | Login, signup, OTP (auth stays Primary even inside the journey). Screens after payment success. Any other flow. | "Pre-book now", "Continue to plan", "Pay ₹X to pre-book" |
| **Acknowledge** | Compound: checkbox row + a Primary that stays Disabled until checked. First-person verification before an irreversible step. | Sticky bar or inline, directly above the gated action. | Generic confirmations (use Primary), multi-checkbox forms, third-person copy. | "मैंने सभी जानकारी सही दी है", "I have read the T&C" |

## 3. Tokens per type and state

Pressed visuals follow D13 and the Android implementation: the fill changes while the finger is down, instantly, with no ripple, scale, opacity dip or overlay. Pressed applies only in the Default state.

### 3.1 Primary

| State | Fill | Border | Label | Icon / spinner |
|---|---|---|---|---|
| Default | `bg/brand` | none | `text/onBrand` | `icon/inverse` |
| Pressed | `bg/brand/pressed` | none | `text/onBrand` | `icon/inverse` |
| Disabled | `bg/disabled` | none | `text/disabled` | `icon/disabled` |
| Loading | `bg/brand` | none | hidden | spinner `icon/inverse` |

### 3.2 Secondary (2 pt border in every state)

| State | Fill | Border | Label | Icon / spinner |
|---|---|---|---|---|
| Default | clear | `stroke/brand/focus` | `text/brand` | `icon/brand` |
| Pressed | `bg/brand/subtle` | `stroke/brand/focus` | `text/brand` | `icon/brand` |
| Disabled | clear | `stroke/subtle` | `text/disabled` | `icon/disabled` |
| Loading | clear | `stroke/brand/focus` | hidden | spinner `icon/brand` |

### 3.3 Tertiary

| State | Fill | Label | Icon / spinner |
|---|---|---|---|
| Default | clear | `text/brand` | `icon/brand` |
| Pressed | `bg/brand/subtle` (in the 16 pt rounded shape) | `text/brand` | `icon/brand` |
| Disabled | clear | `text/disabled` | `icon/disabled` |
| Loading | clear | hidden | spinner `icon/brand` |

### 3.4 Destructive

| State | Fill | Label | Icon / spinner |
|---|---|---|---|
| Default | `bg/critical` | `text/onCritical` | `icon/inverse` |
| Pressed | `bg/critical/pressed` | `text/onCritical` | `icon/inverse` |
| Disabled | `bg/disabled` | `text/disabled` | `icon/disabled` |
| Loading | `bg/critical` | hidden | spinner `icon/inverse` |

### 3.5 Pre-booking (dark label: white on `bg/brand/accent` fails contrast)

| State | Fill | Label | Icon / spinner |
|---|---|---|---|
| Default | `bg/brand/accent` | `text/onBrandAccent` | `icon/action` |
| Pressed | `bg/brand/accent/pressed` | `text/onBrandAccent` | `icon/action` |
| Disabled | `bg/disabled` | `text/disabled` | `icon/disabled` |
| Loading | `bg/brand/accent` | hidden | spinner `icon/action` |

### 3.6 Acknowledge (compound)

| Part | Value | Token |
|---|---|---|
| Checkbox | Wiom checkbox from `wiom-ios-selection-controls` (24 pt box) | per that skill |
| Checkbox to label gap | 12 pt, label top-aligned with the box | `space/12` |
| Row label | `type/label/lg`, `text/default` in every state (only the box dims when disabled) | |
| Row to CTA gap | 16 pt | `space/16` |
| Compound height | Minimum 88 pt (24 + 16 + 48); grows with the label | |

| State | Checkbox | Inner CTA |
|---|---|---|
| Unchecked | Outlined, `stroke/brand/focus` 2 pt | Primary Disabled |
| Checked | Filled `bg/brand`, check `icon/inverse` | Primary Default |
| Disabled | Outlined, `stroke/subtle` 2 pt | Primary Disabled |

The whole row (box + label) toggles the checkbox. Never pre-checked. Copy is always first person ("मैंने…", "I have…"), never third person ("कस्टमर ने…").

## 4. Label and copy

| Rule | Detail |
|---|---|
| Copy names the destination | "Recharge now", not "Continue". |
| Keep it short | Aim for one line at default text size. Guide for a label that must sit side by side: about 14 graphemes Hindi or 18 English (D25: count with `String.count`). |
| **Wrap, never truncate** | At large Dynamic Type the label wraps (centred, usually to two lines) and the button grows taller. Never `lineLimit(1)`, never truncate, never `minimumScaleFactor`. |
| Sentence case | English labels are sentence case ("Change plan"). |
| Source | Real copy comes from the string catalog (Hindi first, English written separately). Examples here are illustrative. |
| Icons | Only when they add meaning (call, delete, forward). Decorative to VoiceOver: the label already says it. |

## 5. Placement and surface contract

The surface owns the gutter; the CTA fills what is left (D15).

| Surface | Side gutter (surface owns) | CTA does |
|---|---|---|
| Inline screen content | `space/16` screen gutter | fill |
| Sticky button bar | `space/16` (see §7) | fill |
| Dialog | `space/24` dialog padding (`wiom-ios-dialog`) | fill |
| Bottom sheet | `space/16` sheet padding (`wiom-ios-bottomsheet`) | fill |
| Card | card padding | fill, or hug for an inline Tertiary |

**Sticky or inline?** If removing the CTA would leave the user no way to finish the screen's purpose, it goes in the sticky button bar. Otherwise inline.

## 6. Button groups (the one rule)

A group is 1 to 3 CTAs with a **12 pt gap** (`space/12`) and no padding of its own. Every CTA in a group fills its slot; side-by-side slots are equal width.

### 6.1 Layout rule: owned here, used by dialog, sheet, sticky bar and cards

> **Side by side only when each label fits on one line in its half-width slot at the current text size. Otherwise stack.**
> The check runs at layout time, so the same group can be side by side at default size and stacked at xxxLarge.

| Surface | Default layout | Falls back to |
|---|---|---|
| **Dialog** | **Stacked.** Side by side is allowed only when both labels fit (rule above). | Stacked |
| **Bottom sheet** pairs (Secondary + Primary, Secondary + Destructive, Secondary + Secondary) | Side by side when both labels fit | Stacked |
| **Destructive confirmation** ("are you sure?") | Always a **dialog**, never a sheet (`wiom-ios-bottomsheet` § Choosing a surface): stacked by default, Destructive on top | Stacked |
| **Sticky button bar** two-action terminal step | Side by side when both fit | Stacked |
| Any group with Tertiary + Primary, or 3 CTAs | Always stacked | |

**Order:** side by side, the preferred action is on the **right**. Stacked, the preferred action is on **top**. When a pair falls back from side by side to stacked, the right-hand action moves to the top.

### 6.2 Pairing table

| Surface | Scenario | CTAs (preferred last) |
|---|---|---|
| **Bottom sheet** | One dominant action | Primary |
| | Dominant + weighty dismiss | Secondary + Primary |
| | Dominant + soft dismiss | Tertiary + Primary (stacked: Primary on top) |
| | Equal weight | Secondary + Secondary |
| | Sheet whose own submit is destructive (e.g. remove a saved address from a picker sheet) | Secondary + Destructive |
| | 3 actions | Primary, Secondary, Tertiary (stacked, in that order) |
| **Dialog** | Simple acknowledgement | Tertiary alone ("ठीक है") |
| | Confirmation | Primary on top, Secondary below |
| | Destructive confirmation | Destructive on top, Secondary below |
| | Celebration / success | Primary |
| **Sticky button bar** | Reason-for-being action | Primary (or Pre-booking in the journey) |
| | Acknowledge gate | Acknowledge row above Primary |
| | Two-action terminal step (rare) | Secondary + Primary |
| **Inline (cards, rows)** | Single inline action | Tertiary, hugging, end-aligned |
| | Card's main action | Primary, filling the card |
| | Edit / Delete on a row | Tertiary + Tertiary |

### 6.3 Choosing a layout by importance gap

```
Acknowledge before the action?                → Acknowledge row above Primary
One dominant + a weighty dismiss (Cancel)     → Secondary + Primary
One dominant + a throwaway dismiss ("बाद में")  → Primary on top, Tertiary below
Dominant is destructive                       → Secondary + Destructive
Equal weight                                  → Secondary + Secondary; shorten copy before accepting a stack
```

## 7. Sticky button bar

The bar is a surface: it owns the gutter, the top border and the safe-area handling (D19). Its children fill.

| Part | Value | Token |
|---|---|---|
| Background | Fills the bar and **extends under the home indicator** | `bg/default` |
| Top border | 1 pt hairline across the full width | `stroke/small` (width), `stroke/subtle` |
| Shadow | none | `shadow/none` |
| Side padding | 16 pt | `space/16` |
| Top padding | 16 pt | `space/16` |
| Bottom, Face ID iPhone | 16 pt from the last button to the top of the home-indicator safe area | `space/16` |
| Bottom, Home-button iPhone (SE) | 16 pt from the last button to the screen edge | `space/16` |
| Bottom, keyboard up | The bar rides on top of the keyboard; 12 pt below the last button | `space/12` |
| Content | One CTA, a button group (§6), or the Acknowledge compound | |

Scroll content above the bar must be able to scroll its last item clear of the bar (attach the bar as a bottom safe-area inset, not as an overlay).

## 8. Universal rules

1. No fixed width or height. Fill (or hug for inline Tertiary); height is a minimum.
2. Max 1 Primary and max 1 Destructive per screen, sheet or dialog. Never pair Primary with Destructive: Destructive replaces Primary.
3. Tertiary is never side by side with Primary.
4. Destructive is never alone.
5. Inside the pre-booking journey every forward action is Pre-booking; outside it, Primary.
6. Labels wrap, never truncate (§4).
7. Content is centred inside the full button width, also when the label is short.
8. Tokens only, by DS V2 name. Flat: no shadow on CTA or sticky bar.
9. Icons are Material Rounded template images from the asset catalog (D4), tinted with the type's `icon/*` token.

## Open questions

| # | Question | Default in this skill |
|---|---|---|
| 1 | The CTA loading spinner is 24 pt with a 2 pt stroke on Android (`WiomButton.kt:167-174`), but the loader's own in-button size is Spinner Sm, 20 pt (`WiomLoader.kt:58-59`). Which is right? | 24 pt, as Android ships. |
| 2 | Source skill says the spinner *replaces* label and icon; Android keeps them laid out at zero opacity (`WiomButton.kt:139-155`), so the button keeps its width. | Follow Android (no size change). |
| 3 | Acknowledge row-to-CTA gap: skill says 16 pt; Android's preview uses 8 pt (`WiomButton.kt:517`) and the row adds 4 pt vertical padding (`WiomButton.kt:208`). | 16 pt (Android's component doesn't own this gap; only its preview differs). |
| 4 | Dialog pairings: skill says Primary + Secondary and Destructive + Secondary; Android dialog previews pair Primary + Tertiary and Destructive + Tertiary (`WiomDialog.kt:509-510, 525-526`). Which is canonical? | Skill table (§6.2). |
| 5 | Is a two-line CTA label acceptable to design at large text sizes, and should copy guidance cap at two lines? | Wrap freely, never truncate; copy aims for one line at default size. |

## iOS (SwiftUI, iOS 16+)

- **Built from:** `Button` + a custom `ButtonStyle` (`WiomButtonStyle`) reading `configuration.isPressed`. Group layout is a small `Layout` (iOS 16). Spinner from `wiom-ios-loader`. Acknowledge checkbox from `wiom-ios-selection-controls`. Never `.borderedProminent`, `.bordered`, `.plain` or system tint.
- **Tokens:** `bg/brand`, `bg/brand/pressed`, `bg/brand/subtle`, `bg/brand/accent`, `bg/brand/accent/pressed`, `bg/critical`, `bg/critical/pressed`, `bg/disabled`, `text/onBrand`, `text/onBrandAccent`, `text/onCritical`, `text/brand`, `text/disabled`, `icon/inverse`, `icon/brand`, `icon/action`, `icon/disabled`, `stroke/brand/focus`, `stroke/subtle`, `type/label/lg`, `space/8`, `space/12`, `space/16`, `radius/large`, `stroke/small`, `stroke/medium`, `icon/sm`, `icon/md`.
- **Size:** fill the width minus the surface gutter; minimum height 48 pt; corner `RoundedRectangle(cornerRadius: Wiom.Radius.large, style: .circular)`; Secondary border via `.strokeBorder` (inside).
- **Dynamic Type:** `type/label/lg` scales with its anchor in `typography.md` §3. No line limit; label is `.multilineTextAlignment(.center)` and wraps; the button grows. Check at xxxLarge and accessibility3 that groups stack (§6.1) and nothing clips.
- **VoiceOver:** one element, trait Button, label = the visible text. Icons and spinner `.accessibilityHidden(true)`. Disabled uses `.disabled(true)` (VoiceOver says "dimmed"). Loading: keep the label, add `.accessibilityValue` with the catalog string for "loading", and **ignore activation** while loading (do not use `.disabled`, so it is not read as dimmed). Acknowledge row: one element combining box + label, value checked / not checked, activates the toggle (use `.isButton` plus value for this checkbox row on iOS 16+).
- **Hit area:** ≥ 44 × 44 pt always. Filling CTAs are 48 pt tall by construction. **Inline Tertiary that hugs its text** still gets `.frame(minWidth: 48, minHeight: 48)` + `.contentShape(RoundedRectangle(...))`, and the pressed fill draws in that full shape.
- **Motion:** pressed fill changes instantly, no animation, no scale. Loading swaps instantly (as Android). The spinner keeps rotating under Reduce Motion (D20). Nothing else moves.
- **Safe areas and keyboard:** sticky bar per §7 and D19, attached with `.safeAreaInset(edge: .bottom)`; background `.ignoresSafeArea(.container, edges: .bottom)` so it reaches under the home indicator but not under the keyboard. Mechanics in `layout.md`.
- **Haptics:** none on taps or anywhere else (D21).
- **Not on iOS:** ripple, hover, focus ring (`stroke/brand/focus` and `stroke/critical/focus` as rings), `.alert` / `.confirmationDialog` buttons (D9), SF Symbols (D4), press-scale or opacity "bounce", `minimumScaleFactor` on labels.

```swift
enum WiomButtonType { case primary, secondary, tertiary, destructive, preBooking }
enum WiomButtonState { case `default`, disabled, loading }

struct WiomButtonStyle: ButtonStyle {
    let type: WiomButtonType
    let state: WiomButtonState
    var fills = true                                    // false only for inline Tertiary

    func makeBody(configuration: Configuration) -> some View {
        let pressed = configuration.isPressed && state == .default
        let v = WiomButtonVisuals(type: type, state: state, pressed: pressed) // §3 tables
        let shape = RoundedRectangle(cornerRadius: Wiom.Radius.large, style: .circular)
        configuration.label
            .wiomTextStyle(.labelLg)                // tracking + line height per typography.md
            .foregroundColor(v.label)
            .multilineTextAlignment(.center)
            .opacity(state == .loading ? 0 : 1)           // keeps size while loading
            .padding(.horizontal, Wiom.Spacing.s16)
            .padding(.vertical, Wiom.Spacing.s12)
            .frame(maxWidth: fills ? .infinity : nil)
            .frame(minWidth: 48, minHeight: 48)
            .background(shape.fill(v.fill))
            .overlay { if let b = v.border { shape.strokeBorder(b, lineWidth: Wiom.BorderWidth.medium) } }
            .overlay { if state == .loading { WiomCTAProgressGlyph(tint: v.icon).accessibilityHidden(true) } } // DS helper: 24 pt glyph, 2 pt stroke; not the 32 pt Spinner md
            .contentShape(shape)
    }
}

// Call site: the action is ignored while loading, so a double tap can't fire twice.
Button { guard state == .default else { return }; onRecharge() } label: { Text("Recharge now") }
    .buttonStyle(WiomButtonStyle(type: .primary, state: state))
    .disabled(state == .disabled)
    .accessibilityValue(state == .loading ? Text("a11y.loading") : Text(""))
```

Button pair (exactly two subviews, dismiss then preferred): side by side only if each label fits half the width, else stacked with the preferred (last) action on top. Three-action groups always use a separate vertical stack per §6.

```swift
struct WiomButtonPairLayout: Layout {               // subviews: [dismiss, preferred]
    var spacing: CGFloat = Wiom.Spacing.s12
    private func sideBySide(_ width: CGFloat, _ s: Subviews) -> Bool {
        let half = (width - spacing) / 2
        return s.allSatisfy { $0.sizeThatFits(.unspecified).width <= half } // one-line ideal width
    }
    func sizeThatFits(proposal: ProposedViewSize, subviews s: Subviews, cache: inout ()) -> CGSize {
        let w = proposal.width ?? s.map { $0.sizeThatFits(.unspecified).width }.reduce(0, +) + spacing
        if sideBySide(w, s) {
            let half = ProposedViewSize(width: (w - spacing) / 2, height: nil)
            return CGSize(width: w, height: s.map { $0.sizeThatFits(half).height }.max() ?? 0)
        }
        let full = ProposedViewSize(width: w, height: nil)
        let h = s.map { $0.sizeThatFits(full).height }.reduce(0, +) + spacing * CGFloat(max(s.count - 1, 0))
        return CGSize(width: w, height: h)
    }
    func placeSubviews(in b: CGRect, proposal: ProposedViewSize, subviews s: Subviews, cache: inout ()) {
        if sideBySide(b.width, s) {
            let half = (b.width - spacing) / 2
            for (i, v) in s.enumerated() {
                v.place(at: CGPoint(x: b.minX + CGFloat(i) * (half + spacing), y: b.minY),
                        proposal: ProposedViewSize(width: half, height: b.height))
            }
        } else {
            var y = b.minY
            for v in s.reversed() {                      // preferred action on top
                let h = v.sizeThatFits(ProposedViewSize(width: b.width, height: nil)).height
                v.place(at: CGPoint(x: b.minX, y: y), proposal: ProposedViewSize(width: b.width, height: h))
                y += h + spacing
            }
        }
    }
}
```

VoiceOver order follows subview order; when stacked, wrap the pair in `.accessibilityElement(children: .contain)` and give the preferred button `.accessibilitySortPriority(1)` so it is read first, matching what is on top.
