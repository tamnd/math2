---
tag: 0GCVEV6BJA
kind: definition
name: Mutual independence of events
msc: [60A05]
defines: 001B78R0DJ
uses: [0P0MZ4X682, 0ZYBZ34RT2, 00SQGJNRTB]
sources:
  - url: https://en.wikipedia.org/wiki/Independence_(probability_theory)
    locator: More than two events
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0ZYBZ34RT2]], let $I$ be an index set, and let $A_i \in \mathcal{F}$ be an [[event|00SQGJNRTB]] for each $i \in I$.
The events $(A_i)_{i \in I}$ are mutually independent if for each finite nonempty subset $J \subseteq I$,
$$P\left(\bigcap_{j \in J} A_j\right) = \prod_{j \in J} P(A_j).$$

## Remarks

For two events this is the [[independence of two events|0P0MZ4X682]].
For three events $A, B, C$ the definition asks for four equations: one for each of the pairs $\{A, B\}$, $\{A, C\}$, $\{B, C\}$ and one for the triple $\{A, B, C\}$.
Mutual independence implies [[pairwise independence|0N57D1XY6T]]. The converse is false: see [[pairwise independent events that are not mutually independent|0AR4B3K5QD]].
If we replace some of the events $A_i$ by their complements, the family stays mutually independent.

## Explanations

### L1 human

For many events, independence must hold for every group of them, not only for every pair.
For three tosses of a fair coin, the events "toss $k$ gives heads" for $k = 1, 2, 3$ are mutually independent, and all three happen with probability $1/8$.
