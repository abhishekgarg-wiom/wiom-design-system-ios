# English copy rules: Wiom customer app (iOS)

> Source: customer-app-kotlin `claude_context/english_copy_rules.md` (binding there; mirrored here). Owner decision D48, 27 Nov 2026.
> **Binding rule.** Applies to every user-facing English string, new or changed. Existing approved copy is never rewritten by an agent (D39, D49).

## The rule

**Hindi is the source of _intent_, never the source of _words_.**

Read the Hindi to learn what the screen promises or asks. Then write that in English from
scratch. Both strings must produce the same understanding and the same next action:
nothing else about them needs to correspond.

The English reader chose English and has **basic** English. Everyday words, short
sentences, sentence case. If a string reads like a translation, it is wrong.

| Hindi | ❌ Translated | ✅ Written |
|---|---|---|
| `और रिचार्ज कितने दिन का होता है?` | And how many days does a recharge last? | How long is recharge valid for? |
| `अपने घर के पास का लैंडमार्क चुनें` | Choose a landmark near your home | Which place is nearby? |
| `जितने दिन, उतना रिचार्ज` | As many days, that much recharge | Recharge for the days you want |

Watch for the tells: passive voice ("can be used"), dropped articles ("Net Box comes
with…"), and Hindi correlatives (जितना/उतना) that have no English form.

## The product name

**`घर का नेट` is `Ghar ka Net` in English**: names are not translated. Capital G, lower
k, capital N. The other name is **`Wiom`** in English and **`व्योम`** in Hindi (ruled 15 Oct 2026).

The name belongs to **booking**, where the customer is still choosing. After booking
(installation, renewal, migration, support) they know what they have, and plain lowercase
`home net` is right. Never the halfway form: not `home Net`, `Home net`, `Home Net`.

### Capitalising `net`

Capital N only inside a name, or at the start of a line. On its own `net` is an ordinary
noun, like `phone`. Hindi has no upper case, so नेट reads as an everyday word; a capital
adds formality the Hindi never had.

| Where | Case | Example |
|---|---|---|
| Inside a name | **Net** | `Ghar ka Net`, `Net-Box`, `Recharge-wala Net` |
| Starts a sentence or field label | **Net** | `Net name`, `Net charges` |
| Anywhere else | **net** | `Set your net password`, `use the net` |

The box is **`Net-Box`** in English and **`नेट-बॉक्स`** in Hindi: hyphenated in both,
capital N and capital B in English. Ruled 15 Oct 2026; never `Net Box`, `net box` or `नेट बॉक्स`.

The auto-pay feature is **`Autopay`** in English: one word, capital A, no hyphen, including
mid-sentence. Ruled 16 Oct 2026; never `autopay`, `Auto-Pay` or `AutoPay` in copy. In Hindi it is
**`ऑटो-पे`**, hyphenated.

## Say "net", not "internet"

The Hindi says नेट almost everywhere; English follows. Two exceptions: where the Hindi
itself says **इंटरनेट**, and errors about the **phone's own** connectivity.

Only string **values** are copy. Never rename a code identifier, route or analytics name to chase this.

## Fragments and fit

Hindi stacks two-part labels where the second half completes the first; English reads each
half alone. `शुरू करने के लिए` / `पहला रिचार्ज` → "To start" / "first recharge" leaves a
dangling half. Restructure so each stands: **"Starting cost"**.

English runs longer. For titles, CTAs, chips and single-line rows, keep close to the
Hindi's visual length: shorten the English rather than let it wrap into the element below.
Real breakage: a two-line cost title pushed its link under the CTA.

Use what English has and Hindi doesn't: `1-day recharge` / `7-day recharge` read correctly,
so English needs no singular/plural fork where Hindi does. Punctuation is per-language:
Hindi's dash is often a comma in English, and `।` has no equivalent.

## Where the pairs live

Hindi and English move together:

1. **The shared string catalog** (`Localizable.xcstrings`, same keys as Android): the Hindi and English values of a key change in the same edit.
2. **Server-driven pages**: SDUI JSON `strings.hi` / `strings.en`.

No hard-coded UI text in code (`Text("…")` with a literal); every string comes from the catalog or the server.

## Checklist

- [ ] Written for an English reader, not translated: stands alone with zero Hindi knowledge
- [ ] Same intent, promise and next action as the Hindi; nothing added or dropped
- [ ] `Ghar ka Net` while booking, plain `home net` after; bare `net` lowercase unless it
      starts the line or sits in a name; `Net-Box` / `नेट-बॉक्स` is hyphenated in both languages
- [ ] `Autopay` / `ऑटो-पे` spelled the ruled way, mid-sentence included
- [ ] Says "net", not "internet", unless the Hindi says इंटरनेट
- [ ] No orphan fragment; fits its frame without wrapping
- [ ] Hindi and English updated together, and the same label spelled identically everywhere
- [ ] Fits the component's D44 target if the copy AI drafted it; approved by Abhishek Garg (D49)

## Server copy and tests

- When the server sends copy (`info.message.hi` / `.en`), show it as sent for the current language; never build copy by parsing a raw `msg`.
- Changing copy means regenerating the expected-copy test files; tests read copy from the app.
- Hindi rules and the full audit checklist: [copy-rules.md](copy-rules.md) (D52).
