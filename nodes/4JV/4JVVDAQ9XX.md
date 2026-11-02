---
tag: 4JVVDAQ9XX
kind: definition
name: Legendre polynomials
msc: [33C45, 42C05]
defines: QFYGJVA996
uses: [0P4JRMSWNH, 47WJ34NC9K]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre_polynomials
---

## Definition

The *Legendre polynomials* are the real polynomials $P_n$, for $n \ge 0$, determined by the following conditions:

1. $P_n$ has [[degree|0P4JRMSWNH]] exactly $n$.
2. $\int_{-1}^{1} P_m(x)\, P_n(x)\, dx = 0$ for all $m \ne n$.
3. $P_n(1) = 1$.

## Remarks

Conditions 1 and 2 fix $P_n$ up to a constant factor, and condition 3 fixes the factor.
Example: $P_2(x) = \frac{3x^2 - 1}{2}$; it has degree $2$, $P_2(1) = 1$, and $\int_{-1}^1 P_2\, dx = \frac{1}{2}\left( 2 - 2 \right) = 0$ and $\int_{-1}^1 x P_2\, dx = 0$ since $x P_2$ is odd.
A non-example: $x^2$ has degree $2$ and value $1$ at $1$, but $\int_{-1}^1 x^2 \cdot 1\, dx = \frac{2}{3} \ne 0$, so it fails condition 2 against $P_0 = 1$.
They are given by $P_n(x) = \frac{1}{2^n n!} \frac{d^n}{dx^n} (x^2 - 1)^n$, and they satisfy $(n + 1) P_{n+1}(x) = (2n + 1)\, x P_n(x) - n P_{n-1}(x)$ and $\int_{-1}^1 P_n(x)^2\, dx = \frac{2}{2n + 1}$.
Their generating function is $\frac{1}{\sqrt{1 - 2xt + t^2}} = \sum_{n \ge 0} P_n(x)\, t^n$ for $\abs{t}$ small.
They are the [[classical orthogonal polynomials|47WJ34NC9K]] of Jacobi type with $\alpha = \beta = 0$, and $P_n$ solves $(1 - x^2) y'' - 2x y' + n(n+1) y = 0$.
