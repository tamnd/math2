---
tag: DG8FBQ8FPY
kind: definition
name: Complete measure
msc: [28A12]
defines: 22K8CSQTYM
uses: [P15VQS5DJ9, VQQM4Y550T]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_measure
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]].
The measure $\mu$, or the measure space, is *complete* if for every [[null set|VQQM4Y550T]] $N \in \Sigma$ and every subset $S \subseteq N$, one has $S \in \Sigma$.

## Remarks

Counting measure on the power set of a set is complete, since every subset is measurable.
Let $X = \set{1, 2, 3}$, let $\Sigma = \set{\varnothing, \set{1, 2}, \set{3}, X}$, and let $\mu(A) = 1$ if $3 \in A$ and $\mu(A) = 0$ otherwise.
Then $\set{1, 2}$ is a null set, but its subset $\set{1}$ is not in $\Sigma$, so $\mu$ is not complete.
For a complete measure, a subset of a null set is again a null set, by monotonicity.
Lebesgue measure on the σ-algebra of Lebesgue measurable sets is complete.
Its restriction to the Borel sets is not complete: the Cantor set is a Borel null set with more subsets than there are Borel sets.
