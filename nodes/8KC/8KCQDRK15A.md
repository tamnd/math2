---
tag: 8KCQDRK15A
kind: proof
name: Proof of the Schur decomposition by induction
msc: ["15A23", "15A21"]
topics: [3YM9EK6VMB]
audience: ug1
proves: V1JG4C7R7B
uses: [08CJB2NQ92, 0FWJ0VW561, 0E2NYPVSP9, 0Y85GYEGSF, 0D6RMJ10M9, 0QRBVFJ50X, 191HBJ7PVZ, 0K1KKMFHYH, KAV44BRV77, ENVF51H5S3, 0J9TVTNB4K]
methods: [0ASJVEFA9J, B2D8PTFNN1, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_decomposition
    locator: Proof
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Proof

We prove part 1 by induction on $n = \dim V$: we split off one unit eigenvector and apply the induction hypothesis to its orthogonal complement.
Part 2 is part 1 for $\mathbb{C}^n$, and part 3 repeats the induction with an invariant subspace of dimension $1$ or $2$ in place of an eigenvector.

1. Base case of part 1. If $n = 1$, every unit vector $e_1$ is an [[orthonormal basis|0FWJ0VW561]], and every $1 \times 1$ matrix is upper triangular.
2. Induction step. Let $n \geq 2$, and assume part 1 for all complex inner product spaces of dimension $n - 1$.
3. The space $V$ is complex and nonzero, so $T$ has [[an eigenvalue|08CJB2NQ92]] $\lambda_1$. Let $e_1$ be an eigenvector for $\lambda_1$ with $\norm{e_1} = 1$.
4. Let $W = e_1^\perp$. By [[the dimension of the orthogonal complement|0E2NYPVSP9]], $\dim W = n - 1$.
5. Define $P \colon V \to W$ by $Pv = v - \ip{v}{e_1} e_1$. The map $P$ is linear, and it lands in $W$ because $\ip{Pv}{e_1} = \ip{v}{e_1} - \ip{v}{e_1} \ip{e_1}{e_1} = 0$.
6. Define $S \colon W \to W$ by $S w = P(Tw)$. It is linear, as a composition of linear maps.
7. By the induction hypothesis for $S$ on $W$, there is an orthonormal basis $e_2, \dots, e_n$ of $W$ with $S e_k \in \operatorname{span}(e_2, \dots, e_k)$ for $k = 2, \dots, n$.
8. The vectors $e_1, \dots, e_n$ are orthonormal, because $e_1$ is a unit vector orthogonal to $W$. Orthonormal vectors are linearly independent, and there are $n$ of them, so they form a basis of $V$.
9. For $k = 1$, step 3 gives $T e_1 = \lambda_1 e_1 \in \operatorname{span}(e_1)$.
10. For $k \geq 2$, the definition of $P$ gives the splitting
$$T e_k = P(T e_k) + \ip{T e_k}{e_1} e_1 = S e_k + \ip{T e_k}{e_1} e_1.$$
11. By step 7, the right side of step 10 lies in $\operatorname{span}(e_1, \dots, e_k)$. So $T e_k \in \operatorname{span}(e_1, \dots, e_k)$ for every $k$.
12. Step 11 says that column $k$ of the matrix of $T$ has zeros below row $k$. So the matrix is upper triangular, and the induction proves part 1.
13. Part 2. Apply part 1 to $T(x) = Ax$ on $\mathbb{C}^n$ with the standard inner product, and let $Q$ be the matrix with the columns $e_1, \dots, e_n$. The columns of $Q$ are orthonormal, so $Q^* Q = I$ and $Q$ is [[unitary|0D6RMJ10M9]].
14. Let $U = (u_{jk})$ be the upper triangular matrix of $T$ from part 1. Column $k$ of $AQ$ is $A e_k = \sum_{j \leq k} u_{jk} e_j$, which is column $k$ of $QU$. So $AQ = QU$, and $A = Q U Q^*$.
15. The matrices $A$ and $U$ are similar, so they have the same characteristic polynomial, by [[the invariants of similar matrices|191HBJ7PVZ]]. By [[the determinant of a triangular matrix|0K1KKMFHYH]], this polynomial is $\prod_k (u_{kk} - t)$. So the diagonal entries of $U$ are the eigenvalues of $A$, with their algebraic multiplicities.
16. Part 3, base case. We use strong induction on $n$. For $n = 1$, take $Q = (1)$ and $M = A$.
17. Let $n \geq 2$, and assume part 3 for all real matrices of size less than $n$. By [[the invariant subspace theorem|KAV44BRV77]], the map $x \mapsto Ax$ on $\mathbb{R}^n$ has an invariant subspace $U_0$ of dimension $k = 1$ or $k = 2$.
18. If $A$ has a real eigenvalue, we choose $k = 1$ and let $U_0$ be spanned by a real eigenvector. Otherwise $k = 2$, because an invariant line $\mathbb{R} u$ would give a real eigenvalue.
19. Choose an orthonormal basis $q_1, \dots, q_k$ of $U_0$, and extend it by [[an orthonormal basis|0Y85GYEGSF]] of $U_0^\perp$ to an orthonormal basis $q_1, \dots, q_n$ of $\mathbb{R}^n$. Let $Q_1$ have these columns. It is an [[orthogonal matrix|0QRBVFJ50X]], since its columns are orthonormal.
20. For $j \leq k$, the vector $A q_j$ lies in $U_0$, so $q_i^{\mathsf{T}} A q_j = 0$ for $i > k$. By [[the block triangular form|ENVF51H5S3]], $Q_1^{\mathsf{T}} A Q_1 = \begin{pmatrix} B & C \\ 0 & A' \end{pmatrix}$ with $B$ of size $k \times k$.
21. If $k = 2$, then $B$ has no real eigenvalue. The reason is that $B$ is the matrix of $A$ on $U_0$, and a real eigenvector of $B$ would give a real eigenvector of $A$ in $U_0$.
22. If $n = k$, we are done with $Q = Q_1$ and $M = B$. Otherwise $A'$ has size $n - k < n$, and the induction hypothesis gives $A' = Q' M' Q'^{\mathsf{T}}$ with $Q'$ orthogonal and $M'$ as in part 3.
23. Let $Q = Q_1 \begin{pmatrix} I_k & 0 \\ 0 & Q' \end{pmatrix}$. It is a product of orthogonal matrices, so it is orthogonal.
24. Block multiplication gives
$$Q^{\mathsf{T}} A Q = \begin{pmatrix} B & C Q' \\ 0 & Q'^{\mathsf{T}} A' Q' \end{pmatrix} = \begin{pmatrix} B & C Q' \\ 0 & M' \end{pmatrix}.$$
Call this matrix $M$.
25. The diagonal blocks of $M$ are $B$ and the diagonal blocks of $M'$. Each is $1 \times 1$ or is $2 \times 2$ without a real eigenvalue, so $A = Q M Q^{\mathsf{T}}$ has the form of part 3.
26. Eigenvalues in part 3. By [[the determinant of a block triangular matrix|0J9TVTNB4K]] and step 15, the characteristic polynomial of $A$ is the product of those of the diagonal blocks. A real $2 \times 2$ block without a real eigenvalue has a pair of conjugate non-real eigenvalues, since its characteristic polynomial is real.

## Idea

Pick one eigenvector, make it the first vector of an orthonormal basis, and repeat on its orthogonal complement.
In that basis the matrix has the eigenvalue in the top left corner and zeros below it, and the rest of the matrix is a smaller problem.
Gram-Schmidt never enters, because each new vector is orthogonal to the earlier ones by construction.
Over $\mathbb{R}$ an eigenvector may not exist, so a $2 \times 2$ invariant block takes its place, and the triangle becomes a block triangle.

## Variants

There is a matrix version of the same proof for part 2.
Choose a unit eigenvector $q_1$, extend it to a unitary $Q_1$, and write $Q_1^* A Q_1 = \begin{pmatrix} \lambda_1 & b \\ 0 & A' \end{pmatrix}$, then apply induction to the $(n - 1) \times (n - 1)$ matrix $A'$.
This is steps 16 to 25 with $k = 1$ every time and with unitary matrices in place of orthogonal ones.

A second proof starts from [[triangularization|0363JMQ42Y]] over $\mathbb{C}$, which gives an invariant flag $V_1 \subset \dots \subset V_n$.
Gram-Schmidt applied to a basis adapted to the flag gives an orthonormal basis with the same spans $V_k$, so the flag stays invariant and the matrix in the new basis is upper triangular.
