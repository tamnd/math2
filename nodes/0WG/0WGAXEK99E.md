---
tag: 0WGAXEK99E
kind: statement
role: proposition
name: A subspace of full dimension is the whole space
msc: [15A03]
uses: [05G2G0P224, 0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: Properties
---

## Statement

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $W$ be a [[linear subspace|00YC1D652K]] of $V$.
If $\dim W = \dim V$, then $W = V$.

## Remarks

A basis of $W$ is a linearly independent family of $\dim V$ vectors in $V$.
So it is a basis of $V$, see [[linearly independent set of the right size is a basis|096V7H13H9]].
The statement fails for infinite-dimensional spaces.
In $F[x]$, the subspace of polynomials with $p(0) = 0$ has the same dimension as $F[x]$, but it is not equal to $F[x]$.

## Explanations

### L1 human

If a subspace is as large as the whole space, measured by dimension, then it is the whole space.
For example, a two-dimensional subspace of the plane is the plane.
This lets us prove that two subspaces are equal by an inclusion and a count.
