---
tag: JWCDDMJE3K
kind: statement
role: theorem
name: Open embedding theorem for Hilbert manifolds
msc: [58B05, 57N20, 46T05]
uses: [R8DMMW0E9M, HM2HHE3J51, 0Z2P41SVDP, 0KZZ70ZHXP, 02BH3MCBQB]
about: [R8DMMW0E9M]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_manifold
---

## Statement

Let $H$ be an infinite-dimensional [[separable|0Z2P41SVDP]] real [[Hilbert space|HM2HHE3J51]].
Let $M$ be a smooth [[Hilbert manifold|R8DMMW0E9M]] modelled on $H$ whose underlying topological space is metrizable and separable.
Then $M$ is [[diffeomorphic|0KZZ70ZHXP]] to an [[open subset|02BH3MCBQB]] of $H$.

## Remarks

The theorem is due to Eells and Elworthy.
The idea is to embed $M$ as a closed submanifold of $H$ and to take an open tubular neighbourhood $U$ of it.
Then $U$ is a bundle over $M$ with Hilbert space fibres, which turns out to be trivial, so $U$ is diffeomorphic to $M \times H$.
Finally, in this separable infinite-dimensional setting $M \times H$ is diffeomorphic to $M$.
Example: the unit sphere $S$ of $H$ is a Hilbert manifold of this kind, and it is in fact diffeomorphic to $H$ itself, which is the open subset $H \subseteq H$.
The infinite dimension is needed: the sphere $S^n$ is a compact $n$-manifold, and a non-empty open subset of $\R^n$ is never compact.
So $S^n$ is not diffeomorphic to an open subset of $\R^n$.


## Explanations

### L1 human

In finite dimension, a sphere cannot be flattened into a piece of the plane; it is closed up on itself.
In a separable infinite-dimensional Hilbert space there is so much room that every manifold of the same kind fits inside the space as an open region.
So every separable Hilbert manifold is, up to diffeomorphism, just an open subset of the space it is modelled on.

### L2 human

The theorem reduces questions about separable Hilbert manifolds to questions about open subsets of $H$.
It is a key step in the classification of such manifolds: two of them are diffeomorphic as soon as they are homotopy equivalent.
This is very different from finite dimension, where homotopy equivalent manifolds are often not diffeomorphic.
It is one reason why infinite-dimensional manifolds of maps, such as path spaces, are studied mainly through their homotopy type.
