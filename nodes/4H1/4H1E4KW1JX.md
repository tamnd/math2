---
tag: 4H1E4KW1JX
kind: definition
name: Hamilton–Jacobi equation
msc: [35F21, 70H20, 49L12]
defines: 5TRXQKP7DY
uses: [GC5BDZ6QBC, 0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Hamilton–Jacobi_equation
---

## Definition

Let $n \ge 1$ and let $H \colon \R^n \times \R^n \to \R$ be a continuous function, called the *Hamiltonian*.
Let $T \in (0, \infty]$.
The *Hamilton–Jacobi equation* with Hamiltonian $H$ is the [[partial differential equation|GC5BDZ6QBC]]
$$\partial_t u + H(\nabla u, x) = 0$$
for $u \colon \R^n \times (0, T) \to \R$.
Here $\nabla u$ is the [[gradient|0ABK9V9Y64]] of $u$ in $x$.
The *stationary* Hamilton–Jacobi equation is $H(\nabla u, x) = 0$ for $u$ defined on an open subset of $\R^n$.

## Remarks

Often $H$ does not depend on $x$, and the equation reads $u_t + H(\nabla u) = 0$, usually with an initial condition $u(x, 0) = g(x)$.
In mechanics the Hamiltonian also depends on time, and the equation is $\partial_t S + H(\nabla S, x, t) = 0$ for Hamilton's principal function $S$.
The [[Hamilton–Jacobi–Bellman equation|SJP9HW82VX]] of optimal control is a Hamilton–Jacobi equation whose Hamiltonian is an infimum or a supremum over controls.

Example: $H(p, x) = \tfrac12 \abs{p}^2$ and $u(x, t) = \dfrac{\abs{x}^2}{2(t + 1)}$ for $t > 0$.
Check: $\partial_t u = -\dfrac{\abs{x}^2}{2(t + 1)^2}$ and $\nabla u = \dfrac{x}{t + 1}$, so $\tfrac12 \abs{\nabla u}^2 = \dfrac{\abs{x}^2}{2(t + 1)^2}$ and the sum is $0$.

Non-example: the heat equation $u_t - \Delta u = 0$ is not a Hamilton–Jacobi equation, since it involves second derivatives of $u$.
Adding a term $-\varepsilon \Delta u$ to a Hamilton–Jacobi equation gives a viscous approximation, whose limits as $\varepsilon \to 0$ lead to viscosity solutions.
