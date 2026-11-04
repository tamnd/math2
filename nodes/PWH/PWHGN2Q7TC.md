---
tag: PWHGN2Q7TC
kind: proof
name: Proof of the law of total probability
msc: [60A05]
proves: 0E5G5FMT2R
uses: [0ZYBZ34RT2, 0VGMEBVW1M, 0FJB06AD2P, 09CCE86A6D, 04WSW8T3SY, 0PQEBTYDZM]
sources:
  - url: https://proofwiki.org/wiki/Total_Probability_Theorem
---

## Proof

1. Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0ZYBZ34RT2]]. Let $(B_i)_{i \in I}$ be the given family, with $I = \set{1, \dots, N}$ or $I = \set{1, 2, \dots}$.
2. So the $B_i$ are pairwise disjoint events with $\bigcup_{i \in I} B_i = \Omega$ and $P(B_i) > 0$. They form a [[partition|09CCE86A6D]] of $\Omega$. Let $A$ be an event.
3. For each integer $i \ge 1$ let $E_i = A \cap B_i$ if $i \in I$, and $E_i = \varnothing$ if $i \notin I$. Each $E_i$ is in $\mathcal{F}$, because $\mathcal{F}$ is a [[σ-algebra|04WSW8T3SY]].
4. The $E_i$ are pairwise disjoint. For $i \ne j$ in $I$ we have $E_i \cap E_j \subseteq B_i \cap B_j = \varnothing$, and the empty sets meet nothing.
5. Their union is $\bigcup_{i \in I} (A \cap B_i) = A \cap \bigcup_{i \in I} B_i = A \cap \Omega = A$.
6. By the [[complement rule|0PQEBTYDZM]], $P(\varnothing) = 1 - P(\Omega) = 0$.
7. By the countable additivity of the [[probability measure|0VGMEBVW1M]] $P$ and step 6, $P(A) = \sum_{i \in I} P(A \cap B_i)$.
8. For $i \in I$ we have $P(B_i) > 0$. By the definition of [[conditional probability|0FJB06AD2P]], $P(A \cap B_i) = P(A \mid B_i) \, P(B_i)$.
9. Substituting step 8 into step 7 gives $P(A) = \sum_{i} P(A \mid B_i) \, P(B_i)$.

## Idea

The partition cuts $A$ into the disjoint pieces $A \cap B_i$, so $P(A)$ is the sum of their probabilities. Each piece has probability $P(A \mid B_i) P(B_i)$ by the definition of conditional probability.
