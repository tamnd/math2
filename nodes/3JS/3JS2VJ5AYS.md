---
tag: 3JS2VJ5AYS
kind: concept
name: Proximal gradient method
msc: [90C25, 65K05]
sources:
  - url: https://en.wikipedia.org/wiki/Proximal_gradient_method
same_as:
  wikidata: Q17086765
  wikipedia: Proximal gradient method
---

## Summary

The proximal gradient method minimises a sum $f + g$, where $f$ is smooth and convex and $g$ is convex.
The function $g$ may be nonsmooth, but its [[proximal operator|E239APE78P]] should be easy to compute.
Each step is a [[gradient descent|12317R8RTJ]] step on $f$ followed by the proximal map of $g$.
It handles constraints (when $g$ is an indicator function) and sparsity penalties such as the $\ell_1$ norm, as in the lasso.
It has the same $O(1/k)$ rate as gradient descent on smooth problems, and an accelerated version reaches $O(1/k^2)$.

## Explanations

### L1 human

Some objectives have a smooth part, easy to differentiate, and a rough part with corners, such as $\abs{x}$.
The method treats them differently: it follows the slope of the smooth part, then "cleans up" the point with a simple rule designed for the rough part.
For the rough part $\lambda \abs{x}$, the clean-up rule moves the point toward $0$ by $\lambda$ times the step size, and sets it to $0$ if it would cross $0$.
This rule, called soft thresholding, is what makes many coordinates exactly zero in sparse models.
