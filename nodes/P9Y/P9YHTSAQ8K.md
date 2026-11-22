---
tag: P9YHTSAQ8K
kind: proof
name: Proof of the primary decomposition theorem
msc: ["15A21", "15A04"]
topics: [Z6S6PWMJPH]
audience: ug2
proves: 49ZHBMYKVE
methods: [0NTF6DMVAP]
uses: [ACBNK1VFVG, 0V58FPM3EQ, 0VTAD25A3G, 00X2A9G9W3, 0VY3WPP9Y3, 06YMXJMXYS, 0DQG39K2NH]
sources:
  - book: isbn:9780135367971
    locator: Section 6.8
  - book: isbn:9783031410253
    locator: Chapter 8
---

## Proof

We check that the powers $p_i^{e_i}$ are pairwise coprime, apply the kernels lemma to get parts 1 and 4, and then compare minimal polynomials to get parts 2 and 3.

*The powers are pairwise coprime.*

1. Let $i \ne j$, and let $d$ be a monic common divisor of $p_i$ and $p_j$.
   Since $p_i$ is [[irreducible|00X2A9G9W3]], $d = 1$ or $d = p_i$.
2. If $d = p_i$, then $p_i$ divides $p_j$, and since $p_j$ is irreducible and both are monic, $p_i = p_j$, which is false.
   So $d = 1$, and $p_i$ and $p_j$ are coprime.
3. By [[Bézout's identity|0VY3WPP9Y3]], $a p_i + b p_j = 1$ for some $a, b \in F[t]$.
4. Put $N = e_i + e_j - 1$, raise the identity to the power $N$, and expand by the binomial theorem in the commutative ring $F[t]$.
5. Each term $\binom{N}{l} (a p_i)^l (b p_j)^{N - l}$ has $l \ge e_i$ or $N - l \ge e_j$, because $l \le e_i - 1$ gives $N - l \ge e_j$.
6. So each term is a multiple of $p_i^{e_i}$ or of $p_j^{e_j}$.
   Collecting terms gives $a' p_i^{e_i} + b' p_j^{e_j} = 1$ for some $a', b' \in F[t]$, so the powers are coprime.

*The decomposition and the projections.*

7. By the definition of the [[minimal polynomial|0V58FPM3EQ]], $m_T(T) = 0$, and $m_T = p_1^{e_1} \cdots p_k^{e_k}$ with pairwise coprime factors by step 6.
8. So $\ker m_T(T) = V$, and part 4 of the [[kernels lemma|ACBNK1VFVG]] gives $V = W_1 \oplus \dots \oplus W_k$, with projections that are polynomials in $T$.
   This proves parts 1 and 4.

*The minimal polynomials of the pieces.*

9. Each $W_i$ is $T$-invariant, by the kernels lemma.
   Let $T_i = T|_{W_i}$, with minimal polynomial $m_i$, where the minimal polynomial of the map on the zero space is $1$.
10. By the definition of $W_i$, $p_i^{e_i}(T_i) = 0$.
    So $m_i$ divides $p_i^{e_i}$, by [[divisibility by the minimal polynomial|0VTAD25A3G]].
11. The ring $F[t]$ is a [[Euclidean domain|0DQG39K2NH]], hence a [[unique factorization domain|06YMXJMXYS]].
    So the monic divisors of $p_i^{e_i}$ are the $p_i^{f}$ with $0 \le f \le e_i$, and $m_i = p_i^{f_i}$ with $f_i \le e_i$.
12. Let $g = p_1^{f_1} \cdots p_k^{f_k}$, and let $w \in W_i$.
    Polynomials in $T$ commute, so $g(T) w = \big(\prod_{j \ne i} p_j^{f_j}\big)(T) \, m_i(T) w$, and $m_i(T) w = m_i(T_i) w = 0$, so $g(T) w = 0$.
13. Every $v \in V$ is a sum of vectors of the $W_i$, by step 8, so $g(T) = 0$.
    Then $m_T$ divides $g$, again by divisibility by the minimal polynomial.
14. By unique factorization, the exponent $e_i$ of $p_i$ in $m_T$ is at most its exponent $f_i$ in $g$.
    With step 11, $f_i = e_i$, so $m_i = p_i^{e_i}$, which proves part 3.
15. If $W_i = 0$, then $m_i = 1$ and $f_i = 0$, which contradicts $f_i = e_i \ge 1$.
    So $W_i \ne 0$, which proves part 2.

## Idea

Distinct irreducible polynomials are coprime, and so are their powers.
The kernels lemma then splits $V$ along the factorization of $m_T$, with projections that are polynomials in $T$.
The minimal polynomial of each piece divides $p_i^{e_i}$, and the product of these minimal polynomials kills $T$, so no exponent can drop.

## Variants

Steps 3 to 6 can be replaced by the fact that in a unique factorization domain, two elements are coprime exactly when they share no irreducible factor, so powers of coprime elements are coprime.
One can also prove part 1 without the kernels lemma, with the polynomials $q_i = m_T / p_i^{e_i}$.
They have no common factor, so $\sum_i c_i q_i = 1$ for some $c_i \in F[t]$, and the maps $\pi_i = (c_i q_i)(T)$ are the projections.
This is the proof in Hoffman and Kunze, Section 6.8.
