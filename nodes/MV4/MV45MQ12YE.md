---
tag: MV45MQ12YE
kind: definition
name: Gauss–Kronrod quadrature formula
msc: [65D32, 41A55]
defines: PT9V59MJZZ
uses: [RGGXDRCJVE, ZYT1JNT1Y0, ADSVMCY77A]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss–Kronrod_quadrature_formula
---

## Definition

Let $n \ge 1$ and let $x_1, \dots, x_n$ be the nodes of the $n$-point [[Gauss–Legendre rule|RGGXDRCJVE]] on $[-1, 1]$.
The $(2n + 1)$-point *Gauss–Kronrod quadrature formula* is a [[quadrature rule|ADSVMCY77A]]
$$\int_{-1}^{1} f(x)\,dx \approx \sum_{i=1}^{n} a_i f(x_i) + \sum_{j=1}^{n+1} b_j f(y_j)$$
in which:

1. the nodes $x_1, \dots, x_n$ are the Gauss–Legendre nodes;
2. the $n + 1$ new nodes $y_1, \dots, y_{n+1}$ and the $2n + 1$ weights $a_i, b_j$ are free parameters;
3. these parameters are chosen so that the rule is exact for every polynomial of degree at most $3n + 1$.

## Remarks

The rule has $3n + 2$ free parameters, which matches the $3n + 2$ conditions of exactness for $1, x, \dots, x^{3n+1}$.
The new nodes are the zeros of the Stieltjes polynomial $E_{n+1}$, the polynomial of degree $n + 1$ with $\int_{-1}^{1} E_{n+1}(x) P_n(x) x^k\,dx = 0$ for $k = 0, \dots, n$, where $P_n$ is the Legendre polynomial.
For the Legendre weight these zeros are real, lie in $(-1, 1)$, and interlace with the Gauss nodes.
In practice $\abs{G_n - K_{2n+1}}$, the difference of the Gauss value and the Kronrod value, serves as an error estimate.

Example: $n = 1$.
The Gauss node is $x_1 = 0$, and the rule $\int_{-1}^{1} f \approx \frac{8}{9} f(0) + \frac{5}{9} f(-\sqrt{3/5}) + \frac{5}{9} f(\sqrt{3/5})$ keeps it and adds two nodes.
It is exact for $1$ ($\frac89 + \frac{10}{9} = 2$), for $x^2$ ($\frac{10}{9} \cdot \frac35 = \frac23$), for $x^4$ ($\frac{10}{9} \cdot \frac{9}{25} = \frac25$), and for odd powers by symmetry, so up to degree $3n + 1 = 4$.
In this smallest case the Kronrod rule coincides with the $3$-point Gauss–Legendre rule.

Non-example: for $n = 2$ the $5$-point Gauss–Legendre rule is not a Gauss–Kronrod formula.
Its nodes are $0$ and the zeros of $63x^4 - 70x^2 + 15$, approximately $\pm 0.538$ and $\pm 0.906$, so they do not contain the $2$-point Gauss nodes $\pm 1/\sqrt{3} \approx \pm 0.577$.
