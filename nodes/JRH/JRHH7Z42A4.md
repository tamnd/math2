---
tag: JRHH7Z42A4
kind: example
name: Translating announcement formulas into epistemic logic
msc: ["03B42"]
topics: [CQM9SRN8PM]
audience: research
instance_of: [9465T2PWZT]
uses: [MFGHDHGV1D, EA34W4ERRE, JS8W7PA6JK]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamic_epistemic_logic
    locator: section Public Events
  - book: isbn:9781402058387
    locator: van Ditmarsch, van der Hoek and Kooi, Dynamic Epistemic Logic, chapter on public announcements
---

## Example

"After $p$ is announced, Ann knows $q$" sounds like a statement about the future, but it is equivalent to a statement about what Ann knows now.
We find that statement with [[the reduction axioms|MFGHDHGV1D]] of [[public announcement logic|9465T2PWZT]], and then check it in a model.
Each step replaces a subformula by an equivalent one.
Replacement under $K_a$ is allowed, since [[the logic K|JS8W7PA6JK]] proves $K_a\alpha \leftrightarrow K_a\beta$ from $\alpha \leftrightarrow \beta$.

### One announcement

Start with $[!p]K_a q$.
The knowledge axiom, part 4, gives $[!p]K_a q \leftrightarrow (p \to K_a[!p]q)$.
The atom axiom, part 1, gives $[!p]q \leftrightarrow (p \to q)$.
Replacing inside $K_a$ gives the following.
$$[!p]K_a q \leftrightarrow (p \to K_a(p \to q)).$$
So Ann learns $q$ from the announcement exactly when, if $p$ is true, she already knew that $p$ implies $q$.

### Two announcements

Next take $[!p][!q]K_a r$.
The composition axiom, part 5, makes it equivalent to $[!(p \wedge [!p]q)]K_a r$.
By part 1, $[!p]q$ is equivalent to $p \to q$, so $p \wedge [!p]q$ is equivalent to $p \wedge q$, and the formula becomes $[!(p \wedge q)]K_a r$.
Parts 4 and 1 then give $(p \wedge q) \to K_a((p \wedge q) \to r)$.

### A check in a model

Let $W = \{w, v\}$, with $p$ and $q$ true at $w$, $p$ true and $q$ false at $v$, and $R_a = W \times W$.
At $w$, $K_a(p \to q)$ fails, since $p \to q$ fails at $v$, so the translation of $[!p]K_a q$ is false at $w$.
Directly, announcing $p$ keeps both worlds, and $q$ fails at $v$, so $K_a q$ fails after the announcement, as the translation says.
Announcing $p$ and then $q$ leaves only $w$.
With $r = q$, the translation $(p \wedge q) \to K_a((p \wedge q) \to q)$ is true at $w$, and indeed Ann knows $q$ in the one-world model.

## Remarks

The translation can make formulas exponentially longer, since parts 2 and 4 copy the announced formula.
For this reason announcement logic is exponentially more succinct than [[epistemic logic|EA34W4ERRE]], as Lutz showed in 2006.
The method stops at common knowledge: $[!p]C_G q$ has no reduction of this form.

## Explanations

### L1 human

An announcement formula says what agents know after some news.
The reduction axioms rewrite it as a formula about what they know before the news.
For example, "after hearing $p$, Ann knows $q$" means "if $p$ is true, Ann already knew that $p$ implies $q$".

### L2 human

The method works from the outside in.
Push $[!\varphi]$ through $\neg$, $\wedge$ and $K_a$ with parts 2, 3 and 4, remove it in front of atoms with part 1, and merge two announcements in a row with part 5.
The typical use is to decide a question about announcements by a question in plain epistemic logic.
Watch out: $[!p]K_a q$ is not $p \to K_a q$, because the announcement also goes inside $K_a$, where it becomes $K_a(p \to q)$.

### L3 human

Rewriting with the axioms from the outside in terminates, but not by induction on length, since part 4 makes formulas longer.
One fix is a complexity measure in which $[!\varphi]\psi$ counts more than every formula its reduction produces.
[[The proof of the reduction theorem|NFFFDP1TK6]] avoids the measure, because it translates from the inside out, by recursion on formulas.
