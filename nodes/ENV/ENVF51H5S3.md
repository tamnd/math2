---
tag: ENVF51H5S3
kind: statement
role: theorem
name: Block triangular form for an invariant subspace
msc: ["15A04", "15A21"]
topics: [Z6S6PWMJPH]
audience: ug1
about: [0KN7EPH7Z0, 0ACX5QT8TE]
uses: [0PFPWKBDTJ, 0YYMY95FWS, 0BZ81AJNWF, 0SVR29SV1V]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_subspace
    locator: For a single operator
  - book: isbn:9780135367971
    locator: Section 6.4
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Statement

An invariant subspace makes the matrix block upper triangular, and the characteristic polynomial then splits into the parts that belong to the subspace and to the quotient.
Let $F$ be a field, let $V$ be a vector space over $F$ of finite dimension $n$, and let $T \colon V \to V$ be linear.
Let $U$ be a $T$-[[invariant subspace|0ACX5QT8TE]] of dimension $k$.
Let $u_1, \dots, u_k$ be a basis of $U$, and let $\mathcal{B} = (u_1, \dots, u_k, v_{k+1}, \dots, v_n)$ be a basis of $V$.

1. The [[matrix|0YQSGNYE3K]] of $T$ in $\mathcal{B}$ has the block form
$$[T]_{\mathcal{B}} = \begin{pmatrix} A & B \\ 0 & C \end{pmatrix},$$
   where $A$ is the $k \times k$ matrix of the [[restriction|0KN7EPH7Z0]] $T|_U$ in the basis $u_1, \dots, u_k$, and $C$ is the $(n - k) \times (n - k)$ matrix of the quotient operator $\bar T$ in the basis $v_{k+1} + U, \dots, v_n + U$.
2. The [[characteristic polynomials|0J5EMJRRFM]] satisfy
$$p_T = p_{T|_U} \cdot p_{\bar T}.$$

Here the characteristic polynomial of an endomorphism of the zero space is $1$.

## Remarks

### Why each hypothesis is needed

Invariance is what puts the zero block in place.
For $T(x, y) = (x, x + y)$ and $U = \R e_1$, the matrix in the basis $e_1, e_2$ is $\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, and the [[subspace is not invariant|B448MTVVJW]], so $T|_U$ and $\bar T$ do not even exist.

The basis must start with a basis of $U$.
For the invariant line $U = \R e_1$ of $\begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$, the reversed basis $e_2, e_1$ gives $\begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}$, with the zero in the upper right corner.

Finite dimension is needed for part 2, because the characteristic polynomial is defined only there.

### What it gives you

The characteristic polynomials of $T|_U$ and of $\bar T$ both divide $p_T$.
So the [[eigenvalues|0BQAA2BK3Q]] of $T$, with their algebraic multiplicities, are those of $T|_U$ together with those of $\bar T$.
Comparing coefficients of the two sides of part 2 gives $\det T = \det(T|_U) \det \bar T$ and $\operatorname{tr} T = \operatorname{tr}(T|_U) + \operatorname{tr} \bar T$.

The rule also computes characteristic polynomials cheaply.
For the matrix $\begin{pmatrix} 1 & 2 & 5 \\ 2 & 1 & 7 \\ 0 & 0 & 4 \end{pmatrix}$ and the plane $z = 0$, the blocks give $(t^2 - 2t - 3)(t - 4) = (t - 3)(t + 1)(t - 4)$, as the [[worked example|D59VWM8NX7]] shows.

For a chain $0 = U_0 \subset U_1 \subset \cdots \subset U_r = V$ of invariant subspaces, applying part 1 again and again gives a block upper triangular matrix whose diagonal blocks are the quotient operators on the $U_i / U_{i-1}$.
When every step has dimension $1$, the matrix is upper triangular, which is the idea of [[triangularization|0363JMQ42Y]].

### The converse

The converse of part 1 holds.
If the matrix of $T$ in a basis $u_1, \dots, u_k, v_{k+1}, \dots, v_n$ has a zero lower left block, then each $T(u_i)$ is a combination of $u_1, \dots, u_k$, so $\operatorname{span}(u_1, \dots, u_k)$ is invariant.

For part 2 one may ask whether every monic factor $f$ of $p_T$ is $p_{T|_U}$ for some invariant $U$.
Over $\C$ the answer is yes: triangularize $T$ with the roots of $f$ placed first on the diagonal, and take for $U$ the span of the first $\deg f$ basis vectors.

### Generalizations

If $V = U \oplus W$ with both summands invariant, then $B = 0$, the matrix is block diagonal, and $T|_W$ is a model of $\bar T$.
The same block form holds for free modules of finite rank over a commutative ring, when $U$ is a direct summand that is free.

## Explanations

### L1 human

Choose coordinates in which the first few directions span the invariant subspace.
Then the matrix of the map has a block of zeros in the lower left corner.
The upper left block describes the map inside the subspace.
The lower right block describes the map on what is left.
The stretch factors of the whole map are the stretch factors of these two blocks.

### L2 human

Here is a typical use: find the characteristic polynomial of $T(x, y, z) = (2x + y + z, \; 3y + 4z, \; 5z)$ on $\R^3$.
The line $U = \R e_1$ is invariant, since $T(e_1) = (2, 0, 0)$.
In the basis $e_1, e_2, e_3$ the matrix is
$$\begin{pmatrix} 2 & 1 & 1 \\ 0 & 3 & 4 \\ 0 & 0 & 5 \end{pmatrix},$$
so $A = (2)$ and $C = \begin{pmatrix} 3 & 4 \\ 0 & 5 \end{pmatrix}$.
Part 2 gives $p_T(t) = (t - 2) \cdot (t - 3)(t - 5)$.
The plane $\operatorname{span}(e_1, e_2)$ is also invariant, and the same rule with $k = 2$ splits off the factor $t - 5$ from the quotient.
Watch out: an eigenvector of $C$ is only an eigenvector of $\bar T$, and it need not give an eigenvector of $T$ in the same coset.

### L3 human

The statement says that the characteristic polynomial is multiplicative on short exact sequences $0 \to U \to V \to V / U \to 0$ of $F[x]$-modules.
Along a composition series, $p_T$ is the product over the simple factors, and a simple factor $F[x] / (q)$ with $q$ irreducible contributes $q$.
Each such factor is a subquotient of $V$, so $q$ divides the [[minimal polynomial|03NDVCSHSB]], and this gives one proof that $p_T$ and $m_T$ have the same irreducible factors.
