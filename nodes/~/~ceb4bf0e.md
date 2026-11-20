---
tag: ~ceb4bf0e
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

Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be a linear map.
Write $\sigma(T)$ for the set of [[eigenvalues|0BQAA2BK3Q]] of $T$ in $F$, and let $p \in F[x]$.

1. If $Tv = \lambda v$ with $v \ne 0$, then $p(T)v = p(\lambda)v$. So $p(\lambda)$ is an eigenvalue of $p(T)$, and
$$p(\sigma(T)) \subseteq \sigma(p(T)).$$
2. If $F$ is algebraically closed and $V$ is finite-dimensional, then
$$\sigma(p(T)) = p(\sigma(T)) = \{p(\lambda) : \lambda \in \sigma(T)\}.$$
3. If $T$ is invertible, then $0 \notin \sigma(T)$, and $\lambda \in \sigma(T)$ if and only if $1/\lambda \in \sigma(T^{-1})$. The eigenvectors of $T$ for $\lambda$ are the eigenvectors of $T^{-1}$ for $1/\lambda$.

The same holds for an $n \times n$ matrix $A$, with $p(A)$ in place of $p(T)$.

## Remarks

The proof is in [[the proof by factoring p(x) minus mu|~c6caae36]].
Here $p(T)$ is the [[value of the polynomial at the endomorphism|0BNEXSKNRV]].

### Why each hypothesis is needed

- Part 2 needs an algebraically closed field. For the rotation $T = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ over $\R$ and $p(x) = x^2$, $\sigma(T) = \emptyset$, but $p(T) = -I$ has $\sigma(p(T)) = \{-1\}$.
- Part 2 needs finite dimension for a constant $p = c$. The [[right shift|~56ecd655]] on complex sequences has no eigenvalue, so $p(\sigma(T)) = \emptyset$. But $p(T) = cI$ has the eigenvalue $c$.
- Part 3 needs $T$ invertible, so that $T^{-1}$ exists.

### Consequences

- If $T^k = 0$ for some $k \ge 1$, then every eigenvalue $\lambda$ satisfies $\lambda^k = 0$. So $\sigma(T) \subseteq \{0\}$.
- If $T^2 = T$, then every eigenvalue satisfies $\lambda^2 = \lambda$, so $\sigma(T) \subseteq \{0, 1\}$.
- More generally, if $q(T) = 0$, then $q(\lambda) = 0$ for every eigenvalue $\lambda$. This is one half of the theorem that the [[eigenvalues are the roots of the minimal polynomial|0QF4ZEFG52]].
- Over $\C$, the eigenvalues of $A^k$ are the $k$-th powers of the eigenvalues of $A$.

### Converse

The converse of part 1 fails: an eigenvector of $p(T)$ need not be an eigenvector of $T$.
For the rotation above, $p(T) = -I$ has every nonzero vector as an eigenvector, but $T$ has none over $\R$.

### Generalizations

- With algebraic multiplicities, over an algebraically closed field: if $p_T = \prod (t - \lambda_i)$, then $p_{p(T)} = \prod (t - p(\lambda_i))$. This follows from [[triangularisation|0363JMQ42Y]].
- In a complex Banach algebra, the [[spectral mapping theorem for polynomials|Q71WX8HFYT]] gives $\sigma(p(a)) = p(\sigma(a))$. This belongs to operator theory.

## History

The finite-dimensional statement is classical and appears in the standard textbooks.
Its extension to Banach algebras, the spectral mapping theorem, is part of spectral theory.

## Explanations

### L1 human

If $v$ is an eigenvector of $T$ for $\lambda$, then $v$ is also an eigenvector of $T^2$ for $\lambda^2$, of $T^3$ for $\lambda^3$, and so on.
So a polynomial in $T$ has the eigenvalue $p(\lambda)$.
Over the complex numbers, these are all the eigenvalues of $p(T)$.

### L2 human

We check part 2 for $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $p(x) = x^2 - 4x$, as in the [[worked example|~d6227a22]].

1. $\sigma(A) = \{1, 3\}$, with eigenvectors $(1, -1)^{\mathsf{T}}$ and $(1, 1)^{\mathsf{T}}$.
2. $p(1) = 1 - 4 = -3$ and $p(3) = 9 - 12 = -3$.
3. $A^2 = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}$, so $p(A) = A^2 - 4A = \begin{pmatrix} -3 & 0 \\ 0 & -3 \end{pmatrix}$.
4. So $\sigma(p(A)) = \{-3\} = p(\sigma(A))$.

The typical use is to find the eigenvalues of $A^k$, $A^{-1}$ or $A + cI$ without a new computation.
A trap: two different eigenvalues of $A$ can have the same value $p(\lambda)$, as here.

### L3 human

Part 2 is the finite-dimensional case of the holomorphic functional calculus, where $\sigma(f(T)) = f(\sigma(T))$ for $f$ holomorphic near $\sigma(T)$.
Over a field that is not algebraically closed, the right statement uses the eigenvalues in an algebraic closure.
