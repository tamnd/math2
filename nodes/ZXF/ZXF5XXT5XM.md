---
tag: ZXF5XXT5XM
kind: definition
name: Completion of a measure
msc: [28A12]
defines: KJNSKV75VQ
uses: [P15VQS5DJ9, VQQM4Y550T, 22K8CSQTYM, 04WSW8T3SY]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_measure
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]].
Let $\Sigma_\mu$ be the family of sets $A \cup S$, where $A \in \Sigma$ and $S$ is a subset of some [[null set|VQQM4Y550T]] $N \in \Sigma$.
Define $\bar{\mu} \colon \Sigma_\mu \to [0, \infty]$ by $\bar{\mu}(A \cup S) = \mu(A)$.
The measure space $(X, \Sigma_\mu, \bar{\mu})$ is the *completion* of $(X, \Sigma, \mu)$.

## Remarks

The family $\Sigma_\mu$ is a [[σ-algebra|04WSW8T3SY]] that contains $\Sigma$.
The value $\bar{\mu}(A \cup S)$ does not depend on the choice of $A$ and $S$.
Indeed, if $A \cup S = A' \cup S'$ with $S \subseteq N$ and $S' \subseteq N'$, then $A$ and $A'$ differ only inside the null set $N \cup N'$, so $\mu(A) = \mu(A')$.
Then $\bar{\mu}$ is a [[complete measure|22K8CSQTYM]] that extends $\mu$, and it is the smallest complete extension.
For example, let $X = \set{1, 2, 3}$, $\Sigma = \set{\varnothing, \set{1, 2}, \set{3}, X}$, and $\mu(A) = 1$ if $3 \in A$ and $0$ otherwise.
The null set $\set{1, 2}$ gives $\Sigma_\mu$ equal to the power set of $X$, with $\bar{\mu}(A) = 1$ if $3 \in A$ and $0$ otherwise.
With the same $\Sigma$ and $\nu(A) = 1$ if $1 \in A$ and $0$ otherwise, the only null sets are $\varnothing$ and $\set{3}$.
So $\Sigma_\nu = \Sigma$, and the power set is not the σ-algebra of the completion of $\nu$.
The completion of Lebesgue measure on the Borel sets of $\R$ is Lebesgue measure on the Lebesgue measurable sets.
