---
tag: T9ZNP5F24M
kind: statement
role: theorem
name: Cauchy momentum equation
msc: [74A10, 76A02]
uses: [KG2XWEMJ30, XYSHP47B2N, SBCV6VZG6D, 3CE48D4MWW, CJW50K5HZB, 0MWV6ZTK6S, 0JX86PSSA9]
about: [KG2XWEMJ30]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_momentum_equation
same_as:
  wikidata: Q4178434
  wikipedia: Cauchy momentum equation
---

## Statement

Let a body move with a $C^2$ motion, with mass density $\rho$ and Eulerian velocity $v$ of class $C^1$.
Let $b$, the body force per unit mass, be continuous.
Assume that the mass of every part is constant in time, and that the [[Cauchy stress tensor|KG2XWEMJ30]] field $\sigma$ is of class $C^1$.
Assume that the balance of linear momentum of [[Euler's laws of motion|SBCV6VZG6D]] holds for every part.
Let $(\operatorname{div} \sigma)_i = \sum_{j} \partial \sigma_{ij} / \partial x_j$ be the row-wise [[divergence|0MWV6ZTK6S]] of $\sigma$.
Then the following holds at every point $x$ of the current configuration and every time $t$.
$$\rho \left( \frac{\partial v}{\partial t} + (v \cdot \nabla) v \right) = \operatorname{div} \sigma + \rho b.$$

## Remarks

The left side is $\rho$ times the [[material derivative|CJW50K5HZB]] of $v$, the acceleration of the particle at $x$.
For the proof, the [[Reynolds transport theorem|3CE48D4MWW]] and conservation of mass give $\frac{d}{dt} \int_{P_t} \rho v\, dV = \int_{P_t} \rho \frac{Dv}{Dt}\, dV$.
[[Cauchy's stress theorem|XYSHP47B2N]] and the [[divergence theorem|0JX86PSSA9]] turn the surface force into $\int_{P_t} \operatorname{div} \sigma\, dV$.
The resulting integral identity holds for every part, so the continuous integrand vanishes.
For a fluid at rest, $\sigma = -p I$ and $v = 0$, and the equation becomes the hydrostatic law $\nabla p = \rho b$; with gravity $b = -g e_3$, pressure grows linearly with depth when $\rho$ is constant.
The equation is not closed: it needs a constitutive equation for $\sigma$; with a Newtonian fluid it becomes the Navier–Stokes equations, and with linear elasticity the Navier–Cauchy equations.

## Explanations

### L1 human

This is Newton's law "mass times acceleration equals force" written for every point of a continuous body.
The force per volume has two sources: differences of stress between neighbouring points, measured by $\operatorname{div} \sigma$, and outside forces such as gravity.

### L2 human

The Cauchy momentum equation is the common starting point of fluid dynamics and solid dynamics.
In the Lagrangian description it reads $\rho_0 \ddot{\varphi} = \operatorname{Div} P + \rho_0 b$, with the first Piola–Kirchhoff stress $P$ and the reference density $\rho_0$.
In statics the left side vanishes, and the equilibrium equation $\operatorname{div} \sigma + \rho b = 0$ is the basic equation of structural analysis.
