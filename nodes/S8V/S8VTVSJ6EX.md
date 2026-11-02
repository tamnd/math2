---
tag: S8VTVSJ6EX
kind: statement
role: theorem
name: Selberg integral
msc: [33B15, 33C70, 15B52]
uses: [0H5SYBSED9, QHNWVSC6AQ, 0W29TBTY12]
about: [0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Selberg_integral
same_as:
  wikidata: Q7447525
  wikipedia: Selberg integral
---

## Statement

Let $n \ge 1$ be an integer, and let $\alpha, \beta, \gamma \in \C$ with $\operatorname{Re} \alpha > 0$, $\operatorname{Re} \beta > 0$ and
$$\operatorname{Re} \gamma > -\min\left( \frac{1}{n}, \frac{\operatorname{Re} \alpha}{n - 1}, \frac{\operatorname{Re} \beta}{n - 1} \right),$$
where the last two terms are omitted when $n = 1$.
Let $\Gamma$ be the [[gamma function|0H5SYBSED9]].
Then
$$\int_{[0,1]^n} \prod_{i=1}^{n} t_i^{\alpha - 1} (1 - t_i)^{\beta - 1} \prod_{1 \le i < j \le n} \abs{t_i - t_j}^{2\gamma} \, dt_1 \cdots dt_n = \prod_{j=0}^{n-1} \frac{\Gamma(\alpha + j\gamma)\, \Gamma(\beta + j\gamma)\, \Gamma(1 + (j+1)\gamma)}{\Gamma(\alpha + \beta + (n + j - 1)\gamma)\, \Gamma(1 + \gamma)}.$$

## Remarks

For $n = 1$ the formula is Euler's [[beta integral|QHNWVSC6AQ]] $\int_0^1 t^{\alpha-1} (1-t)^{\beta-1} \, dt = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}$.
Selberg proved it in 1944.
One proof first treats integer $\gamma$, where the integrand is a polynomial times the beta weights.
It then extends to complex $\gamma$ by Carlson's theorem on entire functions of exponential type.
Another proof, due to Aomoto, derives a recurrence in $\alpha$ by integrating a derivative and using the symmetry of the integrand.
Example: $n = 2$, $\alpha = \beta = 1$, $\gamma = 1$ gives $\int_0^1 \int_0^1 (t_1 - t_2)^2 \, dt_1 dt_2 = \frac{1}{6}$, and the right side is $\frac{\Gamma(1)^2 \Gamma(2)}{\Gamma(3)\Gamma(2)} \cdot \frac{\Gamma(2)^2 \Gamma(3)}{\Gamma(4)\Gamma(2)} = \frac12 \cdot \frac{2}{6} = \frac16$.
The bound on $\operatorname{Re} \gamma$ is needed for convergence: the factor $\abs{t_i - t_j}^{2\gamma}$ is not integrable near the diagonal when $\gamma$ is too negative.

## Explanations

### L1 human

The Selberg integral is an $n$-dimensional version of the beta integral.
It averages a power of the product of all the pairwise distances between $n$ random points in $[0, 1]$, with beta weights at the endpoints.
The surprise is that the answer is an explicit product of gamma values.

### L2 human

The factor $\prod_{i<j} \abs{t_i - t_j}^{2\gamma}$ is the power of a [[Vandermonde determinant|0P84B554AS]], the same factor that governs the eigenvalue densities of [[random matrices|1HS4RT7HK5]].
So the Selberg integral computes the normalizing constants of the Jacobi ensembles, and by limits those of the Laguerre and Gaussian ensembles; the Gaussian case is the [[Mehta integral|4N53T1BZ9S]].
It also has $q$-analogues and analogues for other root systems, linked to the [[Macdonald constant term conjecture|5J25W265JA]].
