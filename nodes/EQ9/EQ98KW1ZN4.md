---
tag: EQ98KW1ZN4
kind: statement
role: theorem
name: Square root of a positive semidefinite matrix
msc: [15A16, 15B57]
topics: [SS4EVPKT3A]
audience: ug2
about: [01MMVW8CKC, 0BJVDCF38Y]
uses: [0880F9EQCP, 0QQCG3JWJ4, 0EKZCX4K3P]
proofs: [MKM42YWBN6]
sources:
  - url: https://en.wikipedia.org/wiki/Square_root_of_a_matrix
    locator: Positive semidefinite matrices
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Square root
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780521839402
    locator: Chapter 7
---

## Statement

A positive semidefinite matrix has exactly one positive semidefinite square root, just as a nonnegative number has exactly one nonnegative square root.
Let $A$ be an $n \times n$ complex [[positive semidefinite|01MMVW8CKC]] matrix.

1. Existence and uniqueness. There is exactly one positive semidefinite matrix $B$ with $B^2 = A$. We write $B = A^{1/2}$ or $B = \sqrt A$.
2. Polynomial form. There is a polynomial $p$ with real coefficients such that $A^{1/2} = p(A)$. So $A^{1/2}$ commutes with every matrix that commutes with $A$.
3. Construction. If $A = U D U^*$ with $U$ unitary and $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$, then $A^{1/2} = U \operatorname{diag}(\sqrt{\lambda_1}, \dots, \sqrt{\lambda_n}) U^*$.
4. Kernel and rank. $A^{1/2}$ and $A$ have the same null space and the same rank. In particular $A^{1/2}$ is [[positive definite|0KX66CZMBB]] if and only if $A$ is.
5. Real case. If $A$ is real, then $A^{1/2}$ is real.

The [[proof by the spectral theorem|MKM42YWBN6]] proves all five parts, and the [[definition of the square root|0N5GP3YT8T]] rests on part 1.

## Remarks

### A first square root

Take $A = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}$.
It stretches the direction $(1, 1)$ by $9$ and the direction $(1, -1)$ by $1$, since $A(1, 1) = (9, 9)$ and $A(1, -1) = (1, -1)$.
A square root must then stretch $(1, 1)$ by $3$ and $(1, -1)$ by $1$, and the matrix that does this is
$$A^{1/2} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}.$$
Check: $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}^2 = \begin{pmatrix} 4 + 1 & 2 + 2 \\ 2 + 2 & 1 + 4 \end{pmatrix} = A$.
The polynomial of part 2 is $p(t) = (t + 3)/4$, since $p(9) = 3$ and $p(1) = 1$, and indeed $\tfrac14 (A + 3I) = \tfrac14 \begin{pmatrix} 8 & 4 \\ 4 & 8 \end{pmatrix}$ is the same matrix.
[[The worked example|QTV6Y0710E]] carries out both recipes in full.

### Why each hypothesis is needed

The condition that $B$ is positive semidefinite is what makes the root unique.
The matrix $A$ above has four symmetric square roots, $\pm \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $\pm \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$, and only the first has nonnegative eigenvalues.
If we drop symmetry too, there are even more roots.
The identity $I_2$ has infinitely many, since every reflection $\begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}$ squares to $I_2$.

The matrix $A$ itself must be positive semidefinite for a root of this kind to exist.
If $B$ is Hermitian, then $B^2 = B^* B$ is positive semidefinite by the [[Gram matrix theorem|0AM050KCAW]].
So a Hermitian matrix with a negative eigenvalue, such as $\operatorname{diag}(1, -1)$, has no Hermitian square root at all.

### What it gives you

Part 1 together with this last remark says that $B \mapsto B^2$ is a bijection from the positive semidefinite matrices onto themselves, and $A \mapsto A^{1/2}$ is its inverse.
Every positive semidefinite $A$ is then a Gram matrix, $A = B^* B$ with $B = A^{1/2}$.
The [[polar decomposition|0J2C7BDJQA]] $A = UP$ takes $P = (A^* A)^{1/2}$, and the [[singular values|09VMDSRXWJ]] of $A$ are the eigenvalues of this $P$.

Part 2 gives a product rule.
If $A$ and $C$ are positive semidefinite and $AC = CA$, then $C$ commutes with $A^{1/2}$, so $AC = A^{1/2} C A^{1/2}$.
The right side is Hermitian and satisfies $x^* A^{1/2} C A^{1/2} x = y^* C y \ge 0$ with $y = A^{1/2} x$, so $AC$ is positive semidefinite.
Without the commuting condition the product need not even be Hermitian.

### Watch out

The square root of a matrix is not the matrix of square roots of its entries.
For the matrix $A$ above,
$$\begin{pmatrix} \sqrt 5 & 2 \\ 2 & \sqrt 5 \end{pmatrix}^2 = \begin{pmatrix} 9 & 4 \sqrt 5 \\ 4 \sqrt 5 & 9 \end{pmatrix} \ne A.$$
The entrywise rule is correct only for diagonal matrices, which is why part 3 first diagonalizes $A$.
A second trap is to forget the positivity condition and call $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ "the" square root of $A$; it squares to $A$, but it has the eigenvalue $-1$.

### Generalizations

The same theorem holds for a positive operator on a finite-dimensional inner product space, in the form of the [[square root of a positive operator|3JY5HNFRMF]].
The recipe of part 3 also defines other functions of a Hermitian matrix, $f(A) = U \operatorname{diag}(f(\lambda_1), \dots, f(\lambda_n)) U^*$, such as $A^r$ for $r > 0$ and $\log A$ for positive definite $A$.
For bounded positive operators on a Hilbert space, a unique positive square root still exists, and that belongs to functional analysis.

### Try it

First, find the positive semidefinite square root of $\begin{pmatrix} 4 & 0 \\ 0 & 0 \end{pmatrix}$.
It is $\begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix}$, since the matrix is already diagonal with eigenvalues $4$ and $0$.

Second, find the root of $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, whose eigenvalues are $3$ and $1$.
The polynomial $p(t) = \big( (\sqrt3 - 1) t + 3 - \sqrt 3 \big)/2$ has $p(3) = \sqrt 3$ and $p(1) = 1$, so the root is $p(A) = \tfrac12 \begin{pmatrix} \sqrt3 + 1 & \sqrt3 - 1 \\ \sqrt3 - 1 & \sqrt3 + 1 \end{pmatrix}$.

## Explanations

### L1 human

A nonnegative number has exactly one nonnegative square root, for example $\sqrt 9 = 3$.
A positive semidefinite matrix behaves the same way.
It stretches some perpendicular directions by nonnegative amounts, and its square root stretches the same directions by the square roots of those amounts.
For example, $\begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}$ stretches the diagonal direction by $9$, and its square root $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ stretches it by $3$.

### L2 human

Here is a typical problem: find $A^{1/2}$ for $A = \begin{pmatrix} 2 & 2 \\ 2 & 5 \end{pmatrix}$.
The characteristic polynomial is $t^2 - 7t + 6 = (t - 6)(t - 1)$, so the eigenvalues are $6$ and $1$, with eigenvectors $(1, 2)$ and $(2, -1)$.
With the unit vectors $u_1 = \tfrac{1}{\sqrt5}(1, 2)$ and $u_2 = \tfrac{1}{\sqrt5}(2, -1)$, part 3 gives
$$A^{1/2} = \sqrt 6 \, u_1 u_1^{\mathsf{T}} + 1 \cdot u_2 u_2^{\mathsf{T}} = \frac{1}{5} \begin{pmatrix} \sqrt6 + 4 & 2\sqrt6 - 2 \\ 2\sqrt6 - 2 & 4\sqrt6 + 1 \end{pmatrix}.$$
Check the top left entry of the square: $\big( (\sqrt6 + 4)^2 + (2\sqrt6 - 2)^2 \big)/25 = (22 + 8\sqrt6 + 28 - 8\sqrt6)/25 = 2$.
Square roots like this one appear whenever a positive definite matrix must be "split in half", as in the polar decomposition or in whitening data with a covariance matrix.
The trap is to take square roots entry by entry, which works only for diagonal matrices.

### L3 human

The square root is the case $f(t) = \sqrt t$ of the functional calculus $f(A) = \sum_k f(\mu_k) P_k$, where the $P_k$ are the projections of the [[spectral decomposition|D5KVBA1K9R]].
Part 2 says that $A^{1/2}$ lies in the algebra generated by $A$, and that fact is the core of the uniqueness proof.
The map $A \mapsto A^{1/2}$ is continuous on the positive semidefinite cone, and it is operator monotone: $A \succeq C \succeq 0$ implies $A^{1/2} \succeq C^{1/2}$ in the [[Loewner order|9G9S92T1VJ]].
The converse fails for squares, since $A \succeq C \succeq 0$ does not imply $A^2 \succeq C^2$; such questions belong to matrix analysis.
