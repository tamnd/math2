---
tag: VWKWYB43A3
kind: definition
name: Binomial proportion confidence interval
msc: [62F25]
defines: MG2NCWHQF2
uses: [0K4NMMJBG2, 0VRWZDWW6B]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval
---

## Definition

Let $n \ge 1$, let $X$ have the [[binomial distribution|0VRWZDWW6B]] with parameters $n$ and unknown $p \in [0, 1]$, and let $\alpha \in (0, 1)$.
A *binomial proportion confidence interval* of level $1 - \alpha$ is an interval $[L(X), U(X)]$ with endpoints computed from $X$ alone.
Its coverage function is $C(p) = P_p\big(L(X) \le p \le U(X)\big)$.
It is a [[confidence interval|0K4NMMJBG2]] of level at least $1 - \alpha$ when $C(p) \ge 1 - \alpha$ for every $p \in [0, 1]$.
It is an approximate interval when $C(p)$ tends to $1 - \alpha$ as $n \to \infty$, for each fixed $p \in (0, 1)$.

## Remarks

Let $\hat p = X/n$ and let $z$ be the $1 - \alpha/2$ quantile of the standard normal law.
The Wald interval $\hat p \pm z \sqrt{\hat p(1 - \hat p)/n}$ is an approximate interval, by the normal approximation to the binomial law.
The Wilson interval is the set of $p$ with $\abs{\hat p - p} \le z \sqrt{p(1 - p)/n}$; it is also approximate, with better coverage for small $n$.
The Clopper–Pearson interval has level at least $1 - \alpha$ for every $p$; its endpoints are quantiles of beta laws.
Non-example: the Wald interval is not of level at least $1 - \alpha$ for all $p$.
If $X = 0$, it is the single point $\set{0}$, so for small $p > 0$ the coverage $C(p)$ is close to $P_p(X \ge 1) = 1 - (1 - p)^n$, which tends to $0$ as $p \to 0$.
