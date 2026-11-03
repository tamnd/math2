---
tag: BFMW2Y3JD2
kind: definition
name: Elastodynamics
msc: [74H05, 74J05, 35Q74]
defines: T1PYEBKBAJ
uses: [6W00ZECYT0, SX32X1D537, 8QS6QMJF5Z, KG2XWEMJ30, 80737NDZ4V]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_elasticity
---

## Definition

Let a linear elastic body occupy a region $\Omega \subset \R^3$, with mass density $\rho > 0$ and [[elasticity tensor|SX32X1D537]] $C$.
Let $x \in \Omega$ and $t \ge 0$.
*Linear elastodynamics* is the study of displacement fields $u(x, t)$ that satisfy
$$\rho \, \frac{\partial^2 u_i}{\partial t^2} = \sum_{j} \frac{\partial \sigma_{ij}}{\partial x_j} + f_i, \qquad \sigma_{ij} = \sum_{k, l} C_{ijkl} \, \varepsilon_{kl}, \qquad \varepsilon_{kl} = \frac{1}{2} \left( \frac{\partial u_k}{\partial x_l} + \frac{\partial u_l}{\partial x_k} \right),$$
together with initial conditions for $u$ and $\partial_t u$ and boundary conditions on $\partial \Omega$.
Here $\sigma$ is the [[Cauchy stress|KG2XWEMJ30]], $\varepsilon$ is the small [[strain tensor|8QS6QMJF5Z]] and $f$ is the body force per unit volume.

## Remarks

For a homogeneous isotropic body with [[Lamé parameters|80737NDZ4V]] $\lambda$ and $\mu$ the equation of motion becomes the Navier–Cauchy equation
$$\rho \, \partial_t^2 u = (\lambda + \mu) \nabla (\nabla \cdot u) + \mu \Delta u + f.$$
Example: in an isotropic body, $u(x, t) = e_1 \sin(x_1 - c t)$ with $c^2 = (\lambda + 2\mu)/\rho$ and $f = 0$ solves this equation.
Indeed $\nabla(\nabla \cdot u) = \Delta u = -e_1 \sin(x_1 - ct)$, so the right side is $-(\lambda + 2\mu) e_1 \sin(x_1 - ct) = \rho \, \partial_t^2 u$.

Non-example: a static solution of [[linear elasticity|6W00ZECYT0]] under a time-dependent load that changes slowly, computed without the inertia term $\rho \, \partial_t^2 u$, is a quasi-static model and not elastodynamics.
