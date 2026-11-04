---
tag: CTSV0ZESYF
kind: proof
name: Proof of the fundamental theorem of arithmetic
msc: [11A51]
proves: 084HH1NDCB
uses: [0AEKDFCYFA, 020K0X7HVR, 051VYKA1EX, 0SN0MAEKYX, 0KMVFSHFGZ]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
    locator: Proof
---

## Proof

Existence is a known result; we prove uniqueness by [[strong induction|0KMVFSHFGZ]] on $n$, using Euclid's lemma.

1. Let $n$ be a positive integer. By the [[existence of prime factorization|020K0X7HVR]], $n$ has a [[prime factorization|0AEKDFCYFA]] $n = p_1 \cdots p_k$ with $p_1 \le \dots \le p_k$.
2. First a claim. Let $p$ be a prime, and let $q_1, \dots, q_l$ be primes with $l \ge 1$ and $p \mid q_1 \cdots q_l$. Then $p = q_j$ for some $j$.
3. We prove the claim by induction on $l$. If $p \mid q_j$ for a prime $q_j$, then $p$ is a positive divisor of $q_j$ other than $1$, so $p = q_j$.
4. For $l = 1$, step 3 applies directly. For $l \ge 2$, we have $p \mid q_1 \cdot (q_2 \cdots q_l)$.
5. By [[Euclid's lemma|051VYKA1EX]], $p \mid q_1$ or $p \mid q_2 \cdots q_l$. In the first case, step 3 gives $p = q_1$. In the second case, the induction hypothesis gives $p = q_j$ with $j \ge 2$.
6. Now let $U(n)$ say: any two prime factorizations of $n$ are equal. Assume that $U(m)$ holds for all positive $m < n$.
7. Let $n = p_1 \cdots p_k = q_1 \cdots q_l$ with [[primes|0SN0MAEKYX]] $p_1 \le \dots \le p_k$ and $q_1 \le \dots \le q_l$.
8. If $n = 1$, then $k = l = 0$, because a product of at least one prime is at least $2$. So the two factorizations are equal.
9. Let $n \ge 2$. Then $k \ge 1$ and $l \ge 1$.
10. Since $p_1 \mid n = q_1 \cdots q_l$, the claim gives $p_1 = q_j$ for some $j$. So $p_1 \ge q_1$.
11. In the same way, $q_1 \mid p_1 \cdots p_k$ gives $q_1 = p_i$ for some $i$. So $q_1 \ge p_1$. Hence $p_1 = q_1$.
12. Put $m = n / p_1$. Cancelling $p_1 = q_1$ gives $m = p_2 \cdots p_k = q_2 \cdots q_l$. Here $1 \le m < n$, because $p_1 \ge 2$.
13. These are two prime factorizations of $m$. By $U(m)$, $k - 1 = l - 1$ and $p_i = q_i$ for $2 \le i \le k$.
14. With step 11, $k = l$ and $p_i = q_i$ for each $i$. So $U(n)$ holds.
15. By strong induction, $U(n)$ holds for every positive integer $n$. Together with step 1, each positive integer has exactly one prime factorization.

## Idea

The smallest prime of one factorization divides the other product, so by Euclid's lemma it appears in the other factorization. Comparing the smallest primes on both sides shows that they are equal. Cancelling them gives a smaller number, where induction finishes the job.
