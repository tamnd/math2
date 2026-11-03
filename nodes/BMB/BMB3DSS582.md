---
tag: BMB3DSS582
kind: definition
name: Smoothed-particle hydrodynamics
msc: [76M28, 65M75]
defines: S9DG3SNXCV
uses: [T4ZFKBZRYK, RW0JK9VDZE, ZV65XMJ9A4]
sources:
  - url: https://en.wikipedia.org/wiki/Smoothed-particle_hydrodynamics
---

## Definition

Let $W \colon \R^d \times (0, \infty) \to [0, \infty)$ be a *smoothing kernel*, that is, a smooth function $W(x, h)$ that is radial in $x$.
It satisfies $\int_{\R^d} W(x, h) \, dx = 1$ for every $h > 0$, and it tends to the Dirac delta as $h \to 0$.
*Smoothed-particle hydrodynamics* (SPH) approximates a fluid by $N$ particles with masses $m_a$, positions $x_a(t)$ and velocities $\mathbf{v}_a(t)$, for $a = 1, \dots, N$, as follows.

1. A field $A$ is approximated by $A(x) \approx \sum_b \frac{m_b}{\rho_b} A_b \, W(x - x_b, h)$, where $A_b$ and $\rho_b$ are the values at particle $b$.
2. The density at particle $a$ is $\rho_a = \sum_b m_b \, W(x_a - x_b, h)$.
3. The particles move with the flow, $\dot{x}_a = \mathbf{v}_a$, and, for the [[Euler equations|RW0JK9VDZE]] of a barotropic fluid with pressure $p_a = P(\rho_a)$, their accelerations are
$$\dot{\mathbf{v}}_a = -\sum_b m_b \left( \frac{p_a}{\rho_a^2} + \frac{p_b}{\rho_b^2} \right) \nabla_a W(x_a - x_b, h).$$

## Remarks

Clause 2 is clause 1 for $A = \rho$; it is the same formula as a [[kernel density estimate|ZV65XMJ9A4]] in statistics, with weights $m_b$.
Since $W$ is radial, $\nabla_a W(x_a - x_b, h) = -\nabla_b W(x_b - x_a, h)$, so the force of $b$ on $a$ is opposite to the force of $a$ on $b$, and the total momentum $\sum_a m_a \mathbf{v}_a$ is conserved exactly.
Example: a common kernel is the Gaussian $W(x, h) = (\pi h^2)^{-d/2} e^{-\abs{x}^2 / h^2}$, whose integral is $1$.
With particles of mass $m = \rho_0 \delta$ on a one-dimensional lattice of spacing $\delta$ much smaller than $h$, clause 2 gives $\rho_a \approx \rho_0 \int W \, dx = \rho_0$, as it should for a uniform fluid.
Non-example: a finite volume scheme on a fixed grid is not SPH, since its unknowns are cell averages, not moving particles.
In practice, kernels with compact support, such as cubic splines, are used so that each particle interacts with few neighbours.
