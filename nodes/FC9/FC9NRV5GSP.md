---
tag: FC9NRV5GSP
kind: definition
name: Sampling distribution
msc: ["62E15", 62A01]
defines: 656Y8FA3RY
uses: [JZ6R7J36K5, 036756NFD6, 0QB913WM5E]
sources:
  - url: https://en.wikipedia.org/wiki/Sampling_distribution
---

## Definition

Let $\mathcal{P} = \set{P_\theta : \theta \in \Theta}$ be a [[statistical model|JZ6R7J36K5]] on a measurable space $(S, \mathcal{S})$, and let $X$ be a random element of $S$.
Let $T = g(X)$ be a [[statistic|036756NFD6]] with values in $\R^k$.
The *sampling distribution* of $T$ under $\theta$ is the [[probability distribution|0QB913WM5E]] of $T$ when $X$ has law $P_\theta$:
$$P_\theta(T \in B) = P_\theta\left(g^{-1}(B)\right)$$
for every Borel set $B \subseteq \R^k$.

## Remarks

Example: let $X_1, \dots, X_n$ be i.i.d. $\mathcal{N}(\mu, \sigma^2)$.
The sample mean $\bar{X}_n$ is a linear combination of independent normal variables, so its sampling distribution is $\mathcal{N}(\mu, \sigma^2/n)$.
Non-example: the histogram of one observed data set is not the sampling distribution of anything; it is a single realization, while a sampling distribution ranges over all possible data.
The standard deviation of the sampling distribution of an estimator is its standard error.
In general the sampling distribution depends on $\theta$; a statistic whose sampling distribution is the same for all $\theta$ is [[ancillary|VBW2A4H6TD]].
