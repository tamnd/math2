---
tag: 30SKVHXFNQ
kind: definition
name: Restriction of a measure
msc: [28A12]
defines: EPS9JT55MV
uses: [P15VQS5DJ9, PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Restriction_(mathematics)
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]] and let $A \in \Sigma$.
The *restriction* of $\mu$ to $A$ is the map $\mu|_A \colon \Sigma \to [0, \infty]$ given by
$$\mu|_A(B) = \mu(A \cap B) \quad \text{for } B \in \Sigma.$$

## Remarks

The map $\mu|_A$ is a [[measure|PR11BZQQPG]] on $(X, \Sigma)$, because intersecting a disjoint family with $A$ gives a disjoint family with the same union intersected with $A$.
Example: if $\lambda$ is Lebesgue measure on $\R$ and $A = [0, 1]$, then $\lambda|_A([0, 5]) = \lambda([0, 1]) = 1$.
For a measurable $f \colon X \to [0, \infty]$ one has $\int_X f \, d(\mu|_A) = \int_A f \, d\mu$.
Non-example: for a set $A \notin \Sigma$, the sets $A \cap B$ need not lie in $\Sigma$, so the formula need not define a measure on $\Sigma$.
A related view keeps only the points of $A$: the trace $\sigma$-algebra $\Sigma_A = \set{A \cap B : B \in \Sigma}$ on $A$, with the measure $\mu$ restricted to $\Sigma_A$.
Other notations are $\mu \llcorner A$ and $\mu(\,\cdot \cap A)$.
