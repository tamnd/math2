---
tag: SBNNV3AB5Z
kind: definition
name: Covariant formulation of classical electromagnetism
msc: [78A25, 83A05, 35Q61]
defines: H65N7N36K2
uses: [A34AF4ZVKM, WRZJRJS44W, BQFCNWFV9Q, EDBPDTG7BS, 9BWWD4QK8Y, S3RZRCH0T5]
sources:
  - url: https://en.wikipedia.org/wiki/Covariant_formulation_of_classical_electromagnetism
---

## Definition

Work in Minkowski space with coordinates $x^0 = ct, x^1, x^2, x^3$, metric $\eta = \operatorname{diag}(1, -1, -1, -1)$ and summation over repeated indices.
The *covariant formulation of classical electromagnetism* is the following system of laws.

1. The sources form the four-current $J^\mu = (c \rho, J_1, J_2, J_3)$, where $\rho$ is the charge density and $J$ the current density.
2. The field is the [[electromagnetic tensor|WRZJRJS44W]] $F^{\mu\nu}$, which obeys
$$\partial_\mu F^{\mu\nu} = \mu_0 J^\nu, \qquad \partial_\lambda F_{\mu\nu} + \partial_\mu F_{\nu\lambda} + \partial_\nu F_{\lambda\mu} = 0.$$
3. A particle of charge $q$ and rest mass $m$, with four-velocity $u^\mu = dx^\mu / d\tau$ for its proper time $\tau$, moves by
$$m \frac{du^\mu}{d\tau} = q F^{\mu\nu} u_\nu.$$

## Remarks

The two field equations are equivalent to the four [[Maxwell's equations|9BWWD4QK8Y]], and the equation of motion has the [[Lorentz force|S3RZRCH0T5]] law $\frac{d}{dt} (m \gamma v) = q (E + v \times B)$ as its spatial part.
The time component $\mu = 0$ of the equation of motion gives the rate of change of energy, $q E \cdot v$.

Since $F^{\mu\nu}$ is antisymmetric, $\partial_\nu \partial_\mu F^{\mu\nu} = 0$, so the first field equation implies $\partial_\nu J^\nu = 0$, which is [[charge conservation|EDBPDTG7BS]].
On a contractible region, such as all of Minkowski space, the homogeneous equation holds exactly when $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ for a [[four-potential|BQFCNWFV9Q]] $A$.
The inhomogeneous equation is the Euler–Lagrange equation, in the variable $A_\mu$, of the Lagrangian density $-\frac{1}{4 \mu_0} F_{\mu\nu} F^{\mu\nu} - J^\mu A_\mu$.

Example: the field of a charge at rest has only electric components.
A Lorentz boost along $x^1$ maps it to a field with nonzero magnetic components, the field of a moving charge.

Non-example: Maxwell's equations written with the three-vectors $E$ and $B$ describe the same physics but are not in covariant form.
The reason is that $E$ and $B$ are not the components of four-vectors.
