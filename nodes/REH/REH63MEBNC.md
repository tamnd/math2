---
tag: REH63MEBNC
kind: definition
name: Neumann boundary condition
msc: [34B05, 35J25]
defines: GS3KT2H645
uses: [TM8VQJWGHZ, 05D5EGMFYV, 0WQJJCCTC8, 06KWGHDN2J]
sources:
  - url: https://en.wikipedia.org/wiki/Neumann_boundary_condition
---

## Definition

Let $a < b$, and consider a second-order ordinary differential equation for $y$ on $[a, b]$.
A *Neumann boundary condition* is a pair of conditions
$$y'(a) = \alpha, \qquad y'(b) = \beta,$$
with given real numbers $\alpha, \beta$.
More generally, let $\Omega \subseteq \R^d$ be a bounded domain, that is, a connected open set, whose [[boundary|05D5EGMFYV]] $\partial \Omega$ is of class $C^1$.
Let $\nu(x)$ be the outward unit [[normal vector|0WQJJCCTC8]] at $x \in \partial \Omega$, and let $g \colon \partial \Omega \to \R$ be a given function.
For an equation for $u$ on $\Omega$, the Neumann boundary condition is
$$\frac{\partial u}{\partial \nu}(x) = \nabla u(x) \cdot \nu(x) = g(x) \quad \text{for all } x \in \partial \Omega,$$
where $\frac{\partial u}{\partial \nu}$ is the [[directional derivative|06KWGHDN2J]] of $u$ along $\nu$.

## Remarks

On $[a, b]$ the outward normal derivatives are $-y'(a)$ and $y'(b)$, so the two forms agree up to the sign at $a$.

Example: $y'' = 2$ on $[0, 1]$ with $y'(0) = 0$ and $y'(1) = 2$.
The function $y = x^2$ has $y'' = 2$, $y'(0) = 0$ and $y'(1) = 2$, so it solves this Neumann problem; so does $x^2 + c$ for every constant $c$.

Non-example: $y(0) = 0$ together with $y'(1) = 0$ is not a Neumann condition, since the first condition prescribes a value.

For $\Delta u = f$ on $\Omega$ with Neumann data $g$, the divergence theorem gives the necessary condition $\int_\Omega f = \int_{\partial \Omega} g$.
Solutions, when they exist, are unique only up to an additive constant.
