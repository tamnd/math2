---
tag: BR3HD0RRA4
kind: statement
role: theorem
name: Minimal deviation property of Chebyshev polynomials
msc: [41A50, 41A10, 33C45]
uses: [M6EAR1JHPP, 0C3QBCR46M, 0DPF6WRZW6]
about: [M6EAR1JHPP]
sources:
  - url: https://en.wikipedia.org/wiki/Chebyshev_polynomials
---

## Statement

Let $n \ge 1$ and let $T_n$ be the [[Chebyshev polynomial|M6EAR1JHPP]] of the first kind of degree $n$.
Let $p$ be a [[monic|0C3QBCR46M]] real polynomial of [[degree|0DPF6WRZW6]] $n$.
Then
$$\max_{-1 \le x \le 1} \abs{p(x)} \ge 2^{1-n},$$
and equality holds if and only if $p = 2^{1-n} T_n$.

## Remarks

Proof idea: the polynomial $\tilde T_n = 2^{1-n} T_n$ is monic and equals $(-1)^k 2^{1-n}$ at the $n + 1$ points $\cos(k\pi/n)$, $k = 0, \dots, n$.
If $\max \abs{p} < 2^{1-n}$, then $\tilde T_n - p$ has degree at most $n - 1$ and alternates in sign at these $n + 1$ points.
So it has $n$ zeros, hence it is $0$, a contradiction.
The equality case follows from a refinement of the same counting, or from the uniqueness of best uniform approximation.

Example: for $n = 2$, $x^2$ has maximum $1$ on $[-1, 1]$, while $\tilde T_2 = x^2 - 1/2$ has maximum $1/2$, the smallest possible value.

Equivalently, $x^n - \tilde T_n$ is the best uniform approximation of $x^n$ on $[-1, 1]$ by polynomials of degree at most $n - 1$, with error $2^{1-n}$.
On an interval $[a, b]$, an affine change of variable gives the minimum $2 \left(\frac{b - a}{4}\right)^n$.

## Explanations

### L1 human

A monic polynomial has leading term $x^n$, which grows fast, and lower terms can partly cancel it.
The theorem says how small such a polynomial can stay on $[-1, 1]$: never below $2^{1-n}$ everywhere.
The scaled Chebyshev polynomial is the one that reaches this bound, because it wiggles evenly between $\pm 2^{1-n}$.

### L2 human

This is the first and model case of Chebyshev's theory of best uniform approximation.
It explains why [[Chebyshev nodes|HYK8J56PSH]] are good for interpolation: the node polynomial $\prod (x - x_k)$ appears in the interpolation error, and the zeros of $T_n$ make its maximum as small as possible.
It also gives the minimax error of $x^n$ and lower bounds for polynomial approximation of smooth functions.
