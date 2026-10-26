---
tag: 02NSMQVQWK
kind: definition
name: Divergence
msc: [26B12]
defines: 0MWV6ZTK6S
uses: [0N67NBKQ5T, 05AXG3QRKR, 0YF0VXKXGB]
sources:
  - url: https://en.wikipedia.org/wiki/Divergence
    locator: Cartesian coordinates
  - url: https://en.wikipedia.org/wiki/Divergence
    locator: Properties
---

## Definition

Let $U \subseteq \mathbb{R}^n$ be open, and let $F = (F_1, \dots, F_n) \colon U \to \mathbb{R}^n$ be a [[vector field|0N67NBKQ5T]] whose [[partial derivatives|05AXG3QRKR]] $\partial F_i / \partial x_i$ exist on $U$.
The divergence of $F$ is the function $\operatorname{div} F \colon U \to \mathbb{R}$,
$$\operatorname{div} F = \nabla \cdot F = \frac{\partial F_1}{\partial x_1} + \frac{\partial F_2}{\partial x_2} + \dots + \frac{\partial F_n}{\partial x_n}.$$

## Remarks

The divergence is the trace of the [[Jacobian matrix|0YF0VXKXGB]] of $F$.
For $F(x) = x$ on $\mathbb{R}^n$, $\operatorname{div} F = n$. For the rotation field $F(x, y) = (-y, x)$, $\operatorname{div} F = 0$.
The divergence is linear, and $\operatorname{div}(\phi F) = \nabla \phi \cdot F + \phi \operatorname{div} F$ for a differentiable function $\phi$.
Take a $C^1$ field and a small region around $x_0$. The divergence at $x_0$ is the limit of the outward flux through the boundary of the region, divided by its volume. This follows from the [[divergence theorem|0JX86PSSA9]].

## Explanations

### L1 human

Think of $F$ as the velocity of a fluid.
Where the divergence is positive, more fluid leaves a small region than enters it, as at a source. Where it is negative, fluid gathers, as at a sink.
