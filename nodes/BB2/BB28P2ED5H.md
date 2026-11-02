---
tag: BB28P2ED5H
kind: statement
role: theorem
name: Hyperbolic Dehn surgery theorem
msc: [57K32, 57K30]
uses: [GHVW1Z35BS, ZA405B0Z1S, C01XBGAHC6]
about: [GHVW1Z35BS, ZA405B0Z1S]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_Dehn_surgery
---

## Statement

Let $M$ be an orientable [[hyperbolic 3-manifold|GHVW1Z35BS]] of finite volume that is the interior of a compact $3$-manifold $\bar{M}$ whose boundary consists of tori $T_1, \ldots, T_n$.
A *slope* on $T_i$ is an isotopy class of essential simple closed curves on $T_i$.
For slopes $s_1, \ldots, s_n$, let $M(s_1, \ldots, s_n)$ be the closed manifold obtained by [[Dehn filling|ZA405B0Z1S]].
It is made by gluing a solid torus to each $T_i$ so that a meridian is glued to $s_i$.
Then for each $i$ there is a finite set $E_i$ of slopes on $T_i$ such that $M(s_1, \ldots, s_n)$ is hyperbolic whenever $s_i \notin E_i$ for every $i$.

## Remarks

The theorem is due to Thurston.
The complete structure on $M$ lies in a space of incomplete hyperbolic structures, parametrised near it by the shapes of ideal tetrahedra.
Nearby incomplete structures whose metric completion is a closed manifold give the filled manifolds.
Thurston also showed that the volumes of the filled manifolds are smaller than the volume of $M$ and tend to it as all slopes go to infinity.
For the complement of the [[figure-eight knot|C01XBGAHC6]], exactly ten slopes give a non-hyperbolic filling: $\infty$, $0$, $\pm 1$, $\pm 2$, $\pm 3$ and $\pm 4$.
The finite set cannot be empty in general: the filling along the meridian of a knot complement gives back $S^3$, which is not hyperbolic.

## Explanations

### L1 human

Start from a hyperbolic space with some tube-shaped ends, and close each end by gluing in a solid doughnut.
There are infinitely many ways to glue each doughnut.
Thurston's theorem says that all of them, except for finitely many on each end, give a closed hyperbolic manifold.

### L2 human

The theorem produces infinitely many closed hyperbolic $3$-manifolds from each cusped one, for example from knot complements.
Since every closed orientable $3$-manifold is obtained by surgery on a link in $S^3$, it suggests that hyperbolic manifolds are generic.
The exceptional slopes are well studied: Lackenby and Meyerhoff proved that a one-cusped manifold has at most ten of them, so the figure-eight knot complement is extremal.
