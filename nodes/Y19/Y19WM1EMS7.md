---
tag: Y19WM1EMS7
kind: definition
name: Robin boundary condition
msc: [34B05, 35J25, 34B24]
defines: 581AGFCCRX
uses: [TM8VQJWGHZ, EETVA6QYX4, GS3KT2H645, 0WQJJCCTC8]
sources:
  - url: https://en.wikipedia.org/wiki/Robin_boundary_condition
---

## Definition

Let $\Omega \subseteq \R^d$ be a bounded domain, that is, a connected open set, with boundary $\partial \Omega$ of class $C^1$ and outward unit [[normal vector|0WQJJCCTC8]] $\nu$.
Let $c_1, c_2$ be nonzero real constants and let $g \colon \partial \Omega \to \R$ be a given function.
For an equation for $u$ on $\Omega$, the *Robin boundary condition* is
$$c_1\, u(x) + c_2\, \frac{\partial u}{\partial \nu}(x) = g(x) \quad \text{for all } x \in \partial \Omega.$$
For a second-order ordinary differential equation on $[a, b]$, where the outward normal derivatives are $-y'(a)$ and $y'(b)$, it reads
$$c_1\, y(a) - c_2\, y'(a) = g_a, \qquad c_1\, y(b) + c_2\, y'(b) = g_b.$$

## Remarks

If $c_2 = 0$, the condition becomes a [[Dirichlet condition|EETVA6QYX4]]; if $c_1 = 0$, it becomes a [[Neumann condition|GS3KT2H645]].
Some authors allow these cases and also let $c_1, c_2$ be functions on the boundary.

Example: $y'' = 0$ on $[0, 1]$ with $y(0) - y'(0) = 0$ and $y(1) + y'(1) = 3$, so $c_1 = c_2 = 1$.
The function $y = 1 + x$ gives $y(0) - y'(0) = 1 - 1 = 0$ and $y(1) + y'(1) = 2 + 1 = 3$, so it solves this [[boundary value problem|TM8VQJWGHZ]].

Non-example: the conditions $y(0) = 0$ and $y(1) = 0$ are not of Robin type, because no derivative appears; they are Dirichlet conditions.

A Sturm–Liouville problem usually has separated conditions $\alpha_1 y(a) + \alpha_2 y'(a) = 0$ and $\beta_1 y(b) + \beta_2 y'(b) = 0$, which include the Robin case.
