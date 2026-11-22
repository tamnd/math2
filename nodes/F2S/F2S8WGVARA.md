---
tag: F2S8WGVARA
kind: statement
role: theorem
name: Eigenvalues of a polynomial in an endomorphism
aliases: [spectral-mapping-for-polynomials-in-linear-algebra, eigenvalues-of-p-t]
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
about: [0E3MV6E6MG, 0BQAA2BK3Q]
uses: [0BNEXSKNRV, 0ZND7NQ970]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Additional properties
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Statement

A polynomial in $T$ has the polynomial of each eigenvalue of $T$ as an eigenvalue, and over an algebraically closed field it has no others.

Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be a linear map.
Write $\sigma(T)$ for the set of [[eigenvalues|0BQAA2BK3Q]] of $T$ in $F$, and let $p \in F[x]$, with $p(T)$ the [[value of p at T|0BNEXSKNRV]].

1. If $Tv = \lambda v$ with $v \ne 0$, then $p(T)v = p(\lambda)v$.
   So $p(\lambda)$ is an eigenvalue of $p(T)$, and
$$p(\sigma(T)) \subseteq \sigma(p(T)).$$
2. If $F$ is algebraically closed and $V$ is finite-dimensional, then
$$\sigma(p(T)) = p(\sigma(T)) = \{ p(\lambda) : \lambda \in \sigma(T) \}.$$
3. If $T$ is invertible, then $0 \notin \sigma(T)$, and $\lambda \in \sigma(T)$ if and only if $1/\lambda \in \sigma(T^{-1})$.
   The eigenvectors of $T$ for $\lambda$ are the eigenvectors of $T^{-1}$ for $1/\lambda$.

The same holds for an $n \times n$ matrix $A$, with $p(A)$ in place of $p(T)$.

## Remarks

### A first check

Take $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, with $\sigma(A) = \{1, 3\}$ and the eigenvectors $(1, -1)^{\mathsf{T}}$ and $(1, 1)^{\mathsf{T}}$, and take $p(x) = x^2 + 1$.
Part 2 predicts $\sigma(p(A)) = \{p(1), p(3)\} = \{2, 10\}$.
Compute directly:
$$A^2 = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}, \qquad p(A) = A^2 + I = \begin{pmatrix} 6 & 4 \\ 4 & 6 \end{pmatrix}.$$
Check: $p(A)(1, 1)^{\mathsf{T}} = (10, 10)^{\mathsf{T}}$ and $p(A)(1, -1)^{\mathsf{T}} = (2, -2)^{\mathsf{T}}$.
The [[proof by factoring p(x) minus mu|AQF42QX6HM]] gives all three parts.

### Why each hypothesis is needed

Part 2 needs an algebraically closed field.
Over $\mathbb{R}$, the rotation $T = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has no eigenvalue, so $p(\sigma(T)) = \emptyset$ for $p(x) = x^2$.
But $p(T) = T^2 = -I$ has the eigenvalue $-1$, so $\sigma(p(T)) = \{-1\}$.
Over $\mathbb{C}$ the gap closes: $\sigma(T) = \{i, -i\}$, and both values square to $-1$.

Part 2 needs finite dimension.
The [[right shift|HBVWZ0FXWC]] on complex sequences has no eigenvalue, so $p(\sigma(T)) = \emptyset$ for every $p$.
For a constant polynomial $p = c$, however, $p(T) = cI$ has the eigenvalue $c$.

Part 3 needs $T$ to be invertible, so that $T^{-1}$ exists at all.

### What it gives you

If $T^k = 0$ for some $k \ge 1$, then every eigenvalue satisfies $\lambda^k = 0$, because $0 = T^k v = \lambda^k v$ for an eigenvector $v$.
So a nilpotent map has no eigenvalue other than $0$.
If $T^2 = T$, then $\lambda^2 = \lambda$, so a projection has only the eigenvalues $0$ and $1$.
In general, if $q(T) = 0$, then $q(\lambda) = 0$ for every eigenvalue $\lambda$, which is one half of the theorem that the [[eigenvalues are the roots of the minimal polynomial|0QF4ZEFG52]].
Over $\mathbb{C}$, the eigenvalues of $A^k$ are the $k$-th powers of the eigenvalues of $A$, and the eigenvalues of $A + cI$ are those of $A$ shifted by $c$.

### The converse

An eigenvector of $p(T)$ need not be an eigenvector of $T$.
For the real rotation above, $p(T) = -I$ has every nonzero vector as an eigenvector, but $T$ has none.
The same happens over $\mathbb{C}$ whenever $p$ takes the same value at two eigenvalues: for $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $p(x) = x^2 - 4x$, both $1$ and $3$ go to $-3$, and $p(A) = -3I$.

### Generalizations

Multiplicities follow the same rule.
Over an algebraically closed field, if $p_T(t) = \prod_i (t - \lambda_i)$, then the characteristic polynomial of $p(T)$ is $\prod_i (t - p(\lambda_i))$.
The reason is [[triangularization|0363JMQ42Y]]: $p$ of a triangular matrix is triangular with the diagonal entries $p(\lambda_i)$.
In a complex Banach algebra, the [[spectral mapping theorem for polynomials|Q71WX8HFYT]] says $\sigma(p(a)) = p(\sigma(a))$ for the spectrum in place of the set of eigenvalues.

## History

The finite-dimensional statement belongs to the basic theory of eigenvalues and appears in the standard textbooks of linear algebra.
Its form for the spectrum in Banach algebras is part of the spectral theory of the twentieth century.

## Explanations

### L1 human

If $v$ is a direction that $T$ stretches by $\lambda$, then $T^2$ stretches it by $\lambda^2$, $T^3$ by $\lambda^3$, and so on.
So a polynomial in $T$ stretches $v$ by the same polynomial of $\lambda$.
For a stretch factor $3$ and $p(x) = x^2 + 1$, the new factor is $10$.
Over the complex numbers these new factors are all the stretch factors that $p(T)$ has.

### L2 human

Here is a typical use: find the eigenvalues of $B = A^3 - 2A$ for the triangular matrix $A = \begin{pmatrix} 1 & 5 \\ 0 & 2 \end{pmatrix}$.
The eigenvalues of $A$ are its diagonal entries $1$ and $2$.
By part 2 with $p(x) = x^3 - 2x$, the eigenvalues of $B$ are
$$p(1) = 1 - 2 = -1, \qquad p(2) = 8 - 4 = 4.$$
Check: $B$ is upper triangular because $A$ is, and its diagonal entries are $1^3 - 2 \cdot 1 = -1$ and $2^3 - 2 \cdot 2 = 4$.
The inverse needs no new work either: by part 3, $A^{-1}$ has the eigenvalues $1$ and $\tfrac{1}{2}$.
Watch out: the eigenvalues of $A + B$ or $AB$ for two different matrices are not given by this rule, because $B$ is not a polynomial in $A$ in general.

### L3 human

Part 2 is the polynomial case of the holomorphic functional calculus, where $\sigma(f(T)) = f(\sigma(T))$ for $f$ holomorphic near $\sigma(T)$.
Over a field that is not algebraically closed, the right statement uses the eigenvalues in an algebraic closure, that is, the roots of the characteristic polynomial.
Part 3 fits the same picture, since in finite dimension $T^{-1}$ is itself a polynomial in $T$, by the [[Cayley-Hamilton theorem|0F765KFC2J]].
