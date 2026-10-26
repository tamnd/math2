---
tag: ~5ba9df6d
kind: statement
role: proposition
name: Second derivative test
msc: [26A24]
uses: [~4d14a831, ~3ed4ce3a, ~5dbd816d]
sources:
  - url: https://en.wikipedia.org/wiki/Derivative_test
    locator: Second-derivative test (single variable)
---

## Statement

Let $f$ be a real function differentiable on an open interval around $c$, with $f'(c) = 0$.
Assume that the [[second derivative|~4d14a831]] $f''(c)$ exists.
If $f''(c) > 0$, then $f$ has a strict [[local minimum|~3ed4ce3a]] at $c$. If $f''(c) < 0$, then $f$ has a strict local maximum at $c$.

## Remarks

If $f''(c) > 0$, then $f'(x)/(x - c) \to f''(c)$. So $f'$ is negative just left of $c$ and positive just right of $c$, and the [[first derivative test|~5dbd816d]] applies.
If $f''(c) = 0$, the test gives no answer. The functions $x^4$, $-x^4$, and $x^3$ at $0$ show all three cases.
Mathlib states the minimum case as `isLocalMin_of_deriv_deriv_pos`.

## Explanations

### L1 human

At a stationary point where the graph bends upward, the point is the bottom of a valley.
Where it bends downward, it is a hilltop.
