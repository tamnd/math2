---
tag: TYASZ4R507
kind: statement
role: theorem
name: Kolosov–Muskhelishvili formulas
msc: [74B05, 74G05]
uses: [6W00ZECYT0, JQT1GBRYTY, AS7WQTM99W, J2GWW1NPTC, NWYZ9QBA84]
about: [6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_elasticity
---

## Statement

Let $\Omega \subset \C$ be a simply connected domain, with points written $z = x + iy$.
Consider a homogeneous isotropic body in [[linear elasticity|6W00ZECYT0]] in a state of [[plane strain|JQT1GBRYTY]] or [[plane stress|AS7WQTM99W]] over $\Omega$, with no body forces.
Let $\mu$ be the [[shear modulus|J2GWW1NPTC]] and $\nu$ the [[Poisson's ratio|NWYZ9QBA84]], and set $\kappa = 3 - 4\nu$ for plane strain and $\kappa = (3 - \nu)/(1 + \nu)$ for plane stress.
Let $u = (u_x, u_y)$ be the displacement and $\sigma_{xx}, \sigma_{yy}, \sigma_{xy}$ the stresses of a smooth equilibrium solution.
Then there are holomorphic functions $\varphi$ and $\psi$ on $\Omega$ such that
$$\sigma_{xx} + \sigma_{yy} = 2\left(\varphi'(z) + \overline{\varphi'(z)}\right) = 4 \operatorname{Re} \varphi'(z),$$
$$\sigma_{yy} - \sigma_{xx} + 2i\sigma_{xy} = 2\left(\bar z \varphi''(z) + \psi'(z)\right),$$
$$2\mu (u_x + i u_y) = \kappa \varphi(z) - z \overline{\varphi'(z)} - \overline{\psi(z)}.$$
Conversely, let $\varphi, \psi$ be any holomorphic functions on $\Omega$.
Then these formulas define a displacement and a stress field that solve the equations of plane linear elasticity without body forces.

## Remarks

The proof starts from the [[Airy stress function|7ZGSJRYBGK]] $\Phi$, which is biharmonic in the absence of body forces.
Every real biharmonic function on a simply connected domain can be written as $\Phi = \operatorname{Re}\left(\bar z \varphi(z) + \chi(z)\right)$ with $\varphi, \chi$ holomorphic, and one puts $\psi = \chi'$.
The stresses are second derivatives of $\Phi$, which gives the first two formulas; integrating Hooke's law gives the third.
The stress determines the pair only up to $\varphi \mapsto \varphi + iCz + a$ and $\psi \mapsto \psi + b$, with $C$ real and $a, b$ complex constants.
These changes add a rigid motion to the displacement.
On a multiply connected domain the functions may have logarithmic and multivalued terms, and single-valuedness of the displacement gives extra conditions.
For example, $\varphi(z) = Az$ and $\psi(z) = Bz$ with $A$ real and $B$ complex give a uniform stress state with $\sigma_{xx} + \sigma_{yy} = 4A$.

## Explanations

### L1 human

In a flat elastic plate the stresses and displacements obey a system of partial differential equations.
These formulas show that every solution comes from just two complex functions that are holomorphic.
Hard elasticity problems then become problems of complex analysis, where conformal maps and Cauchy integrals are available.

### L2 human

The formulas are the starting point of Muskhelishvili's method for plane problems.
Boundary conditions on tractions or on displacements become boundary conditions on $\varphi$ and $\psi$.
For a disc, or a domain mapped onto a disc by a known conformal map, they can be solved with power series or Cauchy integrals.
Classical results such as the stress concentration around a circular or elliptic hole and the stress field near a crack tip are derived this way.
The constant $\kappa$ is the only place where the choice between plane strain and plane stress enters.
