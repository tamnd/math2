---
tag: WNSAZD8EZC
kind: definition
name: Contact manifold
msc: [53D10]
defines: HBQ8BZ7XB5
uses: [F45VQ47GPV, 0E3G0GRPZ6, 0ZHSTAG8ZY, 5Q4BHBFXJY]
sources:
  - url: https://en.wikipedia.org/wiki/Contact_geometry
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] of odd dimension $2n + 1$.
A *contact structure* on $M$ is a smooth field $\xi$ of hyperplanes $\xi_x \subset T_x M$ with the following property.
Each point has an open neighborhood $U$ and a [[differential $1$-form|0E3G0GRPZ6]] $\alpha$ on $U$ with $\xi = \ker \alpha$ on $U$ and
$$\alpha \wedge (d\alpha)^n \ne 0 \quad \text{at every point of } U.$$
Here $d$ is the [[exterior derivative|0ZHSTAG8ZY]].
A *contact manifold* is a pair $(M, \xi)$ with $\xi$ a contact structure.
A $1$-form $\alpha$ defined on all of $M$ with $\ker \alpha = \xi$ is a *contact form* for $\xi$.

## Remarks

The condition does not depend on the choice of $\alpha$: if $\alpha' = h \alpha$ with $h$ nowhere zero, then $\alpha' \wedge (d\alpha')^n = h^{n+1} \alpha \wedge (d\alpha)^n$.
Equivalently, $d\alpha$ restricted to each hyperplane $\xi_x$ is nondegenerate.
A contact form exists globally exactly when $\xi$ is coorientable.

Example: on $\R^3$ with coordinates $(x, y, z)$, let $\alpha = dz - y\,dx$.
Then $d\alpha = dx \wedge dy$ and $\alpha \wedge d\alpha = dz \wedge dx \wedge dy = dx \wedge dy \wedge dz \ne 0$, so $\ker \alpha$ is a contact structure, the standard one.
The unit sphere $S^{2n+1} \subset \C^{n+1}$ with $\alpha = \sum_j (x_j\, dy_j - y_j\, dx_j)$ restricted to it is another standard example.

Non-example: on $\R^3$ the form $\alpha = dz$ has $d\alpha = 0$, so $\alpha \wedge d\alpha = 0$; its kernel is tangent to the planes $z = \text{const}$.
By the [[Frobenius theorem|5Q4BHBFXJY]], $\alpha \wedge d\alpha = 0$ is exactly the condition for $\ker \alpha$ to be tangent to a family of surfaces.
