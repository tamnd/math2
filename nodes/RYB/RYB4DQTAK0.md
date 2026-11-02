---
tag: RYB4DQTAK0
kind: statement
role: theorem
name: Euler's theorem on normal curvatures
msc: [53A05]
uses: [FA8QE1SGP4, 9KHQR16P1B, DQCD11X1VM, 6080X3FAD4]
about: [FA8QE1SGP4, 9KHQR16P1B]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_theorem_(differential_geometry)
same_as:
  wikidata: Q3526990
  wikipedia: Euler's theorem (differential geometry)
---

## Statement

Let $S \subseteq \R^3$ be a [[regular surface|6080X3FAD4]] with a smooth unit normal field near a point $p \in S$.
Let $k_1, k_2$ be the [[principal curvatures|FA8QE1SGP4]] of $S$ at $p$, with orthonormal principal directions $e_1, e_2 \in T_p S$.
For a unit vector $w \in T_p S$, let $k_n(w) = I\!I_p(w)$ be the normal curvature in the direction $w$, where $I\!I_p$ is the [[second fundamental form|9KHQR16P1B]].
If $w = \cos \theta \, e_1 + \sin \theta \, e_2$, then
$$k_n(w) = k_1 \cos^2 \theta + k_2 \sin^2 \theta.$$

## Remarks

The proof is one line: $I\!I_p(w) = \ip{S_p w}{w}$ with the [[shape operator|DQCD11X1VM]] $S_p$, and $S_p e_i = k_i e_i$, so the cross terms vanish.
It follows that $k_1$ and $k_2$ are the maximum and the minimum of the normal curvature over all directions.
Example: on a cylinder of radius $r$ with the inner normal, $k_1 = 1/r$ around the cylinder and $k_2 = 0$ along it.
A direction at angle $\theta$ to the circular sections has normal curvature $\cos^2 \theta / r$.
The normal curvature $k_n(w)$ equals the signed curvature of the normal section, the curve cut out of $S$ by the plane through $p$ spanned by $w$ and the normal.

## Explanations

### L1 human

At a point of a surface, the bending changes with the direction you look in.
Euler's theorem says that this change follows a very simple rule.
Once you know the strongest and the weakest bending, and their directions, you know the bending in every other direction.

### L2 human

The theorem is the diagonal form of the quadratic form $I\!I_p$ in an orthonormal eigenbasis of the self-adjoint map $S_p$.
It explains why the Gaussian curvature $k_1 k_2$ and the mean curvature $(k_1 + k_2)/2$ capture the whole second-order shape, up to the choice of principal directions.
The sign of $k_1 k_2$ decides whether the normal curvature keeps one sign (elliptic point), changes sign (hyperbolic point), or vanishes in one direction (parabolic point).
The directions with $k_n(w) = 0$ at a hyperbolic point are the asymptotic directions, at angles $\theta$ with $\tan^2 \theta = -k_1 / k_2$.
