---
tag: 09T8ZHST1V
kind: definition
name: Independent sigma-algebras
msc: [60A05]
defines: 0B5BA4FRWS
uses: [04WSW8T3SY, 0GCVEV6BJA]
sources:
  - url: https://en.wikipedia.org/wiki/Independence_(probability_theory)
    locator: Independent σ-algebras
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a probability space, let $I$ be an index set, and for each $i \in I$ let $\mathcal{F}_i \subseteq \mathcal{F}$ be a [[σ-algebra|04WSW8T3SY]] on $\Omega$.
The family $(\mathcal{F}_i)_{i \in I}$ is independent if for each finite nonempty subset $J \subseteq I$ and each choice of events $A_j \in \mathcal{F}_j$ for $j \in J$,
$$P\left(\bigcap_{j \in J} A_j\right) = \prod_{j \in J} P(A_j).$$

## Remarks

Events $(A_i)_{i \in I}$ are [[mutually independent|0GCVEV6BJA]] if and only if the σ-algebras $\{\varnothing, A_i, A_i^c, \Omega\}$ are independent.
Random variables are independent when the σ-algebras that they generate are independent.
To check independence, it is enough to check the product formula on a generating family of each $\mathcal{F}_i$ that is closed under finite intersections. This follows from Dynkin's π-λ theorem.

## Explanations

### L1 human

A σ-algebra holds all the information of one part of an experiment, for example everything about the first roll of a die.
Two such σ-algebras are independent when information about one part never changes the chances about the other part.
