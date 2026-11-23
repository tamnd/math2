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

Let $\square$ be the clause with no literals, that is, the empty set of literals.
We check that it is a [[clause|T3SXVH3ZZC]] and that it is unsatisfiable.

1. A clause is a finite set of literals.
   The empty set is finite, and it has no members that fail to be literals, so $\square$ is a clause.
2. A truth assignment $v$ satisfies a clause when it makes at least one literal of the clause true.
3. The clause $\square$ has no literals, so no assignment makes one of its literals true.
4. So no assignment satisfies $\square$, and $\square$ is [[unsatisfiable|QN7M1JCGT9]].
5. Every set of clauses that contains $\square$ is unsatisfiable too, because a satisfying assignment of the set would have to satisfy $\square$.

## Remarks

The empty clause is the empty disjunction, and its value is $0$, the neutral element of $\lor$.
This is the same convention as an empty sum, which is $0$.
The empty set of clauses is the empty conjunction, and its value is $1$, the neutral element of $\land$, as an empty product is $1$.

In [[resolution|ZDW6N1PGJ7]] the empty clause is the goal.
Resolving the unit clauses $\{ p \}$ and $\{ \neg p \}$ removes the only literal of each and leaves $\square$.
A resolution refutation is a derivation of $\square$, so the empty clause plays the role of the constant $\bot$ in clause form.

## Explanations

### L1 human

A clause says "at least one of these must happen".
The empty clause gives an empty list, so it asks that at least one thing from no things happens.
Nothing can meet this demand.
That is why a list of rules that contains the empty clause can never be obeyed.

### L2 human

We derive $\square$ from the clause set $\{ p, q \}$, $\{ \neg p \}$, $\{ \neg q \}$.
Resolve $\{ p, q \}$ with $\{ \neg p \}$ on $p$ to get $\{ q \}$.
Resolve $\{ q \}$ with $\{ \neg q \}$ on $q$ to get $\square$.
Each resolvent is a consequence of its premises, so $\square$ is a consequence of the set, and the set is unsatisfiable.
Check by hand: $\neg p$ and $\neg q$ force $p = q = 0$, and then $p \lor q$ is false.
A solver reports "unsatisfiable" exactly when it reaches the empty clause.
Watch out: the empty clause $\square$ and the empty set of clauses $\emptyset$ are different objects with opposite truth values.
