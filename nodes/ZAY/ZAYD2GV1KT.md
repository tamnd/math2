---
tag: ZAYD2GV1KT
kind: proof
name: Proof of the minimal polynomial criterion by the kernels lemma
msc: ["15A20", "15A18"]
topics: [Z6S6PWMJPH]
audience: ug2
proves: 0MPAJRB23T
methods: [0NTF6DMVAP, 0WCP0PVET6]
uses: [ACBNK1VFVG, 056SW1E0AC, 0V58FPM3EQ, 0VTAD25A3G, 0QF4ZEFG52, 0K3MWA7DMC, 0BNEXSKNRV, 0AYEPBQMAW, 0B5H4208Z9]
sources:
  - book: isbn:9780135367971
    locator: Section 6.4
  - book: isbn:9783031410253
    locator: Chapter 8
---

## Proof

We prove $1.1 \Rightarrow 1.3 \Rightarrow 1.2 \Rightarrow 1.1$, using the kernels lemma for the last step, and then parts 2 and 3.

*From diagonalizable to the form of $m_T$.*

1. Assume that $T$ is diagonalizable, with $T(v_j) = \mu_j v_j$ for a basis $(v_1, \dots, v_n)$.
2. Let $\lambda_1, \dots, \lambda_k$ be the distinct values among the $\mu_j$, and let $f = \prod_{i=1}^k (t - \lambda_i)$.
3. The factors $T - \lambda_i \id_V$ commute with each other, since they are [[polynomials in $T$|0BNEXSKNRV]].
   So we can write $f(T) v_j$ with the factor $T - \mu_j \id_V$ applied first.
4. That factor sends $v_j$ to $0$, so $f(T) v_j = 0$ for every $j$.
   A linear map that vanishes on a basis is zero, so $f(T) = 0$.
5. By [[divisibility by the minimal polynomial|0VTAD25A3G]], $m_T$ divides $f$.
6. Each $\lambda_i$ is an eigenvalue, so $m_T(\lambda_i) = 0$, because [[eigenvalues are the roots of the minimal polynomial|0QF4ZEFG52]].
7. We show by induction on $r$ that $g_r = \prod_{i \le r} (t - \lambda_i)$ divides $m_T$ for $r = 0, \dots, k$.
   For $r = 0$, $g_0 = 1$ divides $m_T$.
8. Suppose that $m_T = g_r h$ with $r < k$.
   Evaluating at $\lambda_{r+1}$ gives $0 = g_r(\lambda_{r+1}) h(\lambda_{r+1})$, and $g_r(\lambda_{r+1}) = \prod_{i \le r} (\lambda_{r+1} - \lambda_i) \ne 0$ because the $\lambda_i$ are distinct.
   So $h(\lambda_{r+1}) = 0$, and the [[factor theorem|0K3MWA7DMC]] gives $h = (t - \lambda_{r+1}) h'$, so $g_{r+1}$ divides $m_T$.
9. By step 8 with $r = k$, $f = g_k$ divides $m_T$.
   Both $f$ and $m_T$ are monic and divide each other, so $m_T = f$, which is condition 1.3.

*From the form of $m_T$ to an annihilating polynomial.*

10. Condition 1.3 implies condition 1.2 with $f = m_T$, since $m_T(T) = 0$.

*From an annihilating polynomial to diagonalizable.*

11. Assume condition 1.2, with $f = \prod_{j=1}^r (t - a_j)$ and distinct $a_j$.
12. For $j \ne l$, we have $(t - a_j) - (t - a_l) = a_l - a_j$, a nonzero constant.
    So every common divisor of $t - a_j$ and $t - a_l$ divides a nonzero constant, and the factors are pairwise coprime.
13. By the [[kernels lemma|ACBNK1VFVG]],
$$\ker f(T) = \ker(T - a_1 \id_V) \oplus \cdots \oplus \ker(T - a_r \id_V).$$
14. Since $f(T) = 0$, the left side is $V$.
    Each nonzero summand is the [[eigenspace|0AYEPBQMAW]] of the eigenvalue $a_j$.
15. Dropping the zero summands, $V$ is the direct sum of eigenspaces for distinct eigenvalues.
16. Every eigenvalue $\mu$ of $T$ appears among the $a_j$.
    Indeed, an [[eigenvector|0B5H4208Z9]] $v$ for $\mu$ gives $0 = f(T) v = f(\mu) v$, so $f(\mu) = 0$.
17. So $V$ is the direct sum of all the eigenspaces of $T$.
    By condition 3 of the [[characterization by eigenvectors|056SW1E0AC]], $T$ is diagonalizable.

*Parts 2 and 3.*

18. For part 2, step 9 shows that the roots of $m_T$ are the distinct values $\mu_j$, which are exactly the eigenvalues of $T$.
19. For part 3, apply step 13 with $f = m_T$, and let $\pi_1, \dots, \pi_k$ be the projections onto the summands $E_{\lambda_i}$.
20. By part 4 of the kernels lemma, each $\pi_i = g_i(T)$ for a polynomial $g_i$.
21. Let $u \in U$.
    Since $U$ is $T$-invariant, it is invariant under every polynomial in $T$, so $\pi_i(u) = g_i(T) u \in U \cap E_{\lambda_i}$.
22. Since $u = \sum_i \pi_i(u)$, the space $U$ is the sum of the $U \cap E_{\lambda_i}$.
    The sum is direct, because the sum of the $E_{\lambda_i}$ is direct.
23. A basis of each nonzero $U \cap E_{\lambda_i}$ consists of eigenvectors of $T|_U$, and together these bases form a basis of $U$.
    So $T|_U$ is diagonalizable.
24. For a matrix $A$, apply steps 1 to 23 to the map $x \mapsto A x$, whose minimal polynomial is $m_A$.

## Idea

A diagonal matrix is killed by the product of $t - \mu$ over its distinct diagonal entries, and no factor can be left out, because each $\mu$ is a root of the minimal polynomial.
In the other direction, distinct linear factors are pairwise coprime.
The kernels lemma then splits $V$ into the kernels of the maps $T - a_j$, and these kernels are eigenspaces.
The projections of the splitting are polynomials in $T$, so they keep every invariant subspace inside itself, and that gives part 3.

## Variants

The [[proof by Lagrange interpolation|E2XSXEVC2Y]] writes the projections explicitly as
$$\pi_i = \prod_{j \ne i} \frac{T - \lambda_j \id_V}{\lambda_i - \lambda_j}.$$
This is the kernels lemma with the Bézout coefficients found by interpolation.
Part 3 also follows from the criterion alone.
Since $m_T(T|_U) = 0$, the minimal polynomial of $T|_U$ divides $m_T$, so it is again a product of distinct linear factors over $F$.
