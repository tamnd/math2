---
tag: ASJBB8RWS5
kind: definition
name: Magnetic monopole
msc: [78A25, 81V10, 35Q61]
defines: QQ7HF9X1GQ
uses: [9BWWD4QK8Y, XRED3C547P, 2K5D5HH89T, 0KPHENZ5S7]
sources:
  - url: https://en.wikipedia.org/wiki/Magnetic_monopole
---

## Definition

Let $\varepsilon_0, \mu_0 > 0$ and $c = 1/\sqrt{\varepsilon_0 \mu_0}$.
Maxwell's equations with magnetic sources are
$$\nabla \cdot E = \frac{\rho_e}{\varepsilon_0}, \qquad \nabla \cdot B = \mu_0 \rho_m, \qquad \nabla \times E = -\partial_t B - \mu_0 J_m, \qquad \nabla \times B = \mu_0 J_e + \frac{1}{c^2} \partial_t E,$$
where $\rho_e, J_e$ are the electric charge and current densities and $\rho_m, J_m$ are the magnetic charge and current densities.
A *magnetic monopole* of magnetic charge $q_m \neq 0$ at rest at the point $r_0 \in \R^3$ is the point source $\rho_m = q_m \, \delta(r - r_0)$, $J_m = 0$, where $\delta$ is the [[Dirac delta|0KPHENZ5S7]].
Its [[magnetic field|XRED3C547P]] is
$$B(r) = \frac{\mu_0 q_m}{4 \pi} \, \frac{r - r_0}{\abs{r - r_0}^3}.$$

## Remarks

In this convention $q_m$ is measured in ampere metres; another common convention, in webers, puts $\mu_0$ in other places.
With $\rho_m = 0$ and $J_m = 0$ the system is [[Maxwell's equations|9BWWD4QK8Y]], and the second equation is [[Gauss's law for magnetism|2K5D5HH89T]].

Example: the field above has $\nabla \cdot B = 0$ away from $r_0$, and its flux through any sphere around $r_0$ is $\frac{\mu_0 q_m}{4\pi} \cdot \frac{1}{R^2} \cdot 4 \pi R^2 = \mu_0 q_m$, as $\nabla \cdot B = \mu_0 q_m \delta(r - r_0)$ requires.

Non-example: a magnetic dipole, such as a small current loop, has zero net flux through every closed surface.
So its magnetic charge is $0$ and it is not a monopole.

On $\R^3 \setminus \set{r_0}$ the monopole field has no vector potential that is smooth on the whole set: by Stokes' theorem the flux through a sphere around $r_0$ would be $0$.
One can instead use two potentials, each smooth outside a half-line that starts at $r_0$, which differ by a gauge transformation where both are defined.

## Explanations

### L1 human

The definition adds magnetic charges and currents to Maxwell's equations, so that the two fields enter in a symmetric way.
A monopole is then a point magnetic charge.
Its field spreads out from the point and weakens with the square of the distance, exactly like the electric field of a point charge.
