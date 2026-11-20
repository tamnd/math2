---
tag: 6PKQTJ32GG
kind: proof
name: Proof that diagonalizable means a basis of eigenvectors
msc: ["15A20"]
topics: [Z6S6PWMJPH]
audience: ug1
proves: 056SW1E0AC
methods: [0NTF6DMVAP, TFQ1845T84]
uses: [0Y17PEKF24, 0B5H4208Z9, 0VTQTPQGAV, 0Q9PGXD9E4, 0YYMY95FWS, 0KWXYZPJKN, 0MQXVZEBMT, 0TWTS88TWN, 0EVHJFTG9Z, 096V7H13H9, 0QK7FPE6VE, 0HNMFG8F8K, FVKY28HHBC, 0AYEPBQMAW, 041JTZCK9Q]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonalizable_matrix
    locator: Characterization
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Proof

We prove $1 \Leftrightarrow 2$, then $2 \Rightarrow 3 \Rightarrow 4 \Rightarrow 2$, and then the matrix form.

1. Let $\mathcal{B} = (v_1, \dots, v_n)$ be a [[basis|0VTQTPQGAV]] of $V$. By the definition of the [[matrix of $T$|0YYMY95FWS]], column $j$ of $[T]_{\mathcal{B}}$ holds the coordinates of $T(v_j)$ in $\mathcal{B}$.
2. So $[T]_{\mathcal{B}}$ is the [[diagonal matrix|0Q9PGXD9E4]] $\operatorname{diag}(\mu_1, \dots, \mu_n)$ if and only if $T(v_j) = \mu_j v_j$ for each $j$.
3. Each $v_j$ is nonzero, since it belongs to a basis. So $T(v_j) = \mu_j v_j$ says that $v_j$ is an [[eigenvector|0B5H4208Z9]] for $\mu_j$.
4. By steps 2 and 3, $T$ has a diagonal matrix in some basis if and only if $V$ has a basis of eigenvectors. This is $1 \Leftrightarrow 2$, by the [[definition of diagonalizable|0Y17PEKF24]].
5. Assume condition 2. Let $u_i \in E_{\lambda_i}$ with $u_1 + \cdots + u_k = 0$. Suppose some $u_i \ne 0$, and let $I$ be the set of such $i$.
6. For $i \in I$, $u_i$ is an eigenvector for $\lambda_i$, and the $\lambda_i$ are distinct. So the $u_i$ with $i \in I$ are [[linearly independent|0HNMFG8F8K]].
7. But $\sum_{i \in I} u_i = 0$ is a relation with all coefficients $1$, which contradicts step 6. So each $u_i = 0$.
8. By step 7 and the [[criterion for a direct sum|FVKY28HHBC]], the sum $W = E_{\lambda_1} + \cdots + E_{\lambda_k}$ is [[direct|041JTZCK9Q]].
9. Each vector of the basis of condition 2 is an eigenvector for some $\lambda_i$, so it lies in $W$. Hence $W = V$, which is condition 3.
10. Assume condition 3. Choose a basis $\mathcal{B}_i$ of each $E_{\lambda_i}$, with $d_i = \dim E_{\lambda_i}$ vectors, and let $\mathcal{C}$ be the list of all these vectors.
11. The list $\mathcal{C}$ spans $V$: each $v \in V$ is a sum $\sum_i u_i$ with $u_i \in E_{\lambda_i}$, and each $u_i$ is a combination of $\mathcal{B}_i$.
12. The list $\mathcal{C}$ is [[linearly independent|0EVHJFTG9Z]]: a relation among its vectors groups into $\sum_i u_i = 0$ with $u_i \in E_{\lambda_i}$. Since the sum is direct, each $u_i = 0$, and then each coefficient is $0$ because $\mathcal{B}_i$ is independent.
13. So $\mathcal{C}$ is a basis of $V$ with $d_1 + \cdots + d_k$ vectors, and this number is $n$. This is condition 4.
14. Assume condition 4. Steps 5 to 8 used only the distinctness of the $\lambda_i$, so the sum $W$ of the eigenspaces is direct. Build $\mathcal{C}$ as in step 10.
15. Step 12 shows that $\mathcal{C}$ is independent. It has $d_1 + \cdots + d_k = n$ vectors, and $\dim V = n$. By the [[right-size criterion|096V7H13H9]], $\mathcal{C}$ is a basis of $V$.
16. Each vector of $\mathcal{C}$ is a nonzero vector of some $E_{\lambda_i}$, so it is an eigenvector. This is condition 2.
17. For the matrix form, let $L(x) = A x$ on $F^n$, with the standard basis $\mathcal{E}$. Then $[L]_{\mathcal{E}} = A$, since $L(e_j) = A e_j$ is column $j$ of $A$.
18. Let $v_1, \dots, v_n$ be a basis of eigenvectors with $A v_i = \mu_i v_i$, and $P$ the matrix with these columns. Then $P$ is the [[change of basis matrix|0KWXYZPJKN]] from $\mathcal{E}$ to $\mathcal{B} = (v_1, \dots, v_n)$.
19. By the [[change of basis formula|0MQXVZEBMT]], $P$ is invertible and $[L]_{\mathcal{B}} = P^{-1} A P$. By step 2, $[L]_{\mathcal{B}} = \operatorname{diag}(\mu_1, \dots, \mu_n)$.
20. Conversely, let $P$ be [[invertible|0TWTS88TWN]] with $P^{-1} A P = D = \operatorname{diag}(d_1, \dots, d_n)$. Then $A P = P D$. Column $j$ of $A P$ is $A v_j$, and column $j$ of $P D$ is $d_j v_j$, where $v_j$ is column $j$ of $P$.
21. If $\sum_j c_j v_j = 0$, then $P c = 0$ for the column $c = (c_j)$, so $c = P^{-1} P c = 0$. So the $v_j$ are independent, and they form a basis of $F^n$, which has [[dimension $n$|0QK7FPE6VE]].
22. So each $v_j$ is nonzero, and $A v_j = d_j v_j$ makes it an eigenvector for $d_j$. This proves the matrix form, and the proof is complete.

## Idea

A matrix is diagonal exactly when each basis vector is sent to a multiple of itself, which is the definition of an eigenvector.
Eigenvectors for distinct eigenvalues are independent, so the eigenspaces form a direct sum.
The direct sum fills $V$ exactly when the dimensions add up to $n$.
For matrices, the equation $A P = P D$ read column by column says that the columns of $P$ are eigenvectors.

## Variants

One can prove $4 \Rightarrow 3$ with the [[dimension criterion for a direct sum|P4JG9DJ2HH]] for two summands and induction on $k$.
In the matrix form, one can avoid the change of basis formula and verify $A P = P D$ directly column by column, as in steps 20 to 22.
