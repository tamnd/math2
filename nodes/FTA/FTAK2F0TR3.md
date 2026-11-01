---
tag: FTAK2F0TR3
kind: definition
name: Polynomial long division
msc: [13F20, 68W30]
defines: D6D0SR1FK3
uses: [0GYGHKX834, 0Q9EZS90GY, 0DPF6WRZW6, 0P05RJC5XA, 0MES3KS0ZC]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_long_division
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $f, g \in R[x]$, where $g$ has [[degree|0DPF6WRZW6]] $m$ and its [[leading coefficient|0P05RJC5XA]] $u$ is a unit of $R$.
Polynomial long division of $f$ by $g$ is the following procedure.

1. Start with $q = 0$ and $r = f$.
2. While $r \ne 0$ and $\deg r \ge m$, let $c$ be the leading coefficient of $r$ and $d = \deg r$, and replace $q$ by $q + u^{-1} c x^{d - m}$ and $r$ by $r - u^{-1} c x^{d - m} g$.
3. When $r = 0$ or $\deg r < m$, stop and return the quotient $q$ and the remainder $r$.

## Remarks

Each pass of step 2 removes the leading term of $r$, so $\deg r$ drops and the procedure stops.
The equation $f = q g + r$ holds at every step, so the output is the unique pair of the [[division algorithm for polynomials|0MES3KS0ZC]].
Example: divide $f = x^3 - 2x^2 - 4$ by $g = x - 3$ in $\Z[x]$.
The steps add $x^2$, then $x$, then $3$ to the quotient, and the remainder is $5$.
Check: $(x - 3)(x^2 + x + 3) + 5 = x^3 - 2x^2 - 9 + 5 = x^3 - 2x^2 - 4$.
Non-example: in $\Z[x]$ the procedure does not apply to $g = 2x$, because the leading coefficient $2$ is not a unit, and the first step for $f = x$ would need the coefficient $\frac{1}{2}$.
Division by a monic $g = x - a$ is often written in a compact table, called synthetic division; it is [[Horner's method|FYBQ3Z52Z7]].

## Explanations

### L1 human

Long division of polynomials repeats one move: kill the highest term of what is left.
It stops when what is left has smaller degree than the divisor.
