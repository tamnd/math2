---
tag: YVDWN0KVG4
kind: definition
name: Clenshaw–Curtis quadrature
msc: [65D32, 41A55]
defines: VEB7J3C74F
uses: [ADSVMCY77A, M6EAR1JHPP]
sources:
  - url: https://en.wikipedia.org/wiki/Clenshaw–Curtis_quadrature
---

## Definition

Let $N \ge 1$ and let $x_k = \cos(k\pi/N)$ for $k = 0, 1, \dots, N$.
For a continuous function $f$ on $[-1, 1]$, let $p_N$ be the interpolating polynomial of degree at most $N$ with $p_N(x_k) = f(x_k)$ for all $k$.
The $(N + 1)$-point *Clenshaw–Curtis quadrature* rule is the [[quadrature rule|ADSVMCY77A]]
$$\int_{-1}^{1} f(x)\,dx \approx \int_{-1}^{1} p_N(x)\,dx = \sum_{k=0}^{N} w_k f(x_k),$$
where $w_k = \int_{-1}^{1} \ell_k(x)\,dx$ and $\ell_k$ is the Lagrange basis polynomial of the node $x_k$.

## Remarks

The nodes are the extreme points of the [[Chebyshev polynomial|M6EAR1JHPP]] $T_N$ on $[-1, 1]$.
Writing $p_N(\cos\theta) = \sum_{j=0}^{N} c_j \cos(j\theta)$ gives $\int_{-1}^{1} p_N = \sum_j c_j \int_0^\pi \cos(j\theta)\sin\theta\,d\theta$, and $\int_0^\pi \cos(j\theta)\sin\theta\,d\theta$ is $2/(1 - j^2)$ for even $j$ and $0$ for odd $j$.
The rule is exact for polynomials of degree at most $N$, and of degree at most $N + 1$ when $N$ is even, by symmetry.

Example: $N = 2$.
The nodes are $1, 0, -1$, and the interpolatory weights are $\frac13, \frac43, \frac13$.
This is Simpson's rule; for $f = x^2$ it gives $\frac13 + 0 + \frac13 = \frac23 = \int_{-1}^{1} x^2\,dx$.

Non-example: the interpolatory rule at the equally spaced points $-1, -\frac13, \frac13, 1$ is a Newton–Cotes rule, not a Clenshaw–Curtis rule, because its nodes are not of the form $\cos(k\pi/3)$, which are $1, \frac12, -\frac12, -1$.
