---
tag: 06MRNP4BNT
kind: statement
role: theorem
name: Every spanning set contains a basis
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [0KCQ9Y3QKA]
uses: [0VTQTPQGAV, 0BJKVF90Z6]
proofs: [GJKC4QQWAW, KS6PP0BVSD]
formal:
  - system: lean4
    library: mathlib
    decl: exists_linearIndependent
    match: stronger
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Properties
  - book: isbn:9783031410253
    locator: Section 2B
  - book: isbn:9780134860244
    locator: Section 1.6
---

## Statement

Let $F$ be a field, let $V$ be a vector space over $F$, and let $S \subseteq V$ be a [[spanning set|0BJKVF90Z6]] of $V$.
Then there is a subset $B \subseteq S$ that is a [[basis|0VTQTPQGAV]] of $V$.

## Remarks

### Why each hypothesis is needed

If $S$ does not span $V$, then no subset of $S$ spans $V$, so no subset is a basis.
Example: $S = \set{(1, 0)}$ in $\R^2$; its subsets $\emptyset$ and $S$ fail the spanning condition.
Over a ring, the statement fails: $\set{2, 3}$ spans $\Z$, but $\set{2}$, $\set{3}$ and $\set{2, 3}$ are not bases of $\Z$.
Here $\set{2}$ and $\set{3}$ fail spanning, and $\set{2, 3}$ fails independence, because $3 \cdot 2 - 2 \cdot 3 = 0$.
For infinite $S$, the general proof uses [[Zorn's lemma|04RXTQA5ZA]]; the finite case needs no choice.

### Consequences

1. A finite-dimensional space has a finite basis, and $\dim V \le \abs{S}$ for each finite spanning set $S$.
2. In $F^m$, the pivot columns of a matrix form a basis of its column space; this is the algorithmic form, see [[the column space basis|11CSKXQNG3]].
3. A spanning set of exactly $\dim V$ vectors is a basis; see [[the right-size criterion|096V7H13H9]].

### Converse

Each basis spans $V$, so each set that contains a basis spans $V$.
So a subset $S \subseteq V$ spans $V$ if and only if it contains a basis.

### Generalizations

The [[extension theorem|0M4SXE5WW3]] gives a basis $B$ with $L \subseteq B \subseteq S$, for $L$ independent and $S$ spanning.
In a matroid, each spanning set contains a basis, by the same argument.
In Mathlib, `exists_linearIndependent` states: each set $t$ contains an independent set $b$ with the same span as $t$.

## Explanations

### L1 human

If a set of vectors reaches the whole space, then some part of it is a basis.
We throw away vectors that the others can already build.
When nothing redundant remains, the remaining vectors form a basis.

### L2 human

For vectors in $F^m$, put them as the columns of a matrix $A$ and row reduce.
The columns of $A$ in the pivot positions form a basis of the span.
Example: the columns $(1, 0), (0, 1), (1, 1)$ have pivots in columns $1$ and $2$, so $(1, 0), (0, 1)$ is a basis.
The set $S = \set{(1, 0), (0, 1), (1, 1)}$ spans $\R^2$.
It is dependent: $(1, 1) = (1, 0) + (0, 1)$.
Remove $(1, 1)$; the set $\set{(1, 0), (0, 1)}$ still spans and is independent, so it is a basis.
The subset $\set{(1, 0), (1, 1)}$ is also a basis, so the basis inside $S$ is not unique.
