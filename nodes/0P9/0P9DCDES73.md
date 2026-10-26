---
tag: 0P9DCDES73
kind: statement
role: proposition
name: Metric spaces are Hausdorff
msc: ["54E35"]
uses: [0MXB4CKHFW, 0DC3MPR7C9, 01M6CW9VM6, 0A6YRNZB2R]
sources:
  - url: https://en.wikipedia.org/wiki/Hausdorff_space
    locator: Examples of Hausdorff and non-Hausdorff spaces
---

## Statement

Let $(X, d)$ be a [[metric space|063W5JMY85]], with the [[metric topology|0A6YRNZB2R]].
Then $X$ is a [[Hausdorff space|0MXB4CKHFW]].

## Remarks

Proof: for $x \neq y$, let $r = d(x, y) / 2 > 0$. The [[open balls|0DC3MPR7C9]] $B(x, r)$ and $B(y, r)$ are open. They are disjoint: a point $z$ in both would give $d(x, y) \le d(x, z) + d(z, y) < 2r$, by the [[triangle inequality|01M6CW9VM6]].
Thus each [[metrizable space|09KDHB82SG]] is Hausdorff. A non-Hausdorff space, such as an infinite set with the cofinite topology, is not metrizable.
For a pseudometric, the statement fails: points at distance $0$ cannot be separated.

## Explanations

### L1 human

Two distinct points of a metric space are at a positive distance. Balls of half that radius about them do not meet.
