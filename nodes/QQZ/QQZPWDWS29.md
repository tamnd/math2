---
tag: QQZPWDWS29
kind: statement
role: theorem
name: Lehmann–Scheffé theorem
msc: [62F10, 62B05]
uses: [MSC0MR8VMH, WP4TGXJQJG, DED6JFAV1K, 0BWGTN92FG, 0477R9PYAE, ZCJX7THBNJ, Y3TX4J41TP]
about: [ZCJX7THBNJ, DED6JFAV1K]
sources:
  - url: https://en.wikipedia.org/wiki/Lehmann–Scheffé_theorem
same_as:
  wikidata: Q1129636
  wikipedia: Lehmann–Scheffé theorem
---

## Statement

Let $\set{P_\theta : \theta \in \Theta}$ be a [[parametric model|MSC0MR8VMH]] for an observation $X$, and let $g \colon \Theta \to \R$.
Let $T = T(X)$ be a [[sufficient statistic|WP4TGXJQJG]] that is [[complete|DED6JFAV1K]].
Let $h$ be a measurable function such that $h(T)$ is [[unbiased|0BWGTN92FG]] for $g(\theta)$ and $\operatorname{Var}_\theta(h(T)) < \infty$ for every $\theta \in \Theta$.
Then $h(T)$ is a [[uniformly minimum-variance unbiased estimator|ZCJX7THBNJ]] of $g(\theta)$: for every unbiased estimator $\delta$ of $g(\theta)$ and every $\theta \in \Theta$,
$$\operatorname{Var}_\theta(h(T)) \le \operatorname{Var}_\theta(\delta).$$
Moreover, $h(T)$ is the only such estimator, up to equality with $P_\theta$-probability $1$ for every $\theta$.

## Remarks

Completeness gives uniqueness: if $h_1(T)$ and $h_2(T)$ are both unbiased for $g(\theta)$, then $E_\theta[h_1(T) - h_2(T)] = 0$ for all $\theta$, so $h_1(T) = h_2(T)$ almost surely.
Given any unbiased $\delta$ with finite [[variance|0477R9PYAE]], the [[Rao–Blackwell theorem|Y3TX4J41TP]] gives the unbiased estimator $E[\delta \mid T]$, a function of $T$, with variance at most $\operatorname{Var}_\theta(\delta)$.
By uniqueness this function is $h(T)$, which proves the claim.

Example: let $X_1, \dots, X_n$ be independent Poisson variables with mean $\lambda > 0$.
The sum $T = X_1 + \cdots + X_n$ is complete and sufficient, and $T/n$ is unbiased for $\lambda$.
So the sample mean is the unique minimum-variance unbiased estimator of $\lambda$.

Completeness cannot be dropped from the uniqueness argument.
If $T$ is not complete, two different functions of $T$ can be unbiased for the same $g(\theta)$.
Then the Rao–Blackwell step alone does not single out a best one.

## Explanations

### L1 human

If a summary of the data is sufficient and complete, then any unbiased estimate built only from that summary is automatically the best unbiased estimate.
"Best" means smallest variance, for every value of the unknown parameter at once.

### L2 human

This is the standard route to minimum-variance unbiased estimators.
First find a complete sufficient statistic, often the natural statistic of an exponential family of full rank.
Then find any function of it that is unbiased, for example by solving $E_\theta[h(T)] = g(\theta)$ or by Rao–Blackwellizing a simple unbiased estimator.
The theorem then certifies optimality without comparing with other estimators one by one.
