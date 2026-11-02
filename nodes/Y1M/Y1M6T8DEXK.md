---
tag: Y1M6T8DEXK
kind: definition
name: Vlasov equation
msc: [35Q83, 82C40]
defines: SJH7M2VCTE
uses: [GC5BDZ6QBC, PVD7VZJZ9B, 0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Vlasov_equation
---

## Definition

Let $d \ge 1$, let $T > 0$, and let $F$ assign to each function $f \colon [0, T) \times \R^d \times \R^d \to [0, \infty)$ a force field $F[f] \colon [0, T) \times \R^d \to \R^d$.
The *Vlasov equation* with force $F$ is the [[partial differential equation|GC5BDZ6QBC]]
$$\partial_t f + v \cdot \nabla_x f + F[f](t, x) \cdot \nabla_v f = 0.$$
The unknown is a density $f(t, x, v) \ge 0$, and $\nabla_x$ and $\nabla_v$ are the [[gradients|0ABK9V9Y64]] in $x$ and in $v$.
The main case is the *Vlasov–Poisson system* in $d = 3$, where $\gamma \in \set{1, -1}$ and
$$F[f](t, x) = \frac{\gamma}{4\pi} \int_{\R^3} \frac{x - y}{\abs{x - y}^3} \rho(t, y) \, dy, \qquad \rho(t, y) = \int_{\R^3} f(t, y, v) \, dv.$$
The sign $\gamma = 1$ gives a repulsive force, as for a plasma of one species, and $\gamma = -1$ gives an attractive force, as for a self-gravitating system.

## Remarks

The force of the Vlasov–Poisson system is $F = -\gamma \nabla_x \phi$, where $-\Delta \phi = \rho$.
With a force that does not depend on $f$, the equation is a linear [[transport equation|PVD7VZJZ9B]] along the trajectories of $\dot x = v$, $\dot v = F$.

Example: for $d = 1$ and the external force $F(t, x) = -x$, every function $f(t, x, v) = h(x^2 + v^2)$ with $h$ differentiable is a stationary solution.
Indeed $v \, \partial_x f - x \, \partial_v f = 2xv \, h' - 2xv \, h' = 0$.

Non-example: with the same force, $f = h(x^2 + 2v^2)$ is not a solution when $h' \ne 0$, because $v \, \partial_x f - x \, \partial_v f = -2xv \, h'(x^2 + 2v^2)$.
