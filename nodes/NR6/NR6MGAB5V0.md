---
tag: NR6MGAB5V0
kind: definition
name: Ancillary statistic
msc: [62B05]
defines: VBW2A4H6TD
uses: [JZ6R7J36K5, 036756NFD6]
sources:
  - url: https://en.wikipedia.org/wiki/Ancillary_statistic
---

## Definition

Let $\set{P_\theta : \theta \in \Theta}$ be a [[statistical model|JZ6R7J36K5]] and let $V = V(X)$ be a [[statistic|036756NFD6]] with values in a measurable space $(\mathcal{V}, \mathcal{B})$.
The statistic $V$ is *ancillary* if its distribution does not depend on $\theta$: for every $B \in \mathcal{B}$, the probability $P_\theta(V \in B)$ is the same for all $\theta \in \Theta$.

## Remarks

Example: let $X_1, \dots, X_n$ be i.i.d. $\mathcal{N}(\mu, 1)$ with $\mu \in \R$ and $n \ge 2$.
Then $X_i - \mu$ are i.i.d. $\mathcal{N}(0, 1)$, and the sample variance $S^2 = \frac{1}{n-1}\sum_i (X_i - \bar{X})^2$ is a function of them alone, because $X_i - \bar{X} = (X_i - \mu) - (\bar{X} - \mu)$; so $S^2$ is ancillary for $\mu$.
Non-example: in the same model, $\bar{X} \sim \mathcal{N}(\mu, 1/n)$, whose law changes with $\mu$, so $\bar{X}$ is not ancillary.
In a location model $X_i = \mu + \varepsilon_i$ with a fixed law of the $\varepsilon_i$, every function of the differences $X_i - X_j$ is ancillary.
In a scale model $X_i = \sigma \varepsilon_i$, every function of the ratios $X_i / X_j$ is ancillary, when these are defined.
