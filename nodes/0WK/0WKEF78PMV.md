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

Let $A$ be an $n \times n$ complex [[Hermitian matrix|0P17NGQQMQ]].
For $1 \le k \le n$, let $\Delta_k$ be the determinant of the upper left $k \times k$ submatrix of $A$.
For a nonempty set $S \subseteq \set{1, \dots, n}$, let $A_S = (a_{ij})_{i, j \in S}$ be the principal submatrix on the rows and columns in $S$.

1. $A$ is [[positive definite|0KX66CZMBB]] if and only if $\Delta_k > 0$ for all $k = 1, \dots, n$.
2. $A$ is [[positive semidefinite|01MMVW8CKC]] if and only if $\det A_S \ge 0$ for every nonempty $S \subseteq \set{1, \dots, n}$.

## Remarks

The numbers $\Delta_k$ are the *leading principal [[minors|0BT9BYWVRY]]* of $A$.
The numbers $\det A_S$ are the *principal minors*; there are $2^n - 1$ of them.
For a real $\begin{pmatrix} a & b \\ b & c \end{pmatrix}$, part 1 is the test $a > 0$ and $ac - b^2 > 0$.

### Why each hypothesis is needed

- $A$ must be Hermitian. [[The matrix $\begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix}$|~23bc28ba]] has $\Delta_1 = \Delta_2 = 1$, but $x^T M x = -1$ at $x = (1, 1)$.
- In part 2, the leading minors are not enough. [[The matrix $\begin{pmatrix} 0 & 0 \\ 0 & -1 \end{pmatrix}$|~ce5f5d94]] has $\Delta_1 = \Delta_2 = 0 \ge 0$, but it is not positive semidefinite. Its principal minor $a_{22} = -1$ is negative.
- In part 1, the strict inequalities are needed. The [[all-ones matrix|~811342c5]] has $\Delta_1 = 1$ and $\Delta_2 = 0$, and it is not positive definite.

### Consequences

- A positive definite matrix has positive diagonal entries and a positive determinant.
- [[The tridiagonal $3 \times 3$ example|~0bee96cf]] is positive definite, since its leading minors are $2, 3, 4$.
- $A$ is negative definite if and only if $-A$ is positive definite, that is, if and only if $(-1)^k \Delta_k > 0$ for all $k$.
- In the proof, $\Delta_k / \Delta_{k-1}$ is the $k$-th pivot of Gaussian elimination without row exchanges. So a positive definite matrix has positive pivots, which links the test to the [[Cholesky decomposition|0WKG8CYY6A]].

### Converse

Both parts are equivalences.
The criterion uses any nested chain of principal submatrices, not only the upper left ones, because a simultaneous permutation of rows and columns keeps positive definiteness.

### Generalizations

- For a real symmetric matrix, the same tests hold with real vectors, since the real and the complex definitions agree.
- For quadratic forms, the test classifies [[positive definite quadratic forms|0RP20HFYM3]], which are treated with quadratic forms.

## History

The criterion is named after James Joseph Sylvester, according to the Wikipedia article on Sylvester's criterion.

## Explanations

### L1 human

Sylvester's criterion tests positive definiteness with $n$ determinants.
We check the top left $1 \times 1$, $2 \times 2$, and so on, up to the full matrix.
All of them must be positive.
For semidefiniteness the test is weaker in each determinant but needs more determinants.
Every square submatrix on the diagonal must have a determinant at least $0$.

### L2 human

Recipe for positive definiteness:

1. Check that $A$ is Hermitian (real symmetric in the real case).
2. Compute $\Delta_1 = a_{11}$, then $\Delta_2$, and so on.
3. Stop at the first $\Delta_k \le 0$: then $A$ is not positive definite.

[[The tridiagonal example|~0bee96cf]] runs this recipe on a $3 \times 3$ matrix.
A trap: the recipe for positive definiteness uses strict inequalities, and replacing them by "$\ge 0$" does not give a test for semidefiniteness.

### L3 human

Part 1 follows from the factorization $A = L D L^*$ with $L$ unit lower triangular and $D$ diagonal, which exists when all $\Delta_k \ne 0$.
The diagonal of $D$ is $\Delta_1, \Delta_2 / \Delta_1, \dots, \Delta_n / \Delta_{n-1}$, and Sylvester's law of inertia counts the signs.
Part 2 needs all principal minors because the semidefinite cone is not open: a zero leading minor carries no information about the rest of the matrix.
The coefficients of the characteristic polynomial of $A$ are, up to sign, the sums of the principal minors of each size, and this is the tool of the proof of part 2.
