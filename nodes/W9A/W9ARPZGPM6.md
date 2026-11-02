---
tag: W9ARPZGPM6
kind: definition
name: Newton–Cotes formulas
msc: [65D32, 41A55]
defines: BQPQAY1FDJ
uses: [ADSVMCY77A, DA3CQJ5MJ6, ZYT1JNT1Y0]
sources:
  - url: https://en.wikipedia.org/wiki/Newton%E2%80%93Cotes_formulas
---

## Definition

Let $a < b$ and let $n \ge 1$ be an integer.
The *closed Newton–Cotes formula* with $n + 1$ nodes on $[a, b]$ is the [[quadrature rule|ADSVMCY77A]]
$$Q_n(f) = \sum_{i=0}^{n} w_i\, f(x_i), \qquad x_i = a + i h, \quad h = \frac{b - a}{n}, \qquad w_i = \int_a^b \ell_i(x)\, dx,$$
where $\ell_0, \dots, \ell_n$ are the [[Lagrange basis polynomials|DA3CQJ5MJ6]] for the nodes $x_0, \dots, x_n$.
For $n \ge 0$, the *open Newton–Cotes formula* with $n + 1$ nodes uses instead the nodes $x_i = a + i h$, $i = 1, \dots, n + 1$, with $h = (b - a)/(n + 2)$, and the weights $\int_a^b \ell_i(x)\, dx$ for these nodes.

## Remarks

So $Q_n(f)$ is the integral of the interpolating polynomial of $f$ at the nodes, and it is exact for polynomials of degree at most $n$.
The closed formula has [[degree of exactness|ZYT1JNT1Y0]] $n$ for odd $n$ and $n + 1$ for even $n$, by symmetry of the nodes.
Example: $n = 1$ gives the trapezoidal rule $\frac{h}{2}(f(a) + f(b))$, $n = 2$ gives Simpson's rule $\frac{h}{3}(f_0 + 4 f_1 + f_2)$, and $n = 3$ gives Simpson's $3/8$ rule $\frac{3h}{8}(f_0 + 3 f_1 + 3 f_2 + f_3)$; the open formula with $n = 0$ is the midpoint rule.
Non-example: the two-point Gauss–Legendre rule on $[-1, 1]$ has nodes $\pm 1/\sqrt{3}$ and weights $1$.
It is interpolatory but not a Newton–Cotes formula.
Its nodes are neither the endpoints $\pm 1$, as a closed formula needs, nor $\pm 1/3$, as the open formula with two nodes needs.
For closed formulas with $n \ge 8$ some weights are negative, and as $n \to \infty$ the formulas need not converge even for analytic integrands, much as in Runge's phenomenon.
