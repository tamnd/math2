---
tag: 56MJSVTHG0
kind: definition
name: Measure space
msc: [28A12]
defines: P15VQS5DJ9
uses: [N4KDT83V3S, PR11BZQQPG, 0NFPJVJJHX]
sources:
  - url: https://en.wikipedia.org/wiki/Measure_space
---

## Definition

A *measure space* is a triple $(X, \Sigma, \mu)$, where $(X, \Sigma)$ is a [[measurable space|N4KDT83V3S]] and $\mu$ is a [[measure|PR11BZQQPG]] on $(X, \Sigma)$.

## Remarks

Let $X = \set{1, \ldots, 6}$, let $\Sigma$ be the power set of $X$, and let $\mu(A) = \abs{A} / 6$.
Then $\Sigma$ is a σ-algebra and $\mu$ is a measure, since the number of elements is additive over disjoint sets, so $(X, \Sigma, \mu)$ is a measure space.
On $\N$, let $\mathcal{A}$ be the family of finite sets and of sets with finite complement, and let $\mu(A) = \abs{A}$ for finite $A$ and $\mu(A) = \infty$ otherwise.
Then $(\N, \mathcal{A}, \mu)$ is not a measure space, since $\mathcal{A}$ is not a σ-algebra: it does not contain the set of even numbers.
A measure space with $\mu(X) = 1$ is a [[probability space|0NFPJVJJHX]].
