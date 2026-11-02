---
tag: FGRPYWW1V1
kind: definition
name: Sasakian manifold
msc: [53C25, 53D10]
defines: B21YEPS76G
uses: [7CBT4SM83Y, CK1DCPC3D3, HBQ8BZ7XB5, GGM63KXCF2]
sources:
  - url: https://en.wikipedia.org/wiki/Sasakian_manifold
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]].
The *metric cone* over $M$ is the manifold $C(M) = (0, \infty) \times M$ with the metric $\bar g = dr^2 + r^2 g$, where $r$ is the coordinate on $(0, \infty)$.
The manifold $(M, g)$ is *Sasakian* if $C(M)$ has an integrable almost complex structure $J$ with two properties.
The metric $\bar g$ is a [[Kähler metric|CK1DCPC3D3]] for $J$, and $J$ is invariant under the dilations $(r, x) \mapsto (\lambda r, x)$ for $\lambda > 0$.

## Remarks

Example: the unit sphere $S^{2n+1} \subset \C^{n+1}$ with the round metric.
The map $(r, x) \mapsto r x$ identifies $C(S^{2n+1})$ with $\C^{n+1} \setminus \set{0}$, and it carries $dr^2 + r^2 g$ to the flat metric, which is Kähler.

Non-example: the round sphere $S^2$ is not Sasakian.
Its cone is $\R^3 \setminus \set{0}$, of odd dimension $3$, so it has no almost complex structure at all.

A Sasakian manifold has odd dimension $2n + 1$.
The vector field $\xi = J(r \partial_r)$, restricted to $\set{1} \times M$, is a unit Killing field, the [[Reeb vector field|GGM63KXCF2]] of the contact form $\eta = g(\xi, \cdot)$, which makes $M$ a [[contact manifold|HBQ8BZ7XB5]].
