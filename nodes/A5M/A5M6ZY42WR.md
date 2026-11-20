---
tag: A5M6ZY42WR
kind: proof
name: Proof of the complex spectral theorem by the Schur decomposition
msc: ["15A21", "47B15"]
topics: [3YM9EK6VMB]
audience: ug1
proves: 04CW1P44VD
uses: [0ENZN5G4CV, V1JG4C7R7B, 0DBTE6HVBD, 0D6RMJ10M9, 0FWJ0VW561, 0N4XY7Z3NN, 0XYKE8BE7X]
methods: [TFQ1845T84, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_theorem
    locator: Normal matrices
  - url: https://en.wikipedia.org/wiki/Schur_decomposition
    locator: Notes
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Proof

The easy direction uses that diagonal matrices commute.
For the main direction, the Schur decomposition gives a triangular matrix, and a normal triangular matrix is diagonal.

1. Part 1, "if". Let $e_1, \dots, e_n$ be an [[orthonormal basis|0FWJ0VW561]] of $V$ with $T e_k = \lambda_k e_k$. The matrix of $T$ in this basis is $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$.
2. By [[the matrix of the adjoint|0DBTE6HVBD]], the matrix of $T^*$ in the same orthonormal basis is $D^* = \operatorname{diag}(\overline{\lambda_1}, \dots, \overline{\lambda_n})$.
3. Diagonal matrices commute, so $D D^* = D^* D$. These are the matrices of $T T^*$ and $T^* T$, so $T T^* = T^* T$, and $T$ is [[normal|0ENZN5G4CV]].
4. Part 1, "only if". Let $T$ be normal. By part 1 of [[the Schur decomposition|V1JG4C7R7B]], $V$ has an orthonormal basis $e_1, \dots, e_n$ in which the matrix $U$ of $T$ is [[upper triangular|0N4XY7Z3NN]].
5. The matrix of $T^*$ in this basis is $U^*$, by the matrix of the adjoint. Since $T T^* = T^* T$, we get $U U^* = U^* U$. So $U$ is a [[normal matrix|0XYKE8BE7X]].
6. Claim: every upper triangular normal $m \times m$ matrix $U$ is diagonal. We prove it by induction on $m$. For $m = 1$, every $1 \times 1$ matrix is diagonal.
7. Let $m \geq 2$, and write $U = \begin{pmatrix} u_{11} & r \\ 0 & U' \end{pmatrix}$ with a row $r$ of length $m - 1$ and an upper triangular $U'$ of size $m - 1$.
8. The $(1, 1)$ entry of $U U^*$ is the first row of $U$ times its conjugate: $\abs{u_{11}}^2 + \norm{r}^2$, where $\norm{r}^2$ is the sum of the $\abs{r_j}^2$.
9. The $(1, 1)$ entry of $U^* U$ is the first column of $U$ times its conjugate. This column is $(u_{11}, 0, \dots, 0)$, so the entry is $\abs{u_{11}}^2$.
10. By step 5, the two entries are equal, so $\norm{r}^2 = 0$, and $r = 0$.
11. Block multiplication now gives $U U^* = \begin{pmatrix} \abs{u_{11}}^2 & 0 \\ 0 & U' U'^* \end{pmatrix}$ and $U^* U = \begin{pmatrix} \abs{u_{11}}^2 & 0 \\ 0 & U'^* U' \end{pmatrix}$. So $U'$ is normal and upper triangular.
12. By the induction hypothesis, $U'$ is diagonal. With $r = 0$, the matrix $U$ is diagonal. This proves the claim.
13. By steps 5 and 12, the matrix of $T$ in the basis $e_1, \dots, e_n$ is diagonal. So $T e_k = u_{kk} e_k$ for every $k$, and $e_1, \dots, e_n$ is an orthonormal basis of eigenvectors.
14. Part 2, "only if". Let $A$ be normal, and apply part 1 to $x \mapsto Ax$ on $\mathbb{C}^n$ with the standard inner product. Let $U$ have the orthonormal eigenvectors $u_1, \dots, u_n$ as columns, with $A u_k = \lambda_k u_k$.
15. The columns of $U$ are orthonormal, so $U^* U = I$, and $U$ is [[unitary|0D6RMJ10M9]]. Column $k$ of $AU$ is $\lambda_k u_k$, so $AU = UD$ with $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$. Hence $A = U D U^*$.
16. Part 2, "if". Let $A = U D U^*$ with $U$ unitary and $D$ diagonal. Then $A A^* = U D U^* U D^* U^* = U D D^* U^*$ and $A^* A = U D^* D U^*$.
17. Since $D D^* = D^* D$, the two products are equal, and $A$ is normal.

## Idea

An operator with an orthonormal eigenbasis is a diagonal matrix in disguise, and diagonal matrices commute with their conjugate transposes.
Conversely, Schur gives an orthonormal basis in which the matrix is triangular.
For a normal triangular matrix, comparing the $(1, 1)$ entries of $U U^*$ and $U^* U$ shows that the first row has no entries off the diagonal, and induction does the rest.

## Variants

- [[The deflation proof|P48CFDFAV9]] uses that an eigenvector of $A$ is also an eigenvector of $A^*$. Then its orthogonal complement is invariant under $A$, and induction on the dimension applies.
- For self-adjoint operators there is a proof without Schur and without the fundamental theorem of algebra. It maximizes the quadratic form on spheres, as in [[the variational proof of the real spectral theorem|GHGBEV51GZ]], and the same steps work over $\mathbb{C}$.
