---
tag: V5H6FW6F9M
kind: example
name: Disjunctive syllogism as a logical consequence
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [1HK0VYWTV7]
uses: [H31CS3HK5P, 0F72FK8EKB, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Disjunctive_syllogism
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Logical_consequence
    locator: Semantic consequence
---

## Example

Let $p$ and $q$ be propositional variables.
We show $p \lor q, \; \neg p \models q$.

1. The formulas contain only $p$ and $q$, so there are four truth assignments to check.
2. The premise $\neg p$ is true exactly when $v(p) = 0$, by the truth table of [[negation|029JBBF693]].
3. When $v(p) = 0$, the premise $p \lor q$ is true exactly when $v(q) = 1$, by the truth table of [[disjunction|0F72FK8EKB]].
4. So the only assignment that makes both premises true is $v(p) = 0$, $v(q) = 1$.
5. This assignment gives $q$ the value 1.
6. Hence every assignment that makes both premises true makes $q$ true, and $p \lor q, \; \neg p \models q$.

## Remarks

This argument form is called disjunctive syllogism.
It is a special case of the resolution rule: from the clauses $\set{p, q}$ and $\set{\neg p}$ we get the clause $\set{q}$.
Each premise alone is not enough.
The assignment $v(p) = 1$, $v(q) = 0$ makes $p \lor q$ true and $q$ false, so $p \lor q \not\models q$.
The assignment $v(p) = v(q) = 0$ makes $\neg p$ true and $q$ false, so $\neg p \not\models q$.
This shows that the set of premises matters as a whole: a consequence of a set need not be a consequence of any one member.

## Explanations

### L1 human

The key is in the left pocket or in the right pocket.
It is not in the left pocket.
So it is in the right pocket.
This conclusion is safe because the only way to make both first sentences true is that the key is in the right pocket.

### L2 human

We check the same consequence with a search for a countermodel.

1. A countermodel needs $v(q) = 0$, so that the conclusion is false.
2. It also needs $\bar v(\neg p) = 1$, so $v(p) = 0$.
3. Then $\bar v(p \lor q) = 0$, so the first premise is false.
4. So no countermodel exists, and the consequence holds.

The typical use: in a case analysis, after we exclude all cases but one, the remaining case must hold.
A trap: with "or" read as "exactly one of", the argument "$p \lor q$ and $p$, so $\neg q$" looks valid, but with the inclusive $\lor$ of logic it is not; the assignment $v(p) = v(q) = 1$ is a countermodel.
