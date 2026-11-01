---
tag: XZ1EXQPJ6S
kind: statement
role: theorem
name: Generalized mean inequality
msc: ["26E60", 26D15]
uses: [0RWMRTPC87, 0DRF0F3XC9]
about: [0RWMRTPC87]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_mean
---

## Statement

Let $x_1, \dots, x_n > 0$ be real numbers and let $w_1, \dots, w_n > 0$ be weights with $w_1 + \dots + w_n = 1$.
For a real number $p \ne 0$, let
$$M_p = \Big( \sum_{i=1}^{n} w_i x_i^{p} \Big)^{1/p}, \qquad M_0 = \prod_{i=1}^{n} x_i^{w_i}.$$
If $p < q$, then $M_p \le M_q$, with equality if and only if $x_1 = x_2 = \dots = x_n$.

## Remarks

Proof idea: for $0 < p < q$, the function $t \mapsto t^{q/p}$ is strictly convex on $(0, \infty)$, and [[Jensen's inequality|0RWMRTPC87]] applied to the numbers $x_i^p$ gives $M_p^q \le M_q^q$.
The case $p < q < 0$ follows by applying this to the numbers $1 / x_i$, since $M_{-r}(x) = 1 / M_r(1/x)$.
The cases with $p = 0$ or $q = 0$ follow from the weighted [[AM–GM inequality|0DRF0F3XC9]], or from the limit $M_p \to M_0$ as $p \to 0$.

Example: the cases $p = -1, 0, 1, 2$ give harmonic mean $\le$ geometric mean $\le$ arithmetic mean $\le$ quadratic mean.
For $x = (1, 4)$ with equal weights these are $8/5$, $2$, $5/2$ and $\sqrt{17/2} \approx 2.92$.

Mathlib states a related form as `Real.rpow_arith_mean_le_arith_mean_rpow`.

## Explanations

### L1 human

There are many ways to average positive numbers: the usual average, the geometric mean, the root mean square, and more.
They form one family indexed by an exponent $p$.
The inequality says that a larger exponent always gives a larger average, unless all the numbers are equal.

### L2 human

The power mean inequality packages the AM–GM inequality, the AM–HM inequality and the AM–QM inequality into one statement.
It is a direct consequence of Jensen's inequality for the power functions.
As $p \to \infty$ the mean $M_p$ tends to $\max_i x_i$, and as $p \to -\infty$ it tends to $\min_i x_i$, so all the means lie between the smallest and the largest number.
