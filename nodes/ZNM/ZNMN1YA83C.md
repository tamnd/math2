---
tag: ZNMN1YA83C
kind: statement
role: theorem
name: Finite-dimensional Hausdorff vector topologies are Euclidean
msc: [46A03, 46A16]
uses: [0S1FJ8VEX9, 0ZHWKQMVX5, 0B8T10CE7N, 0QT00PB5G2]
about: [0ZHWKQMVX5]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_vector_space
---

## Statement

Let $\mathbb{K}$ be $\R$ or $\C$, and give $\mathbb{K}^n$ its Euclidean topology.
Let $E$ be a [[Hausdorff|0S1FJ8VEX9]] topological vector space over $\mathbb{K}$ of [[finite dimension|0ZHWKQMVX5]] $n$.
Then every [[linear isomorphism|0B8T10CE7N]] $T \colon \mathbb{K}^n \to E$ is a [[homeomorphism|0QT00PB5G2]].
In particular, a finite-dimensional vector space over $\mathbb{K}$ carries exactly one Hausdorff topology making it a topological vector space.

## Remarks

The map $T(c_1, \ldots, c_n) = c_1 e_1 + \cdots + c_n e_n$ is continuous, because addition and scalar multiplication are continuous in $E$.
For the continuity of $T^{-1}$, let $S$ be the unit sphere of $\mathbb{K}^n$; it is compact, so $T(S)$ is compact and does not contain $0$.
Since $E$ is Hausdorff, there is a balanced neighbourhood $V$ of $0$ disjoint from $T(S)$.
Then $T^{-1}(V)$ is balanced and misses $S$, so it lies in the open unit ball, which gives continuity of $T^{-1}$ at $0$.
Example: all norms on $\R^n$ define the same topology, since each makes $\R^n$ a Hausdorff topological vector space.
The Hausdorff hypothesis is needed: $\R$ with the indiscrete topology is a topological vector space.
The identity map from $\R$ with the Euclidean topology to it is a continuous linear bijection, but not a homeomorphism.
Consequences: every finite-dimensional subspace of a Hausdorff topological vector space is closed, and every linear map from a finite-dimensional Hausdorff topological vector space to any topological vector space is continuous.

## Explanations

### L1 human

On a finite-dimensional space there is only one reasonable way to say that vectors are close.
Whatever Hausdorff topology you choose, as long as adding and scaling are continuous, you get back the usual topology of coordinates.
So in finite dimension, questions of topology reduce to questions about coordinates.

### L2 human

This theorem explains why topology plays no role in finite-dimensional linear algebra and becomes important only in infinite dimension.
It contains the familiar fact that all norms on $\R^n$ are equivalent, and it implies that [[finite-dimensional normed spaces are complete|0ABP2F2ZP7]] and that the [[Heine–Borel theorem holds in them|0PHT6NBYPB]].
A companion result says that a Hausdorff topological vector space with a compact neighbourhood of $0$ must be finite-dimensional.
Together they show that local compactness singles out the finite-dimensional spaces.
