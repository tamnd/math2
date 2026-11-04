---
tag: 4QXMT9J6AN
kind: proof
name: Proof that R/P is an integral domain iff P is prime
msc: [13A15]
proves: 0AVXBEC05W
uses: [0GYGHKX834, 0MYSA6MYNA, 0VFW4Y69BT, 09S3PFBEPM, 06HC6HK0Z8]
sources:
  - url: https://proofwiki.org/wiki/Prime_Ideal_iff_Quotient_Ring_is_Integral_Domain
---

## Proof

1. Let $R$ be a [[commutative ring|0GYGHKX834]] and let $P$ be an [[ideal|0MYSA6MYNA]] of $R$. The [[quotient ring|0VFW4Y69BT]] $R/P$ is commutative, since $(a + P)(b + P) = a b + P = b a + P = (b + P)(a + P)$.
2. For $a \in R$, $a + P = 0 + P$ if and only if $a \in P$. Indeed, if $a + P = P$, then $a = a + 0 \in P$. If $a \in P$, then $a + P \subseteq P$ and $P = a + (P - a) \subseteq a + P$, since $P$ is an additive subgroup.
3. Claim: $1 + P \neq 0 + P$ if and only if $P \neq R$. By step 2, $1 + P \neq 0 + P$ means $1 \notin P$.
4. If $1 \in P$, then $r = r \cdot 1 \in P$ for every $r \in R$, so $P = R$. If $P = R$, then $1 \in P$. So $1 \notin P$ exactly when $P \neq R$, which proves the claim.
5. Every element of $R/P$ is $a + P$ for some $a \in R$, and $(a + P)(b + P) = a b + P$.
6. So by step 2, the condition "for all $a, b \in R$, $(a + P)(b + P) = 0 + P$ implies $a + P = 0 + P$ or $b + P = 0 + P$" says exactly "for all $a, b \in R$, $a b \in P$ implies $a \in P$ or $b \in P$".
7. By definition, $R/P$ is an [[integral domain|09S3PFBEPM]] when it is commutative, $1 + P \neq 0 + P$, and the condition of step 6 holds in $R/P$.
8. By definition, $P$ is a [[prime ideal|06HC6HK0Z8]] when $P \neq R$ and the condition of step 6 holds for $P$.
9. By steps 1, 3 and 6, the two definitions match term by term. So $R/P$ is an integral domain if and only if $P$ is prime.

## Idea

An element of $R/P$ is zero exactly when its representative lies in $P$. Under this translation, $1 \neq 0$ becomes $P \neq R$, and "no zero divisors" becomes "a product in $P$ has a factor in $P$". These are the two conditions of a prime ideal.
