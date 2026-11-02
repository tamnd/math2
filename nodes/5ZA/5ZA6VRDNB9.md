---
tag: 5ZA6VRDNB9
kind: definition
name: Gauss–Legendre quadrature
msc: [65D32, 41A55, 33C45]
defines: RGGXDRCJVE
uses: [FP37BTP93K, QFYGJVA996]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss–Legendre_quadrature
---

## Definition

Let $n \ge 1$ and let $P_n$ be the [[Legendre polynomial|QFYGJVA996]] of degree $n$.
Let $x_1, \dots, x_n$ be the zeros of $P_n$; they are distinct and lie in $(-1, 1)$.
The $n$-point *Gauss–Legendre quadrature* rule is
$$\int_{-1}^{1} f(x)\,dx \approx \sum_{i=1}^{n} w_i f(x_i), \qquad w_i = \frac{2}{(1 - x_i^2)\, P_n'(x_i)^2}.$$
It is the $n$-point [[Gaussian quadrature|FP37BTP93K]] rule for the weight $w = 1$ on $(-1, 1)$.

## Remarks

The rule is exact for every polynomial of degree at most $2n - 1$.
For an interval $[a, b]$ one uses $\int_a^b g(t)\,dt = \frac{b - a}{2} \int_{-1}^{1} g\big(\frac{b - a}{2} x + \frac{a + b}{2}\big)\,dx$.

Example: $n = 2$.
Here $P_2(x) = \frac12 (3x^2 - 1)$, with zeros $\pm 1/\sqrt{3}$, and $P_2'(x) = 3x$.
The weights are $2 / \big((2/3) \cdot 3\big) = 1$.
For $f(x) = x^2$ the rule gives $2/3$, and for $f(x) = x^3$ it gives $0$, both exact.

Non-example: for $n = 2$ and $f(x) = x^4$ the rule gives $2/9$ while the integral is $2/5$.
This is expected, since $4 > 2n - 1 = 3$.
