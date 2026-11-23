# Writing playbook (iOS customer app)

**Contents:** 1 Voice · 2 Screen patterns · 3 Buttons · 4 Casing · 5 Length limits · 6 Inputs · 7 Words to avoid · 8 Paused service tone · 9 Common phrases

**All examples are illustrative.** Real copy comes from the string catalog, which iOS and Android share: Hindi written first, English written separately (not translated word for word). Never ship an example from this file as UI text.

---

## 1. Voice

Wiom talks like a helpful neighbour who knows technology, explains it simply, and never makes you feel slow.

| Attribute | Means | Example (illustrative) |
|---|---|---|
| Enthusiastic | Energy, never hype or pressure | "आपका घर का नेट तैयार है" |
| Sincere | Honest; no hidden catches; never promise what the product doesn't give | State exactly what is and isn't refundable |
| Casual | Neighbour, not office | "आइए, शुरू करते हैं" not "प्रक्रिया शुरू करें" |
| Respectful | Values the user's time | "चिंता न करें" before explaining a problem |
| Dreamer | What good net makes possible | Study, work, TV, calls |

## 2. Screen patterns

**Form step**
```
Title:    what this step is, benefit first      "अपना पता बताइए"
Support:  why it matters                         "नेट यहीं लगाया जाएगा"
Fields:   labels + example placeholders
Button:   names the next step                   "WiFi का नाम रखें"
```

**Payment**
```
Amount:   large and exact, with what it pays for
Terms:    what is refundable and what is not, in the product's real terms
Trust:    UPI / NPCI marks where they apply
Options:  equal weight; never force one path
Help:     always visible at the bottom
```

**Payment received / commit done** (calm confirmation, no celebration: T-01)
```
Hero:     check mark + exact amount
Proof:    receipt with IDs, copyable
Next:     numbered next steps with time estimates
```

**Net is live** (the journey's one delight moment)
```
Hero:     the net works, said plainly
Delight:  a visual / motion moment, not a "बधाई" string
```

**Error**
```
Say what happened (neutral words)
Reassure first: is the money or data safe? Only say so if it is true
Blame the system, never the user
Retry button + a no-pressure way out
Specific help for this case
```

**Dialogs:** title up to 40 grapheme clusters, body up to 100; empathetic and solution-first.
**Microcopy and tooltips:** up to 50 grapheme clusters.
**Notifications:** title up to 40, body up to 100; clear, never alarming.

## 3. Buttons

- 2 to 3 words is best; 5 at most. Statements, never questions.
- Two context types: **next screen** ("प्लान कन्फर्म करें") or **this screen** ("OTP वेरीफाई करें").
- A pair: Primary = the forward action; Secondary = a safe later option that never feels like a punishment ("बाद में करें").

| Avoid | Why |
|---|---|
| "आगे बढ़ें" alone | Forward to what? |
| A full sentence | Too long; wraps at large text |
| Threats ("अभी करें नहीं तो…") | Pressure; breaks the no-pressure doctrine |
| English-only labels on a Hindi screen ("Continue") | Hindi first |
| "?" | Buttons are statements |

## 4. Casing

- **Hindi has no case.** Nothing to do.
- **English uses sentence case everywhere:** titles, buttons, labels, placeholders, cards. "Cancel booking", "Change address", "Know more". Proper nouns and acronyms keep their capitals (Wiom, WiFi, OTP, UPI).
- Never Title Case, camelCase or ALL CAPS for UI text.

(This replaces the old "1 to 3 words Title Case" rule, which the app's English copy doesn't follow and which has no meaning in Devanagari.)

## 5. Length limits

Counted in **grapheme clusters** (what the eye reads as one letter: "क्षि" is one; Swift `String.count`), not bytes or code points.

| Element | Limit |
|---|---|
| Screen title | 40 to 50 |
| Button | 2 to 3 words (max 5) |
| Dialog title | 30 to 40 |
| Dialog body | 80 to 100 |
| Tooltip / microcopy | 50 |
| Notification title | 30 to 40 |
| Notification body | 80 to 100 |

Component skills may set tighter limits (chips, badges, toasts); theirs win.

## 6. Inputs

```
Label:        what the field is
Placeholder:  an EXAMPLE of a valid value, never an instruction
Helper:       why it matters or the format (below the field)
Icon:         at the start of the field
```

| Field | Label | Placeholder (example) | Helper |
|---|---|---|---|
| Name | आपका नाम | राम कुमार | none |
| Phone | फ़ोन नंबर | 98765 43210 (after the fixed +91) | इसी नंबर पर आगे की जानकारी मिलेगी |
| Address | पूरा पता | मकान नं 12, गली 4, लक्ष्मी नगर | none |
| Pincode | पिनकोड | 110092 | 6 अंकों का |
| WiFi name | WiFi का नाम | Ramesh_Home | यह नाम आस-पास सबके फ़ोन में दिखेगा |
| Password | पासवर्ड | 8 या ज़्यादा अक्षर | अक्षर और नंबर मिलाएं |

All illustrative. Keyboard per field: `wiom-ios-input-fields` §6.

## 7. Words to avoid

| Don't use | Why | Instead |
|---|---|---|
| कृपया | Copy-lane forbidden word (formal, distant) | Say the action directly: "दोबारा कोशिश करें" |
| ध्यान दें | Forbidden: alarming | Say the fact |
| बधाई | Forbidden; and no celebration before the net works | A calm confirmation; the delight moment is visual |
| जल्दी करें, countdowns, "Limited time" | Forbidden: pressure | Nothing; let the user decide |
| Oops | Forbidden | Say what happened |
| रिन्यूअल, बिल | Customer surfaces say रिचार्ज | रिचार्ज |
| WiFi | The glossary keeps WiFi in English | WiFi |
| इंटरनेट (in UI copy) | Customer surfaces say नेट | नेट, घर का नेट |
| Mbps, broadband, FUP, latency | Telecom jargon | What the user can do with it |
| A refund promise | Only where the product truly refunds; the booking fee is **not** returned on cancel | The product's real terms |

The live app still has some of these (for example कृपया); they are fixed in the shared string catalog, never on one platform only.

## 8. Paused or recovering service

- No urgency, no countdowns, no "hurry".
- No red: status in the info colour family (`text/info`, `bg/info/subtle`).
- No gain/loss framing; recharge and the other option are equally valid.
- A calm line such as "कोई जल्दी नहीं है, अपनी सुविधा से फ़ैसला करें" (illustrative).

## 9. Common phrases

| English | Hindi | Tone |
|---|---|---|
| Let's start | आइए, शुरू करते हैं | Warm |
| Excellent | बहुत बढ़िया | Encouraging (not at payment) |
| Don't worry | चिंता न करें | Reassuring |
| Your money is safe | आपका पैसा सुरक्षित है | Trust: **only when true** |
| Not your fault | आपकी कोई गलती नहीं है | No blame |
| Talk to us | हमसे बात करें | Help is here |
| At your convenience | अपनी सुविधा से | No pressure |
| Deposit received | जमा राशि मिल गई | Only for a real refundable deposit |

Full term list: [`glossary.md`](glossary.md).
