---
tag: WNVACS2S2Z
kind: concept
name: Incomplete beta function
msc: ["33B20"]
sources:
  - url: https://en.wikipedia.org/wiki/Beta_function
    locator: Incomplete beta function
---

## Summary

The incomplete beta function $B(x; a, b)$ is the integral of $t^{a-1}(1-t)^{b-1}$ from $0$ to $x$, for $0 \le x \le 1$.
At $x = 1$ it is the [[beta function|QHNWVSC6AQ]] $B(a, b)$.
Divided by $B(a, b)$ it becomes the regularised incomplete beta function $I_x(a, b)$, the distribution function of the [[beta distribution|0EW824Z7G2]].
It also gives the distribution functions of the binomial distribution and of Student's $t$-distribution.

## Explanations

### L1 human

The beta function is the area under the curve $t^{a-1}(1-t)^{b-1}$ between $0$ and $1$.
The incomplete beta function keeps only the part of this area to the left of a point $x$.
As $x$ moves from $0$ to $1$, it grows from $0$ to the full beta function.
For $a = b = 1$ the curve is the constant $1$, and the area up to $x$ is just $x$.
