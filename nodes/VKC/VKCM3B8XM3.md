---
tag: VKCM3B8XM3
kind: definition
name: Fixation probability
msc: [92D15, 60J10]
defines: 5APPKBE8Q4
uses: [0YB93GWTKK]
sources:
  - url: https://en.wikipedia.org/wiki/Fixation_(population_genetics)
---

## Definition

Let $M \ge 1$, and let $(X_t)_{t \ge 0}$ be a population model given by a Markov chain on $\set{0, 1, \dots, M}$.
Here $X_t$ is the number of copies of an allele $A$ at time $t$.
Assume that $0$ and $M$ are absorbing states, so that $(X_t)$ is an [[absorbing Markov chain|0YB93GWTKK]].
The *fixation probability* of $A$ from state $i$ is
$$u(i) = P(X_t = M \text{ for some } t \ge 0 \mid X_0 = i).$$

## Remarks

The function $u$ satisfies $u(0) = 0$, $u(M) = 1$, and $u(i) = \sum_j P(i \to j) \, u(j)$ for $0 < i < M$.
If the chain is absorbed with probability $1$, then $1 - u(i)$ is the probability that $A$ is lost.

Example: in the neutral [[Wright–Fisher model|SR4F169EKF]], $X_t$ is a bounded martingale absorbed at $0$ or $M$.
By optional stopping, $i = E[X_0] = M \, u(i)$, so $u(i) = i / M$.
For one new mutant among $M = 100$ copies, $u(1) = 0.01$.

Non-example: in a model with recurrent mutation from $a$ to $A$ and back, the state $0$ is not absorbing.
Then the definition does not apply, and one studies instead the stationary distribution of $X_t$.

In the [[Moran process|A9M7VKRRV9]] with fitness $r \ne 1$, $u(i) = (1 - r^{-i}) / (1 - r^{-N})$, where $N = M$ is the population size.
