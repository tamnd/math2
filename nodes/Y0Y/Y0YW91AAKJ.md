---
tag: Y0YW91AAKJ
kind: definition
name: Percolation threshold
msc: [60K35, 82B43, 82B26]
defines: MP8VSZK19A
uses: [BH7YPXCYDK, 00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Percolation_threshold
---

## Definition

Let $G = (V, E)$ be an infinite connected [[graph|00C0BR7D7H]] with countably many vertices, each of finite degree, and let $o \in V$.
For $p \in [0, 1]$, let $\theta(p)$ be the probability that the open cluster of $o$ is infinite in Bernoulli bond [[percolation|BH7YPXCYDK]] on $G$ with parameter $p$.
The *bond percolation threshold* of $G$ is
$$p_c(G) = \sup \set{p \in [0, 1] : \theta(p) = 0}.$$
The site percolation threshold is defined in the same way with site percolation.

## Remarks

Since $G$ is connected, $p_c$ does not depend on the choice of $o$.
By Kolmogorov's zero–one law, an infinite open cluster exists with probability $0$ when $p < p_c$ and with probability $1$ when $p > p_c$.
Example: for the line graph $\Z$, $\theta(p) = 0$ for every $p < 1$, so $p_c(\Z) = 1$.
Example: take the infinite tree in which every vertex has $d \ge 3$ neighbours.
After the first step, the open cluster of $o$ grows as a branching process with mean offspring $(d-1)p$, so $p_c = 1/(d-1)$.
Non-example: a finite graph does not satisfy the hypothesis; there every cluster is finite, so $\theta \equiv 0$ and the supremum carries no information.
For the lattice $\Z^d$ with $d \ge 2$, one has $0 < p_c < 1$.
