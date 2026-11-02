---
tag: GRBZT7SWK0
kind: definition
name: Finite element exterior calculus
msc: [65N30, 65N12, 58A12]
defines: 2T8MYCZ7N4
uses: [0E3G0GRPZ6, 0ZHSTAG8ZY, GX74C07T0G, HM2HHE3J51, 98GZ9DVHTA, 87VMQ892VW, PWG3GKZG80]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_element_exterior_calculus
---

## Definition

Let $\Omega \subset \R^n$ be a bounded Lipschitz polyhedral domain.
For $0 \le k \le n$, let $H\Lambda^k(\Omega)$ be the [[differential $k$-forms|0E3G0GRPZ6]] $\omega$ with $\omega \in L^2$ and $d\omega \in L^2$.
Here $d$ is the [[exterior derivative|0ZHSTAG8ZY]] in the weak sense.
These [[Hilbert spaces|HM2HHE3J51]] form the $L^2$ de Rham complex $H\Lambda^0 \xrightarrow{d} H\Lambda^1 \xrightarrow{d} \cdots \xrightarrow{d} H\Lambda^n$.
*Finite element exterior calculus* discretizes this complex by a family of spaces $V_h^k \subseteq H\Lambda^k(\Omega)$, indexed by a mesh parameter $h$, with three properties:

1. each $V_h^k$ is a [[finite element|98GZ9DVHTA]] space of piecewise polynomial $k$-forms on a simplicial mesh of $\Omega$;
2. subcomplex: $d V_h^k \subseteq V_h^{k+1}$ for each $k$;
3. bounded cochain projections: there are projections $\pi_h^k$ onto $V_h^k$ with $d \pi_h^k = \pi_h^{k+1} d$.

The projections in clause 3 are required to be bounded in $L^2$ uniformly in $h$.
The method is the [[mixed|87VMQ892VW]] Galerkin method for the [[Hodge Laplacian|PWG3GKZG80]] on these spaces.

## Remarks

The standard families are $\mathcal{P}_r \Lambda^k$ and $\mathcal{P}_r^- \Lambda^k$ of polynomial $k$-forms.
Example: in $\R^3$, take continuous piecewise linear functions, lowest-order Nédélec edge elements, lowest-order Raviart–Thomas face elements, and piecewise constants.
The gradient of a piecewise linear function is piecewise constant with continuous tangential part, so it lies in the Nédélec space.
The other inclusions hold for the same reason, and the canonical interpolation operators commute with $d$.
Under clauses 2 and 3 the discrete complex has the same [[cohomology|GX74C07T0G]] as the continuous one, and discrete Poincaré inequalities hold uniformly in $h$.

Non-example: take continuous piecewise quadratics for $V_h^0$ and lowest-order Nédélec edge elements for $V_h^1$.
The lowest-order Nédélec fields on a tetrahedron have the form $a + b \times x$.
The gradient of a quadratic such as $x_1^2$ is $(2 x_1, 0, 0)$, which is not of this form, so clause 2 fails.
