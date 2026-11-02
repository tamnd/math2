---
tag: EGQ3CJDH0D
kind: statement
role: theorem
name: Lebedev quadrature
msc: [65D32, 41A55, 33C55]
uses: [ADSVMCY77A, P9CM4GQ2T0, G5S1M9, 3F32Y21HP4]
about: [ADSVMCY77A]
sources:
  - url: https://en.wikipedia.org/wiki/Lebedev_quadrature
same_as:
  wikidata: Q6511268
  wikipedia: Lebedev quadrature
---

## Statement

Let $S^2 \subset \R^3$ be the unit [[sphere|P9CM4GQ2T0]] with its surface measure $\sigma$.
Let $\mathcal{O}_h$ be the [[group|G5S1M9]] of the $48$ orthogonal maps of $\R^3$ that map the cube $[-1, 1]^3$ onto itself.
Consider a rule $Q(f) = \sum_{x \in X} w_x f(x)$ on a finite set $X \subset S^2$ that is invariant: $g(X) = X$ and $w_{g(x)} = w_x$ for all $g \in \mathcal{O}_h$ and $x \in X$.
Let $p \ge 0$.
Then two conditions are equivalent.
The first is that $Q(f) = \int_{S^2} f \, d\sigma$ for every polynomial $f$ on $\R^3$ of degree at most $p$.
The second is that this holds for every such polynomial with $f \circ g = f$ for all $g \in \mathcal{O}_h$.

A *Lebedev quadrature* rule is an invariant rule of this kind with nodes on orbits of $\mathcal{O}_h$.
It is chosen to be exact for all polynomials of degree at most $p$.

## Remarks

Proof idea: for any $f$ let $\bar f = \frac{1}{48} \sum_{g \in \mathcal{O}_h} f \circ g$.
Both $Q$ and the integral are invariant under $\mathcal{O}_h$, so $Q(f) = Q(\bar f)$ and $\int f \, d\sigma = \int \bar f \, d\sigma$, and $\bar f$ is an invariant polynomial of the same degree bound.
This reduction is an instance of a theorem of Sobolev on invariant cubature.
It cuts the number of equations from about $(p+1)^2$, the dimension of the [[spherical harmonics|3F32Y21HP4]] of degree at most $p$, to the number of invariant ones.
Example: the $6$-point rule with nodes $\pm e_1, \pm e_2, \pm e_3$ and weights $\frac{4\pi}{6}$ is invariant.
On $S^2$ the invariant polynomials of degree at most $3$ are constants, because odd ones change sign under $x \mapsto -x$ and the only invariant quadratic is $x_1^2 + x_2^2 + x_3^2 = 1$.
Since the weights add up to $4\pi = \sigma(S^2)$, the rule is exact up to degree $3$; it fails for $x_1^4$, where it gives $\frac{4\pi}{3}$ instead of $\frac{4\pi}{5}$.

## Explanations

### L1 human

Lebedev quadrature approximates an average over the surface of a sphere by a weighted sum over a few well-placed points.
The points are arranged with the symmetry of a cube, which makes the rule fair in all directions.
Thanks to that symmetry, only a few conditions need to be checked to make the rule exact for all polynomials up to a given degree.

### L2 human

Vyacheslav Lebedev computed such rules with many points and high degree, and they are standard in quantum chemistry, where integrals over directions appear in density functional theory.
Compared with product rules in spherical coordinates, they use fewer points for the same degree and do not crowd points near the poles.
The underlying principle, reducing exactness to the invariant functions of a symmetry group, is used for cubature on many other domains.
