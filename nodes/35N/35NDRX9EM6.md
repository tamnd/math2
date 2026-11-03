---
tag: 35NDRX9EM6
kind: definition
name: Orr–Sommerfeld equation
msc: ["76E05", 76D05]
defines: G0ADVS0K99
uses: [18KXZHVF4M, JH9EJ0HA0R, H028A17Z55]
sources:
  - url: https://en.wikipedia.org/wiki/Orr–Sommerfeld_equation
---

## Definition

Consider a viscous incompressible fluid between two walls $y = y_1$ and $y = y_2$, with $y_1 < y_2$.
Let $U \colon [y_1, y_2] \to \R$ be a smooth function.
Assume that the parallel shear flow $\mathbf{u} = (U(y), 0, 0)$, with a suitable pressure, solves the dimensionless [[Navier–Stokes equations|18KXZHVF4M]] with [[Reynolds number|JH9EJ0HA0R]] $\mathrm{Re} > 0$.
Look for a two-dimensional disturbance with stream function $\psi(x, y, t) = \varphi(y) e^{i \alpha (x - c t)}$, where $\alpha > 0$ is the wavenumber and $c \in \C$ is the complex wave speed.
Linearising the Navier–Stokes equations about $U$ gives an equation for $\varphi$, the *Orr–Sommerfeld equation*:
$$(U - c)(\varphi'' - \alpha^2 \varphi) - U'' \varphi = \frac{1}{i \alpha \mathrm{Re}} \left( \varphi'''' - 2 \alpha^2 \varphi'' + \alpha^4 \varphi \right),$$
with the no-slip boundary conditions $\varphi = \varphi' = 0$ at $y = y_1$ and $y = y_2$.

## Remarks

For fixed $\alpha$ and $\mathrm{Re}$ this is an eigenvalue problem for $c$.
The disturbance grows in time when $\operatorname{Im} c > 0$, so the flow is linearly unstable when some eigenvalue has positive imaginary part.
This is the normal mode approach of [[hydrodynamic stability|H028A17Z55]].

Example: plane Poiseuille flow $U(y) = 1 - y^2$ on $[-1, 1]$ is a solution of the Navier–Stokes equations driven by a constant pressure gradient, so the equation applies with $U'' = -2$.
Numerical solution shows that an eigenvalue with $\operatorname{Im} c > 0$ first appears at $\mathrm{Re} \approx 5772$, based on the centre-line speed and the half-width.

Non-example: the equation $(U - c)(\varphi'' - \alpha^2 \varphi) - U'' \varphi = 0$ has no viscous term.
It is the Rayleigh equation, the formal limit $\mathrm{Re} \to \infty$, and it is a second-order equation that only allows the condition $\varphi = 0$ at the walls.
