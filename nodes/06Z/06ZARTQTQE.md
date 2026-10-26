---
tag: 06ZARTQTQE
kind: statement
role: corollary
name: Continuous image of a closed interval is a closed interval
msc: [26A15]
uses: [00KAFBR32E, 0WS1A8E2P9]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_value_theorem
    locator: Theorem
---

## Statement

Let $a \le b$ and let $f \colon [a, b] \to \mathbb{R}$ be continuous.
Then $f([a, b]) = [m, M]$, where $m$ and $M$ are the minimum and the maximum of $f$ on $[a, b]$.

## Remarks

The [[extreme value theorem|0WS1A8E2P9]] gives $m$ and $M$ as values of $f$. The [[intermediate value theorem|00KAFBR32E]] gives all values in between.
The image can be a single point, when $f$ is constant.
Mathlib states it as `ContinuousOn.image_Icc`.

## Explanations

### L1 human

A continuous function maps a closed bounded interval onto a closed bounded interval.
The graph reaches a lowest and a highest point, and it takes every height in between.
