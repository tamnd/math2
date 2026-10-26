---
tag: 0X7SBS8E0F
kind: definition
name: Winding number
aliases: [winding-index, index-of-a-curve]
msc: [55M25]
defines: 0NQSV2EWDR
uses: [00FWNP9TXY]
sources:
  - url: https://en.wikipedia.org/wiki/Winding_number
    locator: Complex analysis
  - url: https://en.wikipedia.org/wiki/Winding_number
    locator: Formal definition
---

## Definition

Let $\gamma : [a, b] \to \mathbb{C}$ be a closed path that is continuous and piecewise continuously differentiable, and let $w \in \mathbb{C}$ be a point that is not on the image of $\gamma$.
The winding number of $\gamma$ around $w$ is
$$n(\gamma, w) = \frac{1}{2 \pi i} \oint_\gamma \frac{dz}{z - w},$$
where the integral is a [[contour integral|00FWNP9TXY]].

## Remarks

The number $n(\gamma, w)$ is an integer. It counts how many times $\gamma$ goes around $w$ counterclockwise, minus the times it goes around $w$ clockwise.
As a function of $w$, it is constant on each connected component of the complement of the image of $\gamma$. It is $0$ on the unbounded component.
For the circle $|z - c| = R$, traveled once counterclockwise, $n = 1$ for $|w - c| < R$ and $n = 0$ for $|w - c| > R$, by the [[integral of 1/(z - w)|0SXZ68HV6F]].

## Explanations

### L1 human

Stand at the point $w$ and watch a point that moves along the closed curve. The winding number is the number of full turns that you make.
A circle around you gives $1$, the same circle traveled twice gives $2$, and a circle that does not go around you gives $0$.
