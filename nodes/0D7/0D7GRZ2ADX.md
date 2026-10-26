---
tag: 0D7GRZ2ADX
kind: statement
role: proposition
name: The exponential function is convex
msc: [26A51]
uses: [0RMVS7RXZX, 0Z41C17TGP, 0EX9GFJ0B3]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_function
    locator: Properties
---

## Statement

The [[exponential function|0RMVS7RXZX]] is strictly convex on $\mathbb{R}$.
That is, $e^{t x + (1 - t) y} < t e^x + (1 - t) e^y$ for all real $x \ne y$ and $t \in (0, 1)$.

## Remarks

The second derivative of $e^x$ is [[$e^x$ itself|0EX9GFJ0B3]], which is positive. So [[the second derivative test for convexity|0Z41C17TGP]] applies, in its strict form.
The tangent line at $0$ gives the inequality [[$1 + x \le e^x$|012C7GFF20]].
Mathlib states convexity as `convexOn_exp`.

## Explanations

### L1 human

The graph of $e^x$ bends upward everywhere.
Every chord of the graph lies above the graph.
