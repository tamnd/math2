---
tag: PQDC17AQHZ
kind: proof
name: Proof of the addition rule for two events
msc: [60A05]
proves: 0BZQ6ZX584
uses: [0ZYBZ34RT2, 00SQGJNRTB, 04WSW8T3SY, 0464Z0JP2E]
sources:
  - url: https://en.wikipedia.org/wiki/Probability_axioms
    locator: Elementary consequences
---

## Proof

1. Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0ZYBZ34RT2]] and let $A, B \in \mathcal{F}$ be [[events|00SQGJNRTB]].
2. The sets $A \cup B$ and $A \cap B = (A^c \cup B^c)^c$ are in $\mathcal{F}$, because $\mathcal{F}$ is a [[σ-algebra|04WSW8T3SY]].
3. We have $A \subseteq A \cup B$. By [[monotonicity of probability|0464Z0JP2E]], $P((A \cup B) \setminus A) = P(A \cup B) - P(A)$.
4. A point of $A \cup B$ that is not in $A$ lies in $B$. So $(A \cup B) \setminus A = B \setminus A$.
5. We have $A \cap B \subseteq B$. By monotonicity of probability again, $P(B \setminus (A \cap B)) = P(B) - P(A \cap B)$.
6. A point of $B$ lies outside $A \cap B$ exactly when it lies outside $A$. So $B \setminus (A \cap B) = B \setminus A$.
7. By steps 3 to 6, both differences equal $P(B \setminus A)$. So $P(A \cup B) - P(A) = P(B) - P(A \cap B)$.
8. Adding $P(A) + P(A \cap B)$ to both sides gives $P(A \cup B) + P(A \cap B) = P(A) + P(B)$. Subtracting $P(A \cap B)$ from both sides gives the equivalent form.

## Idea

The part of $B$ outside $A$ can be measured in two ways. It is what $A \cup B$ adds to $A$, and it is what remains of $B$ after removing $A \cap B$. Equating the two measurements gives the rule.
