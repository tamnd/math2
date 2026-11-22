---
tag: WSQ9AN5H66
kind: proof
name: Proof of the kernels lemma by Bézout's identity
msc: ["15A04", "15A21"]
topics: [Z6S6PWMJPH]
audience: ug2
proves: ACBNK1VFVG
methods: [0NTF6DMVAP, 0ASJVEFA9J, MKHVRNW68H]
uses: [0VY3WPP9Y3, 0DQG39K2NH, 0BNEXSKNRV, 041JTZCK9Q, 8YNE1HTZEP]
sources:
  - book: isbn:9780135367971
    locator: Section 6.8
  - url: https://en.wikipedia.org/wiki/Jordan%E2%80%93Chevalley_decomposition
    locator: Decomposition of a linear operator
---

## Proof

We turn one Bézout identity $a p + b q = 1$ into the identity $a(T) p(T) + b(T) q(T) = \id_V$, use it to split each vector, and then get part 4 by induction on $k$.

*The identity in $T$.*

1. The ring $F[t]$ is a [[Euclidean domain|0DQG39K2NH]], and $p$ and $q$ are coprime.
   So [[Bézout's identity|0VY3WPP9Y3]] gives $a, b \in F[t]$ with $a p + b q = 1$.
2. The map $f \mapsto f(T)$ is a ring homomorphism, by the [[definition of a polynomial in $T$|0BNEXSKNRV]].
   So $a(T) p(T) + b(T) q(T) = \id_V$.
3. Any two polynomials in $T$ commute, because $F[t]$ is commutative and step 2 maps it by a ring homomorphism.

*The direct sum.*

4. If $p(T) x = 0$, then $(p q)(T) x = q(T) p(T) x = 0$, by step 3.
   So $\ker p(T) \subseteq \ker (p q)(T)$, and in the same way $\ker q(T) \subseteq \ker (p q)(T)$.
5. Let $x \in \ker p(T) \cap \ker q(T)$.
   By step 2, $x = a(T) p(T) x + b(T) q(T) x = 0 + 0 = 0$.
6. Let $x \in \ker (p q)(T)$, and put $x_1 = (b q)(T) x$ and $x_2 = (a p)(T) x$.
   By step 2, $x = x_1 + x_2$.
7. By step 3, $p(T) x_1 = b(T) (p q)(T) x = 0$, so $x_1 \in \ker p(T)$.
8. By step 3, $q(T) x_2 = a(T) (p q)(T) x = 0$, so $x_2 \in \ker q(T)$.
9. By steps 4 to 8, $\ker (p q)(T)$ is the sum of $\ker p(T)$ and $\ker q(T)$, and their intersection is $0$.
   So the sum is [[direct|041JTZCK9Q]], which proves part 1.
10. In a direct sum, the decomposition $x = x_1 + x_2$ is unique.
    So by step 6 the projections are $x \mapsto (b q)(T) x$ and $x \mapsto (a p)(T) x$, which proves part 2.

*Kernels and images.*

11. Now assume $(p q)(T) = 0$.
    Then $\ker (p q)(T) = V$, so $V = \ker p(T) \oplus \ker q(T)$ by part 1.
12. For $y \in V$, step 3 gives $p(T) q(T) y = (p q)(T) y = 0$.
    So $\operatorname{im} q(T) \subseteq \ker p(T)$.
13. Let $x \in \ker p(T)$.
    Then $x_2 = a(T) p(T) x = 0$ in step 6, so $x = x_1 = q(T) b(T) x \in \operatorname{im} q(T)$.
14. Steps 12 and 13 give $\ker p(T) = \operatorname{im} q(T)$.
    Exchanging the roles of $p$ and $q$ gives $\ker q(T) = \operatorname{im} p(T)$, which proves part 3.

*Several factors.*

15. We prove part 4 by induction on $k$.
    For $k = 1$ there is nothing to prove, and $k = 2$ is parts 1 and 2.
16. Let $k \ge 3$ and $P = p_1 \cdots p_{k-1}$.
    For each $i < k$, step 1 gives $a_i, b_i$ with $a_i p_i + b_i p_k = 1$.
17. Multiply these $k - 1$ equations.
    Every term of the expanded product except $\big(\prod_i a_i\big) P$ contains the factor $p_k$, so $\big(\prod_i a_i\big) P + c \, p_k = 1$ for some $c \in F[t]$.
18. So $P$ and $p_k$ are coprime, and part 1 gives $\ker (P p_k)(T) = \ker P(T) \oplus \ker p_k(T)$.
19. By the induction hypothesis, $\ker P(T) = \ker p_1(T) \oplus \dots \oplus \ker p_{k-1}(T)$.
    Together with step 18, this gives the direct sum of part 4.
20. For $i < k$, the projection onto $\ker p_i(T)$ is the projection onto $\ker P(T)$, which is $g(T)$ for a polynomial $g$ by part 2, followed by the projection inside $\ker P(T)$, which is $h_i(T)$ for a polynomial $h_i$ by the induction hypothesis.
21. The composite is $(h_i g)(T)$, again a polynomial in $T$.
    The projection onto $\ker p_k(T)$ is a polynomial in $T$ by part 2, which proves part 4.
22. Each $\ker p_i(T)$ is $T$-invariant, because $T$ commutes with $p_i(T)$, by the result that [[kernels of commuting maps are invariant|8YNE1HTZEP]].

## Idea

The identity $a p + b q = 1$ becomes $a(T) p(T) + b(T) q(T) = \id_V$.
Applied to a vector killed by $p q$, its two terms land in the two kernels.
A vector in both kernels is killed by both terms, so it is $0$.
For several factors, the product of the first factors is coprime to the last, and induction finishes the proof.

## Variants

For linear factors $p_i = t - \lambda_i$, the Bézout coefficients come from Lagrange interpolation, as in the [[Lagrange proof of the minimal polynomial criterion|E2XSXEVC2Y]].
In module language, the proof is the Chinese remainder theorem for the ideals $(p)$ and $(q)$ of $F[t]$, applied to the $F[t]$-module $\ker (p q)(T)$.
One can also prove part 4 without induction: put $q_i = \prod_{j \ne i} p_j$, note that $q_1, \dots, q_k$ have no common factor, and use one identity $\sum_i c_i q_i = 1$, whose terms $(c_i q_i)(T)$ are the projections.
