---
tag: NEAE07CSM4
kind: definition
name: Logarithmically convex domain
msc: [32Q02, 32A05]
defines: EHWH6EF4QY
uses: [WA0SE56FVH, 02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Definition

Let $D \subseteq \C^n$ be a [[Reinhardt domain|WA0SE56FVH]] with centre $0$.
Let $D^* = \set{z \in D : z_j \ne 0 \text{ for } j = 1, \dots, n}$, and let $\lambda \colon D^* \to \R^n$ be the map $\lambda(z) = (\log\abs{z_1}, \dots, \log\abs{z_n})$.
The domain $D$ is *logarithmically convex* if $\lambda(D^*)$ is a [[convex set|02AS45T3H9]] in $\R^n$.

## Remarks

Example: for the unit ball $\mathbb{B}^2$, $\lambda(\mathbb{B}^{2*}) = \set{x \in \R^2 : e^{2x_1} + e^{2x_2} < 1}$, a sublevel set of the convex function $e^{2x_1} + e^{2x_2}$, hence convex.
Every polydisc with centre $0$ is logarithmically convex, since its image is a product of half-lines $(-\infty, \log r_j)$.
Non-example: let $D = \set{\abs{z_1} < 1, \abs{z_2} < e^{-2}} \cup \set{\abs{z_1} < e^{-2}, \abs{z_2} < 1}$, a Reinhardt domain.
The points $(e^{-1}, e^{-3})$ and $(e^{-3}, e^{-1})$ lie in $D$, with images $(-1, -3)$ and $(-3, -1)$.
The midpoint $(-2, -2)$ of these images is the image of $(e^{-2}, e^{-2})$, which is not in $D$, so $\lambda(D^*)$ is not convex.
For a complete Reinhardt domain, logarithmic convexity is equivalent to being a domain of holomorphy.
