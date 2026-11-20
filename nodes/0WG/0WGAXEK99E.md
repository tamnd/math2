---
tag: 0WGAXEK99E
kind: statement
role: proposition
name: A subspace of full dimension is the whole space
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [03GSZ8RTZJ]
uses: [05G2G0P224, 0EPTJA5QV4]
proofs: [345D462T59]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: Properties
---

## Statement

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $W$ be a [[linear subspace|00YC1D652K]] of $V$.
If $\dim W = \dim V$, then $W = V$.

## Remarks

### Why each hypothesis is needed

The statement fails for infinite-dimensional spaces.
In $F[x]$, the subspace of polynomials with $p(0) = 0$ has the same dimension $\aleph_0$ as $F[x]$, but it is not equal to $F[x]$; see [[this example|~c51d6709]].
The inclusion $W \subseteq V$ is needed: two different lines in $\R^2$ both have dimension $1$.

### Consequences

Two finite-dimensional subspaces $U \subseteq W$ with $\dim U = \dim W$ are equal.
So a proof of $U = W$ needs only one inclusion and a count of dimensions.

### Converse

The converse is trivial: $W = V$ gives $\dim W = \dim V$.

### Generalizations

This is part 2 of [[the dimension of a subspace|0QW084460E]].
For modules over $\Z$, it fails: $2 \Z \subsetneq \Z$, and both are free of rank $1$.

## Explanations

### L1 human

If a subspace is as large as the whole space, measured by dimension, then it is the whole space.
For example, a two-dimensional subspace of the plane is the plane.
This lets us prove that two subspaces are equal by an inclusion and a count.
