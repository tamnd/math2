---
tag: 0Z5R9TVWQH
kind: definition
name: Interval of convergence
msc: [30B10]
defines: 0ED4HWNDGW
uses: [0VP56B4EMX, 0660QX1VPR]
sources:
  - url: https://en.wikipedia.org/wiki/Radius_of_convergence
    locator: Convergence on the boundary
---

## Definition

Let $\sum a_n (x - c)^n$ be a real [[power series|0VP56B4EMX]].
Its interval of convergence is the set of real numbers $x$ for which the series converges.

## Remarks

Let $R$ be the [[radius of convergence|0660QX1VPR]]. The interval of convergence contains $(c - R, c + R)$ and lies in $[c - R, c + R]$.
Each endpoint must be checked on its own. For $\sum x^n / n$, the interval is $[-1, 1)$.
For $\sum x^n$ it is $(-1, 1)$, and for $\sum x^n / n^2$ it is $[-1, 1]$.

## Explanations

### L1 human

The radius of convergence fixes the interval up to its two endpoints.
At each endpoint the series may converge or diverge, so the interval may be open, closed, or half open.
