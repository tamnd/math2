---
tag: ZCZA6VXCZZ
kind: statement
name: Division with remainder for natural numbers
role: theorem
aliases:
  - natural-number-division-with-remainder
msc:
  - 11A05
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_background_decimal.ptx#L17
    locator: source/s_background_decimal.ptx:17
uses:
  - 0S13V32CPB
  - 06J5DE801P
  - 0HNATXFEV5
---

## Statement

Let $n$ and $d$ be natural numbers (nonnegative integers) with $d > 0$.
Then there is exactly one pair of natural numbers $(q, r)$ such that $n = qd + r$ and $0 \le r < d$.

## Remarks

The number $q$ is the quotient and $r$ is the remainder of $n$ divided by $d$.
Here every number involved is a natural number, so $n$ is not negative and the quotient is not negative.
This is the case of the [[Division algorithm|0CHQKZFK5S]] where $a \ge 0$ and $b > 0$.
