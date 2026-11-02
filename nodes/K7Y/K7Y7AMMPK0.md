---
tag: K7Y7AMMPK0
kind: definition
name: Credible interval
msc: [62F15, 62F25]
defines: 441PZ3T7F0
uses: [0KJ7ZS8AJA, 0JWRJX2RMP]
sources:
  - url: https://en.wikipedia.org/wiki/Credible_interval
---

## Definition

Let $\theta$ be a real parameter, and let $\Pi(\cdot \mid x)$ be its [[posterior distribution|0KJ7ZS8AJA]] given the observed data $x$.
Let $\alpha \in (0, 1)$.
A *credible interval* of level $1 - \alpha$ is an interval $[a, b]$, with $a$ and $b$ depending only on $x$, such that
$$\Pi\left([a, b] \mid x\right) \ge 1 - \alpha.$$
The *equal-tailed* credible interval has as endpoints the $\alpha/2$ and the $1 - \alpha/2$ quantiles of the posterior.
Suppose the posterior has a unimodal density $\pi(\cdot \mid x)$.
The *highest posterior density* interval is then the set $\set{\theta : \pi(\theta \mid x) \ge c}$, with $c$ chosen so that its posterior probability is $1 - \alpha$.

## Remarks

Example: with a uniform prior on $p \in (0, 1)$ and $n$ successes in $n$ Bernoulli trials, the posterior is $\mathrm{Beta}(n + 1, 1)$, with distribution function $p^{n + 1}$ on $[0, 1]$.
So $[\alpha^{1/(n+1)}, 1]$ has posterior probability $1 - \alpha$, and it is a credible interval of level $1 - \alpha$.
Non-example: a frequentist [[confidence interval|0K4NMMJBG2]] is defined by its coverage over repeated samples, not by a posterior probability.
For the same data it can differ from every credible interval, and it need not have posterior probability $1 - \alpha$.
In a parameter space of higher dimension the same notion is called a credible region or credible set.
