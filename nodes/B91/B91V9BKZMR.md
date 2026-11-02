---
tag: B91V9BKZMR
kind: definition
name: Borel measure
msc: [28C15, 28A12]
defines: DYR1QFNGNJ
uses: [0CQHFPGJ45, 0WQXY32Q8D, PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Borel_measure
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $\mathcal{B}(X)$ be its [[Borel σ-algebra|0WQXY32Q8D]], the smallest σ-algebra on $X$ that contains every open set.
A *Borel measure* on $X$ is a [[measure|PR11BZQQPG]] $\mu \colon \mathcal{B}(X) \to [0, \infty]$.

## Remarks

Example: the Dirac measure $\delta_p$ at a point $p \in X$, with $\delta_p(A) = 1$ if $p \in A$ and $0$ otherwise, is a Borel measure.
It is defined on all subsets of $X$, hence on $\mathcal{B}(X)$, and it is countably additive because $p$ lies in at most one set of a disjoint family.

Non-example: on $\R$, let $\Sigma = \set{A \subseteq \R : A \text{ or } \R \setminus A \text{ is countable}}$ and let $\mu$ be $0$ on countable sets and $1$ on the others.
Then $\mu$ is a measure on $\Sigma$, but $\Sigma$ does not contain the interval $(0, 1)$, so $\mu$ is not defined on all Borel sets and is not a Borel measure.

Conventions vary.
Some authors call a measure on a σ-algebra containing $\mathcal{B}(X)$, such as Lebesgue measure on the Lebesgue sets, a Borel measure.
Some authors require in addition that $\mu(K) < \infty$ for every compact set $K$; then counting measure on $\R$ is not a Borel measure.
