---
tag: TDSM4KTT0D
kind: definition
name: Stokeslet
msc: [76D07, 35Q35]
defines: QMTKCY36JE
uses: [13CB7V2YM4, K2NK9A8M5F, 0KPHENZ5S7]
sources:
  - url: https://en.wikipedia.org/wiki/Stokes_flow
---

## Definition

Let $\mu > 0$ be the dynamic viscosity and let $F \in \R^3$ be a vector, the point force.
For $x \in \R^3 \setminus \set{0}$ write $r = \abs{x}$.
The *Stokeslet* with force $F$ at the origin is the pair $(u, p)$ given by
$$u(x) = \frac{1}{8 \pi \mu} \Big( \frac{F}{r} + \frac{(F \cdot x) \, x}{r^3} \Big), \qquad p(x) = \frac{F \cdot x}{4 \pi r^3}.$$
Let $\delta_0$ be the [[Dirac delta|0KPHENZ5S7]] at the origin.
The Stokeslet is the solution, decaying at infinity, of the Stokes equations with a point force in the sense of distributions:
$$-\mu \Delta u + \nabla p = F \, \delta_0, \qquad \nabla \cdot u = 0 \quad \text{in } \R^3.$$
The matrix $G_{ij}(x) = \frac{1}{8 \pi \mu} \big( \frac{\delta_{ij}}{r} + \frac{x_i x_j}{r^3} \big)$ with $u = G F$ is the *Oseen tensor*.

## Remarks

Example check, away from the origin: $\sum_i \partial_i (x_i x_j / r^3) = (3 + 1) x_j / r^3 - 3 x_j / r^3 = x_j / r^3$, and $\partial_j (1 / r) = -x_j / r^3$.
So $\nabla \cdot u = 0$ for $x \ne 0$.

Non-example: the field $u = F / (8 \pi \mu r)$ alone is not divergence-free, since $\nabla \cdot u = -(F \cdot x) / (8 \pi \mu r^3)$, so it fails the second equation.

The Stokeslet is the [[fundamental solution|K2NK9A8M5F]] of the [[Stokes equations|13CB7V2YM4]], and the flow due to a force density $f$ is $u = \int G(x - y) f(y) \, dy$.
In two dimensions the Stokeslet grows like $\log r$, which is the root of [[Stokes' paradox|M1KHFRHCC1]].
