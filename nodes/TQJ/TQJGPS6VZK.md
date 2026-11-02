---
tag: TQJGPS6VZK
kind: definition
name: Coplanarity
msc: [51N10, 51A05]
defines: 4TWY53TBKK
uses: [09XNAPTJQ7, 00YC1D652K, 03GSZ8RTZJ, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Coplanarity
---

## Definition

Let $A$ be an [[affine space|09XNAPTJQ7]] over a field $k$, with space of translations $V$.
A set $S$ of points of $A$ is *coplanar* if the vectors $q - p$, for $p, q \in S$, span a [[linear subspace|00YC1D652K]] of [[dimension|03GSZ8RTZJ]] at most $2$.

## Remarks

When $A$ has dimension at least $2$, the set $S$ is coplanar exactly when some affine plane of $A$ contains $S$.

Example: in $\R^3$ the points $(0,0,0)$, $(1,0,0)$, $(0,1,0)$ and $(1,1,0)$ are coplanar.
Check: all differences lie in the subspace $\set{z = 0}$, which has dimension $2$.

Non-example: the points $(0,0,0)$, $(1,0,0)$, $(0,1,0)$ and $(0,0,1)$ of $\R^3$ are not coplanar.
The differences from the origin are the three standard basis vectors, which span a space of dimension $3$.

In $\R^3$, four points $p_0, p_1, p_2, p_3$ are coplanar exactly when the [[determinant|00KDZRW4C0]] of the $3 \times 3$ matrix with columns $p_1 - p_0$, $p_2 - p_0$, $p_3 - p_0$ is zero.
Every set of at most three points is coplanar.
