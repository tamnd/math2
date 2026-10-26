---
tag: ~f9b6abe8
kind: statement
role: theorem
name: Power series are differentiable inside the radius of convergence
msc: [30B10, 26A24]
uses: [~9b386670, ~83292ea3, ~65290174, ~a6ebaeb5, ~6420cedc]
sources:
  - url: https://en.wikipedia.org/wiki/Power_series
    locator: Differentiation and integration
---

## Statement

Let $f(x) = \sum_{n=0}^{\infty} a_n (x - c)^n$ be a [[power series|~9b386670]] with [[radius of convergence|~83292ea3]] $R > 0$.
Then $f$ is differentiable on $(c - R, c + R)$, and
$$f'(x) = \sum_{n=1}^{\infty} n a_n (x - c)^{n-1}.$$
The derived series also has radius of convergence $R$.

## Remarks

The [[Cauchy–Hadamard formula|~6420cedc]] gives the radius of the derived series, since $\sqrt[n]{n} \to 1$. Then [[term-by-term differentiation|~65290174]] applies on each $[c - r, c + r]$ with $r < R$.
By induction, $f$ is infinitely differentiable, and $a_n = f^{(n)}(c)/n!$. So the series is the Taylor series of $f$ at $c$.
Mathlib states differentiability as `HasFPowerSeriesOnBall.differentiableOn`.

## Explanations

### L1 human

A power series can be differentiated like a polynomial, one term at a time.
The new series converges on the same open interval.
