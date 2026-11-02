---
tag: AFRP1AAPV9
kind: concept
name: Gradient flow on a manifold
msc: ["37C10", "58E05", 57R70]
specializes: [06738GGWWK]
sources:
  - url: https://en.wikipedia.org/wiki/Gradient-like_vector_field
---

## Summary

The gradient flow of a smooth function $f$ on a [[Riemannian manifold|7CBT4SM83Y]] is the [[flow|06738GGWWK]] of the vector field $-\nabla f$.
Some authors use $\nabla f$ instead.
Along its flow lines the function decreases, strictly away from the [[critical points|0YTCMFB4HC]], which are exactly the rest points of the flow.
It is the basic tool of Morse theory and of critical point theory: it deforms sublevel sets of $f$ and connects critical points.

## Explanations

### L1 human

Think of $f$ as the height of a landscape and let water run downhill along the steepest path.
The path that a drop follows is a flow line of the negative gradient flow.
Drops stop only where the ground is flat, that is, at critical points of $f$.
For example, for $f(x, y) = x^2 + y^2$ on the plane, the flow lines are the rays $t \mapsto e^{-2t}(x_0, y_0)$, which run into the minimum at the origin.
