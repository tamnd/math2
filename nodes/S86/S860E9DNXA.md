---
tag: S860E9DNXA
kind: example
name: Box distributes over conjunction in K
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [D1TJYZZDCY]
uses: [D1TJYZZDCY, JS8W7PA6JK, G989VP2NGP, 05006AJ7DZ, 0Y0MQYST0M, NGHWZ9Y7ZV]
sources:
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Example

We derive the following equivalence in the [[normal modal logic|D1TJYZZDCY]] $\mathsf{K}$:
$$\vdash \square(p \wedge q) \leftrightarrow (\square p \wedge \square q).$$
The tools are [[tautology|05006AJ7DZ]] instances, the axiom $\mathrm{K}$, [[modus ponens|0Y0MQYST0M]] (MP) and [[necessitation|G989VP2NGP]] (Nec).
We first prove the direction from left to right.

1. $(p \wedge q) \to p$ is a tautology.
2. $\square((p \wedge q) \to p)$ follows by Nec from line 1.
3. $\square((p \wedge q) \to p) \to (\square(p \wedge q) \to \square p)$ is an instance of $\mathrm{K}$.
4. $\square(p \wedge q) \to \square p$ follows by MP from lines 2 and 3.
5. $\square(p \wedge q) \to \square q$ follows in the same way from the tautology $(p \wedge q) \to q$.
6. $\square(p \wedge q) \to (\square p \wedge \square q)$ follows from lines 4 and 5 by the tautology $(\alpha \to \beta) \to ((\alpha \to \gamma) \to (\alpha \to \beta \wedge \gamma))$ and MP twice.

Then we prove the direction from right to left.

7. $p \to (q \to (p \wedge q))$ is a tautology.
8. $\square(p \to (q \to (p \wedge q)))$ follows by Nec from line 7.
9. $\square p \to \square(q \to (p \wedge q))$ follows by the instance of $\mathrm{K}$ for line 8 and MP.
10. $\square(q \to (p \wedge q)) \to (\square q \to \square(p \wedge q))$ is an instance of $\mathrm{K}$.
11. $\square p \to (\square q \to \square(p \wedge q))$ follows from lines 9 and 10 by chaining.
12. $(\square p \wedge \square q) \to \square(p \wedge q)$ follows from line 11 by propositional logic, and with line 6 it gives the equivalence.

For the diamond, substitute $\neg p$ and $\neg q$ for $p$ and $q$, and use the rule RE of [[normal modal logic K|JS8W7PA6JK]] on $\neg(p \vee q) \leftrightarrow (\neg p \wedge \neg q)$.
Negating both sides gives $\vdash \lozenge(p \vee q) \leftrightarrow (\lozenge p \vee \lozenge q)$.

## Remarks

In every normal modal logic the box commutes with conjunction, and the diamond commutes with disjunction.

The box does not commute with disjunction: $\square(p \vee q) \to (\square p \vee \square q)$ is not a theorem of $\mathsf{K}$.
It fails at world $1$ of [[truth sets in a three-world Kripke model|6JXBZ2C9B4]], and soundness turns this into non-derivability.

For the diamond and conjunction only one direction holds: $\vdash \lozenge(p \wedge q) \to (\lozenge p \wedge \lozenge q)$, by the rule RM for the diamond.
The converse fails on the model with $W = \{ 1, 2, 3 \}$, $R = \{ (1, 2), (1, 3) \}$, $V(p) = \{ 2 \}$ and $V(q) = \{ 3 \}$.
There $\lozenge p$ and $\lozenge q$ are true at $1$, but no successor of $1$ has both $p$ and $q$, so $\lozenge(p \wedge q)$ is false at $1$.

## Explanations

### L1 human

"Necessarily, it rains and it is cold" means the same as "necessarily it rains, and necessarily it is cold".
This works because "necessarily" means "in every possible situation", and "every" passes through "and".
It does not pass through "or".
In each situation it may rain or be cold, with rain in one situation and cold in another.
Then neither "necessarily it rains" nor "necessarily it is cold" holds.

### L2 human

We check the result in a [[Kripke model|NGHWZ9Y7ZV]].
The formula $\square(p \wedge q)$ is true at $w$ when every successor of $w$ has both $p$ and $q$.
That is the same as saying that every successor has $p$ and every successor has $q$, which is $\square p \wedge \square q$.
So the semantic check agrees with lines 6 and 12.
For disjunction, "every successor has $p$ or $q$" does not give "every successor has $p$" or "every successor has $q$".
The typical use of the law is to move boxes in and out of conjunctions during derivations, for example in the proof of the [[truth lemma|NM4CB7QAYT]].
Watch out: the dual for the diamond is disjunction, not conjunction, so $(\lozenge p \wedge \lozenge q) \to \lozenge(p \wedge q)$ is not a theorem.
