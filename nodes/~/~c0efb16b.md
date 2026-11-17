---
tag: ~c0efb16b
kind: example
name: An unsatisfiable set from modus ponens
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
not_instance_of:
  - target: QN7M1JCGT9
    note: every assignment that makes p and p → q true makes q true, so it makes ¬q false, and no assignment makes all three members true
uses: [~41f42e3d, 0NMG7W7Q11, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Satisfiability
    locator: Reduction of validity to satisfiability
---

## Example

Let $\Gamma = \set{p, \; p \to q, \; \neg q}$.
We show that $\Gamma$ is unsatisfiable.

1. Suppose that a truth assignment $v$ satisfies $\Gamma$.
2. Then $v(p) = 1$, because $p \in \Gamma$.
3. Then $v(q) = 1$, because $\bar v(p \to q) = 1$ and an [[implication|0NMG7W7Q11]] with a true antecedent and a false consequent is false.
4. Then $\bar v(\neg q) = 0$ by the truth table of [[negation|029JBBF693]], so $v$ does not satisfy $\neg q \in \Gamma$.
5. This contradicts step 1, so no assignment satisfies $\Gamma$.

## Remarks

Each member alone is satisfiable, and so is each pair of members: $\set{p, p \to q}$ by $v(p) = v(q) = 1$, $\set{p, \neg q}$ by $v(p) = 1$, $v(q) = 0$, and $\set{p \to q, \neg q}$ by $v(p) = v(q) = 0$.
So the failure lies only in the three members together.
The set is the set of premises $\set{p, p \to q}$ with the negated conclusion $\neg q$ added, so its unsatisfiability is the same fact as $p, \; p \to q \models q$, which is [[modus ponens as a consequence|~3c1e0885]].
In clause form the set is $\set{p}$, $\set{\neg p, q}$, $\set{\neg q}$, and two steps of resolution derive the empty clause.

## Explanations

### L1 human

"The alarm rings."
"If the alarm rings, the dog barks."
"The dog does not bark."
These three sentences cannot all be true: the first two make the dog bark, and the third says it does not.

### L2 human

We confirm the result with a truth table on $p$ and $q$.

1. Row $v(p) = 1$, $v(q) = 1$: the member $\neg q$ is false.
2. Row $v(p) = 1$, $v(q) = 0$: the member $p \to q$ is false.
3. Row $v(p) = 0$, $v(q) = 1$: the member $p$ is false.
4. Row $v(p) = 0$, $v(q) = 0$: the member $p$ is false.
5. Every row makes some member false, so $\Gamma$ is unsatisfiable.

The typical use: to prove that a conclusion follows, negate it, add it to the premises, and show that the result is unsatisfiable.
A trap: a row of the table must make all members true at once to count; a row that makes two of the three members true does not help.
