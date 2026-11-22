---
tag: E2XSXEVC2Y
kind: proof
name: Proof by Lagrange interpolation that a matrix is diagonalizable iff its minimal polynomial has simple roots
msc: ["15A20"]
topics: [Z6S6PWMJPH]
audience: ug2
proves: 0MPAJRB23T
methods: [0NTF6DMVAP, 0ASJVEFA9J]
uses: [0Y17PEKF24, 0V58FPM3EQ, 0BNEXSKNRV, 0VTAD25A3G, 0QF4ZEFG52, 0K3MWA7DMC, 0KJVQV3E0F, 0AYEPBQMAW, 06MRNP4BNT, 056SW1E0AC, 0B5H4208Z9, 0GJM24EXP9]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/minpolyandappns.pdf
    locator: Theorem 4.11 and Remark 4.12
---

## Proof

We prove the equivalence of conditions 1.1 and 1.3 for an $n \times n$ matrix $A$ with $n \ge 1$, and we use Lagrange interpolation polynomials for the hard direction.
For an endomorphism $T$, the same argument applies to the matrix of $T$ in any basis.

*Similar matrices have the same minimal polynomial.*

1. For a square matrix $C$, the polynomials that kill $C$ are those that kill the map $x \mapsto C x$, because $p(C) x$ is the value of $p$ at this map applied to $x$.
   So results on [[minimal polynomials|0V58FPM3EQ]] of endomorphisms apply to matrices.
2. Let $P$ be invertible and $C = P^{-1} A P$.
   By induction on $k$, $C^k = P^{-1} A^k P$, so $p(C) = P^{-1} p(A) P$ for each $p \in F[t]$, by the definition of the [[value of $p$|0BNEXSKNRV]].
3. By step 2, $p(C) = 0$ if and only if $p(A) = 0$, hence $m_C = m_A$.

*From diagonalizable to the form of $m_A$.*

4. Let $A$ be [[diagonalizable|0Y17PEKF24]], and choose $P$ with $P^{-1} A P = D = \operatorname{diag}(d_1, \dots, d_n)$.
   Let $\mu_1, \dots, \mu_k$ be the distinct values among $d_1, \dots, d_n$, and let $f = \prod_{j=1}^{k} (t - \mu_j)$.
5. Powers and linear combinations of diagonal matrices are computed entry by entry, so $f(D) = \operatorname{diag}(f(d_1), \dots, f(d_n))$.
   Each $f(d_i) = 0$, hence $f(D) = 0$.
6. By step 5 and [[divisibility by the minimal polynomial|0VTAD25A3G]], $m_D$ divides $f$.
7. Each $\mu_j$ equals some $d_i$, and $D e_i = d_i e_i$ for the standard basis vector $e_i$.
   So $\mu_j$ is an eigenvalue of $D$, and $m_D(\mu_j) = 0$ because [[eigenvalues are the roots of the minimal polynomial|0QF4ZEFG52]].
8. We show by induction on $r$ that $g_r = \prod_{j=1}^{r} (t - \mu_j)$ divides $m_D$ for $r = 0, \dots, k$.
   For $r = 0$, $g_0 = 1$.
   Suppose that $m_D = g_r h$ with $r < k$.
9. Evaluating at $\mu_{r+1}$ gives $0 = g_r(\mu_{r+1}) h(\mu_{r+1})$.
   The factor $g_r(\mu_{r+1}) = \prod_{j \le r} (\mu_{r+1} - \mu_j)$ is nonzero, so $h(\mu_{r+1}) = 0$.
10. By the [[factor theorem|0K3MWA7DMC]], $h = (t - \mu_{r+1}) h'$, so $g_{r+1}$ divides $m_D$, and the induction is complete.
11. By steps 6 and 10, $f$ and $m_D$ divide each other.
    Write $f = m_D a$ and $m_D = f b$, so that $f = f a b$.
    By [[cancellation|0GJM24EXP9]] in the integral domain $F[t]$, $a b = 1$, so $a$ and $b$ are constants, and $a = 1$ because both polynomials are monic.
12. By steps 3 and 11, $m_A = m_D = (t - \mu_1) \cdots (t - \mu_k)$ with pairwise distinct $\mu_j \in F$.

*From the form of $m_A$ to diagonalizable.*

13. Let $m_A = (t - \lambda_1) \cdots (t - \lambda_k)$ with pairwise distinct $\lambda_i \in F$.
    Since $n \ge 1$, the constant $1$ does not kill $A$, so $k \ge 1$.
14. For each $i$, let $f_i = \prod_{j \ne i} (t - \lambda_j)$ and $c_i = f_i(\lambda_i)$.
    Then $c_i = \prod_{j \ne i} (\lambda_i - \lambda_j) \ne 0$, because the $\lambda_j$ are distinct.
15. Let $h = \sum_{i=1}^{k} c_i^{-1} f_i$.
    For each $l$, $f_i(\lambda_l) = 0$ when $i \ne l$, so $h(\lambda_l) = c_l^{-1} c_l = 1$.
16. The polynomial $h - 1$ has degree at most $k - 1$ and the $k$ roots $\lambda_1, \dots, \lambda_k$.
    A nonzero polynomial has [[at most as many roots as its degree|0KJVQV3E0F]], so $h - 1 = 0$ and $h = 1$.
17. By steps 2 and 16, $I_n = \sum_i c_i^{-1} f_i(A)$.
    For $v \in F^n$, let $u_i = c_i^{-1} f_i(A) v$, so that $v = u_1 + \cdots + u_k$.
18. Since $(t - \lambda_i) f_i = m_A$, we get $(A - \lambda_i I_n) u_i = c_i^{-1} m_A(A) v = 0$.
    So $u_i$ lies in the [[eigenspace|0AYEPBQMAW]] of $\lambda_i$.
19. So each $u_i$ is zero or an [[eigenvector|0B5H4208Z9]] of $A$.
    By step 17, every $v$ is a sum of eigenvectors, so the set $S$ of all eigenvectors of $A$ spans $F^n$.
20. [[Every spanning set contains a basis|06MRNP4BNT]], so $F^n$ has a basis contained in $S$, which is a basis of eigenvectors of $A$.
21. By the [[characterization by eigenvectors|056SW1E0AC]], $A$ is diagonalizable over $F$.

## Idea

A diagonal matrix is killed by the product of $t - \mu$ over its distinct diagonal entries, and every one of these factors is needed, because each $\mu$ is a root of the minimal polynomial.
For the converse, the interpolation polynomials $f_i / f_i(\lambda_i)$ take the value $1$ at $\lambda_i$ and $0$ at the other roots, so they add up to the constant $1$.
Put $A$ into this identity and apply it to a vector $v$.
The result writes $v$ as a sum of pieces, and $m_A(A) = 0$ makes each piece an eigenvector.

## Variants

The [[proof by the kernels lemma|ZAYD2GV1KT]] replaces the interpolation polynomials by Bézout coefficients.
It works for any pairwise coprime factors, not only for linear ones, so it also gives the [[primary decomposition|49ZHBMYKVE]].
