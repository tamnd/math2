---
tag: 0CDVK9RQBH
kind: definition
name: Martingale
msc: [60G42]
defines: 0D0GBNDKDH
uses: [0YAMJRK04E, 0QH5ENKZM1, 0DCT0QZVQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Martingale_(probability_theory)
    locator: General definition
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a probability space with a filtration $(\mathcal{F}_n)_{n \ge 0}$: σ-algebras with $\mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq \dots \subseteq \mathcal{F}$.
A martingale with respect to $(\mathcal{F}_n)$ is a sequence $(M_n)_{n \ge 0}$ of real random variables with these three properties:
1. $M_n$ is $\mathcal{F}_n$-measurable for each $n$.
2. $E[|M_n|] < \infty$ for each $n$.
3. $E[M_{n+1} \mid \mathcal{F}_n] = M_n$ almost surely for each $n$.

## Remarks

If "$=$" in property 3 is replaced by "$\ge$", the sequence is a submartingale. If it is replaced by "$\le$", it is a supermartingale.
By the [[law of total expectation|04RRB6HM00]], $E[M_n] = E[M_0]$ for each $n$.
Examples: the simple random walk $S_n$ and $S_n^2 - n$ are martingales for the filtration of the steps.
Doob's optional stopping theorem and Doob's martingale convergence theorem are the main tools of the theory.

## Explanations

### L1 human

A martingale is a fair game: given everything you know now, your expected fortune after the next round is your fortune now.
No betting strategy can change the expected value of a martingale at fixed times.
