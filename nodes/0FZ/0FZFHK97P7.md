---
tag: 0FZFHK97P7
kind: statement
role: proposition
name: Second derivative test
msc: [26A24]
uses: [0Y9D2FJRQ4, 0NS8BP96QX, 01A2EGXJEM]
sources:
  - url: https://en.wikipedia.org/wiki/Derivative_test
    locator: Second-derivative test (single variable)
inventory: [YJHTDW54AW]
---

## Statement

Let $f$ be a real function differentiable on an open interval around $c$, with $f'(c) = 0$.
Assume that the [[second derivative|0Y9D2FJRQ4]] $f''(c)$ exists.
If $f''(c) > 0$, then $f$ has a strict [[local minimum|0NS8BP96QX]] at $c$. If $f''(c) < 0$, then $f$ has a strict local maximum at $c$.

## Remarks

If $f''(c) > 0$, then $f'(x)/(x - c) \to f''(c)$. So $f'$ is negative just left of $c$ and positive just right of $c$, and the [[first derivative test|01A2EGXJEM]] applies.
If $f''(c) = 0$, the test gives no answer. The functions $x^4$, $-x^4$, and $x^3$ at $0$ show all three cases.
Mathlib states the minimum case as `isLocalMin_of_deriv_deriv_pos`.

## Explanations

### L1 human

At a stationary point where the graph bends upward, the point is the bottom of a valley.
Where it bends downward, it is a hilltop.
