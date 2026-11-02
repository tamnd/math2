---
tag: YNBTV2S7SR
kind: definition
name: Frequentist inference
msc: [62A01]
defines: YDSNHKM3EG
uses: [FXCQWFY5RV, FC9NRV5GSP, JZ6R7J36K5, 0K4NMMJBG2]
sources:
  - url: https://en.wikipedia.org/wiki/Frequentist_inference
---

## Definition

Let $\set{P_\theta : \theta \in \Theta}$ be a [[statistical model|JZ6R7J36K5]] and let $X$ be the data, with law $P_\theta$ for a fixed unknown $\theta$.
*Frequentist inference* is the approach to [[statistical inference|FXCQWFY5RV]] in which:

1. the parameter $\theta$ is treated as fixed, and no probability distribution is placed on $\Theta$;
2. a procedure $\delta(X)$ is assessed through its [[sampling distribution|FC9NRV5GSP]] under $P_\theta$;
3. a guarantee about $\delta$ must hold for every $\theta \in \Theta$, or be stated as a function of $\theta$.

## Remarks

Example: a [[confidence set|0K4NMMJBG2]] of level $1 - \alpha$ is a set-valued statistic $C(X)$ with $P_\theta(\theta \in C(X)) \ge 1 - \alpha$ for every $\theta \in \Theta$.
For $n$ i.i.d. $\mathcal{N}(\theta, 1)$ observations, $C(X) = [\bar{X}_n - z/\sqrt{n}, \bar{X}_n + z/\sqrt{n}]$, with $z$ the $1 - \alpha/2$ quantile of $\mathcal{N}(0, 1)$, has coverage exactly $1 - \alpha$ for every $\theta$, since $\sqrt{n}(\bar{X}_n - \theta) \sim \mathcal{N}(0, 1)$.
Non-example: a Bayesian credible interval is computed from a posterior distribution on $\Theta$; it violates clause 1, and in general it has no coverage guarantee that holds for every $\theta$.
A test of level $\alpha$ is likewise a procedure whose probability of rejecting a true hypothesis is at most $\alpha$ under every $\theta$ of the hypothesis.
