---
tag: 0WKEF78PMV
kind: statement
role: theorem
name: Sylvester's criterion
msc: [15B57, 15A15]
topics: [SS4EVPKT3A]
audience: ug1
about: [0KX66CZMBB, 01MMVW8CKC]
uses: [0QQCG3JWJ4, 0880F9EQCP, 0SD528P0EK, 0EKZCX4K3P]
proofs: [5BZ123RQNH]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester's_criterion
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Sylvester's_criterion
    locator: Proof for the case of positive semidefinite matrices
  - book: isbn:9780521839402
    locator: Chapter 7
same_as:
  wikidata: Q2709660
  wikipedia: Sylvester's criterion
---

## Statement

Sylvester's criterion tests definiteness with determinants: the top left corners decide positive definiteness, and all the principal submatrices decide positive semidefiniteness.

Let $A$ be an $n \times n$ complex [[Hermitian matrix|0P17NGQQMQ]].
For $1 \le k \le n$, let $\Delta_k$ be the determinant of the upper left $k \times k$ submatrix of $A$.
For a nonempty set $S \subseteq \{1, \dots, n\}$, let $A_S = (a_{ij})_{i, j \in S}$ be the principal submatrix on the rows and columns in $S$.

1. $A$ is [[positive definite|0KX66CZMBB]] if and only if $\Delta_k > 0$ for all $k = 1, \dots, n$.
2. $A$ is [[positive semidefinite|01MMVW8CKC]] if and only if $\det A_S \ge 0$ for every nonempty $S \subseteq \{1, \dots, n\}$.

The same holds for a real symmetric matrix, with the real definitions.
The [[proof|5BZ123RQNH]] goes by induction for part 1 and by a perturbation $A + \varepsilon I$ for part 2.

## Remarks

### The minors involved

The numbers $\Delta_k$ are the *leading principal [[minors|0BT9BYWVRY]]* of $A$, and there are $n$ of them.
The numbers $\det A_S$ are the *principal minors*, and there are $2^n - 1$ of them, one for each nonempty $S$.
For a real $2 \times 2$ matrix $\begin{pmatrix} a & b \\ b & c \end{pmatrix}$, part 1 asks for $a > 0$ and $ac - b^2 > 0$.
Part 2 asks for $a \ge 0$, $c \ge 0$ and $ac - b^2 \ge 0$, three conditions instead of two.
For example, [[the tridiagonal 3 by 3 matrix|RSQW92W4PD]] has leading minors $2, 3, 4$, so it is positive definite.

### Why each hypothesis is needed

The matrix must be Hermitian.
[[The matrix with rows (1, -3) and (0, 1)|VB4AQ8TKVP]] has $\Delta_1 = \Delta_2 = 1$, but its form is $-1$ at $x = (1, 1)$.
For a real matrix that is not symmetric, run the test on the symmetric part $\tfrac12 (M + M^{\mathsf{T}})$ instead.

Part 1 needs strict inequalities.
[[The all-ones matrix|YAAQD2E1BZ]] has $\Delta_1 = 1$ and $\Delta_2 = 0$, and it is not positive definite.

Part 2 needs all principal minors, and the leading ones are not enough.
[[The matrix diag(0, -1)|9ZQ1GV2F0G]] has $\Delta_1 = 0$ and $\Delta_2 = 0$, both $\ge 0$, but its form is $-1$ at $(0, 1)$.
The principal minor $a_{22} = -1$ for $S = \{2\}$ shows the failure.

### What it gives you

A positive definite matrix has positive diagonal entries and a positive determinant.
A Hermitian $A$ is negative definite exactly when $-A$ is positive definite, and the leading minors of $-A$ are $(-1)^k \Delta_k$.
So $A$ is negative definite exactly when the signs of $\Delta_1, \Delta_2, \Delta_3, \dots$ alternate, starting with $\Delta_1 < 0$.

The ratios $\Delta_k / \Delta_{k-1}$, with $\Delta_0 = 1$, are the pivots of Gaussian elimination without row exchanges.
So part 1 says that a Hermitian matrix is positive definite exactly when elimination meets only positive pivots, and this links the test to the [[Cholesky decomposition|0WKG8CYY6A]].

### The converse

Both parts are equivalences.
The criterion works with any nested chain of principal submatrices, not only the upper left ones, because a simultaneous permutation of rows and columns is a change of basis $P^{\mathsf{T}} A P$ and keeps definiteness.
For example, the bottom right corners $a_{nn}$, then the last two rows and columns, and so on, give a second valid test for part 1.

### Generalizations

For quadratic forms over $\R$, the test classifies [[positive definite quadratic forms|0RP20HFYM3]], since the form $x^{\mathsf{T}} A x$ with $A$ symmetric is positive definite exactly when $A$ is.
When all $\Delta_k \ne 0$, the signs of the pivots $\Delta_k / \Delta_{k-1}$ give the full signature of the form, by [[Sylvester's law of inertia|0WFED3K3DQ]].

## History

The criterion is named after James Joseph Sylvester.

## Explanations

### L1 human

Sylvester's criterion tests positive definiteness with $n$ determinants.
We check the top left $1 \times 1$ corner, then the $2 \times 2$ corner, and so on, up to the full matrix.
All of them must be positive.
For semidefiniteness we must look at more corners: every square block that sits on the diagonal must have a determinant at least $0$.

### L2 human

Here is a typical use: for which real $t$ is
$$A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & t & 1 \\ 0 & 1 & 2 \end{pmatrix}$$
positive definite?
The leading minors are $\Delta_1 = 2$, $\Delta_2 = 2t - 1$ and
$$\Delta_3 = 2(2t - 1) - 1 \cdot (2 - 0) + 0 = 4t - 4.$$
So we need $t > \tfrac12$ and $t > 1$, that is, $t > 1$.
Check: at $t = 1$ the vector $x = (1, -2, 1)$ gives $Ax = (0, 0, 0)$, so the matrix is singular there, as $\Delta_3 = 0$ says.
Watch out: replacing "$> 0$" by "$\ge 0$" in the recipe does not give a test for semidefiniteness, since that needs every principal minor.

### L3 human

Part 1 is a statement about the factorization $A = L D L^*$ with $L$ unit lower triangular and $D$ diagonal, which exists exactly when all $\Delta_k \ne 0$.
The diagonal of $D$ is $\Delta_1, \Delta_2 / \Delta_1, \dots, \Delta_n / \Delta_{n-1}$, and the law of inertia counts its signs.
Part 2 needs all principal minors because the semidefinite cone is closed but not open: a zero leading minor carries no information about the rest of the matrix.
The coefficient of $t^{n-k}$ in $\det(tI - A)$ is $(-1)^k$ times the sum of the principal minors of size $k$, and this links part 2 with the eigenvalue test.
