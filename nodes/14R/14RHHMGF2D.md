---
tag: 14RHHMGF2D
kind: statement
role: theorem
name: Huisken's theorem on convex hypersurfaces
msc: ["53E10", "53C44"]
uses: [PA78NFEPCF, FA8QE1SGP4]
sources:
  - url: https://en.wikipedia.org/wiki/Mean_curvature_flow
---

## Statement

Let $n \ge 2$ and let $M_0$ be a compact, connected, smooth hypersurface without boundary embedded in $\R^{n+1}$.
Assume that $M_0$ is uniformly convex, that is, all [[principal curvatures|FA8QE1SGP4]] of $M_0$ are positive at every point.
Then:

1. The [[mean curvature flow|2YYV01C7QQ]] starting from $M_0$ has a unique smooth solution $(M_t)_{0 \le t < T}$ on a maximal time interval with $T < \infty$.
2. Each $M_t$ is uniformly convex.
3. As $t \to T$, the hypersurfaces $M_t$ shrink to a single point $p \in \R^{n+1}$.
4. The rescaled hypersurfaces $(2n(T - t))^{-1/2}(M_t - p)$ converge smoothly to the unit sphere $S^n$ as $t \to T$.

## Remarks

The proof first shows that convexity is preserved by the maximum principle applied to the evolution of the second fundamental form.
The key estimate is a pinching estimate: the ratio of the smallest to the largest principal curvature tends to $1$ where the [[mean curvature|PA78NFEPCF]] blows up.
Together with bounds on the derivatives of the curvature, this forces the rescaled surfaces to become round.
For a round sphere of radius $r_0$, the flow gives spheres of radius $r(t) = \sqrt{r_0^2 - 2nt}$, so $T = r_0^2/(2n)$ and the rescaled surfaces are all the unit sphere.
Convexity is needed: a dumbbell, made of two large spheres joined by a thin neck, can pinch off at the neck before it shrinks to a point.
The case $n = 1$ of convex curves in the plane is the theorem of Gage and Hamilton, part of the [[Gage–Hamilton–Grayson theorem|FVGW1381TZ]].

## Explanations

### L1 human

Mean curvature flow moves each point of a surface inward at a speed given by how curved the surface is there.
Huisken's theorem says that a convex closed surface, such as an egg shape, stays convex under this flow.
It shrinks to a point in finite time.
Just before it disappears, it looks more and more like a round sphere.

### L2 human

Huisken proved this in 1984, for hypersurfaces of dimension at least two.
It is the model result for geometric flows that make a shape round.
It parallels Hamilton's theorem that the Ricci flow deforms a closed $3$-manifold with positive Ricci curvature into a round one.
The method combines the parabolic maximum principle with curvature pinching estimates.
Later work of Huisken and others studies what happens without convexity, where singularities such as neck pinches appear.
