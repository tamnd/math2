---
tag: 4XY92PVEHK
kind: proof
name: Proof of the continuity of probability measures
msc: [60A10]
proves: 0X8HBKCSYB
uses: [0ZYBZ34RT2, 0VGMEBVW1M, 04WSW8T3SY, 0464Z0JP2E]
sources:
  - url: https://proofwiki.org/wiki/Measure_of_Limit_of_Increasing_Sequence_of_Measurable_Sets
  - url: https://proofwiki.org/wiki/Measure_of_Limit_of_Decreasing_Sequence_of_Measurable_Sets
---

## Proof

We prove continuity from below with disjoint pieces, then continuity from above with differences.

1. Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0ZYBZ34RT2]]. Let $A_1 \subseteq A_2 \subseteq \cdots$ be events and let $A = \bigcup_{n=1}^{\infty} A_n$.
2. Let $F_1 = A_1$ and $F_n = A_n \setminus A_{n-1}$ for $n \ge 2$. Each $F_n$ is in $\mathcal{F}$, because $\mathcal{F}$ is a [[σ-algebra|04WSW8T3SY]].
3. The sets $F_n$ are pairwise disjoint. Let $m < n$. Then $F_m \subseteq A_m \subseteq A_{n-1}$, because the sequence increases, and $F_n$ has no point in $A_{n-1}$.
4. We show $P(A_n) = \sum_{i=1}^{n} P(F_i)$ by induction on $n$. For $n = 1$ this is $P(A_1) = P(F_1)$.
5. For the inductive step, $A_{n-1} \subseteq A_n$. By [[monotonicity of probability|0464Z0JP2E]], $P(A_n) = P(A_{n-1}) + P(A_n \setminus A_{n-1}) = P(A_{n-1}) + P(F_n)$. The induction hypothesis then gives the claim for $n$.
6. We show $\bigcup_n F_n = A$. Each $F_n \subseteq A_n \subseteq A$.
7. Conversely, let $\omega \in A$ and let $n$ be the least index with $\omega \in A_n$. If $n = 1$, then $\omega \in F_1$. If $n \ge 2$, then $\omega \notin A_{n-1}$, so $\omega \in F_n$.
8. By the countable additivity of the [[probability measure|0VGMEBVW1M]] $P$, $P(A) = \sum_{i=1}^{\infty} P(F_i)$.
9. The sum of a series is the limit of its partial sums. By step 4, these partial sums are $P(A_n)$. So $P(A) = \lim_{n \to \infty} P(A_n)$. This is the first claim.
10. Now let $B_1 \supseteq B_2 \supseteq \cdots$ be events and let $B = \bigcap_{n=1}^{\infty} B_n$. Let $D_n = B_1 \setminus B_n$, an event.
11. The sets $D_n$ increase, because $B_{n+1} \subseteq B_n$ gives $B_1 \setminus B_n \subseteq B_1 \setminus B_{n+1}$.
12. We claim $\bigcup_n D_n = B_1 \setminus B$. A point $\omega \in B_1$ lies outside $B$ exactly when $\omega \notin B_n$ for some $n$, that is, when $\omega \in D_n$ for some $n$.
13. By steps 11 and 12 and the first claim, $P(B_1 \setminus B) = \lim_{n \to \infty} P(B_1 \setminus B_n)$.
14. We have $B \subseteq B_1$ and $B_n \subseteq B_1$. By monotonicity of probability, $P(B_1 \setminus B) = P(B_1) - P(B)$ and $P(B_1 \setminus B_n) = P(B_1) - P(B_n)$.
15. So $P(B_1) - P(B_n) \to P(B_1) - P(B)$. Subtracting both sides from the constant $P(B_1)$ gives $P(B_n) \to P(B)$. This is the second claim.

## Idea

An increasing union is a disjoint union of the "new parts" $A_n \setminus A_{n-1}$. Countable additivity makes $P(A)$ the sum of the new parts, and the partial sums are exactly $P(A_n)$. For a decreasing sequence, the differences $B_1 \setminus B_n$ increase, so the first part applies to them. All the numbers are finite, so one can subtract.
