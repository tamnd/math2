---
tag: ~bc47cab2
kind: example
name: Translating announcement formulas into epistemic logic
msc: ["03B42"]
topics: [CQM9SRN8PM]
audience: research
instance_of: [~0c910f5d]
uses: [~93aa2d58, ~8b9604fb, JS8W7PA6JK]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamic_epistemic_logic
    locator: section Public Events
  - book: isbn:9781402058387
    locator: van Ditmarsch, van der Hoek and Kooi, Dynamic Epistemic Logic, chapter on public announcements
---

## Example

We remove the announcement operators from two formulas with [[the reduction axioms|~93aa2d58]].
Each step replaces a subformula by an equivalent one.
Replacement under $K_a$ is allowed, since $\mathsf{K}$ proves $K_a\alpha \leftrightarrow K_a\beta$ from $\alpha \leftrightarrow \beta$.

First formula: $[!p]K_a q$, "after $p$ is announced, $a$ knows $q$".

1. By the knowledge axiom (part 4), $[!p]K_a q \leftrightarrow (p \to K_a[!p]q)$.
2. By the atom axiom (part 1), $[!p]q \leftrightarrow (p \to q)$.
3. Replacing inside $K_a$ gives $[!p]K_a q \leftrightarrow (p \to K_a(p \to q))$.

So $a$ learns $q$ from the announcement exactly when, if $p$ is true, she already knew that $p$ implies $q$.

Second formula: $[!p][!q]K_a r$.

4. By the composition axiom (part 5), it is equivalent to $[!(p \wedge [!p]q)]K_a r$.
5. By part 1, $[!p]q$ is equivalent to $p \to q$, so $p \wedge [!p]q$ is equivalent to $p \wedge q$.
6. The formula becomes $[!(p \wedge q)]K_a r$.
7. Parts 4 and 1 give $(p \wedge q) \to K_a((p \wedge q) \to r)$.

A check in a model.
Let $W = \set{w, v}$, with $p, q$ true at $w$, $p$ true and $q$ false at $v$, and $R_a = W \times W$.

8. At $w$, $K_a(p \to q)$ fails, since $p \to q$ fails at $v$. So the translation of $[!p]K_a q$ is false at $w$.
9. Directly: announcing $p$ keeps both worlds, and $q$ fails at $v$. So $K_a q$ fails after the announcement, as the translation says.
10. Announcing $p$ and then $q$ leaves only $w$. With $r = q$, the translation $(p \wedge q) \to K_a((p \wedge q) \to q)$ is true, and $a$ knows $q$.

## Remarks

The translation can make formulas exponentially longer, since part 2 and part 4 copy the announced formula.
Announcement logic is exponentially more succinct than epistemic logic for this reason (Lutz 2006).
The translation fails with common knowledge: $[!p]C_G q$ has no reduction of this form.

## Explanations

### L1 human

An announcement formula says what agents know after some news.
The reduction axioms rewrite it as a formula about what they know before the news.
For example, "after hearing $p$, Ann knows $q$" means "if $p$ is true, Ann already knew that $p$ implies $q$".

### L2 human

The method works from the outside in.

1. Push $[!\varphi]$ through $\neg$, $\wedge$ and $K_a$ with parts 2, 3 and 4.
2. Remove it in front of atoms with part 1.
3. Merge two announcements in a row with part 5.

The typical use is to decide a question about announcements by a question in plain epistemic logic.
A trap: $[!p]K_a q$ is not $p \to K_a q$.
The announcement is inside $K_a$ too, as $K_a(p \to q)$.

### L3 human

Rewriting with the axioms from the outside in terminates, but not by induction on length, since part 4 makes formulas longer.
One fix is a complexity measure in which $[!\varphi]\psi$ counts more than every formula its reduction produces.
[[The proof of the reduction theorem|~b6c2785f]] avoids the measure: it translates from the inside out, by recursion on formulas.
