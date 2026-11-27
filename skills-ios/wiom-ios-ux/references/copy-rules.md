# Copy rules: Hindi and English

**Required for any user-facing copy (D52).** These rules are what the Wiom live copy audit checks the shipped app against (checks LC-A to LC-S), so copy that follows them passes the audit.

Sources:
- the copy audit's checks;
- the copy agent's checks C1 to C38;
- tone rules R1 to R10 and pattern rules R1 to R29;
- the locked rulings T-01 and T2;
- the glossary usage rules;
- the shipped app's binding contract: `CLAUDE.md` rule 6, UI-06 and `english_copy_rules.md`, in `customer-app-kotlin`;
- the copy-audit fixes (PR #473 and the second round), where the word choices come from.

English-only rules live in [english-copy-rules.md](english-copy-rules.md) (D48).

**Must** = a locked rule; breaking it fails the audit (S1). **Should** = a style or draft rule (S2); fix it when you touch the string.

## 1. Who writes copy

- Approved copy in the app is never changed by an agent (D39). An agent may only propose a change.
- When the system needs new copy, the copy AI drafts it within these rules and the D44 length targets, and Abhishek Garg approves it (D49).
- Pick words by counted precedent in the app, not taste. When two words mean the same thing, use the one the app already uses more (for example तारीख 7 vs तिथि 3; वापस 34 vs वापिस 3).

## 2. Both languages, one meaning (must)

| Check | Rule |
|---|---|
| LC-A parity | Every string exists in Hindi **and** English. A key in one language only is a defect. |
| LC-H figures | Placeholders and every ₹ amount, day count and date match across the pair. The English never drops a figure the Hindi shows, or the reverse. |
| LC-B script | No Devanagari in an English string. No Latin word in a Hindi string when the glossary has a Hindi word for it. |
| LC-P no path | No Hindi literal outside the string catalog. Copy hard-coded in a view has no English path. |
| LC-R empty | No empty string on a slot that renders. Exception: two languages split a sentence differently, for example a Hindi suffix with no English twin. |
| UI-06 storage | No literal text in code. Hindi and English keys move together in the shared string catalog, and in server-driven JSON (`strings.hi` / `strings.en`). |
| Server copy | When the server sends copy (`info.message.hi` / `.en`), show it as sent for the current language. Never build copy by parsing a raw `msg`. |
| Tests | Changing copy means regenerating the expected-copy test files. Tests read copy from the app; never paste copy into a test. |

## 3. Hindi voice (must)

| Check | Never | Instead |
|---|---|---|
| LC-D forbidden words (T2) | कृपया · ध्यान दें · बधाई · जल्दी करें · Oops | Say the fact or the next step |
| LC-D2 English equivalents (should) | please · kindly · congratulations · hurry · limited time · last chance | The same, in plain English |
| LC-F celebration (T-01) | बधाई, शाबाश, बहुत बढ़िया, "Great!", 🎉 🥳 🎊 before the service works | A calm confirmation: "पेमेंट मिल गया।" Confirm, never congratulate |
| LC-F pressure | Countdowns, scarcity, "limited time", fear | The factual condition |
| LC-G advisory | करना चाहिए, ध्यान रखें, "you should", "make sure" | State the consequence |
| LC-G formal address | श्रीमान, महोदय | आप, आपका |
| LC-E term (glossary rule 7) | रिन्यूअल | रिचार्ज |
| LC-C English inside Hindi | English words, for example "Terms & Conditions", "App", "Welcome" | Hindi: नियम और शर्तें, ऐप, वेलकम. Keep only OTP, GST, ISP, WiFi, WhatsApp, ID, UPI, QR, SMS and the glossary's "Keep English" entries |
| N1 money screens | धैर्य रखें as a title | Say what is happening: "पेमेंट चेक हो रहा है" |

## 4. Plain spoken Hindi (should)

Use the spoken word (LC-L). These swaps come from the audit fixes:

| Avoid | Use |
|---|---|
| विफल, असफल | नहीं हो सका / नहीं हो पाया |
| स्थिति | स्टेटस |
| विवरण | जानकारी |
| प्रयास, पुनः | कोशिश, दोबारा |
| आवश्यक | ज़रूरी |
| शुल्क | फ़ीस |
| तिथि | तारीख |
| देय (कुल देय) | भुगतान (कुल भुगतान) |
| द्वारा | से / पर |
| सूचित कर दिया जाएगा | बता देंगे |
| OTP दोबारा प्राप्त करें | OTP दोबारा भेजें |
| एवं | और |
| इत्यादि | वगैरह |
| वापिस | वापस |
| प्रतीक्षा, त्रुटि, सत्यापन | इंतज़ार, दिक्कत, जाँच |

- Spelling: इलाका / इलाके, वजह (no nukta). Check verb agreement (हैं for plural).
- **Comprehension (R7):** a 10-year-old understands it, and it reads on its own in about 10 seconds.
- Shorter is better: "मेरे इलाक़े में घर का नेट कब तक आएगा?" became "घर का नेट कब आएगा?".

## 5. Shape by surface (pattern rules R1 to R11)

| Surface | Shape | Example (illustrative) |
|---|---|---|
| Badge | `[state]` only | नहीं हो सका |
| Banner | `[state] + [effect]` | रिचार्ज 2 दिन में खत्म होगा |
| CTA | `[verb] + करें`, **5 words max, 3 ideal**. English: Title Case up to 3 words, sentence case from 4 | रिचार्ज करें |
| Chat CTA | The user's own reply, not a command (exempt from `[verb] + करें`) | हाँ, यही पता है |
| Transaction row | `[type] + [reference]` | रिचार्ज · 12 नवंबर |
| Summary | `[magnitude]` only | ₹599 |
| Consequence | `[what will happen]` | नेट 2 दिन बाद बंद हो जाएगा |
| Field label | `[what this number is]` | मोबाइल नंबर |
| Blocked reason | `[fact] + [timing if known]` | आपके इलाके में अभी नहीं |
| Success toast | `[what happened]` | पेमेंट मिल गया |
| Failure toast | `[what failed]` | पेमेंट नहीं हो सका |
| Empty state | Factual, neutral | अभी कोई बिल नहीं है |

- No explanation on a badge, CTA or banner (R6). A chat line or document may explain.
- English is sentence case: "Available coupons", "Bill summary", "Total payable".

## 6. Same thing, same words

- **Same state, same string** (R15, R16, LC-M) on every surface, unless an override is declared.
- **Glossary first** (R18a). If the glossary has no word, reuse the word already used for that meaning (R18b).
- **One retry label:** **दोबारा कोशिश करें / Try again**.
- **Phone offline:** **इंटरनेट से कनेक्ट करके दोबारा कोशिश करें / No internet connection on your phone.** This is the one place इंटरनेट is right: the phone's own connection.
- **Names:**
  - व्योम / Wiom, never WIOM;
  - व्योम ऐप, never "Wiom App";
  - नेट-बॉक्स / Net-Box;
  - ऑटो-पे / Autopay;
  - घर का नेट / Ghar ka Net while booking, home net after (see `english-copy-rules.md`).

## 7. Length and fit (D44, R20, LC-J)

- Length limits in the skills are targets for drafted copy. Under 10% over: rewrite shorter. 10% or more over: must rewrite, or ask.
- English must not run much longer than its Hindi sibling on a CTA, title, chip, badge or single-line row.
- The UI still grows; it never truncates where a skill says grow.
- Check at the largest text size: the audit rendered every changed string at 2x font with zero clipping.

## 8. Chat lines (draft rules, should)

Every chat line passes all five (LC-N):
1. It reduces uncertainty.
2. It reflects the real system state.
3. It creates no obligation.
4. It cannot read as a sales push.
5. The customer can say what happens next.

Never claim a state, time or outcome the backend can't confirm (LC-O, Operational Honesty).

## 9. Before you submit copy

- [ ] Hindi and English both exist, mean the same, show the same figures (§2)
- [ ] None of the §3 words; no celebration, pressure or advice
- [ ] Spoken Hindi from §4; passes the 10-second read
- [ ] Shape matches the surface (§5); CTA 5 words max
- [ ] Same state uses the same string; names spelled as §6
- [ ] English follows `english-copy-rules.md` (written, not translated)
- [ ] Fits at large text sizes; length within the D44 target
- [ ] New copy is a proposal for approval (D49); approved copy is not changed

**Known clash:** the glossary maps "Payable" to देय. The app now uses भुगतान (audit fix). The glossary is owned by Ashish, so this is raised as a clash (LC-CONFLICT) rather than edited.
