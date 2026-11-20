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

Let $F$ be a field, let $V$ be a vector space over $F$, and let $B \subseteq V$ be a subset.
Then these three conditions are equivalent:

1. $B$ is a [[basis|0VTQTPQGAV]] of $V$.
2. $B$ is a maximal linearly independent set: $B$ is [[independent|0EVHJFTG9Z]], and $B \cup \set{v}$ is dependent for each $v \in V \setminus B$.
3. $B$ is a minimal spanning set: $B$ [[spans|0BJKVF90Z6]] $V$, and $B \setminus \set{b}$ does not span $V$ for each $b \in B$.

## Remarks

### Why each hypothesis is needed

"Maximal" refers to inclusion, not to size: no larger count is needed, but no independent proper superset may exist.
The field matters: in the $\Z$-module $\Z$, the set $\set{2, 3}$ spans, and each of $\set{2}$ and $\set{3}$ does not span, so $\set{2, 3}$ is a minimal spanning set; it is not a basis, because $3 \cdot 2 - 2 \cdot 3 = 0$.

### Consequences

Condition 2 is the form used in the [[proof by Zorn's lemma|00MS9VMQ9Z]] that every space has a basis.
Condition 3 is the form used to [[shrink a spanning set to a basis|06MRNP4BNT]].

### Converse

The statement is a list of equivalences.

### Generalizations

The same equivalences hold for the bases of a [[matroid|PX31ZNYS3Z]], where maximal independent sets and minimal spanning sets coincide by the exchange axiom.
They fail for modules over rings that are not fields, as the example with $\Z$ shows.

## Explanations

### L1 human

A basis cannot be enlarged without creating a redundant vector.
It also cannot be made smaller without losing some direction.
Both facts characterize bases.

### L2 human

Example in $\R^2$: the set $\set{(1, 0), (0, 1)}$ is a basis.
Adding $(2, 3)$ gives the relation $2(1, 0) + 3(0, 1) - (2, 3) = 0$, so the larger set is dependent.
Removing $(0, 1)$ leaves $\set{(1, 0)}$, whose span is the $x$-axis, so the smaller set does not span.
