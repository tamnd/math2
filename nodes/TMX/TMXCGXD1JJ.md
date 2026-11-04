---
tag: TMXCGXD1JJ
kind: proof
name: Proof of Bayes' theorem
msc: [62F15]
proves: 0NM6E9VW04
uses: [0ZYBZ34RT2, 0FJB06AD2P]
sources:
  - url: https://en.wikipedia.org/wiki/Bayes'_theorem
    locator: Statement of theorem
---

## Proof

1. Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0ZYBZ34RT2]] and let $A, B \in \mathcal{F}$ with $P(A) > 0$ and $P(B) > 0$.
2. Since $P(B) > 0$, the definition of [[conditional probability|0FJB06AD2P]] gives $P(A \mid B) = P(A \cap B) / P(B)$.
3. Since $P(A) > 0$, the same definition gives $P(B \mid A) = P(B \cap A) / P(A)$.
4. Multiplying step 3 by $P(A)$ and using $B \cap A = A \cap B$ gives $P(A \cap B) = P(B \mid A) \, P(A)$.
5. Substituting step 4 into step 2 gives $P(A \mid B) = \dfrac{P(B \mid A) \, P(A)}{P(B)}$.

## Idea

The probability $P(A \cap B)$ can be written with a condition on $B$ or with a condition on $A$. Equating the two expressions and dividing by $P(B)$ swaps the roles of the two events.
