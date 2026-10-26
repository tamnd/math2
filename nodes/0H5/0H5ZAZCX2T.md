---
tag: 0H5ZAZCX2T
kind: statement
role: theorem
name: Taylor's theorem with the Lagrange remainder
msc: [41A80]
uses: [0HFSFVMWQB, 0194DY35BG]
sources:
  - url: https://en.wikipedia.org/wiki/Taylor%27s_theorem
    locator: Explicit formulas for the remainder
---

## Statement

Let $k \ge 0$ and let $a \ne x$ be real numbers. Let $J$ be the closed interval with endpoints $a$ and $x$.
Let $f$ be a real function with $f^{(k)}$ continuous on $J$ and $f^{(k+1)}$ existing on the interior of $J$.
Then there is $\xi$ strictly between $a$ and $x$ with
$$f(x) = P_k(x) + \frac{f^{(k+1)}(\xi)}{(k + 1)!} (x - a)^{k+1},$$
where $P_k$ is the [[Taylor polynomial|0HFSFVMWQB]] of degree $k$ of $f$ at $a$.

## Remarks

For $k = 0$ this is the [[mean value theorem|0BARQY52N5]].
If $|f^{(k+1)}| \le M$ between $a$ and $x$, then $|f(x) - P_k(x)| \le M |x - a|^{k+1} / (k + 1)!$.
Mathlib states it as `taylor_mean_remainder_lagrange`.

## Explanations

### L1 human

The error of the Taylor polynomial looks like the next term of the polynomial.
Only the derivative is taken at an unknown point $\xi$ instead of at $a$.
