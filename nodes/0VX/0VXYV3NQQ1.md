---
tag: 0VXYV3NQQ1
kind: statement
role: proposition
name: Gradient is orthogonal to level sets
msc: [26B12]
uses: [0NS2QYVC4Y, 0Y5Q8Q9WJ7, 0A8TJ0VHC7]
sources:
  - url: https://en.wikipedia.org/wiki/Gradient
    locator: Level sets
  - url: https://en.wikipedia.org/wiki/Level_set
    locator: Level sets versus the gradient
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be open, let $f \colon U \to \mathbb{R}$, and let $c \in \mathbb{R}$.
Let $I \subseteq \mathbb{R}$ be an open interval and let $\gamma \colon I \to U$ be a curve that lies in the [[level set|0Y5Q8Q9WJ7]] $L_c(f)$, so that $f(\gamma(t)) = c$ for each $t \in I$.
Let $t_0 \in I$, and suppose that $\gamma$ is differentiable at $t_0$ and $f$ is differentiable at $\gamma(t_0)$.
Then $\nabla f(\gamma(t_0)) \cdot \gamma'(t_0) = 0$.

## Remarks

The proof is one step: $f \circ \gamma$ is constant, so its derivative is $0$, and by the [[chain rule for a curve|0A8TJ0VHC7]] that derivative is $\nabla f(\gamma(t_0)) \cdot \gamma'(t_0)$.
So the [[gradient|0NS2QYVC4Y]] is orthogonal to each tangent vector of the level set at the point. Let $\nabla f \ne 0$ and let $f$ be of class $C^1$. Then the level set near the point is a smooth hypersurface, and $\nabla f$ is a normal vector to it.
For $f(x, y, z) = x^2 + y^2 + z^2$, the level set at $c = 1$ is the unit sphere, and $\nabla f(p) = 2p$ is normal to the sphere at $p$.

## Explanations

### L1 human

Along a contour line the height does not change, so the slope along the line is $0$.
The gradient gives the slope in each direction by a dot product, so it must be at right angles to the contour line.
