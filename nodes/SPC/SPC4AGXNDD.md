---
tag: SPC4AGXNDD
kind: definition
name: Stellar dynamics
msc: [85A05, 70F10]
defines: 4V8BT1ZD00
uses: [29WRN5J730, SJH7M2VCTE, DWK5N5SKTK]
sources:
  - url: https://en.wikipedia.org/wiki/Stellar_dynamics
---

## Definition

*Stellar dynamics* is the study of self-gravitating systems of $N$ point masses, called stars, with $N$ large.
The exact model is the $N$-body problem.
Stars of masses $m_i$ at positions $x_i(t) \in \R^3$, $i = 1, \dots, N$, obey [[Newton's law of gravitation|29WRN5J730]]
$$\ddot x_i = -\sum_{j \ne i} \frac{G m_j (x_i - x_j)}{\abs{x_i - x_j}^3},$$
where $G$ is the gravitational constant.
The collisionless model describes the system by a mass density $f(t, x, v) \ge 0$ in phase space.
This density solves the [[Vlasov equation|SJH7M2VCTE]]
$$\partial_t f + v \cdot \nabla_x f - \nabla_x \Phi \cdot \nabla_v f = 0,$$
where the potential $\Phi$ solves [[Poisson's equation|DWK5N5SKTK]] $\Delta \Phi = 4\pi G \rho$ with $\rho(t, x) = \int_{\R^3} f(t, x, v) \, dv$.

## Remarks

In stellar dynamics the Vlasov equation with a gravitational potential is usually called the *collisionless Boltzmann equation*.
The collisionless model is a good approximation for times shorter than the two-body relaxation time.
For a galaxy this time is much longer than the age of the universe, and for a globular cluster it is shorter than its age.

Example: a single star in the fixed potential $\Phi(x) = \frac{1}{2} \omega^2 \abs{x}^2$ of a homogeneous sphere moves on an ellipse centred at the origin.
Any $f$ that depends only on $\frac{1}{2}\abs{v}^2 + \Phi(x)$ is a steady solution of the Vlasov equation in this potential.

Non-example: in a gas cloud, particles collide often and exchange momentum.
Its dynamics is described by the Navier–Stokes equations, not by a collisionless model, and is not part of stellar dynamics.
