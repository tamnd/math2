---
tag: MKJRFAB6Z4
kind: definition
name: Material derivative
msc: [76A02]
defines: CJW50K5HZB
uses: [5E6K4ATM9W, 09EGC6F8PT, 0ABK9V9Y64, 0RXX2PT1MQ]
sources:
  - url: https://en.wikipedia.org/wiki/Material_derivative
---

## Definition

Let $\Omega \subseteq \R^3$ be open, let $I$ be an open interval and let $\mathbf{u} \colon \Omega \times I \to \R^3$ be a velocity field.
Let $f \colon \Omega \times I \to \R$ be a continuously differentiable scalar field.
The *material derivative* of $f$ is the field
$$\frac{Df}{Dt} = \frac{\partial f}{\partial t} + \mathbf{u} \cdot \nabla f = \frac{\partial f}{\partial t} + \sum_{i=1}^{3} u_i \frac{\partial f}{\partial x_i},$$
where $\nabla f$ is the [[gradient|0ABK9V9Y64]] of $f$ in the space variables.
For a vector field, the material derivative is taken component by component.

## Remarks

If $X(a, t)$ is the [[Lagrangian path|5E6K4ATM9W]] of the parcel labelled $a$, then the [[chain rule|0RXX2PT1MQ]] gives $\frac{d}{dt} f(X(a, t), t) = \frac{Df}{Dt}(X(a, t), t)$.
Example: for $f(x, t) = x_1$ and $\mathbf{u} = (2, 0, 0)$, $\frac{Df}{Dt} = 0 + 2 \cdot 1 = 2$.
Non-example: the [[partial derivative|09EGC6F8PT]] $\partial f / \partial t = 0$ in this example is not the material derivative, because it omits the transport term $\mathbf{u} \cdot \nabla f$.
The acceleration of a fluid parcel is $\frac{D\mathbf{u}}{Dt} = \partial_t \mathbf{u} + (\mathbf{u} \cdot \nabla) \mathbf{u}$.
Other names are convective derivative, substantial derivative and Lagrangian derivative.
