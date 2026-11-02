---
tag: 89S5KGQEMJ
kind: statement
role: theorem
name: Gauss–Hermite quadrature
msc: [65D32, 41A55, 33C45]
uses: [FP37BTP93K, MGACY98E9H, ZYT1JNT1Y0]
about: [FP37BTP93K]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%E2%80%93Hermite_quadrature
same_as:
  wikidata: Q5527850
  wikipedia: Gauss–Hermite quadrature
---

## Statement

Let $n \ge 1$ and let $H_n$ be the physicists' [[Hermite polynomial|MGACY98E9H]] of degree $n$.
Let $x_1, \ldots, x_n$ be the zeros of $H_n$; they are real and simple.
Set
$$w_i = \frac{2^{n-1} \, n! \, \sqrt{\pi}}{n^2 \, H_{n-1}(x_i)^2}, \qquad i = 1, \ldots, n.$$
Then $w_i > 0$ for each $i$, and for every polynomial $p$ of degree at most $2n - 1$,
$$\int_{-\infty}^{\infty} e^{-x^2} p(x) \, dx = \sum_{i=1}^{n} w_i \, p(x_i).$$

## Remarks

This is the [[Gaussian quadrature|FP37BTP93K]] rule for the weight $e^{-x^2}$ on $\R$, whose orthogonal polynomials are the $H_n$.
For $p$ of degree at most $2n - 1$, write $p = q H_n + r$ with $\deg q, \deg r \le n - 1$.
Orthogonality kills $\int e^{-x^2} q H_n$, and $r$ is integrated exactly by the interpolatory weights.
The closed form of $w_i$ comes from the Christoffel–Darboux formula.
Example: for $n = 2$, $H_2 = 4x^2 - 2$ has zeros $\pm 1/\sqrt{2}$, and $H_1(x) = 2x$ gives $w_1 = w_2 = \frac{4\sqrt{\pi}}{4 \cdot 2} = \frac{\sqrt{\pi}}{2}$.
Check with $p(x) = x^2$: the rule gives $2 \cdot \frac{\sqrt{\pi}}{2} \cdot \frac12 = \frac{\sqrt{\pi}}{2} = \int_{\R} x^2 e^{-x^2} dx$.
For $f \in C^{2n}(\R)$ with suitable growth, the error is $\frac{n! \sqrt{\pi}}{2^n} \frac{f^{(2n)}(\xi)}{(2n)!}$ for some real $\xi$.
The degree $2n - 1$ is the best possible: $p = H_n^2$ has degree $2n$, the rule gives $0$, but the integral is positive.

## Explanations

### L1 human

Many integrals over the whole real line carry a bell-shaped factor $e^{-x^2}$.
Gauss–Hermite quadrature replaces such an integral by a weighted sum of a few function values at special points.
With $n$ points it is exact for every polynomial up to degree $2n - 1$, and very accurate for smooth functions that do not grow too fast.

### L2 human

The rule computes expectations under a normal distribution: if $Z$ is standard normal, then $\mathbb{E}[g(Z)] = \frac{1}{\sqrt{\pi}} \int_{\R} e^{-x^2} g(\sqrt{2} x) \, dx$.
It is used in statistics, in quantum mechanics with harmonic oscillator states, and in uncertainty quantification.
For functions that are not smooth or that grow fast, the nodes spread out and accuracy can be poor, and a change of variable may help.
