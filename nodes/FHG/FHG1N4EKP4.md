---
tag: FHG1N4EKP4
kind: statement
role: theorem
name: Chern–Moser normal form
msc: [32V05, 32V40]
uses: [80MTNXWW80, ZC78JKZX9S]
about: [ZC78JKZX9S]
sources:
  - url: https://en.wikipedia.org/wiki/CR_manifold
---

## Statement

Let $n \ge 1$ and let $M$ be a real-analytic real hypersurface in $\C^{n+1}$.
Let $p \in M$, and assume that the [[Levi form|80MTNXWW80]] of $M$ at $p$ is nondegenerate, with $r$ positive and $n - r$ negative eigenvalues.
Write $\langle z, z \rangle = \sum_{j=1}^{n} \varepsilon_j \abs{z_j}^2$, where $\varepsilon_j = 1$ for $j \le r$ and $\varepsilon_j = -1$ for $j > r$, and let $\operatorname{tr} = \sum_{j=1}^{n} \varepsilon_j \frac{\partial^2}{\partial z_j \partial \bar z_j}$.
Then there are local holomorphic coordinates $(z, w) \in \C^n \times \C$ centred at $p$, with $w = u + iv$, in which $M$ is given near $p$ by
$$v = \langle z, z \rangle + \sum_{k, l \ge 2} F_{kl}(z, \bar z, u),$$
where:

1. each $F_{kl}$ is a polynomial of degree $k$ in $z$ and $l$ in $\bar z$, with coefficients real-analytic in $u$, and $F_{lk} = \overline{F_{kl}}$;
2. $\operatorname{tr} F_{22} = 0$, $\operatorname{tr}^2 F_{32} = 0$ and $\operatorname{tr}^3 F_{33} = 0$.

## Remarks

The result is due to S.-S. Chern and J. Moser.
The proof removes, degree by degree, all terms of the defining equation that can be killed by a holomorphic change of coordinates; the remaining terms are the normal form.
The model case is the hyperquadric $v = \langle z, z \rangle$, where all $F_{kl}$ vanish; for $r = n$ it is biholomorphic to the unit sphere minus a point.
The normalising coordinates are not unique: they are determined up to the action of the group of local biholomorphisms that preserve the hyperquadric.
For $n = 1$ the trace conditions force $F_{22} = F_{32} = F_{33} = 0$, so the first term that may survive is $F_{24}$, which carries the invariant found earlier by É. Cartan.
Without the nondegeneracy of the Levi form the quadratic part $\langle z, z \rangle$ is degenerate and this normal form does not apply.

## Explanations

### L1 human

Two hypersurfaces in complex space may look different but be the same after a holomorphic change of coordinates.
The theorem gives a standard way to write such a hypersurface near a point, so that the remaining coefficients are true geometric information.
The leading part is a quadratic "complex paraboloid", and the corrections are put into a reduced shape by fixed trace conditions.

### L2 human

The normal form solves the local equivalence problem for real-analytic Levi-nondegenerate hypersurfaces.
Two such germs are equivalent exactly when their normal forms agree up to the stability group of the hyperquadric.
Chern and Moser also gave a geometric approach that builds a Cartan connection on a bundle over $M$, whose curvature yields the local invariants.
These invariants show for instance that a generic small perturbation of the sphere is not locally biholomorphic to the sphere.
The method is a complex analogue of the use of normal coordinates in Riemannian geometry.
