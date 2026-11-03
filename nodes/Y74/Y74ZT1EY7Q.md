---
tag: Y74ZT1EY7Q
kind: definition
name: Tajima's D
msc: [62P10, 92D10]
defines: F3P1C35630
uses: [AVJWVXG5VZ, T06A0Q0QNW, 0Q5CG2NEQ8]
sources:
  - url: https://en.wikipedia.org/wiki/Tajima%27s_D
---

## Definition

Let $n \ge 4$ DNA sequences be sampled, and let $S \ge 1$ be the number of segregating sites, as in the [[infinite sites model|AVJWVXG5VZ]].
Let $d_{ij}$ be the number of sites at which sequences $i$ and $j$ differ, and let $\pi = \binom{n}{2}^{-1} \sum_{i < j} d_{ij}$ be the mean pairwise difference.
Put
$$a_1 = \sum_{i=1}^{n-1} \frac1i, \quad a_2 = \sum_{i=1}^{n-1} \frac1{i^2}, \quad b_1 = \frac{n+1}{3(n-1)}, \quad b_2 = \frac{2(n^2 + n + 3)}{9n(n-1)},$$
$$c_1 = b_1 - \frac1{a_1}, \quad c_2 = b_2 - \frac{n+2}{a_1 n} + \frac{a_2}{a_1^2}, \quad e_1 = \frac{c_1}{a_1}, \quad e_2 = \frac{c_2}{a_1^2 + a_2}.$$
*Tajima's D* is the [[statistic|0Q5CG2NEQ8]]
$$D = \frac{\pi - S/a_1}{\sqrt{e_1 S + e_2 S(S - 1)}}.$$

## Remarks

The numerator is the difference of two estimates of $\theta$: $\pi$, and the [[Watterson estimator|T06A0Q0QNW]] $S/a_1$; the denominator estimates the standard deviation of that difference under the neutral model.
Example: take $n = 4$ sequences with one segregating site at which one sequence differs from the other three.
Then $S = 1$, $\pi = 3/6 = 1/2$, $a_1 = 11/6$, and a computation gives $e_1 = 2/363$, so $D = (1/2 - 6/11)/\sqrt{2/363} = -\sqrt6/4 \approx -0.61$.
Non-example: for $n = 3$ one has $b_1 = 2/3 = 1/a_1$, so $e_1 = 0$, and with $S = 1$ the denominator vanishes; this is why the definition asks $n \ge 4$.
