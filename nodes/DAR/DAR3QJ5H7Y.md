---
tag: DAR3QJ5H7Y
kind: statement
role: theorem
name: Monte Carlo integration
msc: [65C05, 65D30]
uses: [HWP11G3HTN, 2Z2QVWZ262, 0AREFQ9Z65, 00MRN0FARV, 0477R9PYAE, 0DFWHQ839T, 0EPZC4Z1FC, 0V0778DCW9]
about: [HWP11G3HTN]
sources:
  - url: https://en.wikipedia.org/wiki/Monte_Carlo_integration
same_as:
  wikidata: Q39879
  wikipedia: Monte Carlo integration
---

## Statement

Let $d \ge 1$, let $\Omega \subseteq \R^d$ be a measurable set with [[Lebesgue measure|2Z2QVWZ262]] $V$, $0 < V < \infty$, and let $f \colon \Omega \to \R$ be integrable, with $I = \int_\Omega f(x)\, dx$.
Let $X_1, X_2, \ldots$ be [[independent and identically distributed|00MRN0FARV]] random points with the [[uniform distribution|0AREFQ9Z65]] on $\Omega$, and let
$$Q_n = \frac{V}{n} \sum_{i=1}^{n} f(X_i).$$
Then:

1. $\mathbb E Q_n = I$ for every $n \ge 1$;
2. $Q_n \to I$ almost surely as $n \to \infty$;
3. if moreover $\int_\Omega f^2 < \infty$, then $\operatorname{Var} Q_n = V^2 \sigma^2 / n$, where $\sigma^2 = \operatorname{Var} f(X_1) = \frac{1}{V}\int_\Omega f^2 - \frac{I^2}{V^2}$;
4. under the hypothesis of clause 3 and $\sigma > 0$, $\sqrt{n}\,(Q_n - I) / (V \sigma)$ converges in distribution to the standard normal distribution.

## Remarks

The density of $X_1$ is $1/V$ on $\Omega$, so $\mathbb E[V f(X_1)] = \int_\Omega f$; this gives clause 1.
Clause 2 is the [[strong law of large numbers|0DFWHQ839T]] for the variables $V f(X_i)$, and clause 4 is the [[central limit theorem|0EPZC4Z1FC]].
Clause 3 follows from the [[variance of a sum of independent random variables|0V0778DCW9]].
So the root-mean-square error is $V\sigma / \sqrt{n}$; the rate $n^{-1/2}$ does not depend on the dimension $d$ or on the smoothness of $f$.
Example: for $f(x) = x^2$ on $\Omega = [0, 1]$ one has $I = 1/3$ and $\sigma^2 = 1/5 - 1/9 = 4/45$, so with $n = 10^4$ the standard error is about $0.003$.
In practice $\sigma$ is unknown and is replaced by the sample standard deviation, which gives approximate confidence intervals.
Without square-integrability clause 3 fails, and the convergence in clause 2 may be much slower than $n^{-1/2}$.

## Explanations

### L1 human

To find the integral of a function over a region, pick many random points in the region, average the function values, and multiply by the volume.
On average this gives exactly the right answer, and the scatter of the answer shrinks like one over the square root of the number of points.
The remarkable feature is that this rate is the same in dimension $1$ and in dimension $1000$.
Grid-based rules, by contrast, need exponentially many points as the dimension grows.

### L2 human

This is the basic [[Monte Carlo method|HWP11G3HTN]] applied to $Y = V f(X)$ with $X$ uniform.
In low dimension and for smooth $f$, classical quadrature rules converge much faster than $n^{-1/2}$, so Monte Carlo is mainly useful when $d$ is large or $f$ is rough.
Variance reduction techniques, such as importance sampling, control variates and stratification, keep the rate $n^{-1/2}$ but reduce the constant $\sigma$.
Quasi-Monte Carlo methods replace the random points by deterministic low-discrepancy points.
For functions of bounded variation in the sense of Hardy and Krause, they reach a rate close to $n^{-1}$.
Uniform sampling on $\Omega$ is often replaced by sampling from another density, which is the idea of importance sampling.
