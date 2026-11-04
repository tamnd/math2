---
tag: 6PKQTJ32GG
kind: proof
name: Proof that a matrix is diagonalisable iff it has a basis of eigenvectors
msc: [15A20]
proves: 056SW1E0AC
uses: [0Y17PEKF24, 0B5H4208Z9, 0VTQTPQGAV, 0Q9PGXD9E4, 0YYMY95FWS, 0KWXYZPJKN, 0MQXVZEBMT, 0TWTS88TWN, 0EVHJFTG9Z, 096V7H13H9, 0QK7FPE6VE]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonalizable_matrix
    locator: Characterization
---

## Proof

We prove the formula for $P^{-1} A P$ first, and then both implications.

1. Let $L \colon F^n \to F^n$ be the linear map $L(x) = A x$, and let $E = (e_1, \dots, e_n)$ be the standard basis. Then $L(e_j) = A e_j$ is column $j$ of $A$, so the [[matrix of $L$|0YYMY95FWS]] in $E$ is $[L]_E = A$.
2. Let $B' = (v_1, \dots, v_n)$ be a [[basis|0VTQTPQGAV]] of $F^n$ with $A v_i = \lambda_i v_i$ for each $i$. Let $P$ be the matrix with columns $v_1, \dots, v_n$.
3. Column $j$ of $P$ is $v_j = [v_j]_E$. So $P$ is the [[change of basis matrix|0KWXYZPJKN]] from $E$ to $B'$.
4. Since $L(v_j) = \lambda_j v_j$, column $j$ of $[L]_{B'}$ has $\lambda_j$ in row $j$ and $0$ elsewhere. So $[L]_{B'} = D$, the [[diagonal matrix|0Q9PGXD9E4]] $\operatorname{diag}(\lambda_1, \dots, \lambda_n)$.
5. By the [[change of basis formula|0MQXVZEBMT]], $P$ is invertible and $[L]_{B'} = P^{-1} [L]_E P$. By steps 1 and 4, $P^{-1} A P = D$.
6. This proves the formula of the statement. It also shows that if $F^n$ has a basis of eigenvectors of $A$, then $A$ is [[diagonalisable|0Y17PEKF24]].
7. Conversely, let $A$ be diagonalisable. So there is an [[invertible|0TWTS88TWN]] matrix $P$ with $P^{-1} A P = D = \operatorname{diag}(d_1, \dots, d_n)$.
8. Let $v_1, \dots, v_n$ be the columns of $P$. Multiplying by $P$ on the left gives $A P = P D$.
9. Column $j$ of $A P$ is $A v_j$. Column $j$ of $P D$ is $P (d_j e_j) = d_j v_j$. So $A v_j = d_j v_j$ for each $j$.
10. Let $c_1, \dots, c_n \in F$ with $\sum_j c_j v_j = 0$, and let $c$ be the column with entries $c_j$. Then $P c = 0$, so $c = P^{-1} P c = 0$.
11. By step 10, $v_1, \dots, v_n$ are [[linearly independent|0EVHJFTG9Z]]. The space $F^n$ has [[dimension $n$|0QK7FPE6VE]], so they form a basis [[by counting|096V7H13H9]].
12. Each $v_j$ is nonzero, since it belongs to a basis. By step 9, $v_j$ is an [[eigenvector|0B5H4208Z9]] of $A$ for $d_j$.
13. So $F^n$ has a basis of eigenvectors of $A$. Together with step 6, this proves the equivalence.

## Idea

The equation $A P = P D$ read column by column says exactly that each column of $P$ is an eigenvector, with eigenvalue the matching diagonal entry of $D$. The matrix $P$ is invertible exactly when its columns form a basis. So diagonalising $A$ and finding a basis of eigenvectors are the same task.
