---
tag: 0HNMFG8F8K
kind: statement
role: theorem
name: Eigenvectors with distinct eigenvalues are linearly independent
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
about: [0N6960W0BV, 0G0RFPG8HR]
uses: [0B5H4208Z9, 0EVHJFTG9Z, 0AYEPBQMAW]
formal:
  - system: lean4
    library: mathlib
    decl: Module.End.eigenvectors_linearIndependent
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenspaces, geometric multiplicity, and the eigenbasis
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Statement

Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be a linear map.

1. Let $v_1, \dots, v_k$ be [[eigenvectors|0N6960W0BV]] of $T$ for eigenvalues $\lambda_1, \dots, \lambda_k$ that are pairwise distinct. Then $v_1, \dots, v_k$ are [[linearly independent|0CRMGPAH83]].
2. For pairwise distinct scalars $\lambda_1, \dots, \lambda_k$, the sum $E_{\lambda_1} + \cdots + E_{\lambda_k}$ of the [[eigenspaces|0G0RFPG8HR]] is a direct sum.
3. If $\dim V = n$ is finite, then $T$ has at most $n$ distinct eigenvalues, and $\sum_\lambda \dim E_\lambda \le n$.

## Remarks

### Why each hypothesis is needed

- The eigenvalues must be distinct. For $T = \id_{\R^2}$, the vectors $e_1$, $e_2$ and $e_1 + e_2$ are eigenvectors for the eigenvalue $1$, and they are dependent.
- The vectors must be nonzero. The zero vector satisfies $T(0) = \lambda \cdot 0$ for every $\lambda$, and any list that contains it is dependent.

### Consequences

- An $n \times n$ matrix with $n$ distinct eigenvalues is diagonalisable, by the theorem that [[distinct eigenvalues imply diagonalisability|0Y95Z7MT02]].
- $T$ is [[diagonalisable|07SQCNV233]] if and only if $\sum_\lambda \dim E_\lambda = \dim V$.
- In infinite dimension, the functions $e^{\lambda x}$ for distinct real $\lambda$ are linearly independent, because they are eigenvectors of the [[derivative|1SKH5XJ5RB]] for distinct eigenvalues.

### Converse

The converse fails: independent eigenvectors can share an eigenvalue, as $e_1$ and $e_2$ for $\id_{\R^2}$.

### Generalizations

- Generalised eigenvectors for distinct eigenvalues are linearly independent, and the sum of the [[generalised eigenspaces|0Z3GDY89T5]] is direct.
- More generally, if $p_1, \dots, p_k \in F[x]$ are pairwise coprime, then the sum of the kernels of $p_i(T)$ is direct.

## History

The result is part of the classical theory of diagonalisation, and it appears in all standard textbooks of linear algebra.

## Explanations

### L1 human

Eigenvectors for different eigenvalues point in genuinely different directions.
None of them is a combination of the others.
This is the main fact behind diagonalisation.

### L2 human

We check the theorem for $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$.

1. The eigenvalues are $1$ and $3$, the diagonal entries of the triangular matrix.
2. $v_1 = (1, 0)^{\mathsf{T}}$ satisfies $A v_1 = (1, 0)^{\mathsf{T}} = v_1$.
3. $v_2 = (1, 1)^{\mathsf{T}}$ satisfies $A v_2 = (3, 3)^{\mathsf{T}} = 3 v_2$.
4. $\det \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = 1 \ne 0$, so $v_1$ and $v_2$ are independent, as the theorem says.

The typical use is to show that a matrix with $n$ distinct eigenvalues has an eigenbasis.
A trap: the theorem says nothing about two eigenvectors for the same eigenvalue.

### L3 human

In module language, $V$ is a module over $F[x]$, and the eigenspaces are the parts killed by the coprime polynomials $x - \lambda_i$.
The sum of the submodules killed by pairwise coprime polynomials is direct, by the Chinese remainder theorem.
This is the first step of the primary decomposition.
