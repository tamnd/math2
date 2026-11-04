---
tag: FHMWMHSVNS
kind: proof
name: Proof of the monotonicity of probability
msc: [60A05]
proves: 0464Z0JP2E
uses: [0ZYBZ34RT2, 0VGMEBVW1M, 00SQGJNRTB, 0FE8Q5S42Y, 04WSW8T3SY, 0PQEBTYDZM]
sources:
  - url: https://en.wikipedia.org/wiki/Probability_axioms
    locator: Elementary consequences
---

## Proof

1. Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0ZYBZ34RT2]] and let $A, B \in \mathcal{F}$ be [[events|00SQGJNRTB]] with $A$ a [[subset|0FE8Q5S42Y]] of $B$.
2. The set $B \setminus A = B \cap A^c$ is in $\mathcal{F}$, because a [[σ-algebra|04WSW8T3SY]] is closed under complements and finite intersections.
3. By the [[complement rule|0PQEBTYDZM]] applied to the event $\Omega$, $P(\varnothing) = 1 - P(\Omega) = 0$.
4. Let $E_1 = A$, $E_2 = B \setminus A$ and $E_n = \varnothing$ for $n \ge 3$. These sets are pairwise disjoint, because no point of $B \setminus A$ lies in $A$.
5. Their union is $A \cup (B \setminus A)$. This equals $B$, because $A \subseteq B$.
6. By the countable additivity of the [[probability measure|0VGMEBVW1M]] $P$ and step 3, $P(B) = P(A) + P(B \setminus A)$.
7. All three numbers are real. So $P(B \setminus A) = P(B) - P(A)$.
8. The measure $P$ takes values in $[0, 1]$, so $P(B \setminus A) \ge 0$. Hence $P(A) \le P(B)$.

## Idea

When $A \subseteq B$, the event $B$ splits into $A$ and the part of $B$ outside $A$. Additivity gives the probability of $B$ as the probability of $A$ plus a nonnegative remainder.
