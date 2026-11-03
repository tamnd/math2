---
tag: JCV5PJJ039
kind: definition
name: Stream function
msc: [76A02, 76B99]
defines: E66111XRRA
uses: [2JZ0C15A9C, ZWF8B7T5NX, 09EGC6F8PT, 0QW64ARSHB]
sources:
  - url: https://en.wikipedia.org/wiki/Stream_function
---

## Definition

Let $\Omega \subseteq \R^2$ be open and let $\mathbf{u} = (u, v) \colon \Omega \to \R^2$ be a continuously differentiable velocity field.
A *stream function* for $\mathbf{u}$ is a twice continuously differentiable function $\psi \colon \Omega \to \R$ such that
$$u = \frac{\partial \psi}{\partial y}, \qquad v = -\frac{\partial \psi}{\partial x}$$
at every point of $\Omega$.
If the flow depends on time, the same equations hold at each fixed time.

## Remarks

If a stream function exists, then $\partial u / \partial x + \partial v / \partial y = \psi_{yx} - \psi_{xy} = 0$, so the flow is [[incompressible|2JZ0C15A9C]].
Conversely, on a [[simply connected domain|0QW64ARSHB]] every divergence-free field has a stream function, unique up to an additive constant.
Example: the uniform flow $\mathbf{u} = (U, 0)$ has the stream function $\psi = U y$; check: $\psi_y = U$ and $-\psi_x = 0$.
Non-example: the field $\mathbf{u} = (x, y)$ has divergence $2$, so it has no stream function.
Along a [[streamline|ZWF8B7T5NX]] the function $\psi$ is constant, since $\mathbf{u} \cdot \nabla \psi = \psi_y \psi_x - \psi_x \psi_y = 0$.
