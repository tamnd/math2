---
tag: T5BG7Y4J0T
kind: counterexample
name: Formal fallacies
aliases: [formal-fallacy, deductive-fallacy, logical-fallacy-formal]
msc: ["03B05", "03B10"]
topics: [PM1AYWABA7]
audience: school
uses: [QPD3X471Q1, 0NMG7W7Q11, 05RSK4Q657, 0GHS47PDAQ, 0MSRQHCNN9, 1HK0VYWTV7, FWHBT4HABW]
sources:
  - url: https://en.wikipedia.org/wiki/Formal_fallacy
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Affirming_the_consequent
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Denying_the_antecedent
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Quantifier_shift
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
---

## Counterexample

"If it rains, the ground is wet; the ground is wet; so it rained."
The argument sounds right, but a garden sprinkler on a dry day makes both premises true and the conclusion false.
A formal fallacy is an argument form like this one: it looks like a [[rule of inference|QPD3X471Q1]], but it is not valid.
A form is valid when every interpretation that makes all premises true also makes the conclusion true, which is the relation of [[logical consequence|1HK0VYWTV7]].
So one interpretation with true premises and a false conclusion, a [[countermodel|FWHBT4HABW]], refutes the form.

We refute three standard fallacies.
Affirming the consequent concludes $p$ from $p \to q$ and $q$.
Denying the antecedent concludes $\neg q$ from $p \to q$ and $\neg p$.
The quantifier shift concludes $\exists y \, \forall x \, P(x, y)$ from $\forall x \, \exists y \, P(x, y)$.
For the first two we use the [[truth table|05RSK4Q657]] of [[material implication|0NMG7W7Q11]]:

| row | $p$ | $q$ | $p \to q$ | $\neg p$ | $\neg q$ |
|---|---|---|---|---|---|
| 1 | T | T | T | F | F |
| 2 | T | F | F | F | T |
| 3 | F | T | T | T | F |
| 4 | F | F | T | T | T |

1. Affirming the consequent.
   In row 3, $p \to q = \mathrm{T}$ and $q = \mathrm{T}$, so both premises are true.
   In the same row $p = \mathrm{F}$, so the conclusion is false, and row 3 is a countermodel.
2. Denying the antecedent.
   In row 3, $p \to q = \mathrm{T}$ and $\neg p = \mathrm{T}$, so both premises are true.
   In the same row $\neg q = \mathrm{F}$, so row 3 is a countermodel to this form too.
3. The quantifier shift.
   Take the domain $D = \{0, 1\}$ and let $P(x, y)$ mean $x = y$.
   For $x = 0$ the element $y = 0$ works, and for $x = 1$ the element $y = 1$ works, so $\forall x \, \exists y \, P(x, y)$ is true.
4. No single $y$ works for both values of $x$.
   The element $y = 0$ fails for $x = 1$, because $1 \neq 0$, and $y = 1$ fails for $x = 0$.
   So $\exists y \, \forall x \, P(x, y)$ is false, and this structure is a countermodel.

By steps 1 to 4, none of the three forms is a rule of inference.
In the rain example, row 3 is the dry day with the sprinkler: "it rains" is false and "the ground is wet" is true.

## Remarks

### Validity is about form

An argument of an invalid form can still have true premises and a true conclusion.
In row 1, both premises of affirming the consequent and its conclusion $p$ are true.
The form is invalid anyway, because row 3 exists, and a proof that relies on the form proves nothing.
Mathematical instances of the three forms are on the pages [[affirming the consequent is not a valid deduction|2XXTDXK1ZC]], [[denying the antecedent is not a valid deduction|6FH1TVDXGS]] and [[quantifier shift fallacy|CRW82NARQV]].
The errors that these forms cause in written proofs are on the page [[affirming the consequent and denying the antecedent|J7KFCFQRBT]].

### The valid forms next door

Each fallacy is a valid rule with the roles of the parts exchanged.
[[Modus ponens|0Y0MQYST0M]] concludes $q$ from $p \to q$ and $p$: only row 1 makes both premises true, and $q$ is true there.
[[Modus tollens|32AQPJQQAM]] concludes $\neg p$ from $p \to q$ and $\neg q$: only row 4 makes both premises true, and $\neg p$ is true there.
The reverse quantifier shift, from $\exists y \, \forall x \, P(x, y)$ to $\forall x \, \exists y \, P(x, y)$, is valid, as the page on the [[order of quantifiers|0FYQMKFE77]] explains.

### More fallacies of the same kind

[[Affirming a disjunct|3X34TM3SRT]] concludes $\neg q$ from $p \lor q$ and $p$, and the row $p = q = \mathrm{T}$ refutes it.
Generalizing from one instance concludes $\forall x \, P(x)$ from $P(a)$.
On $D = \{0, 1\}$ with $a = 0$ and $P$ true only at $0$, the premise is true and the conclusion is false.
Merging two witnesses concludes $\exists x \, (P(x) \land Q(x))$ from $\exists x \, P(x)$ and $\exists x \, Q(x)$.
On $D = \{0, 1\}$ with $P$ true only at $0$ and $Q$ true only at $1$, the premises are true and the conclusion is false.
The same $P$ and $Q$ refute the step from $\forall x \, (P(x) \lor Q(x))$ to $\forall x \, P(x) \lor \forall x \, Q(x)$.

### What repairs the forms

Add the premise $q \to p$, and affirming the consequent becomes modus ponens with $q \to p$; row 3 makes this new premise false.
The same premise repairs denying the antecedent, because $\neg p$ and $q \to p$ give $\neg q$ by modus tollens.
So both fallacies become valid when the implication holds in both directions, which is why a [[biconditional|0S6GMNJ62Y]] can be used either way.
The quantifier shift needs a domain with at least two elements to fail.
On a domain $\{a\}$ with one element, both quantified sentences say $P(a, a)$.

### Formal and informal fallacies

A formal fallacy is an error of form, and a countermodel detects it without any reference to the meaning of $p$, $q$ or $P$.
An informal fallacy is an error of content, language or relevance, and its form can be valid.
[[Circular reasoning|JPHE53PABT]] has the valid form "from $p$, conclude $p$", and its error is that the premise is the claim to be proved.
Equivocation uses one word in two meanings, so the argument does not have the form that it seems to have.
Most [[mathematical fallacies|S2BW0FDHV8]], such as a hidden division by zero, are false steps of content, not invalid forms.

### Try it

Is "from $p \to q$ and $\neg q$, conclude $\neg p$" a fallacy?
No, it is modus tollens, and only row 4 makes both premises true, where $\neg p$ holds.

Refute "from $\exists x \, P(x)$, conclude $\forall x \, P(x)$" on the domain $\{1, 2\}$ with $P(x)$ meaning "$x$ is even".
The premise holds with $x = 2$, and the conclusion fails at $x = 1$.

## Explanations

### L1 human

"If it rains, the street is wet; the street is wet; so it rained" sounds right, but it is wrong.
A water truck can make the street wet on a dry day.
That dry day with a wet street is the counterexample: everything the argument assumes is true, and its conclusion is false.
An argument pattern with such a counterexample is a formal fallacy.
"If it rains, the street is wet; it does not rain; so the street is dry" fails on the same day.

### L2 human

Is the form "from $p \to q$, $q \to r$ and $r$, conclude $p$" valid?
Search for a countermodel, starting from what it must contain.
The conclusion must be false, so $p = \mathrm{F}$, and the third premise must be true, so $r = \mathrm{T}$.
With $r = \mathrm{T}$ the premise $q \to r$ is true for both values of $q$, and with $p = \mathrm{F}$ the premise $p \to q$ is true for both values of $q$.
So $p = \mathrm{F}$, $q = \mathrm{F}$, $r = \mathrm{T}$ makes every premise true and the conclusion false.
The form is invalid, since it affirms the consequent of the chain $p \to r$.
This search is the standard method: begin from a false conclusion and fill in values that make each premise true.
If every branch of the search fails, the form is valid, and if one branch succeeds, that branch is the countermodel.
Watch out: testing only the cases that come to mind, such as row 1, can make an invalid form look valid.

### L3 human

Validity of a propositional form is decidable, because a form with $n$ variables has $2^n$ rows and a countermodel is one of them.
For first-order forms, [[Gödel's completeness theorem|WQ1ZE255SF]] says that a form which a complete proof system cannot derive has a countermodel, so "formal fallacy" means the same on the semantic side and on the proof side.
No algorithm decides first-order validity, so a search for a countermodel need not end.
Some invalid first-order forms have only infinite countermodels.
For example, "every $x$ has some $y$ with $R(x, y)$" and "$R$ is transitive" do not give "some $x$ has $R(x, x)$", and $\mathbb{N}$ with $<$ is a countermodel.
Every countermodel is infinite: in a finite one, a chain $x_0, x_1, x_2, \dots$ with $R(x_i, x_{i+1})$ repeats an element, and transitivity then gives $R(x_i, x_i)$.
