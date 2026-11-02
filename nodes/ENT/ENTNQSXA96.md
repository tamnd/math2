---
tag: ENTNQSXA96
kind: definition
name: Bochner integral
msc: [28B05, 46G10]
defines: MHSMQ097GP
uses: [P15VQS5DJ9, JDM2M1FRY6, DG76G5Z6XW, 0BDTTM24DP]
sources:
  - url: https://en.wikipedia.org/wiki/Bochner_integral
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]] and let $E$ be a [[Banach space|0BDTTM24DP]] over $\R$ or $\C$.
An *integrable simple function* is a function $s = \sum_{i=1}^{n} \mathbf{1}_{A_i} e_i$ with $e_i \in E$ and pairwise disjoint $A_i \in \Sigma$ with $\mu(A_i) < \infty$.
Its integral is $\int_X s \, d\mu = \sum_{i=1}^{n} \mu(A_i) \, e_i$.
A function $f \colon X \to E$ is *Bochner integrable* if both of the following hold.

1. The function $f$ is [[strongly measurable|JDM2M1FRY6]].
2. There are integrable simple functions $s_1, s_2, \dots$ with $\lim_{n \to \infty} \int_X \norm{f - s_n} \, d\mu = 0$.

The integrals in clause 2 are [[integrals of non-negative functions|DG76G5Z6XW]].
The *Bochner integral* of $f$ is then $\int_X f \, d\mu = \lim_{n \to \infty} \int_X s_n \, d\mu$, a limit in $E$.

## Remarks

The limit exists, since $\norm{\int s_n - \int s_m} \le \int \norm{s_n - s_m}$, so the integrals form a Cauchy sequence in $E$.
It does not depend on the choice of the $s_n$.

Example: let $X = [0, 1]$ with Lebesgue measure and let $f \colon X \to E$ be continuous.
The step functions $s_n$ equal to $f(k/n)$ on $[k/n, (k+1)/n)$ for $0 \le k < n$ and to $f(1)$ at $1$ converge to $f$ uniformly, so $\int \norm{f - s_n} \to 0$.
So $f$ is Bochner integrable, and its integral is the limit of the Riemann sums $\frac{1}{n} \sum_{k=0}^{n-1} f(k/n)$.

Non-example: take $X = \R$ with Lebesgue measure, $E = \R$ and $f = 1$.
It is strongly measurable, but every integrable simple function vanishes outside a set of finite measure, so $\int \norm{f - s} = \infty$ for each of them.

Bochner's theorem: a strongly measurable function $f$ is Bochner integrable if and only if $\int_X \norm{f} \, d\mu < \infty$.
For $E = \R$ or $E = \C$ the Bochner integral is the Lebesgue integral.
For a bounded linear map $T \colon E \to F$ one has $T \int f \, d\mu = \int T f \, d\mu$.
