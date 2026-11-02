---
tag: EHWH6EF4QY
kind: concept
name: Logarithmically convex domain
msc: [32Q02, 32A05]
specializes: [WA0SE56FVH]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Summary

A logarithmically convex domain is a [[Reinhardt domain|WA0SE56FVH]] whose image under the map $z \mapsto (\log\abs{z_1}, \dots, \log\abs{z_n})$ is a convex subset of $\R^n$.
The [[domain of convergence of a power series|D8S8JWE45R]] always has this property.
For complete Reinhardt domains, logarithmic convexity is exactly the condition that the domain is a domain of holomorphy.
The notion is close to that of a [[logarithmically convex function|8FRWATNNMX]]: a function is logarithmically convex when its logarithm is convex.

## Explanations

### L1 human

A Reinhardt domain can be drawn by the absolute values of its points.
Take logarithms of these absolute values: the picture then lives in $\R^n$.
The domain is logarithmically convex when this new picture is convex, that is, contains the segment between any two of its points.
For example, $\set{\abs{z_1 z_2} < 1}$ becomes the half-plane $\set{x_1 + x_2 < 0}$, which is convex.
A union of two thin polydiscs crossing like a plus sign becomes an L-shape, which is not convex.
