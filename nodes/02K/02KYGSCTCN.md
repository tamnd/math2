---
tag: 02KYGSCTCN
kind: definition
name: Stationary distribution
msc: [60J10]
defines: 0KRH5157WP
uses: [033TJBZDG0, 0F1KBVY161]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete-time_Markov_chain
    locator: Stationary distributions
---

## Definition

Let $P = (p_{ij})_{i, j \in S}$ be the [[transition matrix|0F1KBVY161]] of a time-homogeneous [[Markov chain|033TJBZDG0]] on a countable state space $S$.
A stationary distribution of the chain is a family $\pi = (\pi_j)_{j \in S}$ of real numbers with $\pi_j \ge 0$ for each $j$, $\sum_{j \in S} \pi_j = 1$, and
$$\pi_j = \sum_{i \in S} \pi_i \, p_{ij} \quad \text{for each } j \in S.$$
In matrix form, $\pi P = \pi$ for the row vector $\pi$.

## Remarks

If $X_0$ has the law $\pi$, then $X_n$ has the law $\pi$ for each $n \ge 0$.
An irreducible chain on a finite state space has exactly one stationary distribution. Its entries are positive, and $\pi_j = 1 / E_j[T_j]$, where $T_j$ is the time of the first return to $j$.
For an irreducible and aperiodic finite chain, $P(X_n = j) \to \pi_j$ as $n \to \infty$, for each initial law.
The simple random walk on $\mathbb{Z}$ has no stationary distribution.

## Explanations

### L1 human

A stationary distribution is a balance: the flow of probability into each state equals the flow out.
For many chains, it also describes the long-run fraction of time that the chain spends in each state.
