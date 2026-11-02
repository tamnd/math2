---
tag: 19WY7FYPXK
kind: definition
name: Liouville's equation
msc: [35J61, 53A05]
defines: C8E0TWY3WT
uses: [RCNY89A4NY, 0E0B6RA8K0, SQVQ5DQT6W]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%27s_equation
---

## Definition

Let $\Omega \subseteq \R^2$ be an open set and let $K \in \R$ be a constant.
*Liouville's equation* on $\Omega$ is the [[semilinear|RCNY89A4NY]] equation
$$\Delta u + K e^{2u} = 0$$
for a twice continuously differentiable function $u \colon \Omega \to \R$, where $\Delta = \partial_x^2 + \partial_y^2$ is the [[Laplacian|0E0B6RA8K0]].

## Remarks

The metric $e^{2u}(dx^2 + dy^2)$ has [[Gaussian curvature|SQVQ5DQT6W]] $-e^{-2u} \Delta u$, so $u$ solves the equation exactly when this metric has constant curvature $K$.
Example: for $K = 1$, $u(x, y) = \log 2 - \log(1 + r^2)$ with $r^2 = x^2 + y^2$ is a solution on $\R^2$.
Indeed, $\Delta \log(1 + r^2) = 4/(1 + r^2)^2$, so $\Delta u = -4/(1 + r^2)^2 = -e^{2u}$.
Non-example: for $K = 1$, the function $u = 0$ is not a solution, since $\Delta u + e^{2u} = 1$.
Other normalizations are common: the substitution $u = v/2$ gives $\Delta v + 2K e^{v} = 0$, so the form $\Delta v + \lambda e^{v} = 0$ is equivalent.
Locally, the solutions for $K > 0$ are $u = \log\big( 2 \abs{f'} / (1 + K \abs{f}^2) \big)$ with $f$ a holomorphic function of $z = x + iy$ whose derivative has no zeros.
