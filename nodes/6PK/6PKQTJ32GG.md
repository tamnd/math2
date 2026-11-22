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

We read a diagonal matrix column by column to get $1 \Leftrightarrow 2$, then prove $2 \Rightarrow 3 \Rightarrow 4 \Rightarrow 2$ with the independence of eigenvectors, and finish with the matrix form.

*Conditions 1 and 2.*

1. Let $\mathcal{B} = (v_1, \dots, v_n)$ be a [[basis|0VTQTPQGAV]] of $V$.
   By the definition of the [[matrix of $T$|0YYMY95FWS]], column $j$ of $[T]_{\mathcal{B}}$ holds the coordinates of $T(v_j)$ in $\mathcal{B}$.
2. So $[T]_{\mathcal{B}}$ is the [[diagonal matrix|0Q9PGXD9E4]] $\operatorname{diag}(\mu_1, \dots, \mu_n)$ if and only if $T(v_j) = \mu_j v_j$ for each $j$.
3. Each $v_j$ is nonzero, because it belongs to a basis.
   So $T(v_j) = \mu_j v_j$ says that $v_j$ is an [[eigenvector|0B5H4208Z9]] for $\mu_j$.
4. By steps 2 and 3, $T$ has a diagonal matrix in some basis if and only if $V$ has a basis of eigenvectors.
   By the [[definition of diagonalizable|0Y17PEKF24]], this is $1 \Leftrightarrow 2$.

*From condition 2 to condition 3.*

5. We first show that the sum $W = E_{\lambda_1} + \cdots + E_{\lambda_k}$ is direct, using only that the $\lambda_i$ are distinct.
   Let $u_i \in E_{\lambda_i}$ with $u_1 + \cdots + u_k = 0$, and suppose that the set $I$ of indices with $u_i \ne 0$ is not empty.
6. For $i \in I$, the vector $u_i$ is an eigenvector for $\lambda_i$, and these eigenvalues are distinct.
   So the $u_i$ with $i \in I$ are linearly independent, because [[eigenvectors with distinct eigenvalues are linearly independent|0HNMFG8F8K]].
7. But $\sum_{i \in I} u_i = 0$ is a relation among them with all coefficients $1$, which contradicts step 6.
   So $I$ is empty, and every $u_i = 0$.
8. By step 7 and the [[criterion for a direct sum|FVKY28HHBC]], the sum $W$ is [[direct|041JTZCK9Q]].
9. Now assume condition 2.
   Each vector of the basis of eigenvectors lies in the eigenspace of its eigenvalue, so it lies in $W$.
   Hence $W$ contains a basis of $V$, so $W = V$, which is condition 3.

*From condition 3 to condition 4.*

10. Assume condition 3, and choose a basis $\mathcal{B}_i$ of each $E_{\lambda_i}$, with $d_i = \dim E_{\lambda_i}$ vectors.
    Let $\mathcal{C}$ be the list of all these vectors.
11. The list $\mathcal{C}$ spans $V$.
    Each $v \in V$ is a sum $\sum_i u_i$ with $u_i \in E_{\lambda_i}$ by condition 3, and each $u_i$ is a combination of $\mathcal{B}_i$.
12. The list $\mathcal{C}$ is [[linearly independent|0EVHJFTG9Z]].
    A relation among its vectors groups into $\sum_i u_i = 0$ with $u_i \in E_{\lambda_i}$, and each $u_i = 0$ because the sum is direct.
    Then each coefficient is $0$, because each $\mathcal{B}_i$ is independent.
13. So $\mathcal{C}$ is a basis of $V$ with $d_1 + \cdots + d_k$ vectors, and this number is $\dim V = n$.
    This is condition 4.

*From condition 4 to condition 2.*

14. Assume condition 4.
    By steps 5 to 8, the sum $W$ of the eigenspaces is direct, so the list $\mathcal{C}$ of step 10 is independent by the argument of step 12.
15. The list $\mathcal{C}$ has $d_1 + \cdots + d_k = n$ vectors, and $\dim V = n$.
    By the [[right-size criterion|096V7H13H9]], $\mathcal{C}$ is a basis of $V$.
16. Each vector of $\mathcal{C}$ is a nonzero vector of some $E_{\lambda_i}$, so it is an eigenvector.
    This is condition 2.

*The matrix form.*

17. Let $L(x) = A x$ on $F^n$, and let $\mathcal{E}$ be the standard basis.
    Then $[L]_{\mathcal{E}} = A$, since $L(e_j) = A e_j$ is column $j$ of $A$.
18. Let $v_1, \dots, v_n$ be a basis of eigenvectors with $A v_i = \mu_i v_i$, and let $P$ have these columns.
    Then $P$ is the [[change of basis matrix|0KWXYZPJKN]] from $\mathcal{E}$ to $\mathcal{B} = (v_1, \dots, v_n)$, because its column $j$ holds the coordinates of $v_j$ in $\mathcal{E}$.
19. By the [[change of basis formula|0MQXVZEBMT]], $P$ is invertible and $[L]_{\mathcal{B}} = P^{-1} A P$.
    By step 2, $[L]_{\mathcal{B}} = \operatorname{diag}(\mu_1, \dots, \mu_n)$.
20. Conversely, let $P$ be [[invertible|0TWTS88TWN]] with $P^{-1} A P = D = \operatorname{diag}(d_1, \dots, d_n)$, and let $v_j$ be column $j$ of $P$.
    Multiplying by $P$ on the left gives $A P = P D$.
    Column $j$ of $A P$ is $A v_j$, and column $j$ of $P D$ is $d_j v_j$, so $A v_j = d_j v_j$.
21. If $\sum_j c_j v_j = 0$, then $P c = 0$ for the column $c = (c_j)$, so $c = P^{-1} P c = 0$.
    So the $v_j$ are independent, and they form a basis of $F^n$, which has [[dimension $n$|0QK7FPE6VE]].
22. In particular each $v_j$ is nonzero, so $A v_j = d_j v_j$ makes it an eigenvector for $d_j$.
    This proves the matrix form, and the proof is complete.

## Idea

A matrix is diagonal exactly when each basis vector is sent to a multiple of itself, and that is the definition of an eigenvector.
So "diagonal in some basis" and "a basis of eigenvectors" say the same thing.
Eigenvectors for distinct eigenvalues are independent, so the eigenspaces always form a direct sum, and the only question is whether this sum fills $V$.
It fills $V$ exactly when the dimensions add up to $n$.
For matrices, the equation $A P = P D$ read one column at a time says that the columns of $P$ are eigenvectors.

## Variants

The step $4 \Rightarrow 3$ can also be done with the [[dimension criterion for a direct sum|P4JG9DJ2HH]] for two summands and induction on $k$.
For the matrix form, we can skip the change of basis formula and check $A P = P D$ column by column, as steps 20 to 22 do for the converse.
