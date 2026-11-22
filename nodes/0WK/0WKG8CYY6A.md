---
tag: 0WKG8CYY6A
kind: statement
role: theorem
name: Cholesky decomposition
msc: [15A23, 65F05]
topics: [SS4EVPKT3A]
audience: ug1
about: [0KX66CZMBB, 00J3KZP8Y0]
uses: [0QQCG3JWJ4, 0EZSD6T9E0, 0EKZCX4K3P, 0EX045E2BP]
proofs: [NRPFJZNDZ6]
sources:
  - url: https://en.wikipedia.org/wiki/Cholesky_decomposition
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Cholesky decomposition
  - book: isbn:9780521839402
    locator: Chapter 7
same_as:
  wikidata: Q515375
  wikipedia: Cholesky decomposition
---

## Statement

The Cholesky decomposition writes a positive definite matrix as a lower triangular matrix times its own conjugate transpose, and it does so in exactly one way.
Let $A$ be an $n \times n$ complex [[Hermitian matrix|0P17NGQQMQ]], and write $L^*$ for the [[conjugate transpose|0EX045E2BP]] of a matrix $L$.

1. Existence and uniqueness. If $A$ is [[positive definite|0KX66CZMBB]], then there is exactly one [[lower triangular matrix|00J3KZP8Y0]] $L$ with real positive diagonal entries such that $A = L L^*$.
2. Converse. If $A = L L^*$ for some lower triangular matrix $L$ with real positive diagonal entries, then $A$ is positive definite.
3. Real case. If $A$ is real and positive definite, then the matrix $L$ of part 1 is real, and $A = L L^{\mathsf{T}}$.

The matrix $L$ is the *Cholesky factor* of $A$.
The [[proof by induction on the size|NRPFJZNDZ6]] proves all three parts.

## Remarks

### A first factorization

Take $A = \begin{pmatrix} 4 & 2 \\ 2 & 5 \end{pmatrix}$ and look for $L = \begin{pmatrix} a & 0 \\ b & c \end{pmatrix}$ with $a, c > 0$.
Multiply out:
$$L L^{\mathsf{T}} = \begin{pmatrix} a & 0 \\ b & c \end{pmatrix} \begin{pmatrix} a & b \\ 0 & c \end{pmatrix} = \begin{pmatrix} a^2 & ab \\ ab & b^2 + c^2 \end{pmatrix}.$$
Now match the entries with $A$ one at a time.
The corner gives $a^2 = 4$, so $a = 2$.
Then $ab = 2$ gives $b = 1$, and $b^2 + c^2 = 5$ gives $c^2 = 4$, so $c = 2$.
Check: $\begin{pmatrix} 2 & 0 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 4 & 2 \\ 2 & 1 + 4 \end{pmatrix} = A$.
At each step the positive diagonal left only one choice, and that is the uniqueness of part 1 in miniature.
[[The 3 by 3 example|M3YVJ6CFJ5]] runs the same steps on three columns.

### The algorithm, column by column

The same matching works for every size.
Column $j$ of $L$ comes from column $j$ of $A$ and the columns of $L$ already found:
$$l_{jj} = \sqrt{a_{jj} - \sum_{k < j} \abs{l_{jk}}^2}, \qquad l_{ij} = \frac{1}{l_{jj}} \Big( a_{ij} - \sum_{k < j} l_{ik} \overline{l_{jk}} \Big) \quad (i > j).$$
The number under each square root equals $\Delta_j / \Delta_{j-1}$, the ratio of two leading principal minors, with $\Delta_0 = 1$.
So it is positive at every step exactly when $A$ is positive definite, by [[Sylvester's criterion|0WKEF78PMV]].
This makes the algorithm a practical test: run it, and if a number under a square root is zero or negative, the matrix is not positive definite.
Once $L$ is known, a system $Ax = b$ splits into two triangular systems, $Ly = b$ by forward substitution and $L^* x = y$ by back substitution.
The work is about half the work of an [[LU decomposition|0RKG5YW66Y]], because the symmetry of $A$ is used.

### Why positive definite is needed

If $L$ has a positive diagonal, then $L$ is invertible, and part 2 makes $L L^*$ positive definite.
So a matrix that is only [[semidefinite|01MMVW8CKC]] has no factor with a positive diagonal.
For [[the all-ones matrix|YAAQD2E1BZ]] this is visible at once: $\det A = 0$, while $\det (L L^*) = \abs{\det L}^2 = (l_{11} l_{22})^2 > 0$.

If we allow a nonnegative diagonal, semidefinite matrices do have factors, but uniqueness is lost.
For $A = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$, the matrix $L = \begin{pmatrix} 0 & 0 \\ a & b \end{pmatrix}$ gives
$$L L^{\mathsf{T}} = \begin{pmatrix} 0 & 0 \\ 0 & a^2 + b^2 \end{pmatrix},$$
so every pair with $a^2 + b^2 = 1$ and $b \ge 0$ works.
Both $\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ are lower triangular factors with nonnegative diagonal.

The positive diagonal is what makes the factor unique.
For every diagonal $D$ with entries of modulus $1$ we have $(LD)(LD)^* = L D D^* L^* = L L^*$, and the condition $l_{jj} > 0$ removes exactly this freedom.

### Links with LU and with Gram-Schmidt

Let $D$ be the diagonal of $L$.
Then $A = (L D^{-1})(D L^*)$, where $L D^{-1}$ is lower triangular with ones on the diagonal and $D L^*$ is upper triangular.
This is the LU decomposition of $A$, found without row exchanges, and its pivots are the squares $l_{jj}^2$.
For the first factorization above, $D = \operatorname{diag}(2, 2)$ and
$$A = \begin{pmatrix} 1 & 0 \\ \tfrac12 & 1 \end{pmatrix} \begin{pmatrix} 4 & 2 \\ 0 & 4 \end{pmatrix}.$$
Check: the bottom right entry of the product is $\tfrac12 \cdot 2 + 4 = 5$.
The form $A = (L D^{-1}) D^2 (L D^{-1})^*$ is the $LDL^*$ decomposition, and it needs no square roots.

The [[Gram-Schmidt process|0VT6P0GNQR]] gives the same triangle from another side.
If a matrix $B$ has independent columns and $B = QR$ is its [[QR decomposition|0ERWG4NXQ9]] with a positive diagonal in $R$, then $B^* B = R^* Q^* Q R = R^* R$.
So $R^*$ is the Cholesky factor of the Gram matrix $B^* B$.
For the columns $(1, 2, 2)$ and $(3, 0, 3)$, Gram-Schmidt finds $R = \begin{pmatrix} 3 & 3 \\ 0 & 3 \end{pmatrix}$, and $B^{\mathsf{T}} B = \begin{pmatrix} 9 & 9 \\ 9 & 18 \end{pmatrix}$ has the Cholesky factor $\begin{pmatrix} 3 & 0 \\ 3 & 3 \end{pmatrix} = R^{\mathsf{T}}$.

### Watch out

The formulas read only the entries on and below the diagonal, so they never notice a matrix that is not symmetric.
For $A = \begin{pmatrix} 1 & 5 \\ 1 & 2 \end{pmatrix}$ they return $L = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, but $L L^{\mathsf{T}} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \ne A$.
Check that $A$ is Hermitian before you factor it.
Positive entries are not enough either.
For $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ the algorithm gives $l_{11} = 1$ and $l_{21} = 2$, and then it needs $\sqrt{1 - 4}$, so it stops, and the matrix is not positive definite, as [[the example with positive entries|N9TX4J2W4R]] confirms.

### Try it

First, factor $\begin{pmatrix} 9 & 3 \\ 3 & 5 \end{pmatrix}$.
You get $l_{11} = 3$, $l_{21} = 1$ and $l_{22} = \sqrt{5 - 1} = 2$, and indeed $\begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 9 & 3 \\ 3 & 5 \end{pmatrix}$.

Second, for which real $t$ does $\begin{pmatrix} 1 & t \\ t & 1 \end{pmatrix}$ have a Cholesky factor?
The algorithm gives $l_{11} = 1$, $l_{21} = t$ and $l_{22}^2 = 1 - t^2$, so it succeeds exactly when $\abs{t} < 1$.

## History

André-Louis Cholesky devised the method for real symmetric matrices.
It was published after his death, in 1924.

## Explanations

### L1 human

A positive number is the square of its positive square root.
A positive definite matrix is, in the same way, a "square" $L L^{\mathsf{T}}$ of a triangular matrix $L$ with a positive diagonal.
For example, $\begin{pmatrix} 4 & 2 \\ 2 & 5 \end{pmatrix}$ equals $\begin{pmatrix} 2 & 0 \\ 1 & 2 \end{pmatrix}$ times its transpose.
You find the entries of $L$ one at a time, from the top left corner, with one square root for each diagonal entry.
If a square root of a negative number turns up, the matrix was not positive definite.

### L2 human

Here is a typical use: solve $Ax = b$ for $A = \begin{pmatrix} 4 & 2 \\ 2 & 5 \end{pmatrix}$ and $b = (8, 12)$.
The first factorization gives $L = \begin{pmatrix} 2 & 0 \\ 1 & 2 \end{pmatrix}$.
First solve $Ly = b$ from the top:
$$2 y_1 = 8, \qquad y_1 + 2 y_2 = 12, \qquad \text{so } y = (4, 4).$$
Then solve $L^{\mathsf{T}} x = y$ from the bottom:
$$2 x_2 = 4, \qquad 2 x_1 + x_2 = 4, \qquad \text{so } x = (1, 2).$$
Check: $A(1, 2) = (4 + 4, 2 + 10) = (8, 12)$.
Each triangular system costs little, and the factor can be used again for many right sides, which is why Cholesky is the standard solver for symmetric positive definite systems such as the [[normal equations|4D7MRG4D91]].
The trap is to run the algorithm on a matrix that is not symmetric, where it returns a factor of a different matrix.

### L3 human

The group $GL_n(\C)$ acts on the positive definite matrices by $A \mapsto T A T^*$, and the orbit of $I$ is the whole set.
The Cholesky decomposition says more: the subgroup of lower triangular matrices with positive diagonal already acts simply transitively, since $L$ is the unique such matrix that moves $I$ to $A$.
Seen from the columns of a matrix $B$, Cholesky on $B^* B$ and Gram-Schmidt on $B$ compute the same triangular matrix, which links the factorization to orthogonality.
The [[simultaneous diagonalization with a positive definite matrix|K559AQ9H67]] uses the Cholesky factor to turn one form into the identity.
In numerical linear algebra the algorithm is backward stable without pivoting, a topic of that area.
