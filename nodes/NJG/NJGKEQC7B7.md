---
tag: NJGKEQC7B7
kind: definition
name: Wright–Fisher model
msc: [92D10, 92D15, 60J10]
defines: SR4F169EKF
uses: [033TJBZDG0, 0VRWZDWW6B]
sources:
  - url: https://en.wikipedia.org/wiki/Genetic_drift
---

## Definition

Let $M \ge 1$ be the number of gene copies in the population, and consider two alleles $A$ and $a$.
For a diploid population of $N$ individuals, $M = 2N$.
The neutral *Wright–Fisher model* is the [[Markov chain|033TJBZDG0]] $(X_t)_{t \ge 0}$ on $\set{0, 1, \dots, M}$ in which $X_t$ is the number of copies of $A$ in generation $t$.
Given $X_t = i$, the number $X_{t+1}$ has the [[binomial distribution|0VRWZDWW6B]] with parameters $M$ and $i / M$.
So the transition probabilities are
$$P(X_{t+1} = j \mid X_t = i) = \binom{M}{j} \left( \frac{i}{M} \right)^j \left( 1 - \frac{i}{M} \right)^{M - j}.$$

## Remarks

Each copy in generation $t + 1$ picks its parent uniformly at random among the $M$ copies of generation $t$, independently of the others.
The states $0$ and $M$ are absorbing, and the chain reaches one of them with probability $1$.
Since $E[X_{t+1} \mid X_t] = X_t$, the chain is a martingale, and the probability of fixation of $A$ is $X_0 / M$.

Example: for $M = 2$ and $X_t = 1$, the next state is $0$, $1$ or $2$ with probabilities $1/4$, $1/2$ and $1/4$.

Non-example: a model in which each generation has exactly the same number of $A$ copies as the last one has no randomness.
It fails the binomial rule, since for $0 < i < M$ the binomial distribution gives positive probability to $j \ne i$.

With selection, the parameter $i/M$ is replaced by $(1 + s) i / ((1 + s) i + M - i)$, where $s$ is the selective advantage of $A$.
With mutation, it is replaced by the expected frequency after mutation.
