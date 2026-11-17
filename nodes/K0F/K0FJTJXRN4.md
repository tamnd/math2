---
tag: K0FJTJXRN4
kind: example
name: The empty clause
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [T3SXVH3ZZC]
uses: [H31CS3HK5P, QN7M1JCGT9]
sources:
  - url: https://en.wikipedia.org/wiki/Clause_(logic)
    locator: Empty clauses
---

## Example

Let $\square$ be the clause with no literals, the empty set of literals.
We check that it is a clause and that it is unsatisfiable.

1. A clause is a finite set of literals. The empty set is finite, and it has no members that fail to be literals, so $\square$ is a clause.
2. A truth assignment $v$ satisfies a clause when it makes at least one literal of the clause true.
3. The clause $\square$ has no literals, so no assignment makes one of its literals true.
4. So no assignment satisfies $\square$, and $\square$ is [[unsatisfiable|QN7M1JCGT9]].
5. Every set of clauses that contains $\square$ is unsatisfiable too, since a satisfying assignment of the set would satisfy $\square$.

## Remarks

The empty clause is the empty disjunction, and its value is $0$, the neutral element of $\lor$, in the same way that an empty sum is $0$.
The empty set of clauses is the empty conjunction, and its value is $1$, the neutral element of $\land$.
Resolution derives $\square$ from the unit clauses $\set{p}$ and $\set{\neg p}$, and a resolution refutation is a derivation of $\square$.
So the empty clause plays the role of the constant $\bot$ in clause form.

## Explanations

### L1 human

A clause says "at least one of these must happen".
The empty clause gives an empty list, and so asks that at least one thing from no things happens.
Nothing can meet this demand.
That is why a list of rules that contains the empty clause can never be obeyed.

### L2 human

We derive $\square$ from an unsatisfiable set by resolution.

1. Start with the clauses $\set{p, q}$, $\set{\neg p}$, $\set{\neg q}$.
2. Resolve $\set{p, q}$ with $\set{\neg p}$ on $p$: the result is $\set{q}$.
3. Resolve $\set{q}$ with $\set{\neg q}$ on $q$: the result is $\square$.
4. Each resolvent is a consequence of its two premises, so $\square$ is a consequence of the set, and the set is unsatisfiable.

The typical use: a solver or a prover reports "unsatisfiable" when it produces the empty clause.
A trap: the empty clause $\square$ and the empty set of clauses $\emptyset$ are different objects with opposite truth values.
