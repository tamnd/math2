---
tag: AMXXM288Y0
kind: definition
name: Minimal sufficient statistic
msc: [62B05]
defines: RADE160VJN
uses: [QNMR5F525C, JZ6R7J36K5]
sources:
  - url: https://en.wikipedia.org/wiki/Sufficient_statistic
    locator: Minimal sufficiency
---

## Definition

Let $\set{P_\theta : \theta \in \Theta}$ be a [[statistical model|JZ6R7J36K5]] on $(S, \mathcal{S})$ and let $X$ be the data.
A statistic $T = T(X)$ is *minimal sufficient* if:

1. $T$ is [[sufficient|QNMR5F525C]] for $\theta$, and
2. for every sufficient statistic $U = U(X)$ there is a measurable function $\varphi$ with $T = \varphi(U)$ $P_\theta$-almost surely for every $\theta \in \Theta$.

## Remarks

Example: for $X_1, \dots, X_n$ i.i.d. Bernoulli($p$), $p \in (0, 1)$, the sum $T = \sum_i X_i$ is minimal sufficient.
Indeed, the likelihood ratio $P_p(X = x)/P_p(X = y) = (p/(1 - p))^{\sum_i x_i - \sum_i y_i}$ is free of $p$ only when $\sum_i x_i = \sum_i y_i$, and by the criterion below this makes $T$ minimal.
Non-example: for $n \ge 2$, the whole sample $X$ is sufficient but not minimal.
Clause 2 fails with $U = T$: $X$ is not a function of $T$, since $(1, 0, \dots, 0)$ and $(0, 1, 0, \dots, 0)$ have the same sum.
A common criterion, for a model with densities $f_\theta$: if $T(x) = T(y)$ holds exactly when $f_\theta(x)/f_\theta(y)$ does not depend on $\theta$, then $T$ is minimal sufficient.
A minimal sufficient statistic is unique up to one-to-one measurable functions.
