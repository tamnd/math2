---
tag: WY4AG6FBBH
kind: definition
name: Retarded potential
msc: [78A25, 35Q61, 35L05]
defines: 9Q1NE5EP37
uses: [1AE7YGNX2R, SAEDXNM3Y1, 8PEMR2J7EF, YBHAVTWF82, EDBPDTG7BS]
sources:
  - url: https://en.wikipedia.org/wiki/Retarded_potential
---

## Definition

Let $\varepsilon_0, \mu_0 > 0$ be the vacuum permittivity and permeability, and let $c = 1/\sqrt{\varepsilon_0 \mu_0}$.
Let $\rho \colon \R^3 \times \R \to \R$ and $J \colon \R^3 \times \R \to \R^3$ be continuous charge and current densities that vanish outside a fixed bounded set of $\R^3$.
For $r, r' \in \R^3$ and $t \in \R$, the *retarded time* is $t_r = t - \abs{r - r'} / c$.
The *retarded potentials* are
$$\varphi(r, t) = \frac{1}{4 \pi \varepsilon_0} \int_{\R^3} \frac{\rho(r', t_r)}{\abs{r - r'}} \, d^3 r', \qquad A(r, t) = \frac{\mu_0}{4 \pi} \int_{\R^3} \frac{J(r', t_r)}{\abs{r - r'}} \, d^3 r'.$$

## Remarks

If $\rho$ and $J$ are twice continuously differentiable, then $\varphi$ and $A$ solve the [[inhomogeneous electromagnetic wave equations|1AE7YGNX2R]] $\square \varphi = \rho / \varepsilon_0$ and $\square A = \mu_0 J$, with $\square = \frac{1}{c^2} \partial_t^2 - \Delta$.
If moreover $\rho$ and $J$ satisfy the continuity equation $\partial_t \rho + \nabla \cdot J = 0$ of [[charge conservation|EDBPDTG7BS]], then they satisfy the [[Lorenz gauge condition|YBHAVTWF82]], and $E = -\nabla \varphi - \partial_t A$ and $B = \nabla \times A$ solve Maxwell's equations.
The kernel $\delta(t - \abs{r}/c) / (4 \pi \abs{r})$ behind these formulas is the retarded Green's function of $\square$.

Example: for a charge density $\rho$ that does not depend on time and $J = 0$, the delay has no effect.
Then $\varphi$ is the electrostatic potential $\frac{1}{4 \pi \varepsilon_0} \int \rho(r') / \abs{r - r'} \, d^3 r'$ and $A = 0$.

Non-example: the *advanced potentials* use the time $t + \abs{r - r'}/c$ in place of $t_r$.
They also solve the same wave equations, but they depend on the future of the sources, so they are not retarded potentials.

## Explanations

### L1 human

The formula looks like the Coulomb formula, with one change: each source point is read at an earlier time.
The delay is the distance to the field point divided by the speed of light.
This makes the potentials depend only on the past, as causality demands.
