---
tag: 2NVEYM6HN9
kind: definition
name: Jordan–Kinderlehrer–Otto scheme
msc: [49Q22, 35Q84, 35K05]
defines: 3MWNBBG9EH
uses: [VEY29CS26X, 059TJN0NZ1]
sources:
  - url: https://en.wikipedia.org/wiki/Wasserstein_metric
---

## Definition

Let $\mathcal{P}_2(\R^n)$ be the set of Borel [[probability measures|059TJN0NZ1]] on $\R^n$ with finite second moment, with the [[Wasserstein distance|VEY29CS26X]] $W_2$.
Let $F \colon \mathcal{P}_2(\R^n) \to (-\infty, +\infty]$ be a functional, let $\tau > 0$ be a time step, and let $\rho_0 \in \mathcal{P}_2(\R^n)$ with $F(\rho_0) < \infty$.
The *Jordan–Kinderlehrer–Otto scheme* for $F$ with step $\tau$ is a sequence $(\rho_k^\tau)_{k \ge 0}$ in $\mathcal{P}_2(\R^n)$ with $\rho_0^\tau = \rho_0$.
For each $k \ge 0$, the measure $\rho_{k+1}^\tau$ is required to minimize the functional
$$\rho \mapsto F(\rho) + \frac{1}{2\tau} W_2(\rho, \rho_k^\tau)^2$$
over $\mathcal{P}_2(\R^n)$.
The associated discrete flow is the piecewise constant curve $\rho^\tau(t) = \rho_k^\tau$ for $t \in [k\tau, (k + 1)\tau)$.

## Remarks

Example: let $\beta > 0$, let $\Psi \colon \R^n \to [0, \infty)$ be smooth with $\abs{\nabla \Psi(x)} \le C(\Psi(x) + 1)$ for a constant $C$, and let
$$F(\rho) = \int \Psi \rho \, dx + \beta^{-1} \int \rho \log \rho \, dx$$
for $\rho$ with a density, and $F(\rho) = +\infty$ otherwise.
Jordan, Kinderlehrer and Otto proved that minimizers exist at each step, and that $\rho^\tau$ converges, as $\tau \to 0$, to the solution of the Fokker–Planck equation $\partial_t \rho = \operatorname{div}(\rho \nabla \Psi) + \beta^{-1} \Delta \rho$ with initial datum $\rho_0$.
With $\Psi = 0$ and $\beta = 1$ this gives the heat equation $\partial_t \rho = \Delta \rho$.

Non-example: replacing $W_2$ by the $L^2$ distance between densities gives a different scheme, the implicit Euler scheme for the $L^2$ gradient flow.
For the entropy $\int \rho \log \rho$ this flow is $\partial_t \rho = -(\log \rho + 1)$, which is not the heat equation.

The step is the Wasserstein analogue of the implicit Euler step $x_{k+1} \in \operatorname{argmin}_x \left( f(x) + \frac{1}{2\tau} \abs{x - x_k}^2 \right)$ for the gradient flow $\dot x = -\nabla f(x)$ in $\R^n$.
