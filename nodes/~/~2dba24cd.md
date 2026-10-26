---
tag: ~2dba24cd
kind: definition
name: Tangent plane to a graph
msc: [26B05]
defines: ~d7c5a467
uses: [~9740fd2d, ~4c15835a, 0JBJYT69ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_approximation
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Tangent_space
    locator: Informal description
---

## Definition

Let $U \subseteq \mathbb{R}^2$ be open, let $f \colon U \to \mathbb{R}$, and let $(a, b) \in U$ be a point at which $f$ is [[differentiable|~9740fd2d]].
The tangent plane to the [[graph|0JBJYT69ZV]] $z = f(x, y)$ at the point $(a, b, f(a, b))$ is the plane in $\mathbb{R}^3$ with the equation
$$z = f(a, b) + \frac{\partial f}{\partial x}(a, b)\,(x - a) + \frac{\partial f}{\partial y}(a, b)\,(y - b).$$
More generally, let $U \subseteq \mathbb{R}^n$ be open and let $f$ be differentiable at $a \in U$. The tangent hyperplane to the graph at $(a, f(a))$ is the set of points $(x, z) \in \mathbb{R}^n \times \mathbb{R}$ with $z = f(a) + \nabla f(a) \cdot (x - a)$.

## Remarks

The vector $\big(\partial f / \partial x(a, b), \, \partial f / \partial y(a, b), \, -1\big)$ is normal to the tangent plane.
For $f(x, y) = x^2 + y^2$ at $(1, 1)$, the tangent plane is $z = 2 + 2(x - 1) + 2(y - 1)$, that is, $z = 2x + 2y - 2$.
The tangent plane exists only where $f$ is differentiable. The existence of the [[partial derivatives|~4c15835a]] alone gives a plane, but this plane need not touch the graph well.

## Explanations

### L1 human

Put a flat sheet on top of a smooth hill so that it touches the hill at one point and does not tilt against it.
That sheet is the tangent plane. Near the point of contact, the hill and the sheet are almost the same.
