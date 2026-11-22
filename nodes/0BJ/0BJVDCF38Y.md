---
tag: 0BJVDCF38Y
kind: concept
name: Square root of a positive semidefinite matrix
msc: [15A16, 15B57]
topics: [SS4EVPKT3A]
audience: ug2
uses: [0880F9EQCP, 0DGZBQWZWN]
sources:
  - url: https://en.wikipedia.org/wiki/Square_root_of_a_matrix
    locator: Positive semidefinite matrices
---

## Summary

Every nonnegative number has exactly one nonnegative square root, and positive semidefinite matrices behave the same way.
The square root of a [[positive semidefinite matrix|01MMVW8CKC]] $A$ is the positive semidefinite matrix $B$ with $B^2 = A$, and the [[square root theorem|EQ98KW1ZN4]] says that there is exactly one such $B$.
To find it, diagonalize $A$ by an orthonormal basis of eigenvectors and take the nonnegative square root of each eigenvalue:
$$A = U \operatorname{diag}(\lambda_1, \dots, \lambda_n) U^*, \qquad A^{1/2} = U \operatorname{diag}(\sqrt{\lambda_1}, \dots, \sqrt{\lambda_n}) U^*.$$
The [[formal definition|0N5GP3YT8T]] states this, and the [[proof of existence and uniqueness|MKM42YWBN6]] shows that the result does not depend on the choice of $U$.

## Motivation

A positive semidefinite matrix often plays the part of a squared quantity.
A covariance matrix is a matrix of squared spreads, the matrix $M^* M$ measures squared lengths of the vectors $Mx$, and a positive definite matrix defines an inner product $\langle x, y \rangle_A = x^* A y$.
Taking the square root brings us back to the first power.
The root of $M^* M$ is the length factor in the [[polar decomposition|0J2C7BDJQA]] $M = W \lvert M \rvert$, and its eigenvalues are the [[singular values|09VMDSRXWJ]] of $M$.
The root of an inner product matrix turns $\langle x, y \rangle_A$ into the ordinary inner product of $A^{1/2} x$ and $A^{1/2} y$.
Numerical methods such as the [[unscented Kalman filter|AYW3HY3PZP]] use the root of a covariance matrix to place sample points.

## Notation

The root is written $A^{1/2}$ or $\sqrt{A}$, and for $M^* M$ also $\lvert M \rvert$.
For a real symmetric matrix the root is real, and $U^*$ is the transpose $U^{\mathsf{T}}$.
Some texts call any matrix $B$ with $B^* B = A$ a square root of $A$, for example the triangular factor of the [[Cholesky decomposition|0WKG8CYY6A]].
Here the square root of a positive semidefinite matrix always means the positive semidefinite $B$ with $B^2 = A$.

## Remarks

### A first computation

Take
$$A = \begin{pmatrix} 10 & 6 \\ 6 & 10 \end{pmatrix}.$$
Its characteristic polynomial is $(10 - t)^2 - 36 = (t - 16)(t - 4)$, so the eigenvalues are $16$ and $4$, with the unit eigenvectors $u_1 = \tfrac{1}{\sqrt{2}}(1, 1)$ and $u_2 = \tfrac{1}{\sqrt{2}}(1, -1)$.
With the projections $P_1 = u_1 u_1^{\mathsf{T}}$ and $P_2 = u_2 u_2^{\mathsf{T}}$ we have $A = 16 P_1 + 4 P_2$, and the root replaces $16$ by $4$ and $4$ by $2$:
$$A^{1/2} = 4 P_1 + 2 P_2 = \frac{4}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} + \frac{2}{2} \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}.$$
Check: $\begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}^2 = \begin{pmatrix} 9 + 1 & 3 + 3 \\ 3 + 3 & 1 + 9 \end{pmatrix} = A$, and the root is symmetric with the eigenvalues $4$ and $2$, so it is positive semidefinite.
The [[worked 2 by 2 example|QTV6Y0710E]] does the same for another matrix and also lists the roots that are not positive semidefinite.

### The root is a polynomial in A

Choose a polynomial $p$ with $p(\lambda) = \sqrt{\lambda}$ at each eigenvalue $\lambda$ of $A$.
Then $p(A) = U \operatorname{diag}(p(\lambda_1), \dots, p(\lambda_n)) U^* = A^{1/2}$.
For the matrix above we need $p(16) = 4$ and $p(4) = 2$, and the line $p(t) = \tfrac{t + 8}{6}$ does this.
Check: $p(A) = \tfrac{1}{6}(A + 8I) = \tfrac{1}{6} \begin{pmatrix} 18 & 6 \\ 6 & 18 \end{pmatrix} = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$.
So $A^{1/2}$ commutes with every matrix that commutes with $A$.

### Why there is only one

Let $B$ be positive semidefinite with $B^2 = A$.
Then $B$ commutes with $B^2 = A$, so $B$ maps each eigenspace of $A$ into itself.
On the eigenspace for $\lambda$, the matrix $B$ is still Hermitian with nonnegative eigenvalues, and its square is $\lambda$ times the identity.
So each eigenvalue $\mu$ of $B$ there has $\mu^2 = \lambda$ and $\mu \ge 0$, which gives $\mu = \sqrt{\lambda}$, and a Hermitian map with the single eigenvalue $\sqrt{\lambda}$ is $\sqrt{\lambda}$ times the identity.
Hence $B$ acts as $\sqrt{\lambda}$ on each eigenspace, so $B = A^{1/2}$.

### What the root keeps

The root has the same eigenvectors as $A$, the same null space and the same rank, since $\sqrt{\lambda} = 0$ exactly when $\lambda = 0$.
So $A^{1/2}$ is positive definite exactly when $A$ is.
For example, $A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ has the eigenvalues $2$ and $0$, and since $A^2 = 2A$ its root is $\tfrac{1}{\sqrt{2}} A$, again of rank $1$ with the null space spanned by $(1, -1)$.

### What it is not

A matrix can have many square roots, and the positive semidefinite condition picks one.
The identity $I_2$ has the root $I_2$, but every reflection $\begin{pmatrix} \cos\varphi & \sin\varphi \\ \sin\varphi & -\cos\varphi \end{pmatrix}$ also squares to $I_2$, and these reflections are symmetric with the eigenvalues $1$ and $-1$.
Outside the positive semidefinite matrices a root need not exist at all: if $B^2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, then $B$ is nilpotent, so $B^2 = 0$ for a $2 \times 2$ matrix, which is false.

### Watch out

The root is not taken entry by entry.
For $A = \begin{pmatrix} 10 & 6 \\ 6 & 10 \end{pmatrix}$, the entrywise roots give a matrix whose top left entry squares to $10 + 6 = 16$, not $10$.
Also, $(AB)^{1/2} = A^{1/2} B^{1/2}$ can fail when $A$ and $B$ do not commute, because then $AB$ need not even be Hermitian.

### Try it

First, find the root of $\operatorname{diag}(9, 0, 4)$.
It is $\operatorname{diag}(3, 0, 2)$, since a diagonal matrix with nonnegative entries is already in the form $U \operatorname{diag}(\lambda_i) U^*$ with $U = I$.

Second, find the root of $A = \begin{pmatrix} 5 & 3 \\ 3 & 5 \end{pmatrix}$.
The eigenvalues are $8$ and $2$, and $A^{1/2} = \sqrt{8} P_1 + \sqrt{2} P_2 = \tfrac{1}{\sqrt{2}} \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$, whose square is $\tfrac{1}{2} \begin{pmatrix} 10 & 6 \\ 6 & 10 \end{pmatrix} = A$.

## Explanations

### L1 human

The number $9$ has two square roots, $3$ and $-3$, and we usually mean the positive one.
Some matrices behave like nonnegative numbers: they stretch space along perpendicular directions by nonnegative factors.
For such a matrix, stretch along the same directions by the square root of each factor.
Doing this twice gives back the original stretch, and no other matrix of the same kind does that.
So these matrices, like nonnegative numbers, have exactly one square root of their own kind.

### L2 human

Here is a typical problem: find a formula for the root of a $2 \times 2$ positive semidefinite matrix $A \ne 0$ without computing eigenvectors.
Let $B = A^{1/2}$, with $\det B = \sqrt{\det A}$ and trace $\tau = \operatorname{tr} B > 0$.
The Cayley-Hamilton theorem for $B$ gives $B^2 - \tau B + (\det B) I = 0$, so
$$\tau B = A + \sqrt{\det A} \, I.$$
Taking the trace of $B^2 = A$ in the form $\tau^2 = \operatorname{tr}(B^2) + 2 \det B$ gives $\tau = \sqrt{\operatorname{tr} A + 2\sqrt{\det A}}$.
For $A = \begin{pmatrix} 10 & 6 \\ 6 & 10 \end{pmatrix}$ we get $\det A = 64$ and $\tau = \sqrt{20 + 16} = 6$, so $B = \tfrac{1}{6}(A + 8I) = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$, as before.
This is the typical use of the root at this level: a closed formula for small matrices, checked by squaring.

### L3 human

The construction is the continuous functional calculus for the function $t \mapsto \sqrt{t}$ on the spectrum of $A$, and the [[square root of a positive operator|3JY5HNFRMF]] carries it to bounded operators on a Hilbert space.
The map $A \mapsto A^{1/2}$ is continuous on the positive semidefinite cone, and it is monotone for the [[Loewner order|9G9S92T1VJ]]: $0 \le A \le B$ implies $A^{1/2} \le B^{1/2}$, although the square map $A \mapsto A^2$ is not monotone.
The root of $M^* M$ gives the polar decomposition and the singular value decomposition, and the inverse root $A^{-1/2}$ of a positive definite covariance matrix is the whitening transform of statistics.
In numerical practice the root is computed from an eigendecomposition or by Newton-type iterations, while the Cholesky factor is cheaper when any factor $B$ with $B^* B = A$ will do.
