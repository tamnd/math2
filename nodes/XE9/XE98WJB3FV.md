---
tag: XE98WJB3FV
kind: statement
role: theorem
name: Gauss–Laguerre quadrature
msc: [65D32, 41A55, 33C45]
uses: [FP37BTP93K, WAMRHWW82R, ZYT1JNT1Y0]
about: [FP37BTP93K]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%E2%80%93Laguerre_quadrature
same_as:
  wikidata: Q4218412
  wikipedia: Gauss–Laguerre quadrature
---

## Statement

Let $n \ge 1$ and let $L_n$ be the [[Laguerre polynomial|WAMRHWW82R]] of degree $n$, normalised by $L_n(0) = 1$.
Let $x_1, \ldots, x_n$ be the zeros of $L_n$; they are simple and lie in $(0, \infty)$.
Set
$$w_i = \frac{x_i}{(n+1)^2 \, L_{n+1}(x_i)^2} = \frac{1}{x_i \, L_n'(x_i)^2}, \qquad i = 1, \ldots, n.$$
Then $w_i > 0$ for each $i$, and for every polynomial $p$ of degree at most $2n - 1$,
$$\int_{0}^{\infty} e^{-x} p(x) \, dx = \sum_{i=1}^{n} w_i \, p(x_i).$$

## Remarks

This is the [[Gaussian quadrature|FP37BTP93K]] rule for the weight $e^{-x}$ on $[0, \infty)$, whose orthogonal polynomials are the $L_n$; the proof is the general one, by division by $L_n$ and orthogonality.
Example: for $n = 2$, $L_2(x) = \frac12 (x^2 - 4x + 2)$ has zeros $2 \pm \sqrt{2}$ and $L_2'(x) = x - 2 = \pm\sqrt{2}$ there, so $w = \frac{1}{2(2 \pm \sqrt{2})} = \frac{2 \mp \sqrt{2}}{4}$.
Check: the weights add up to $1 = \int_0^\infty e^{-x} dx$, and $\sum_i w_i x_i^2 = \frac{2 + \sqrt{2}}{2} + \frac{2 - \sqrt{2}}{2} = 2 = \int_0^\infty x^2 e^{-x} dx$.
The degree $2n - 1$ cannot be raised: for $p = L_n^2$ the rule gives $0$ and the integral is positive.
With the generalized Laguerre polynomials $L_n^{(\alpha)}$, $\alpha > -1$, the same construction gives rules for the weight $x^{\alpha} e^{-x}$.

## Explanations

### L1 human

Integrals from $0$ to infinity with a decaying factor $e^{-x}$ appear in physics, probability and the Laplace transform.
Gauss–Laguerre quadrature replaces such an integral by a weighted sum of a few values of the remaining factor at special points.
With $n$ points it integrates every polynomial of degree up to $2n - 1$ exactly.

### L2 human

To integrate $\int_0^\infty g(x)\,dx$, one writes $g(x) = e^{-x} \big(e^x g(x)\big)$ and applies the rule to $f(x) = e^x g(x)$.
This works well when $f$ is smooth and grows at most like a polynomial.
The rule is the half-line companion of [[Gauss–Hermite quadrature|89S5KGQEMJ]] on the whole line and of Gauss–Legendre quadrature on a bounded interval.
