---
tag: HTWCTA2MTJ
kind: statement
role: theorem
name: Jenkins–Traub algorithm
msc: [65H04]
uses: [019MA1VTR2, 0BDX4MBKT4, 07EXVNF9VP, 09FTAET5Z4]
about: [019MA1VTR2]
sources:
  - url: https://en.wikipedia.org/wiki/Jenkins–Traub_algorithm
same_as:
  wikidata: Q6177639
  wikipedia: Jenkins–Traub algorithm
---

## Statement

Let $p$ be a [[monic polynomial|0BDX4MBKT4]] of degree $n \ge 2$ with [[complex|09FTAET5Z4]] coefficients and $p(0) \ne 0$.
Given complex shifts $s_0, s_1, \dots$ with $p(s_\lambda) \ne 0$, define polynomials $H^{(\lambda)}$ of degree at most $n - 1$ by $H^{(0)} = p'$ and
$$H^{(\lambda + 1)}(z) = \frac{1}{z - s_\lambda} \left( H^{(\lambda)}(z) - \frac{H^{(\lambda)}(s_\lambda)}{p(s_\lambda)} \, p(z) \right).$$
Write $\bar H^{(\lambda)}$ for $H^{(\lambda)}$ divided by its leading coefficient, when this is defined.
The *Jenkins–Traub algorithm* runs three stages:

1. no shift: $s_\lambda = 0$ for $0 \le \lambda < M$;
2. fixed shift: $s_\lambda = s$ for $M \le \lambda < L$, where $s$ is a fixed complex number;
3. variable shift: $s_L = s - p(s) / \bar H^{(L)}(s)$ and $s_{\lambda + 1} = s_\lambda - p(s_\lambda) / \bar H^{(\lambda + 1)}(s_\lambda)$ for $\lambda \ge L$.

Suppose $p$ has a [[root|019MA1VTR2]] $\alpha_1$ with $\abs{s - \alpha_1} < \abs{s - \alpha}$ for every other root $\alpha$ of $p$.
Then $\bar H^{(L)}(z) \to p(z)/(z - \alpha_1)$ as $L \to \infty$, coefficient by coefficient, and for $L$ large enough the variable shifts $s_\lambda$ of stage 3 converge to $\alpha_1$.

## Remarks

Write $p(z) = \prod_j (z - \alpha_j)$ over the roots, so that $H^{(0)} = p' = \sum_j p(z)/(z - \alpha_j)$.
One checks by induction that $H^{(\lambda)}$ stays a combination of the polynomials $p(z)/(z - \alpha_j)$, and that each shift multiplies the coefficient of the $j$-th one by $1/(\alpha_j - s_\lambda)$.
With a fixed shift $s$, the term of the root nearest to $s$ grows fastest, so the normalized $\bar H^{(\lambda)}$ tends to $p(z)/(z - \alpha_1)$.
Then $p(z)/\bar H^{(\lambda)}(z)$ is close to $z - \alpha_1$, and the stage 3 step behaves like [[Newton's method|07EXVNF9VP]] with an ever better model; its convergence is very fast.
In practice $s$ is taken at a random angle on a circle whose radius is a lower bound for the moduli of the roots.
Stage 2 is ended by a test on the shifts.
After a root is found, it is divided out and the algorithm runs again on the quotient.
A variant for real polynomials works with quadratic factors and real arithmetic.

## Explanations

### L1 human

The Jenkins–Traub algorithm finds the roots of a polynomial one after the other, roughly in order of increasing size.
It builds a sequence of auxiliary polynomials that slowly forget all roots except the one nearest to a chosen point.
Once that root dominates, a fast Newton-like phase homes in on it.

### L2 human

It was for a long time the standard black-box polynomial root finder in numerical libraries, under the name CPOLY for the complex version.
The stages give a global convergence guarantee that Newton's method alone lacks.
Finding the small roots first makes the deflation steps numerically stable.
