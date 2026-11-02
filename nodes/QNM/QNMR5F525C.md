---
tag: QNMR5F525C
kind: definition
name: Sufficient statistic
msc: [62B05]
defines: WP4TGXJQJG
uses: [JZ6R7J36K5, 036756NFD6, 0YAMJRK04E]
sources:
  - url: https://en.wikipedia.org/wiki/Sufficient_statistic
    locator: Mathematical definition
---

## Definition

Let $\set{P_\theta : \theta \in \Theta}$ be a [[statistical model|JZ6R7J36K5]] on a measurable space $(S, \mathcal{S})$, and let $X$ be the identity random element of $S$.
Let $T = T(X)$ be a [[statistic|036756NFD6]] with values in a measurable space.
The statistic $T$ is *sufficient* for $\theta$ if the following holds for every $A \in \mathcal{S}$.
There is a version of the conditional probability $P_\theta(X \in A \mid T)$ that is the same for all $\theta \in \Theta$.
That is, there is a function $k_A(T)$ with $k_A(T) = P_\theta(X \in A \mid T)$ $P_\theta$-almost surely, for every $\theta$, as a [[conditional expectation|0YAMJRK04E]] of $\mathbf{1}\set{X \in A}$ given $T$.

## Remarks

Example: let $X = (X_1, \dots, X_n)$ be i.i.d. Bernoulli($p$), $p \in (0, 1)$, and $T = X_1 + \dots + X_n$.
For $x \in \set{0, 1}^n$ with $x_1 + \dots + x_n = t$, one has $P_p(X = x \mid T = t) = p^t(1 - p)^{n - t} / \left(\binom{n}{t} p^t (1 - p)^{n - t}\right) = 1/\binom{n}{t}$, which does not depend on $p$; so $T$ is sufficient.
Non-example: for $n \ge 2$, the statistic $X_1$ is not sufficient, since given $X_1$ the variable $X_2$ is still Bernoulli($p$), and its law depends on $p$.
The whole sample $X$ is always sufficient, and any one-to-one measurable function of a sufficient statistic with measurable inverse is sufficient.
