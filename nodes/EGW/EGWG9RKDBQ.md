---
tag: EGWG9RKDBQ
kind: definition
name: Inner measure
msc: [28A12]
defines: FTE966EMW8
uses: [P15VQS5DJ9, 00E0YZCERH, 0R3H5PANRQ]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_measure
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]].
Let $\mathcal{P}(X)$ be the [[power set|00E0YZCERH]] of $X$.
The *inner measure* induced by $\mu$ is the map $\mu_* \colon \mathcal{P}(X) \to [0, \infty]$ given by
$$\mu_*(A) = \sup \set{ \mu(B) : B \in \Sigma, \ B \subseteq A },$$
the [[supremum|0R3H5PANRQ]] of the measures of the measurable subsets of $A$.

## Remarks

The outer measure induced by $\mu$ is $\mu^*(A) = \inf \set{ \mu(B) : B \in \Sigma, \ A \subseteq B }$, and $\mu_*(A) \le \mu^*(A)$ for all $A$.
If $A \in \Sigma$, then $\mu_*(A) = \mu(A) = \mu^*(A)$.
For Lebesgue measure $\lambda$ on $\R^n$, the supremum may be taken over compact subsets of $A$.
For Lebesgue measure and a set $A$ with $\lambda^*(A) < \infty$, the set $A$ is Lebesgue measurable if and only if $\lambda_*(A) = \lambda^*(A)$.
Example: for $A = \Q \cap [0, 1]$ and Lebesgue measure, $A$ is measurable with $\lambda_*(A) = \lambda^*(A) = 0$.
Non-example of measurability: a Vitali set $V \subseteq [0, 1]$ has $\lambda_*(V) = 0 < \lambda^*(V)$.
Unlike an outer measure, an inner measure is superadditive: $\mu_*(A \cup B) \ge \mu_*(A) + \mu_*(B)$ for disjoint $A$ and $B$.
Some authors define inner measures abstractly by such axioms, without a given measure.
