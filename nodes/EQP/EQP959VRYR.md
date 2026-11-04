---
tag: EQP959VRYR
kind: proof
name: Proof of the law of total probability for an event and its complement
msc: [60A05]
proves: 0W62TKMW7V
uses: [0ZYBZ34RT2, 0E5G5FMT2R, 0PQEBTYDZM, 0B1FSS1VZW]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_total_probability
    locator: Statement
---

## Proof

1. Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0ZYBZ34RT2]] and let $A, B \in \mathcal{F}$ with $0 < P(B) < 1$. Let $B^c = \Omega \setminus B$ be the [[complement|0B1FSS1VZW]] of $B$.
2. By the [[complement rule|0PQEBTYDZM]], $P(B^c) = 1 - P(B)$. Since $P(B) < 1$, we get $P(B^c) > 0$.
3. The events $B_1 = B$ and $B_2 = B^c$ are disjoint, and $B_1 \cup B_2 = \Omega$. Both have positive probability, by the hypothesis and step 2.
4. The [[law of total probability|0E5G5FMT2R]] for the family $B_1, B_2$ gives $P(A) = P(A \mid B) \, P(B) + P(A \mid B^c) \, P(B^c)$.
5. Substituting step 2 gives $P(A) = P(A \mid B) \, P(B) + P(A \mid B^c) \, (1 - P(B))$.

## Idea

An event and its complement form the simplest partition of the sample space. The condition $0 < P(B) < 1$ makes both pieces have positive probability, so both conditional probabilities are defined.
