---
tag: NFM5VN2WH9
kind: definition
name: Poisson's equation in electrostatics
msc: [78A30, 35J05]
defines: FC64B1A65B
uses: [DWK5N5SKTK, SAEDXNM3Y1, 6XPSV47R56, 0E0B6RA8K0, S8RG6N1PRT]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson%27s_equation
---

## Definition

Let $\varepsilon_0 > 0$ be the vacuum permittivity, let $U \subseteq \R^3$ be an open set, and let $\rho \colon U \to \R$ be a given [[charge density|6XPSV47R56]].
*Poisson's equation of electrostatics* on $U$ is the equation
$$\Delta \varphi = -\frac{\rho}{\varepsilon_0}$$
for an unknown function $\varphi \colon U \to \R$, the electrostatic potential.
Here $\Delta$ is the [[Laplacian|0E0B6RA8K0]].
A classical solution is a twice continuously differentiable $\varphi$ that satisfies the equation at every point of $U$.

## Remarks

It is [[Poisson's equation|DWK5N5SKTK]] $\Delta u = f$ with $f = -\rho / \varepsilon_0$.
In a region without charge it becomes [[Laplace's equation|S8RG6N1PRT]] $\Delta \varphi = 0$.
If $\rho$ is twice continuously differentiable with compact support, then the Coulomb [[electric potential|SAEDXNM3Y1]] of $\rho$ is a classical solution on $\R^3$.
Example: a ball of radius $R$ with constant density $\rho_0$ has, inside the ball, the potential $\varphi(x) = \rho_0 (3R^2 - \abs{x}^2) / (6 \varepsilon_0)$.
The check: $\Delta \abs{x}^2 = 6$ in $\R^3$, so $\Delta \varphi = -\rho_0 / \varepsilon_0$.
Non-example: $\varphi(x) = \rho_0 \abs{x}^2 / (6 \varepsilon_0)$ has $\Delta \varphi = +\rho_0 / \varepsilon_0$, so it has the wrong sign.
In Gaussian units the equation reads $\Delta \varphi = -4 \pi \rho$.
