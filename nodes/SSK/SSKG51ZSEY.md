---
tag: SSKG51ZSEY
kind: proof
name: Proof of the multiplication rule
msc: [60A05]
proves: 0BS3RMX8HM
uses: [0ZYBZ34RT2, 0FJB06AD2P, 0464Z0JP2E, 04WSW8T3SY]
sources:
  - url: https://en.wikipedia.org/wiki/Chain_rule_(probability)
    locator: Chain rule for events
---

## Proof

We argue by induction on the number of events in the intersection.

1. Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0ZYBZ34RT2]] and let $A_1, \dots, A_n \in \mathcal{F}$ with $n \ge 2$ and $P(A_1 \cap \dots \cap A_{n-1}) > 0$.
2. For $1 \le k \le n$ let $C_k = A_1 \cap \dots \cap A_k$. Each $C_k$ is in $\mathcal{F}$, because $\mathcal{F}$ is a [[σ-algebra|04WSW8T3SY]].
3. Let $1 \le k \le n - 1$. Then $C_{n-1} \subseteq C_k$. By [[monotonicity of probability|0464Z0JP2E]], $P(C_k) \ge P(C_{n-1}) > 0$.
4. So for $1 \le k \le n - 1$ the [[conditional probability|0FJB06AD2P]] $P(A_{k+1} \mid C_k) = P(A_{k+1} \cap C_k) / P(C_k)$ is defined.
5. Since $A_{k+1} \cap C_k = C_{k+1}$, step 4 gives $P(C_{k+1}) = P(C_k) \, P(A_{k+1} \mid C_k)$ for $1 \le k \le n - 1$.
6. We claim that $P(C_m) = P(A_1) \prod_{k=1}^{m-1} P(A_{k+1} \mid C_k)$ for $1 \le m \le n$. For $m = 1$ the product is empty and the claim reads $P(C_1) = P(A_1)$, which holds since $C_1 = A_1$.
7. Suppose the claim holds for some $m$ with $1 \le m \le n - 1$. Step 5 with $k = m$ multiplies $P(C_m)$ by $P(A_{m+1} \mid C_m)$, so the claim holds for $m + 1$.
8. The case $m = n$ of the claim reads $P(A_1 \cap \dots \cap A_n) = P(A_1) \, P(A_2 \mid A_1) \cdots P(A_n \mid A_1 \cap \dots \cap A_{n-1})$.

## Idea

Each factor $P(A_{k+1} \mid C_k)$ is the ratio $P(C_{k+1}) / P(C_k)$. Multiplying all these ratios and $P(A_1)$ gives a telescoping product that leaves $P(C_n)$. The hypothesis on the last intersection makes all the denominators positive.
