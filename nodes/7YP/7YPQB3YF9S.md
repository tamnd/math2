---
tag: 7YPQB3YF9S
kind: proof
name: Proof of Boole's inequality by disjoint pieces
msc: ["60E15"]
proves: 0EGSEE9J9R
uses: [0ZYBZ34RT2, 0VGMEBVW1M, 00SQGJNRTB, 04WSW8T3SY, 0464Z0JP2E, 0PQEBTYDZM]
sources:
  - url: https://en.wikipedia.org/wiki/Boole's_inequality
    locator: Proof without using induction
---

## Proof

1. Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0ZYBZ34RT2]] and let $A_1, A_2, \dots$ be [[events|00SQGJNRTB]].
2. If the family is finite, say $A_1, \dots, A_N$, set $A_i = \varnothing$ for $i > N$. This changes neither the union nor the sum, because $P(\varnothing) = 1 - P(\Omega) = 0$ by the [[complement rule|0PQEBTYDZM]]. So we may assume an infinite sequence.
3. Let $C_1 = A_1$ and $C_n = A_n \setminus (A_1 \cup \dots \cup A_{n-1})$ for $n \ge 2$. Each $C_n$ is in $\mathcal{F}$, because $\mathcal{F}$ is a [[σ-algebra|04WSW8T3SY]].
4. By construction $C_n \subseteq A_n$ for each $n$.
5. The sets $C_n$ are pairwise disjoint. Let $m < n$. Then $C_m \subseteq A_m \subseteq A_1 \cup \dots \cup A_{n-1}$, and $C_n$ has no point in this union.
6. We claim $\bigcup_n C_n = \bigcup_n A_n$. The inclusion $\subseteq$ follows from step 4.
7. For $\supseteq$, let $\omega \in \bigcup_n A_n$ and let $n$ be the least index with $\omega \in A_n$. Then $\omega \notin A_1 \cup \dots \cup A_{n-1}$, so $\omega \in C_n$.
8. By the countable additivity of the [[probability measure|0VGMEBVW1M]] $P$, $P\left(\bigcup_n A_n\right) = P\left(\bigcup_n C_n\right) = \sum_n P(C_n)$.
9. By step 4 and [[monotonicity of probability|0464Z0JP2E]], $P(C_n) \le P(A_n)$ for each $n$.
10. So each partial sum satisfies $\sum_{n=1}^{N} P(C_n) \le \sum_{n=1}^{N} P(A_n) \le \sum_{n=1}^{\infty} P(A_n)$. The last sum lies in $[0, \infty]$, because its terms are nonnegative.
11. Letting $N \to \infty$ in step 10 and using step 8 gives $P\left(\bigcup_n A_n\right) \le \sum_n P(A_n)$.

## Idea

Overlaps are what make the union smaller than the sum. Removing from each $A_n$ the part already covered by earlier events gives disjoint pieces with the same union. Countable additivity applies to these pieces, and each piece is no more likely than the event it came from.
