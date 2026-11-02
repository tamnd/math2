---
tag: Y3TX4J41TP
kind: statement
role: theorem
name: Rao–Blackwell theorem
msc: [62F10, 62B05]
uses: [MSC0MR8VMH, WP4TGXJQJG, 0SSS6ERQ0S, 0TTDGTEFMN, 05NZ1HHQMV]
about: [WP4TGXJQJG, 0SSS6ERQ0S]
sources:
  - url: https://en.wikipedia.org/wiki/Rao–Blackwell_theorem
same_as:
  wikidata: Q579515
  wikipedia: Rao–Blackwell theorem
---

## Statement

Let $\set{P_\theta : \theta \in \Theta}$ be a [[parametric model|MSC0MR8VMH]] for an observation $X$, and let $g \colon \Theta \to \R$.
Let $T = T(X)$ be a [[sufficient statistic|WP4TGXJQJG]] for $\theta$.
Let $\delta(X)$ be an [[estimator|0SSS6ERQ0S]] of $g(\theta)$ with $E_\theta[\delta(X)^2] < \infty$ for every $\theta \in \Theta$.
Put $\delta_1 = E[\delta(X) \mid T]$, the [[conditional expectation|0TTDGTEFMN]] given $T$.
Then:

1. $\delta_1$ does not depend on $\theta$, so it is an estimator, and $E_\theta[\delta_1] = E_\theta[\delta(X)]$ for every $\theta$.
2. For every $\theta \in \Theta$, the [[mean squared errors|05NZ1HHQMV]] satisfy
$$E_\theta\big[(\delta_1 - g(\theta))^2\big] \le E_\theta\big[(\delta(X) - g(\theta))^2\big].$$
3. Equality holds in 2 for a given $\theta$ if and only if $\delta(X) = \delta_1$ with $P_\theta$-probability $1$.

## Remarks

Sufficiency means that the conditional law of $X$ given $T$ is the same for all $\theta$, so $\delta_1$ is computed without knowing $\theta$.
The tower property gives the same mean, and the law of total variance gives $\operatorname{Var}_\theta(\delta) = \operatorname{Var}_\theta(\delta_1) + E_\theta[\operatorname{Var}(\delta \mid T)]$.
The last term is nonnegative, and it is zero exactly when $\delta$ is already a function of $T$ almost surely.
The same argument with the conditional Jensen inequality shows that $\delta_1$ is at least as good as $\delta$ for every loss that is convex in the estimate.

Example: let $X_1, \dots, X_n$ be independent Bernoulli variables with parameter $p$.
The estimator $\delta = X_1$ is unbiased for $p$, and $T = X_1 + \cdots + X_n$ is sufficient.
By symmetry $E[X_1 \mid T] = T/n$, so the Rao–Blackwell step turns $X_1$, of variance $p(1-p)$, into the sample mean, of variance $p(1-p)/n$.

Sufficiency is needed: conditioning on a statistic that is not sufficient gives a quantity that depends on the unknown $\theta$ in general, and so it is not an estimator.

## Explanations

### L1 human

Start with any rough estimate, then average it over all the data sets that carry the same summary information.
The averaged estimate is never worse, in mean squared error, than the rough one.
So a good estimator should only depend on the data through a sufficient statistic.

### L2 human

The theorem is the main tool for improving unbiased estimators: conditioning on a sufficient statistic keeps the bias and lowers the variance.
Combined with completeness of the sufficient statistic, it gives the Lehmann–Scheffé theorem, which identifies the unique minimum-variance unbiased estimator.
In practice one often guesses a crude unbiased estimator, such as a single observation or an indicator, and computes its conditional expectation given the sufficient statistic.
