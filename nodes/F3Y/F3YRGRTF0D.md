---
tag: F3YRGRTF0D
kind: proof
name: Proof of the Euler product formula
msc: [11M06]
proves: 0C3PN4075R
uses: [0SN0MAEKYX, 084HH1NDCB, 020K0X7HVR, 0ZNSSK8ZK1, 04Z5G0THN6, 0Y123X48GA, 0HYNZE940T, 0FJZMBX0ZZ, 0734RSVF2V, 0FM6N4R0VB]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_of_the_Euler_product_formula_for_the_Riemann_zeta_function
    locator: Another proof
---

## Proof

We expand each factor as a geometric series and bound the error by a tail of the series for $\zeta(\sigma)$.

1. Write $s = \sigma + i t$ with real $\sigma > 1$ and real $t$. For a real $a > 0$, $a^{-s} = \exp(-s \ln a)$.
2. Two standard facts about the complex exponential are $\exp(z + w) = \exp z \exp w$ and $|\exp z| = \exp(\operatorname{Re} z)$.
3. With $\ln(ab) = \ln a + \ln b$, they give $(ab)^{-s} = a^{-s} b^{-s}$ for real $a, b > 0$, and $|a^{-s}| = a^{-\sigma}$.
4. By the [[p-series test|0ZNSSK8ZK1]], $\sum_{n \ge 1} n^{-\sigma}$ converges, because $\sigma > 1$. For $N \ge 1$, let $T_N = \sum_{n > N} n^{-\sigma}$. Then $T_N \to 0$ as $N \to \infty$.
5. The real and imaginary parts of $n^{-s}$ have absolute value at most $|n^{-s}| = n^{-\sigma}$. By the [[comparison test|04Z5G0THN6]], their series converge absolutely.
6. By [[absolutely convergent series converge|0Y123X48GA]], both real series converge. So $Z_M = \sum_{n=1}^{M} n^{-s}$ converges to a limit $\zeta(s)$ as $M \to \infty$.
7. For a prime $p$, put $r_p = p^{-s}$. Then $|r_p| = p^{-\sigma} \le 2^{-\sigma} < 1/2$. In particular $r_p \neq 1$.
8. For $K \ge 0$, put $G_{p,K} = \sum_{k=0}^{K} r_p^k$. The sum telescopes: $(1 - r_p) G_{p,K} = 1 - r_p^{K+1}$.
9. By [[multiplicativity of the modulus|0HYNZE940T]], $|r_p^{K+1}| = |r_p|^{K+1} < 2^{-(K+1)}$, which tends to $0$. So $G_{p,K} \to 1/(1 - r_p)$ as $K \to \infty$.
10. Fix an integer $N \ge 2$. Let $q_1 < \dots < q_m$ be the primes at most $N$. Put $P_N = \prod_{j=1}^{m} 1/(1 - r_{q_j})$ and $F_{N,K} = \prod_{j=1}^{m} G_{q_j,K}$.
11. A product of finitely many convergent complex sequences converges to the product of the limits. This follows from the [[real case|0734RSVF2V]] applied to real and imaginary parts. So $F_{N,K} \to P_N$ as $K \to \infty$.
12. Multiplying out, $F_{N,K}$ is the sum, over all tuples $(k_1, \dots, k_m)$ with $0 \le k_j \le K$, of $\prod_j r_{q_j}^{k_j}$. By step 3, this term is $n^{-s}$ with $n = q_1^{k_1} \cdots q_m^{k_m}$.
13. By the [[fundamental theorem of arithmetic|084HH1NDCB]], distinct tuples give distinct integers $n$. Let $S_{N,K}$ be the set of these integers. Then $F_{N,K} = \sum_{n \in S_{N,K}} n^{-s}$.
14. Let $K \ge N$. Each integer $n$ with $1 \le n \le N$ lies in $S_{N,K}$. Indeed, by the [[existence of prime factorization|020K0X7HVR]], $n$ is a product of primes at most $n \le N$.
15. In that factorization, a prime $q$ with exponent $e$ satisfies $2^e \le q^e \le n \le N \le K < 2^K$. So $e \le K$, and $n \in S_{N,K}$.
16. Let $M$ be at least the largest element of $S_{N,K}$. Then $Z_M - F_{N,K}$ is the sum of $n^{-s}$ over the $n \le M$ with $n \notin S_{N,K}$. By step 14, all these $n$ exceed $N$.
17. By the [[triangle inequality|0FJZMBX0ZZ]] for the modulus, $|Z_M - F_{N,K}| \le \sum_{N < n \le M} n^{-\sigma} \le T_N$.
18. Let $M \to \infty$. Since $Z_M \to \zeta(s)$ and the modulus is continuous, $|\zeta(s) - F_{N,K}| \le T_N$ for every $K \ge N$.
19. Let $K \to \infty$. By step 11 and continuity of the modulus, $|\zeta(s) - P_N| \le T_N$.
20. Let $N \to \infty$. By step 4, $P_N \to \zeta(s)$. The numbers $P_N$ are the partial products of $\prod_p 1/(1 - p^{-s})$ over the primes in increasing order. So the product equals $\zeta(s)$.
21. For absolute convergence, write $1/(1 - r_p) = 1 + a_p$ with $a_p = r_p/(1 - r_p)$. We show that $\sum_p |a_p|$ converges.
22. By the triangle inequality, $|1 - r_p| \ge 1 - |r_p| > 1/2$. So $|a_p| < 2 |r_p| = 2 p^{-\sigma}$.
23. The partial sums of $\sum_p |a_p|$ increase, and they are at most $2 \sum_{n \ge 1} n^{-\sigma}$. By the [[monotone convergence theorem|0FM6N4R0VB]], $\sum_p |a_p|$ converges.
24. So the product $\prod_p 1/(1 - p^{-s})$ converges absolutely, and its value is $\zeta(s)$.

## Idea

Each factor $1/(1 - p^{-s})$ is a geometric series $\sum_k p^{-ks}$. Multiplying these series over the primes up to $N$ gives $\sum n^{-s}$ over the integers built from those primes, each exactly once by unique factorization. Every $n \le N$ appears, so the error is at most the tail $\sum_{n > N} n^{-\sigma}$, which tends to $0$.
