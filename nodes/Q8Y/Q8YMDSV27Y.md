---
tag: Q8YMDSV27Y
kind: statement
role: theorem
name: Somigliana identity
msc: [74B05, 74S15]
uses: [6W00ZECYT0, GQ3K59MRJP, SG3RXYFQ3B, E0WD2ATFZD, KG2XWEMJ30]
about: [6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Boundary_element_method
---

## Statement

Let $\Omega \subset \R^3$ be a bounded domain with smooth boundary $\partial\Omega$ and outward unit normal $n$.
Let the material be homogeneous, isotropic and linear elastic with shear modulus $\mu > 0$ and Poisson's ratio $\nu$ with $-1 < \nu < \tfrac12$.
Let $f$ be a continuous body force on $\overline{\Omega}$.
Let $u \in C^2(\overline{\Omega})^3$ solve the [[Navier–Cauchy equations|GQ3K59MRJP]] $\mu \Delta u + \frac{\mu}{1 - 2\nu} \nabla(\nabla \cdot u) + f = 0$ in $\Omega$.
Let $\sigma$ be the [[stress|KG2XWEMJ30]] of $u$, and let $t = \sigma n$ be its traction on $\partial\Omega$.
For $x \neq y$, let $r = \abs{y - x}$ and let
$$U_{ik}(x, y) = \frac{1}{16\pi\mu(1 - \nu)\, r}\left( (3 - 4\nu)\,\delta_{ik} + \frac{(y_i - x_i)(y_k - x_k)}{r^2} \right)$$
be the [[Kelvin solution|SG3RXYFQ3B]].
It is the $i$-th displacement component at $y$ caused by a unit point force at $x$ in direction $k$ in an infinite body.
Let $T_{ik}(x, y)$ be the $i$-th component of the traction at $y \in \partial\Omega$, on the surface with normal $n(y)$, of the same displacement field.
Then for every $x \in \Omega$ and $k = 1, 2, 3$,
$$u_k(x) = \int_{\partial\Omega} \Big( U_{ik}(x, y)\, t_i(y) - T_{ik}(x, y)\, u_i(y) \Big)\, dS_y + \int_\Omega U_{ik}(x, y)\, f_i(y)\, dy,$$
with summation over $i = 1, 2, 3$.

## Remarks

The proof applies [[Betti's reciprocal theorem|E0WD2ATFZD]] to $u$ and the Kelvin field on $\Omega$ with a small ball $B_\rho(x)$ removed.
On the small sphere, the traction of the Kelvin field is of order $\rho^{-2}$ while the area is of order $\rho^2$.
In the limit $\rho \to 0$ this term gives $u_k(x)$, and the other terms on the sphere tend to $0$.
The identity is the elastic analogue of Green's representation formula for harmonic functions.
Letting $x$ tend to a smooth boundary point gives a boundary integral equation with the factor $\tfrac12 u_k(x)$ on the left, and the second integral is then a Cauchy principal value.
This boundary equation is the basis of the [[boundary element method|4KPQ61JGD5]] in elastostatics.

## Explanations

### L1 human

The identity says that the displacement at any point inside an elastic body is determined by the displacements and forces on its surface, plus the body forces.
Each piece of surface acts as if it pushed on an infinite body with a point force, and the effects are added up.
So to know the inside one only needs to know the boundary.

### L2 human

The identity plays for the Navier–Cauchy equations the role that Green's third identity plays for the Laplace equation.
In the boundary element method one takes $x$ to the boundary, so the identity becomes an integral equation linking the unknown boundary displacements and tractions.
Half of these are given by the boundary conditions, and solving for the rest gives the full solution through the identity.
It also gives integral formulas for stresses inside the body by differentiating in $x$.
