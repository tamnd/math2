---
tag: 0ZS54B9GJF
kind: statement
role: proposition
name: The logarithm is strictly concave
msc: [26A51]
uses: [0044CPHJBV, 0EF2VG8XKQ, 07X1QA6BRW]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_logarithm
    locator: In calculus
---

## Statement

The [[natural logarithm|0044CPHJBV]] is strictly [[concave|0EF2VG8XKQ]] on $(0, \infty)$.
That is, $\ln(t x + (1 - t) y) > t \ln x + (1 - t) \ln y$ for all $x \ne y$ in $(0, \infty)$ and $t \in (0, 1)$.

## Remarks

The [[derivative of $\ln x$|07X1QA6BRW]] is $1/x$, and its second derivative is $-1/x^2 < 0$.
The concavity gives the [[AM–GM inequality|0DRF0F3XC9]] through Jensen's inequality.
Mathlib states it as `strictConcaveOn_log_Ioi`.

## Explanations

### L1 human

The graph of $\ln x$ bends downward everywhere.
Every chord of the graph lies below the graph.
