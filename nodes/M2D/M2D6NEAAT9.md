---
about:
- 7WV6B2502K
kind: statement
msc:
- 34B24
- 34L10
- 42C10
name: Eigenfunction expansion for a regular Sturm–Liouville problem
role: theorem
sources:
- locator: ch-eigenvalue-probs.tex:435
  url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-eigenvalue-probs.tex#L435
tag: M2D6NEAAT9
uses:
- 7WV6B2502K
- SNJC87TBHD
---

## Statement

Consider a regular problem of [[Sturm–Liouville theory|7WV6B2502K]] on an interval $[a, b]$, with a weight function $r$.
Pick one eigenfunction $y_n$ for each eigenvalue, and list them as $y_1, y_2, \ldots$.
Let $f$ be a continuous, piecewise smooth function on $[a, b]$.

Then there are real numbers $c_1, c_2, \ldots$, given by the weighted projection formula
$$c_n = \frac{\int_a^b f(x)\, y_n(x)\, r(x)\, dx}{\int_a^b y_n(x)^2\, r(x)\, dx},$$
such that the series $\sum_n c_n y_n(x)$ converges and its sum equals $f(x)$ at every $x$ with $a < x < b$.

## Remarks

The series is a [[generalized Fourier series|SNJC87TBHD]] of $f$ in the eigenfunctions.
The result only claims equality inside the open interval, not at the endpoints.
