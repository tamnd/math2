---
tag: G3XFT0MWKH
kind: definition
name: Dirichlet boundary condition
msc: [34B05, 35J25]
defines: EETVA6QYX4
uses: [TM8VQJWGHZ, 05D5EGMFYV]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_boundary_condition
---

## Definition

Let $a < b$, and consider a second-order ordinary differential equation for $y$ on $[a, b]$.
A *Dirichlet boundary condition* is a pair of conditions
$$y(a) = \alpha, \qquad y(b) = \beta,$$
with given real numbers $\alpha, \beta$.
More generally, let $\Omega \subseteq \R^d$ be a bounded domain, that is, a connected open set, with [[boundary|05D5EGMFYV]] $\partial \Omega$, and let $g \colon \partial \Omega \to \R$ be a given function.
For an equation for $u$ on $\Omega$, the Dirichlet boundary condition is $u(x) = g(x)$ for all $x \in \partial \Omega$.
The condition is *homogeneous* if $\alpha = \beta = 0$, respectively $g = 0$.

## Remarks

A differential equation together with a Dirichlet condition is a Dirichlet problem, a kind of [[boundary value problem|TM8VQJWGHZ]].

Example: $y'' = 0$ on $[0, 1]$ with $y(0) = 1$ and $y(1) = 3$.
The function $y = 1 + 2x$ has $y'' = 0$, $y(0) = 1$ and $y(1) = 3$, so it solves this Dirichlet problem.

Non-example: the conditions $y(0) = 1$ and $y'(1) = 3$ do not form a Dirichlet condition, because the second one prescribes a derivative and not a value.

For the Laplace equation $\Delta u = 0$ on a bounded domain with continuous $g$, a solution that is continuous up to the boundary is unique when it exists, by the maximum principle.
