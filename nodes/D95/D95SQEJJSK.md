---
tag: D95SQEJJSK
kind: conjecture
name: Hopf conjecture
msc: [53C20, 53C21]
uses: [7CBT4SM83Y, 1X42JAA349, RNDDWDAFJ5, 0TVJZYB6SH]
about: [1X42JAA349, RNDDWDAFJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_conjectures
history:
  posed_by: "Heinz Hopf"
---

## Statement

Let $M$ be a compact connected [[Riemannian manifold|7CBT4SM83Y]] without boundary, of even dimension $2d$.
Let $\chi(M)$ be its [[Euler characteristic|RNDDWDAFJ5]].

1. If $M$ has positive [[sectional curvature|1X42JAA349]], then $\chi(M) > 0$.
2. If $M$ has negative sectional curvature, then $(-1)^d \chi(M) > 0$.

## Remarks

Both parts are open in dimension $6$ and higher.
In dimension $2$ both parts follow from the [[Gauss–Bonnet theorem|ESGEHKPD60]], since the integral of the Gaussian curvature equals $2\pi \chi(M)$.
In dimension $4$ both parts follow from the [[Chern–Gauss–Bonnet theorem|GG6NYPKMHX]], because in that dimension the integrand is positive when the sectional curvature is either everywhere positive or everywhere negative.
For the positive case in dimension $4$ there is also a topological argument: by [[Synge's theorem|Z8JJ04X1JX]] an orientable such $M$ is simply connected, so $b_1 = b_3 = 0$ and $\chi(M) = 2 + b_2 > 0$.
In dimensions $2d \ge 6$ the Chern–Gauss–Bonnet integrand can be negative at a point even when the sectional curvature is positive, so this route fails.
The positive case is known for manifolds whose curvature is pinched enough, since then the [[sphere theorem|7GRSF20H15]] shows that $M$ is covered by a sphere.
Weaker forms with non-strict inequalities are also attributed to Hopf: nonnegative curvature should give $\chi(M) \ge 0$, and nonpositive curvature should give $(-1)^d \chi(M) \ge 0$.
A different question of Hopf, often also called the Hopf conjecture, asks whether $S^2 \times S^2$ carries a metric of positive sectional curvature; this is also open.

## Explanations

### L1 human

Curvature is a local quantity, measured near each point.
The Euler characteristic is a global number: for a surface cut into polygons it is vertices minus edges plus faces.
Hopf asked whether the sign of the curvature everywhere forces the sign of this global count.
For surfaces the answer is yes.
A positively curved closed surface is a sphere or a projective plane, and both have positive Euler characteristic.
A negatively curved closed surface always has negative Euler characteristic.
The conjecture asks the same in every even dimension, and in general it is proved only up to dimension $4$.
