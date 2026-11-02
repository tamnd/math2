---
tag: N6DZXEGD9D
kind: definition
name: Boltzmann equation
msc: [35Q20, 82C40]
defines: MH6CSWD7F0
uses: [GC5BDZ6QBC, 0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Boltzmann_equation
---

## Definition

Let $B \colon \R^3 \times S^2 \to [0, \infty)$ be a given function, the *collision kernel*, where $S^2$ is the unit sphere in $\R^3$.
For $v, v_* \in \R^3$ and $\sigma \in S^2$ put
$$v' = \frac{v + v_*}{2} + \frac{\abs{v - v_*}}{2} \sigma, \qquad v'_* = \frac{v + v_*}{2} - \frac{\abs{v - v_*}}{2} \sigma.$$
For a function $g \colon \R^3 \to \R$ the *collision operator* is
$$Q(g, g)(v) = \int_{\R^3} \int_{S^2} B(v - v_*, \sigma) \big( g(v') g(v'_*) - g(v) g(v_*) \big) \, d\sigma \, dv_*.$$
The *Boltzmann equation* is the [[partial differential equation|GC5BDZ6QBC]]
$$\partial_t f + v \cdot \nabla_x f = Q(f, f)$$
for an unknown function $f \colon [0, \infty) \times \R^3 \times \R^3 \to [0, \infty)$, $(t, x, v) \mapsto f(t, x, v)$.
The operator $Q$ acts on the variable $v$, and $\nabla_x$ is the [[gradient|0ABK9V9Y64]] in $x$.

## Remarks

The pair $(v', v'_*)$ runs over the velocities after an elastic collision of two particles with velocities $v$ and $v_*$: one has $v' + v'_* = v + v_*$ and $\abs{v'}^2 + \abs{v'_*}^2 = \abs{v}^2 + \abs{v_*}^2$.

Example: for $\rho, T > 0$ and $w \in \R^3$, the Maxwellian $M(v) = \rho (2\pi T)^{-3/2} e^{-\abs{v - w}^2/(2T)}$, constant in $t$ and $x$, is a solution.
The left side vanishes, and $M(v') M(v'_*) = M(v) M(v_*)$ by the two conservation laws above, so $Q(M, M) = 0$.

Non-example: $f(t, x, v) = t M(v)$ is not a solution, because $\partial_t f = M \ne 0$ while $v \cdot \nabla_x f = 0$ and $Q(f, f) = t^2 Q(M, M) = 0$.

For hard spheres the kernel is $B(z, \sigma) = c \abs{z}$ for a constant $c > 0$.
