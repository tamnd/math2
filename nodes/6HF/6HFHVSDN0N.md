---
tag: 6HFHVSDN0N
kind: definition
name: Swendsen–Wang algorithm
msc: [82M31, 82B20, 65C05]
defines: 5NV45XZF81
uses: [R0KGM32QN6, DR0E829VX6, VCTMYPDXPX, 5GY2J6ZGXJ]
sources:
  - url: https://en.wikipedia.org/wiki/Swendsen%E2%80%93Wang_algorithm
---

## Definition

Let $G = (V, E)$ be a finite graph, let $J > 0$ and $\beta > 0$, and consider the [[Ising model|R0KGM32QN6]] on $G$ with zero field, with energy $H(\sigma) = -J \sum_{\set{u, v} \in E} \sigma_u \sigma_v$ for $\sigma \in \set{-1, +1}^V$.
Let $p = 1 - e^{-2 \beta J}$.
One step of the *Swendsen–Wang algorithm* maps a configuration $\sigma$ to a random configuration $\sigma'$ as follows.

1. For each edge $\set{u, v}$ with $\sigma_u = \sigma_v$, declare it open with probability $p$, independently of the other edges; declare every other edge closed.
2. Let the clusters be the connected components of the graph $(V, \text{open edges})$.
3. For each cluster independently, choose a value in $\set{-1, +1}$ uniformly at random, and let $\sigma'_v$ be this value for every vertex $v$ of the cluster.

## Remarks

The chain has the Ising measure as a stationary distribution, is irreducible and aperiodic, so it is a valid [[Monte Carlo method|DR0E829VX6]].
The reason is the Edwards–Sokal coupling of spins and open edges.
Its marginals are the Ising model and the [[random cluster model|VCTMYPDXPX]] with $q = 2$, and clauses 1 and 3 sample its two conditional laws.
Example: on the graph with two vertices and one edge, let $\pi_a$ and $\pi_d$ be the probabilities that the spins agree or disagree.
From an agreeing state the spins still agree after a step with probability $p + (1 - p)/2 = (1 + p)/2$; from a disagreeing state, with probability $1/2$.
Stationarity requires $\pi_a (1 - p)/2 = \pi_d / 2$, so $\pi_a / \pi_d = 1/(1 - p) = e^{2\beta J}$, which is the Ising ratio $e^{\beta J} / e^{-\beta J}$.
Non-example: opening edges between equal spins with probability $1/2$, whatever $\beta$, breaks the check above unless $e^{2\beta J} = 2$, so it does not sample the Ising model.
For the $q$-state [[Potts model|5GY2J6ZGXJ]] with energy $-J \sum \delta(\sigma_u, \sigma_v)$, the same algorithm works with $p = 1 - e^{-\beta J}$ and a uniform choice among the $q$ values.

## Explanations

### L1 human

Step 1 builds clusters of equal spins with a temperature-dependent bonding probability.
Step 3 throws away the old spins and paints each cluster with a fresh random value.
