---
tag: F02XA3MYX8
kind: statement
role: theorem
name: Steiner formula
msc: [52A39, 52A38]
uses: [QB3Q5FBJ08, SXS6D87PHE, 437FSG3419, 0Q0H13G8ZB]
about: [QB3Q5FBJ08]
sources:
  - url: https://en.wikipedia.org/wiki/Mixed_volume
---

## Statement

Let $n \ge 1$, let $K$ be a nonempty compact convex subset of $\R^n$ (a [[convex body|437FSG3419]]), and let $B$ be the [[closed unit ball|0Q0H13G8ZB]] of $\R^n$.
Then for every $t \ge 0$,
$$\operatorname{vol}(K + tB) = \sum_{j=0}^{n} \binom{n}{j} V(K[n - j], B[j]) \, t^j.$$
Here $K + tB$ is the [[Minkowski sum|SXS6D87PHE]] and $V$ is the [[mixed volume|QB3Q5FBJ08]].
The notation $K[n-j], B[j]$ means $K$ repeated $n - j$ times and $B$ repeated $j$ times.
In particular $\operatorname{vol}(K + tB)$ is a polynomial in $t$ of degree at most $n$.

## Remarks

The formula is the defining expansion of mixed volumes for $K$ and $B$, with $\lambda_1 = 1$ and $\lambda_2 = t$.
One groups the terms by the number of copies of $B$.
The coefficients $W_j(K) = V(K[n-j], B[j])$ are the [[quermassintegrals|H1K36H9ZWB]].
Rewritten with the [[intrinsic volumes|C2CK6KSSTV]] $V_j$, it reads $\operatorname{vol}(K + tB) = \sum_{j=0}^n \kappa_{n-j} V_j(K)\, t^{n-j}$, where $\kappa_m$ is the volume of the unit ball of $\R^m$.

Example: for a cube $K = [0, a]^3$ in $\R^3$,
$$\operatorname{vol}(K + tB) = a^3 + 6 a^2 t + 3 \pi a t^2 + \tfrac{4}{3} \pi t^3.$$
The terms come from the cube, six slabs over the faces, twelve quarter cylinders along the edges, and eight eighths of a ball at the corners.

Convexity is needed for a polynomial: for $K = \set{0, 1} \subseteq \R$ the length of $K + tB$ is $4t$ for $t \le \frac12$ and $1 + 2t$ for $t \ge \frac12$.

## Explanations

### L1 human

Thicken a convex shape by a margin $t$ on every side.
The volume of the thickened shape is a polynomial in $t$.
In the plane it is area plus perimeter times $t$ plus $\pi t^2$.
The coefficients are the basic size measurements of the shape: volume, surface area, and so on down to a constant.

### L2 human

The Steiner formula is the origin of quermassintegrals and intrinsic volumes.
It explains why surface area is a derivative of volume: $\frac{d}{dt} \operatorname{vol}(K + tB)$ at $t = 0$ is $n V(K[n-1], B)$, the surface area of $K$.
Combined with the [[Brunn–Minkowski theorem|9B02RPN7XD]] it yields the [[isoperimetric inequality|KBX8RBZ626]].
Its local versions lead to curvature measures, and a version for sets of positive reach is due to Federer.
