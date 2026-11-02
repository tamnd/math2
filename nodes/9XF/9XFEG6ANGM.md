---
tag: 9XFEG6ANGM
kind: concept
name: Shape derivative
msc: [49Q10, 49Q12]
sources:
  - url: https://en.wikipedia.org/wiki/Shape_optimization
---

## Summary

The shape derivative measures how a quantity that depends on a domain changes when the domain is deformed a little.
One moves each point $x$ of the domain to $x + \theta(x)$ for a small vector field $\theta$.
The shape derivative is the derivative of the quantity with respect to $\theta$.
For smooth domains it usually depends only on the normal component of $\theta$ on the boundary.
This fact is known as the Hadamard structure theorem.
It is the gradient that drives numerical methods of [[shape optimization|WWQJQXJECK]].

## Explanations

### L1 human

Push the boundary of a region outward a little, in some places more than in others.
The area of the region grows, and to first order the growth is the outward push integrated along the boundary.
That first-order rate of change is the shape derivative of the area.
For other quantities, such as the drag on a wing, the shape derivative tells an engineer where to push the boundary to improve the design.
