---
tag: XYWMB0G011
kind: definition
name: Conservation law
msc: [35L65, 35F20]
defines: 8RA7AMWSAF
uses: [GC5BDZ6QBC, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Conservation_law
---

## Definition

Let $n, m \ge 1$ and let $F = (F_1, \dots, F_n)$ with each $F_j \colon \R^m \to \R^m$ a $C^1$ function, called the *flux*.
The *system of conservation laws* with flux $F$ is the [[partial differential equation|GC5BDZ6QBC]]
$$\partial_t u + \sum_{j=1}^n \partial_{x_j} \big( F_j(u) \big) = 0$$
for an unknown $u \colon \R^n \times (0, \infty) \to \R^m$, where $\partial_t$ and $\partial_{x_j}$ are [[partial derivatives|09EGC6F8PT]].
For $m = 1$ it is called a *scalar conservation law*.
The components of $u$ are the *conserved quantities*.

## Remarks

The name comes from the integral form.
Let $u$ be a $C^1$ solution, and let $V \subseteq \R^n$ be a bounded region with smooth boundary and outer unit normal $\nu$.
Then
$$\frac{d}{dt} \int_V u \, dx = - \int_{\partial V} \sum_{j=1}^n F_j(u)\, \nu_j \, dS,$$
by the divergence theorem, so the total amount of $u$ in $V$ changes only through the flux across $\partial V$.
The integral form, or the equivalent weak form with test functions, still makes sense for discontinuous $u$, and it is the basis of weak solutions.

Example: the inviscid [[Burgers' equation|NEGHXN8RE1]] $u_t + (u^2/2)_x = 0$ is a scalar conservation law with $n = m = 1$ and $F(u) = u^2/2$.
The Euler equations of gas dynamics are a system with $m = n + 2$ conserved quantities: mass, momentum and energy.

Non-example: the equation $u_t + x\, u_x = 0$ is not of conservation form with a flux depending on $u$ only.
Indeed it equals $u_t + (x u)_x = u$, so the amount of $u$ is not conserved: $\int_\R u(x, t)\, dx$ grows like $e^{t}$ for integrable solutions, as $u(x, t) = g(x e^{-t})$ shows.
