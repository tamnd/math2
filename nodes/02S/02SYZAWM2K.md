---
tag: 02SYZAWM2K
kind: statement
role: theorem
name: Cauchy mean value theorem
aliases: [extended-mean-value-theorem]
msc: [26A24]
uses: [0194DY35BG, 0BARQY52N5]
sources:
  - url: https://en.wikipedia.org/wiki/Mean_value_theorem
    locator: Cauchy's mean value theorem
---

## Statement

Let $a < b$ and let $f, g \colon [a, b] \to \mathbb{R}$ be continuous on $[a, b]$ and differentiable on $(a, b)$.
Then there is $c \in (a, b)$ with
$$(f(b) - f(a)) \, g'(c) = (g(b) - g(a)) \, f'(c).$$

## Remarks

Apply [[Rolle's theorem|0194DY35BG]] to $h(x) = (f(b) - f(a)) g(x) - (g(b) - g(a)) f(x)$, which has $h(a) = h(b)$.
With $g(x) = x$ it is the [[mean value theorem|0BARQY52N5]].
It is the main step in the proof of [[L'Hôpital's rule|0JWT4PPQ7B]]. Mathlib states it as `exists_ratio_deriv_eq_ratio_slope`.

## Explanations

### L1 human

Think of $(g(t), f(t))$ as a point moving along a curve in the plane.
At some time, the direction of motion is parallel to the chord joining the start and the end.
