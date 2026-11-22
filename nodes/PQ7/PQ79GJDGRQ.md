---
tag: PQ79GJDGRQ
kind: proof
name: Proof of triangularization by induction on the size
msc: ["15A20", "15A21"]
topics: [Z6S6PWMJPH]
audience: ug1
proves: 0363JMQ42Y
methods: [B2D8PTFNN1, 0NTF6DMVAP]
uses: [0EP59ESQ94, 0YYMY95FWS, 039HF58KQ5, 0MKABWDRNC, 027KDW2K72, 0TYMASG33Y, 0K1KKMFHYH, 053QVHF6N7, 0B5H4208Z9, 0M4SXE5WW3, 0KWXYZPJKN, 0MQXVZEBMT, 0J9TVTNB4K, 0GJM24EXP9, 0B5Z1EC66J, 0M0SNKZ482, 0K3MWA7DMC, 02SJG1HC32, 0JP0W07Y9A]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Triangularisability
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Proof

We first prove the matrix form of $1 \Leftrightarrow 3$: one direction is a determinant computation, and the other is an induction on $n$ that puts an eigenvector first.
Then we prove $1 \Leftrightarrow 2$ by reading the columns of a triangular matrix, and we pass from matrices to endomorphisms.

*A triangular form makes the characteristic polynomial split.*

1. Suppose $A$ is [[similar|027KDW2K72]] to an [[upper triangular|0MKABWDRNC]] matrix $U = (u_{ij})$.
   [[Similar matrices have the same characteristic polynomial|0TYMASG33Y]], so $p_A = p_U$.
2. The matrix $t I_n - U$ is upper triangular over the commutative ring $F[t]$, with diagonal entries $t - u_{ii}$.
   By the [[determinant of a triangular matrix|0K1KKMFHYH]],
   $$p_A(t) = p_U(t) = (t - u_{11}) \cdots (t - u_{nn}),$$
   so $p_A$ splits over $F$.

*A split characteristic polynomial gives a triangular form.*

3. We prove by induction on $n \ge 1$: if $p_A = (t - \lambda_1) \cdots (t - \lambda_n)$ with all $\lambda_i \in F$, then $A$ is similar to an upper triangular matrix.
   For $n = 1$, every $1 \times 1$ matrix is upper triangular.
4. Let $n \ge 2$, and assume the claim for size $n - 1$.
   Since $p_A(\lambda_1) = 0$, the scalar $\lambda_1$ is an eigenvalue of $A$, by the theorem that [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]].
   Choose an [[eigenvector|0B5H4208Z9]] $v \ne 0$ with $A v = \lambda_1 v$.
5. The family $(v)$ is linearly independent because $v \ne 0$, so it [[extends to a basis|0M4SXE5WW3]] $(v, w_2, \dots, w_n)$ of $F^n$.
   Let $Q$ be the [[change of basis matrix|0KWXYZPJKN]] with the columns $v, w_2, \dots, w_n$.
6. By the [[change of basis formula|0MQXVZEBMT]], $Q$ is invertible and $Q^{-1} A Q$ is the [[matrix|0YYMY95FWS]] of $x \mapsto A x$ in the new basis.
   Its first column holds the coordinates of $A v = \lambda_1 v$, which are $(\lambda_1, 0, \dots, 0)$, so
   $$Q^{-1} A Q = \begin{pmatrix} \lambda_1 & r \\ 0 & A' \end{pmatrix}$$
   for a row $r$ of length $n - 1$ and an $(n - 1) \times (n - 1)$ matrix $A'$.
7. By the [[determinant of a block triangular matrix|0J9TVTNB4K]] over $F[t]$ and by step 1 applied to the similar matrices $A$ and $Q^{-1} A Q$,
   $$(t - \lambda_1) \, p_{A'}(t) = p_A(t) = (t - \lambda_1) \prod_{i = 2}^{n} (t - \lambda_i).$$
8. The ring $F[t]$ is an [[integral domain|0B5Z1EC66J]], so we may [[cancel|0GJM24EXP9]] the factor $t - \lambda_1$.
   This gives $p_{A'} = \prod_{i = 2}^{n} (t - \lambda_i)$, which splits.
9. By the induction hypothesis there is an invertible $(n - 1) \times (n - 1)$ matrix $R$ such that $U' = R^{-1} A' R$ is upper triangular.
10. The [[block diagonal matrix|0M0SNKZ482]] $S = \operatorname{diag}(1, R)$ is invertible with inverse $\operatorname{diag}(1, R^{-1})$, and block multiplication gives
    $$S^{-1} Q^{-1} A Q S = \begin{pmatrix} \lambda_1 & r R \\ 0 & U' \end{pmatrix}.$$
    This matrix is upper triangular because $U'$ is, so $P = Q S$ makes $P^{-1} A P$ upper triangular, and the induction is complete.

*The algebraically closed case.*

11. Let $F$ be [[algebraically closed|02SJG1HC32]].
    Every monic polynomial of degree $d \ge 1$ over $F$ has a root $c$, and the [[factor theorem|0K3MWA7DMC]] gives $f = (t - c) g$ with $g$ monic of degree $d - 1$.
    Induction on $d$ shows that $f$ splits, so $p_A$ splits and step 10 applies.
12. By the [[fundamental theorem of algebra|0JP0W07Y9A]], $\C$ is algebraically closed, so every complex square matrix is triangularizable.

*Endomorphisms and flags.*

13. For an endomorphism $T$, choose a basis $\mathcal{B}$ and put $A = [T]_{\mathcal{B}}$.
    Then $p_T = p_A$, and $T$ is triangular in some basis exactly when $A$ is similar to a triangular matrix, by the change of basis formula.
    So steps 1 to 12 prove $1 \Leftrightarrow 3$ for $T$.
14. Let $(v_1, \dots, v_n)$ be a basis of $V$, and put $V_i = \operatorname{span}(v_1, \dots, v_i)$.
    Column $j$ of the matrix of $T$ holds the coordinates of $T(v_j)$, so the matrix is upper triangular exactly when $T(v_j) \in V_j$ for each $j$.
15. Since $V_i$ is spanned by $v_1, \dots, v_i$ and $V_j \subseteq V_i$ for $j \le i$, step 14 holds exactly when $T(V_i) \subseteq V_i$ for each $i$, that is, when each $V_i$ is [[invariant|0EP59ESQ94]].
    So a triangular basis gives the flag of condition 2.
16. Conversely, given a flag as in condition 2, choose $v_i \in V_i$ with $v_i \notin V_{i-1}$ for each $i$.
    By induction on $i$, $(v_1, \dots, v_i)$ is linearly independent with $i$ vectors in a space of dimension $i$, so it is a basis of $V_i$.
    Step 15 then shows that the matrix in the basis $(v_1, \dots, v_n)$ is upper triangular, which is condition 1.
17. Finally, in a triangular form $U$, step 2 gives $p_T = \prod_i (t - u_{ii})$.
    So each eigenvalue occurs on the diagonal exactly as often as it occurs as a root of $p_T$, which is its algebraic multiplicity.

## Idea

A triangular matrix shows its characteristic polynomial already factored on the diagonal.
For the converse, a root of $p_A$ gives an eigenvector, and putting it first in a basis makes the first column $(\lambda_1, 0, \dots, 0)$.
The remaining block of size $n - 1$ still has a split characteristic polynomial, because we only removed one linear factor, so induction triangularizes it.
The flag is the same fact said without coordinates: triangular in a basis means that the span of the first $i$ basis vectors is invariant for each $i$.

## Variants

The induction can be written without matrices, with the [[quotient operator|0PFPWKBDTJ]].
Let $U = F v$ for an eigenvector $v$ with eigenvalue $\lambda_1$.
By the [[block triangular form|ENVF51H5S3]], $p_T = (t - \lambda_1) \, p_{\bar T}$, so $p_{\bar T}$ splits on $V / U$.
A flag of $\bar T$-invariant subspaces of $V / U$ pulls back under the quotient map to invariant subspaces of $V$ that contain $U$, and adding $U$ at the bottom gives a full flag of $V$.
Over $\C$ with an inner product, the Gram-Schmidt process applied to a triangular basis keeps the flag and gives the [[Schur decomposition|V1JG4C7R7B]].
