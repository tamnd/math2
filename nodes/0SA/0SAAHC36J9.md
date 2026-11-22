---
tag: 0SAAHC36J9
kind: definition
name: Generalized eigenvector
msc: ["15A18"]
topics: [Z6S6PWMJPH]
audience: ug2
defines: 01H6QKWGDH
uses: [0B5H4208Z9, 0BNEXSKNRV]
formal:
  - system: lean4
    library: mathlib
    decl: Module.End.genEigenspace
    match: variant
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_eigenvector
    locator: Overview and definition
  - book: isbn:9783031410253
    locator: Chapter 8
---

## Definition

A generalized eigenvector for $\lambda$ is a nonzero vector that some power of $T - \lambda \id_V$ sends to zero.
Let $F$ be a field, let $V$ be a vector space over $F$, let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]], and let $\lambda \in F$.
A *generalized eigenvector* of $T$ for $\lambda$ is a vector $v \in V$ with $v \ne 0$ and
$$(T - \lambda \id_V)^k (v) = 0$$
for some integer $k \ge 1$.
The least such $k$ is the *rank* of the generalized eigenvector.
Here $(T - \lambda \id_V)^k$ is the [[polynomial $(t - \lambda)^k$ evaluated at $T$|0BNEXSKNRV]].

## Notation

The kernel $\ker (T - \lambda \id_V)^k$ consists of $0$ and the generalized eigenvectors of rank at most $k$.
The union of these kernels over all $k$ is the [[generalized eigenspace|07PNDWA7CE]] $V_\lambda$.
The Mathlib declaration `Module.End.genEigenspace` gives the subspaces $\ker (T - \lambda \id_V)^k$, and not the vectors themselves, so the match is a variant.

## Remarks

Each condition of the definition has a reason.
The condition $v \ne 0$ is there because the zero vector satisfies the equation for every $\lambda$, and it would make every scalar look like an eigenvalue.
The exponent $k$ may depend on $v$, because different vectors need different numbers of steps.
Taking $k = 1$ gives back the [[eigenvectors|0B5H4208Z9]], so every eigenvector is a generalized eigenvector of rank $1$.

A small example: for $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $\lambda = 1$, we have
$$(A - I) e_2 = e_1 \ne 0, \qquad (A - I)^2 e_2 = (A - I) e_1 = 0.$$
So $e_2$ is a generalized eigenvector of rank $2$, and it is not an eigenvector.
A case that fails: for the same $A$ and $\lambda = 3$, the matrix $A - 3I$ is invertible, so no power of it sends a nonzero vector to $0$.

If $v$ has rank $k$, then $(T - \lambda \id_V)^{k-1} v$ is an eigenvector, so $\lambda$ is an eigenvalue.
The concept page [[generalized eigenvector|01H6QKWGDH]] has more examples and the Jordan chains.

## Explanations

### L1 human

Some matrices do not have enough eigenvectors to make a basis.
Generalized eigenvectors fill the gap.
An eigenvector reaches zero after one application of $T - \lambda \id$, and a generalized eigenvector may need several.

### L2 human

Let $J = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}$ and $\lambda = 2$.

1. The map $N = J - 2I$ sends $e_1 \mapsto 0$, $e_2 \mapsto e_1$ and $e_3 \mapsto e_2$, by reading the columns of $N$.
2. So $N e_1 = 0$, and $e_1$ has rank $1$.
3. We have $N e_2 = e_1 \ne 0$ and $N^2 e_2 = 0$, so $e_2$ has rank $2$.
4. We have $N^2 e_3 = e_1 \ne 0$ and $N^3 e_3 = 0$, so $e_3$ has rank $3$.

The typical use is to build a basis of Jordan chains.
Watch out: a test with $k = 1$ alone finds the eigenvector $e_1$ and misses $e_2$ and $e_3$.

### L3 human

The definition makes sense for a module over any commutative ring, with $\lambda$ in the ring.
In Mathlib, the subspaces $\ker (T - \lambda)^k$ form an increasing family, and their union is the maximal generalized eigenspace `Module.End.maxGenEigenspace`.
