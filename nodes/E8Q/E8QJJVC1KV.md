---
tag: E8QJJVC1KV
kind: statement
role: theorem
name: Gauss–Kronrod quadrature
msc: [65D32, 41A55]
uses: [PT9V59MJZZ, RGGXDRCJVE, QFYGJVA996, ZYT1JNT1Y0]
about: [PT9V59MJZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%E2%80%93Kronrod_quadrature_formula
---

## Statement

Let $n \ge 1$ and let $P_n$ be the [[Legendre polynomial|QFYGJVA996]] of degree $n$.
Its zeros $x_1, \ldots, x_n$ are the nodes of the $n$-point [[Gauss–Legendre rule|RGGXDRCJVE]] on $[-1, 1]$.
Let $E_{n+1}$ be the Stieltjes polynomial: the unique monic polynomial of degree $n + 1$ with
$$\int_{-1}^{1} P_n(x) E_{n+1}(x) x^k \, dx = 0 \quad \text{for } k = 0, 1, \ldots, n.$$
Then:

1. the zeros $y_1, \ldots, y_{n+1}$ of $E_{n+1}$ are real, simple, lie in $(-1, 1)$, and interlace with $x_1, \ldots, x_n$;
2. the interpolatory rule $K_{2n+1}(f) = \sum_{i=1}^{n} a_i f(x_i) + \sum_{j=1}^{n+1} b_j f(y_j)$ on these $2n + 1$ nodes satisfies $K_{2n+1}(p) = \int_{-1}^{1} p(x) \, dx$ for every polynomial $p$ of degree at most $3n + 1$.

## Remarks

Clause 2 follows from clause 1 by division.
Write $p = q \, P_n E_{n+1} + r$ with $\deg q \le n$ and $\deg r \le 2n$.
The term $q P_n E_{n+1}$ vanishes at all $2n+1$ nodes and has integral $0$ by the defining property of $E_{n+1}$.
The remainder $r$ is integrated exactly, because an interpolatory rule with $2n + 1$ nodes is exact up to degree $2n$.
Clause 1 is harder; it was proved by Szegő for the Legendre weight, and it can fail for other weight functions.
Example: for $n = 1$, $P_1 = x$ and the conditions give $E_2(x) = x^2 - \tfrac35$, so the Kronrod rule uses the nodes $0, \pm\sqrt{3/5}$ and is the $3$-point Gauss–Legendre rule, exact up to degree $5$.
In practice the difference $\abs{K_{2n+1}(f) - G_n(f)}$, where $G_n$ is the Gauss rule, serves as an error estimate that costs only $n + 1$ new function values.

## Explanations

### L1 human

A Gauss rule samples a function at a few clever points and gives a very accurate integral, but it does not tell how accurate.
The Kronrod extension adds new points between the old ones, keeps the old samples, and gives a second, more accurate value.
Comparing the two values tells how large the error is.

### L2 human

The $n$-point Gauss rule has [[degree of exactness|ZYT1JNT1Y0]] $2n - 1$, and a fresh $(2n+1)$-point Gauss rule would have degree $4n + 1$ but it would reuse almost none of the old nodes.
The Kronrod rule gives up some degree, $3n + 1$ instead of $4n + 1$, in exchange for reusing all $n$ old nodes.
Pairs such as $G_7$–$K_{15}$ and $G_{10}$–$K_{21}$ are the basis of adaptive integrators, for example in the QUADPACK library.
