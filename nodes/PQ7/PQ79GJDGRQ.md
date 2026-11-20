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

We prove the matrix form of $1 \Leftrightarrow 3$: the forward implication is a determinant computation, and the converse is by induction on $n$.
Then we prove $1 \Leftrightarrow 2$ and pass from matrices to endomorphisms.

1. Suppose $A$ is [[similar|027KDW2K72]] to an [[upper triangular|0MKABWDRNC]] matrix $U = (u_{ij})$. [[Similar matrices have the same characteristic polynomial|0TYMASG33Y]], so $p_A = p_U$.
2. The matrix $t I_n - U$ is upper triangular over the commutative ring $F[t]$, with diagonal entries $t - u_{ii}$. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $p_U = (t - u_{11}) \cdots (t - u_{nn})$. So $p_A$ splits over $F$.
3. For the converse, we prove by induction on $n \ge 1$: if $p_A$ splits over $F$, then $A$ is similar to an upper triangular matrix. For $n = 1$, every $1 \times 1$ matrix is upper triangular.
4. Let $n \ge 2$, and assume the claim for size $n - 1$. The [[characteristic polynomial|039HF58KQ5]] $p_A$ is monic of degree $n$. As it splits, $p_A = \prod_{i=1}^{s} (a_i t + b_i)$ with $a_i \ne 0$. Comparing degrees gives $s = n$, and comparing leading coefficients gives $\prod_i a_i = 1$. With $\lambda_i = -b_i / a_i$, we get $p_A = (t - \lambda_1) \cdots (t - \lambda_n)$.
5. Let $L \colon F^n \to F^n$ be $L(x) = A x$. Its matrix in the standard basis is $A$, so $p_L = p_A$. Since $p_L(\lambda_1) = 0$, the scalar $\lambda_1$ is an eigenvalue of $L$ by [[the roots of the characteristic polynomial|053QVHF6N7]]. Choose an [[eigenvector|0B5H4208Z9]] $v$, so $v \ne 0$ and $A v = \lambda_1 v$.
6. The set $\set{v}$ is linearly independent, since $v \ne 0$. By [[extension to a basis|0M4SXE5WW3]], there is a basis $B' = (v, w_2, \dots, w_n)$ of $F^n$.
7. Let $Q$ be the matrix with columns $v, w_2, \dots, w_n$. It is the [[change of basis matrix|0KWXYZPJKN]] from the standard basis to $B'$. The [[matrix of $L$|0YYMY95FWS]] in the standard basis is $A$.
8. By the [[change of basis formula|0MQXVZEBMT]], $Q$ is invertible and $Q^{-1} A Q = [L]_{B'}$. Since $L(v) = \lambda_1 v$, the first column of $[L]_{B'}$ is $\lambda_1 e_1$.
9. So $Q^{-1} A Q = \begin{pmatrix} \lambda_1 & r \\ 0 & A' \end{pmatrix}$ for some $1 \times (n-1)$ row $r$ and some $(n-1) \times (n-1)$ matrix $A'$.
10. By step 9 and the [[determinant of a block triangular matrix|0J9TVTNB4K]] over $F[t]$, $p_{Q^{-1} A Q} = (t - \lambda_1) p_{A'}$. By [[invariance under similarity|0TYMASG33Y]], this equals $p_A$.
11. So $(t - \lambda_1) p_{A'} = (t - \lambda_1) \prod_{i=2}^{n} (t - \lambda_i)$. The ring $F[t]$ is an [[integral domain|0B5Z1EC66J]], so [[cancellation|0GJM24EXP9]] gives $p_{A'} = \prod_{i=2}^{n} (t - \lambda_i)$. Thus $p_{A'}$ splits.
12. By the induction hypothesis, there is an invertible $(n-1) \times (n-1)$ matrix $R$ such that $U' = R^{-1} A' R$ is upper triangular.
13. Let $S$ be the [[block diagonal matrix|0M0SNKZ482]] $\operatorname{diag}(1, R)$. It is invertible, with inverse $\operatorname{diag}(1, R^{-1})$.
14. Block multiplication gives $S^{-1} Q^{-1} A Q S = \begin{pmatrix} \lambda_1 & r R \\ 0 & U' \end{pmatrix}$. This matrix is upper triangular, since $U'$ is.
15. With the invertible matrix $P = Q S$, step 14 says $P^{-1} A P$ is upper triangular. This completes the induction.
16. Now let $F$ be [[algebraically closed|02SJG1HC32]]. We show by induction on $d \ge 1$ that each monic $f \in F[t]$ of degree $d$ splits. The polynomial $f$ has a root $c \in F$, and the [[factor theorem|0K3MWA7DMC]] gives $f = (t - c) g$.
17. Here $g$ is monic of degree $d - 1$. If $d = 1$, then $g = 1$. If $d \ge 2$, then $g$ splits by the induction hypothesis, so $f$ splits.
18. So over an algebraically closed field, $p_A$ splits, and $A$ is similar to an upper triangular matrix by step 15.
19. By the [[fundamental theorem of algebra|0JP0W07Y9A]], each nonconstant complex polynomial has a complex root. So $\C$ is algebraically closed, and step 18 applies to $\C$.

20. For an endomorphism $T$, choose a basis $\mathcal{B}$ and let $A = [T]_{\mathcal{B}}$. Then $p_T = p_A$, and $T$ is triangular in some basis exactly when $A$ is similar to a triangular matrix, by the [[change of basis formula|0MQXVZEBMT]]. So steps 1 to 19 prove $1 \Leftrightarrow 3$ for $T$.
21. Let $(v_1, \dots, v_n)$ be a basis and $V_i = \operatorname{span}(v_1, \dots, v_i)$. Column $j$ of the [[matrix of $T$|0YYMY95FWS]] holds the coordinates of $T(v_j)$.
22. So the matrix is upper triangular exactly when $T(v_j) \in V_j$ for each $j$.
23. Since $V_i$ is spanned by $v_1, \dots, v_i$, this holds exactly when $T(V_i) \subseteq V_i$ for each $i$, that is, when each $V_i$ is [[invariant|0EP59ESQ94]].
24. So a triangular basis gives the flag $(V_i)$ of condition 2. Conversely, given a flag, choose $v_i \in V_i \setminus V_{i-1}$ for each $i$.
25. By induction on $i$, $(v_1, \dots, v_i)$ is a basis of $V_i$, since $\dim V_i = i$ and $v_i \notin V_{i-1}$. Then steps 22 and 23 give condition 1.
26. In a triangular form $U$, step 2 gives $p_T = \prod_i (t - u_{ii})$. So each $\lambda$ occurs on the diagonal as often as its algebraic multiplicity.

## Idea

A triangular matrix visibly has a split characteristic polynomial.
Conversely, a root of $p_A$ gives an eigenvector, and putting it first in a basis makes the first column $\lambda_1 e_1$.
The remaining $(n-1) \times (n-1)$ block still has a split characteristic polynomial, so induction triangularizes it.
Triangular in the basis $(v_1, \dots, v_n)$ means exactly that the spans of the first $i$ vectors are invariant.

## Variants

The same induction can be written without matrices, with the [[quotient operator|0PFPWKBDTJ]].
Let $U = F v$ for an eigenvector $v$.
By the [[block triangular form|ENVF51H5S3]], $p_T = (t - \lambda_1) p_{\bar T}$, so $p_{\bar T}$ splits on $V / U$.
A flag of $\bar T$-invariant subspaces of $V / U$ pulls back under the quotient map to a flag of $T$-invariant subspaces of $V$ that contain $U$.
Adding $U$ at the bottom gives a full flag of $V$.
Over $\C$ with an inner product, applying Gram-Schmidt to a triangular basis keeps the flag, which gives the [[Schur decomposition|V1JG4C7R7B]].
