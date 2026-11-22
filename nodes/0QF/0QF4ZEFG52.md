---
tag: 0QF4ZEFG52
kind: statement
role: theorem
name: Eigenvalues are the roots of the minimal polynomial
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
about: [03NDVCSHSB, 0BQAA2BK3Q]
uses: [0V58FPM3EQ, 0ZND7NQ970, 0BZ81AJNWF]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: Properties
  - book: isbn:9783031410253
    locator: Chapter 5
  - book: isbn:9780135367971
---

## Statement

The minimal polynomial has exactly the eigenvalues as its roots, so it finds the same eigenvalues as the characteristic polynomial, often with a polynomial of smaller degree.
Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, let $T \colon V \to V$ be an endomorphism with [[minimal polynomial|03NDVCSHSB]] $m_T$, and let $\lambda \in F$.

1. $\lambda$ is an [[eigenvalue|0BQAA2BK3Q]] of $T$ if and only if $m_T(\lambda) = 0$.
2. So $m_T$ and the [[characteristic polynomial|0J5EMJRRFM]] $p_T$ have the same roots in $F$.

The same holds for an $n \times n$ matrix $A$ over $F$.

## Remarks

### A check on a 3 by 3 matrix

Take the [[matrix with 4 on the diagonal and 1 elsewhere|7XFGVVTZ2X]],
$$A = \begin{pmatrix} 4 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 4 \end{pmatrix}.$$
The matrix $A - 3I$ has every entry equal to $1$, and every column of $A - 6I$, such as $(-2, 1, 1)$, has entries with sum $0$.
Each entry of $(A - 3I)(A - 6I)$ is a row of ones times a column of $A - 6I$, which is a column sum, so the product is $0$.
Neither $A - 3I$ nor $A - 6I$ is zero, so $m_A = (x - 3)(x - 6)$, with the roots $3$ and $6$.
The theorem predicts that these are the eigenvalues, and indeed
$$A \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} = \begin{pmatrix} 3 \\ -3 \\ 0 \end{pmatrix}, \qquad A \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 6 \\ 6 \\ 6 \end{pmatrix}.$$
The characteristic polynomial $p_A = (x - 3)^2 (x - 6)$ has the same roots, and only the multiplicity of $3$ is different.

### Why each hypothesis is needed

The space must be finite-dimensional so that $m_T$ exists at all.

The roots must be taken in $F$.
Over $\mathbb{R}$, the rotation $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ by a right angle has $J^2 = -I$, and since $J$ is not a multiple of $I$, its minimal polynomial is $x^2 + 1$.
This polynomial has no real root, and $J$ has no real eigenvalue, because no line through $0$ is fixed by a rotation by $90$ degrees.
Over $\mathbb{C}$ both sides change together: $x^2 + 1$ has the roots $\pm i$, and $J (1, \mp i)^{\mathsf{T}} = (\pm i, 1)^{\mathsf{T}} = \pm i (1, \mp i)^{\mathsf{T}}$.

### What it gives you

The [[proof without the Cayley-Hamilton theorem|RJYK29EFS2]] uses only the definition of $m_T$ and the factor theorem for part 1, and the theorem that the [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]] for part 2.
So the theorem is available before the Cayley-Hamilton theorem.

It has several quick consequences.
If $T^k = 0$, then $m_T$ divides $x^k$, so $0$ is the only possible eigenvalue.
The map $T$ is invertible exactly when $0$ is not an eigenvalue, that is, when $m_T(0) \ne 0$.
If $T$ is diagonalizable with distinct eigenvalues $\lambda_1, \dots, \lambda_r$, then $(x - \lambda_1) \cdots (x - \lambda_r)$ kills each vector of an eigenbasis, so it annihilates $T$, and part 1 says that each factor must occur in $m_T$; so $m_T = (x - \lambda_1) \cdots (x - \lambda_r)$.

### The converse

Part 1 is already an equivalence, but a polynomial with the same roots as $m_T$ need not annihilate $T$.
For the [[shear|HTAWRAC3QE]] $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, the polynomial $x - 1$ has the same root as $m = (x - 1)^2$, but the shear minus $I$ is not zero.
So the roots of $m_T$ are determined by the eigenvalues, while the multiplicities carry extra information.

### Generalizations

Over any field, $m_T$ and $p_T$ have the same irreducible factors in $F[x]$, not only the same roots in $F$.
For the rotation $J$ above, both are $x^2 + 1$.
The proof uses the structure of $V$ as a module over $F[x]$, from the sub-area on [[canonical forms|GEBYZKYV3D]].
The [[eigenvalues of a polynomial in an endomorphism|F2S8WGVARA]] follow a related rule: if $T v = \lambda v$, then $q(T) v = q(\lambda) v$ for every polynomial $q$.

## History

The result appears in the standard treatments of the minimal polynomial.
Axler, in *Linear Algebra Done Right*, proves it without determinants and uses it as the main way to locate eigenvalues.

## Explanations

### L1 human

A matrix satisfies its minimal polynomial, and each of its stretch factors must satisfy the same equation.
For example, if the minimal polynomial is $(x - 3)(x - 6)$, then every stretch factor is $3$ or $6$.
The theorem adds that both numbers really occur as stretch factors.
So the minimal polynomial and the characteristic polynomial point to the same eigenvalues, and only the number of times each one is counted can differ.

### L2 human

Here is a typical use: a matrix satisfies $A^2 = 9A - 18I$; what can its eigenvalues be?
Move everything to one side:
$$A^2 - 9A + 18I = (A - 3I)(A - 6I) = 0.$$
So $m_A$ divides $(x - 3)(x - 6)$, and by part 1 every eigenvalue of $A$ is $3$ or $6$.
To know which of them occur, find $m_A$: if $A \ne 3I$ and $A \ne 6I$, then $m_A = (x - 3)(x - 6)$ and both are eigenvalues.
The matrix with $4$ on the diagonal and $1$ elsewhere is of this kind.
Watch out: the exponent of $x - \lambda$ in $m_A$ is not the algebraic multiplicity of $\lambda$; here $3$ has algebraic multiplicity $2$ but exponent $1$.

### L3 human

View $V$ as a module over $F[x]$, with $x$ acting as $T$, so that $V$ is a quotient of a sum of copies of $F[x]/(m_T)$.
An eigenvector for $\lambda$ spans a submodule isomorphic to $F[x]/(x - \lambda)$, and it exists exactly when $x - \lambda$ divides $m_T$.
The proof of the converse direction builds this submodule inside the image of $q(T)$, where $m_T = (x - \lambda) q$.
For an operator on an infinite-dimensional space without a minimal polynomial, the eigenvalues form the point spectrum, studied in operator theory.
