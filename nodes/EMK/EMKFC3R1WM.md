---
tag: EMKFC3R1WM
kind: definition
name: Shallow water equations
msc: [76B15, 35Q35, 35Q86]
defines: NT73Y95RY5
uses: [GC5BDZ6QBC, XN081NCPF5, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Shallow_water_equations
---

## Definition

Let $g > 0$ be a constant, the gravitational acceleration.
The one-dimensional *shallow water equations* over a flat bottom are the system
$$\partial_t h + \partial_x (h u) = 0, \qquad \partial_t (h u) + \partial_x \big( h u^2 + \tfrac{1}{2} g h^2 \big) = 0,$$
for unknown functions $h, u \colon \R \times [0, \infty) \to \R$ with $h > 0$.
Here $h$ is the depth of the fluid and $u$ its horizontal velocity.
The symbols $\partial_t$ and $\partial_x$ denote [[partial derivatives|09EGC6F8PT]].

## Remarks

The system has the form $\partial_t U + \partial_x \Phi(U) = 0$ for $U = (h, hu)$, so it is a system of [[hyperbolic conservation laws|XN081NCPF5]].
The eigenvalues of the Jacobian matrix of $\Phi$ are $u \pm \sqrt{g h}$, which are real and distinct when $h > 0$.

Example: for constants $H > 0$ and $U_0 \in \R$, the uniform flow $h = H$, $u = U_0$ is a solution, since all derivatives vanish.

Non-example: $h(x, t) = 1 + x^2$ and $u = 0$ do not form a solution, because $\partial_x(\tfrac{1}{2} g h^2) = g h \, \partial_x h = 2 g x (1 + x^2)$ is not identically $0$.

In two dimensions, with velocity $(u, v)$, the equations are $\partial_t h + \nabla \cdot (h u, h v) = 0$ together with two momentum equations of the same form.
Variants add a varying bottom, friction or the Coriolis force.
