---
tag: NX0PKAWT0Y
kind: definition
name: Almost complex manifold
msc: [53C15, 32Q60]
defines: 9SYWRGVTRS
uses: [F45VQ47GPV, WY6K3P4YCG, WX302T93TW, 68FGQEBD6J]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_complex_manifold
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] with [[tangent bundle|WY6K3P4YCG]] $TM$.
An *almost complex structure* on $M$ is a smooth [[tensor field|WX302T93TW]] $J$ of type $(1, 1)$ such that $J^2 = -\id$.
Thus $J \colon TM \to TM$ is a smooth map that is linear on each tangent space $T_p M$.
An *almost complex manifold* is a pair $(M, J)$ of a smooth manifold and an almost complex structure on it.

## Remarks

Example: on $\R^{2n}$ with coordinates $(x_1, \ldots, x_n, y_1, \ldots, y_n)$, put $J \partial_{x_k} = \partial_{y_k}$ and $J \partial_{y_k} = -\partial_{x_k}$.
Then $J^2 \partial_{x_k} = J \partial_{y_k} = -\partial_{x_k}$ and likewise for $\partial_{y_k}$, so $J^2 = -\id$.
This is multiplication by $i$ under $\R^{2n} \cong \C^n$, and every complex manifold carries the structure obtained in this way from its charts.

Non-example: no manifold of odd dimension $m$ has an almost complex structure.
A real linear map $J$ of $T_p M$ with $J^2 = -\id$ gives $\det(J)^2 = \det(-\id) = (-1)^m = -1$, which is impossible.

The *Nijenhuis tensor* of $J$ is
$$N_J(X, Y) = [JX, JY] - J[JX, Y] - J[X, JY] - [X, Y]$$
for vector fields $X, Y$, where $[\cdot, \cdot]$ is the [[Lie bracket of vector fields|68FGQEBD6J]].
The structure $J$ is called *integrable* when $N_J = 0$.
The sphere $S^6$ has an almost complex structure coming from the octonions, while $S^4$ has none.
