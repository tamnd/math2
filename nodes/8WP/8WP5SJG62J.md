---
tag: 8WP5SJG62J
kind: definition
name: Wolff algorithm
msc: [82M31, 82B20, 65C05]
defines: A9VN0WNG00
uses: [R0KGM32QN6, DR0E829VX6, CTGN6CK1ZS, 5NV45XZF81]
sources:
  - url: https://en.wikipedia.org/wiki/Wolff_algorithm
---

## Definition

Let $G = (V, E)$ be a finite graph, let $J > 0$ and $\beta > 0$, and consider the [[Ising model|R0KGM32QN6]] on $G$ with zero field and energy $H(\sigma) = -J \sum_{\set{u, v} \in E} \sigma_u \sigma_v$.
Let $p = 1 - e^{-2\beta J}$.
One step of the *Wolff algorithm* maps a configuration $\sigma$ to a configuration $\sigma'$ as follows.

1. Choose a vertex $x \in V$ uniformly at random, and let the cluster be $C = \set{x}$.
2. For each new vertex $u$ of $C$, test each untested edge $\set{u, v}$ with $v \notin C$ and $\sigma_v = \sigma_u$.
The test adds $v$ to $C$ with probability $p$, independently of other tests.
Repeat until no new vertex is added.
3. Let $\sigma'_v = -\sigma_v$ for $v \in C$ and $\sigma'_v = \sigma_v$ for $v \notin C$.

## Remarks

The step satisfies [[detailed balance|CTGN6CK1ZS]] with respect to the Ising measure.
The idea of the check: for a given cluster $C$, the edges on its boundary that join equal spins were all tested and rejected, each with probability $e^{-2\beta J}$.
Flipping $C$ turns the agreeing boundary edges into disagreeing ones and back, and the ratio of the rejection factors equals the ratio of the Boltzmann weights.
Example: on the graph with two vertices and one edge, from a disagreeing state the cluster is always a single vertex, and its flip makes the spins agree.
From an agreeing state the step makes them disagree with probability $1 - p = e^{-2\beta J}$, which matches the Ising ratio $\pi_a / \pi_d = e^{2 \beta J}$.
Non-example: growing the cluster with $p = 1$ flips the whole connected region of equal spins every time, which violates detailed balance for $\beta < \infty$.
The cluster $C$ has the law of the cluster of $x$ in one [[Swendsen–Wang|5NV45XZF81]] step.
Wolff introduced the method for the $O(n)$ models, where the flip is a reflection of the spins across a random hyperplane.

## Explanations

### L1 human

Instead of building all clusters as Swendsen–Wang does, the Wolff algorithm builds only the one through a random seed and always flips it.
