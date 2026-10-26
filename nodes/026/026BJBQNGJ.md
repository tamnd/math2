---
tag: 026BJBQNGJ
kind: statement
role: corollary
name: A function with nonnegative derivative is increasing
msc: [26A24]
uses: [0BARQY52N5]
sources:
  - url: https://en.wikipedia.org/wiki/Monotonic_function
    locator: Some basic applications and results
---

## Statement

Let $I$ be an interval and let $f \colon I \to \mathbb{R}$ be continuous, and differentiable at each interior point of $I$.
If $f'(x) \ge 0$ for each interior point $x$ of $I$, then $f$ is increasing on $I$. That is, $f(x) \le f(y)$ for $x \le y$ in $I$.

## Remarks

The proof uses the [[mean value theorem|0BARQY52N5]].
For differentiable $f$ on an open interval, the converse holds too: if $f$ is increasing, then $f' \ge 0$.
Mathlib states it as `monotoneOn_of_deriv_nonneg`.

## Explanations

### L1 human

If the slope is never negative, the graph never goes down.
It may stay flat on some parts.
