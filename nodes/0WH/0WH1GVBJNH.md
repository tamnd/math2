---
tag: 0WH1GVBJNH
kind: example
name: Circle as a quotient of the real line
aliases: [real-line-modulo-integers]
msc: [54B15]
instance_of: [0CQHFPGJ45]
uses: [0V8046R0P9, 0FF2FJ8CH2, 0430ETCMKD]
sources:
  - url: https://en.wikipedia.org/wiki/Circle_group
    locator: Periodic interval under addition
  - url: https://en.wikipedia.org/wiki/Circle_group
    locator: Topological, measurable, and analytic structure
---

## Example

On $\mathbb{R}$, let $s \sim t$ when $s - t \in \mathbb{Z}$. Let $\mathbb{R} / \mathbb{Z}$ be the set of classes, with the [[quotient topology|0V8046R0P9]].
Let $S^1 = \{ (x, y) \in \mathbb{R}^2 : x^2 + y^2 = 1 \}$ be the unit circle, with the [[subspace topology|0D5YHQGDJY]] of $\mathbb{R}^2$.
Then the map $[t] \mapsto (\cos 2\pi t, \sin 2\pi t)$ is a [[homeomorphism|05GZ11PWRY]] from $\mathbb{R} / \mathbb{Z}$ to $S^1$.

## Remarks

The map is well defined and continuous by the [[universal property of the quotient topology|0FF2FJ8CH2]], and it is bijective.
The space $\mathbb{R} / \mathbb{Z}$ is compact, because it is the image of $[0, 1]$ under the quotient map. The circle is Hausdorff. Thus the map is a homeomorphism, by [[this theorem|0430ETCMKD]].
Equivalently, $S^1$ is homeomorphic to $[0, 1]$ with the two endpoints $0$ and $1$ glued together.
Addition of classes makes $\mathbb{R} / \mathbb{Z}$ a group, the circle group.

## Explanations

### L1 human

Wrap the real line around a circle of length $1$. Points that differ by an integer land at the same place.
The quotient $\mathbb{R} / \mathbb{Z}$ records exactly this wrapping.
