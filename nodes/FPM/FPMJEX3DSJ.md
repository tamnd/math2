---
tag: FPMJEX3DSJ
kind: statement
role: theorem
name: Myers's theorem
msc: [53C20, 53C21]
uses: [7CBT4SM83Y, 4GTNM0WHDH, B4QR306D8G, 0KW3PN547K, S1XK3HXHFX, Y1YPE6PM52, ZB91TH6FKV]
about: [4GTNM0WHDH]
sources:
  - url: https://en.wikipedia.org/wiki/Myers%27s_theorem
same_as:
  wikidata: Q929547
  wikipedia: Myers's theorem
---

## Statement

Let $(M, g)$ be a connected complete [[Riemannian manifold|7CBT4SM83Y]] of dimension $n \ge 2$.
Suppose there is a real number $k > 0$ such that the [[Ricci curvature|4GTNM0WHDH]] satisfies $\operatorname{Ric}(v, v) \ge (n-1) k \, g(v, v)$ for every tangent vector $v$.
Then:

1. The [[diameter|0KW3PN547K]] of $M$ for the [[Riemannian distance|B4QR306D8G]] is at most $\pi / \sqrt{k}$.
2. $M$ is compact.
3. The [[fundamental group|S1XK3HXHFX]] of $M$ is finite.

## Remarks

The idea of the proof: let $\gamma$ be a minimizing unit-speed geodesic of length $L > \pi/\sqrt{k}$.
Take an orthonormal frame $E_1, \dots, E_{n-1}$ of parallel fields normal to $\gamma$ and the variation fields $\sin(\pi t / L) E_i$.
By the [[second variation formula|ZB91TH6FKV]], the sum of the second variations of length is negative, so one of them is negative and $\gamma$ is not minimizing, a contradiction.
Part 2 follows from part 1 and the Hopf–Rinow theorem.
For part 3, apply parts 1 and 2 to the [[universal cover|Y1YPE6PM52]] with the pulled-back metric: it is compact, so the covering has finitely many sheets.

Example: the unit sphere $S^n$ has $\operatorname{Ric} = (n-1) g$ and diameter exactly $\pi$, so the bound is sharp.
By a theorem of Cheng, equality of the diameter with $\pi/\sqrt{k}$ holds only for the round sphere of radius $1/\sqrt{k}$.

The uniform lower bound is needed: the paraboloid $z = x^2 + y^2$ in $\R^3$ is complete with positive curvature, but its curvature tends to $0$ at infinity and it is not compact.

## Explanations

### L1 human

If a space is curved positively at least by a fixed amount in every direction, it must close up on itself, like a sphere.
The theorem gives an explicit bound: no two points are farther apart than on the sphere of the same curvature.

### L2 human

Myers's theorem is one of the first results linking a lower bound on Ricci curvature to global topology.
For example, it shows that a compact manifold with infinite fundamental group, such as a torus, carries no metric of positive Ricci curvature.
It has a sharp volume analogue, the Bishop–Gromov inequality, and it is used in general relativity to show that certain spacetimes are closed.
