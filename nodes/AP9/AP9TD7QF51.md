---
tag: AP9TD7QF51
kind: statement
role: proposition
name: A basis is a maximal independent family and a minimal spanning family
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [0KCQ9Y3QKA]
uses: [0VTQTPQGAV, 0EVHJFTG9Z, 0BJKVF90Z6, H75GS7QVPB]
proofs: [Q8T6CQK7R0]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Properties
  - book: isbn:9780134860244
    locator: Section 1.7
---

## Statement

A basis is an independent set that cannot grow and a spanning set that cannot shrink.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $B \subseteq V$ be a subset.
Then the following three conditions are equivalent.

1. $B$ is a [[basis|0VTQTPQGAV]] of $V$.
2. $B$ is a *maximal linearly independent set*: $B$ is [[linearly independent|0EVHJFTG9Z]], and $B \cup \{v\}$ is linearly dependent for each $v \in V \setminus B$.
3. $B$ is a *minimal spanning set*: $B$ [[spans|0BJKVF90Z6]] $V$, and $B \setminus \{b\}$ does not span $V$ for each $b \in B$.

## Remarks

### A check in the plane

Take the basis $B = \{(1, 0), (0, 1)\}$ of $\mathbb{R}^2$.
Add any other vector, say $(2, 3)$.
The larger set satisfies the relation
$$2 (1, 0) + 3 (0, 1) - (2, 3) = (0, 0),$$
so it is dependent, as condition 2 predicts.
Now remove $(0, 1)$.
What is left spans only the $x$-axis, so it misses $(0, 1)$, as condition 3 predicts.
The same two tests work for every vector we add and every vector we remove.

### Why each hypothesis is needed

"Maximal" and "minimal" refer to inclusion, not to size.
Condition 2 does not compare $B$ with independent sets of other sizes; it only asks that no single new vector keeps $B$ independent.
That every maximal independent set has the same size is a separate result, the [[dimension theorem|0WK0Y8RH1M]].

The scalars must form a field, because the proof divides by a nonzero coefficient.
In the $\mathbb{Z}$-module $\mathbb{Z}$, the set $\{2, 3\}$ spans, since $3 - 2 = 1$.
Each of $\{2\}$ and $\{3\}$ spans only $2\mathbb{Z}$ or $3\mathbb{Z}$, so $\{2, 3\}$ is a minimal spanning set.
It is not a basis, because $3 \cdot 2 - 2 \cdot 3 = 0$ is a nontrivial relation.

### What it gives you

Condition 2 is the form used in the [[proof by Zorn's lemma|00MS9VMQ9Z]] that every vector space has a basis: Zorn's lemma produces a maximal independent set, and the statement turns it into a basis.
Condition 3 is the form used to [[shrink a spanning set to a basis|06MRNP4BNT]]: throw away vectors until no more can go.
Condition 2 also explains how to [[extend an independent set to a basis|0M4SXE5WW3]]: add vectors outside the span until no more can be added.

### The converse

The statement is a list of equivalences, so each condition is also a converse of the others.
The same equivalences hold for families, where we remove or add one member of the family.
A repeated vector then fails conditions 1 and 3 together: the family $(v, v)$ with $v \ne 0$ spans the line through $v$, and it still spans after we remove one copy.

### Generalizations

The same three conditions are equivalent for the bases of a [[matroid|PX31ZNYS3Z]], where independence is an abstract property of sets.
For modules over rings that are not fields they fail, as the example of $\{2, 3\}$ in $\mathbb{Z}$ shows.

## Explanations

### L1 human

A basis is a set of directions that you cannot improve.
If you add one more direction, it is already a mix of the old ones, so it is redundant.
If you take one direction away, some vectors can no longer be reached.
For example, "east" and "north" reach every point of a map, any third direction is a mix of these two, and "east" alone never takes you north.

### L2 human

Here is a typical use: shrink the spanning set $S = \{(1, 2), (2, 4), (1, 0)\}$ of $\mathbb{R}^2$ to a basis.
The vector $(2, 4)$ is $2 (1, 2)$, so removing it does not change the span, and $\{(1, 2), (1, 0)\}$ still spans.
Now neither vector is a multiple of the other, so removing either one leaves a single line.
So $\{(1, 2), (1, 0)\}$ is a minimal spanning set, and by the statement it is a basis.
Check: $c (1, 2) + d (1, 0) = (0, 0)$ gives $2c = 0$ and then $d = 0$, so the set is independent.
Watch out: minimal means that no single vector can be removed, which is not the same as "has the fewest vectors among all spanning sets you have tried".

### L3 human

The statement says that the bases of $V$ are the maximal elements of the set of independent subsets, ordered by inclusion, and also the minimal elements of the set of spanning subsets.
This is the shape that makes Zorn's lemma apply in infinite dimension, since a union of a chain of independent sets is independent.
The same pattern, maximal independent equals minimal spanning, is the defining feature of matroids, and it returns for algebraically independent sets in field extensions, where maximal ones are transcendence bases.
