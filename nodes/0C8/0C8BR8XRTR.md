---
tag: 0C8BR8XRTR
kind: concept
name: Normal operator
msc: ["47B15", "15A04"]
topics: [3YM9EK6VMB]
audience: ug1
uses: [0R9NMSM1ZP, 0ST8QF9T3T, 0J7H0YBFDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_operator
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Normal_matrix
    locator: Special cases
  - url: https://en.wikipedia.org/wiki/Normal_matrix
    locator: Equivalent definitions
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780134860244
    locator: Section 6.4
same_as:
  wikidata: Q854946
  wikipedia: Normal operator
inventory: [3TQD4SG7V4]
---

## Summary

Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$.
A linear operator $T \colon V \to V$ is normal when it commutes with its [[adjoint|0R9NMSM1ZP]]: $T T^* = T^* T$.
A square matrix $A$ is a [[normal matrix|0MR0BYF0K2]] when $A A^* = A^* A$, and the [[formal definition|0ENZN5G4CV]] states both forms.
Normal operators matter because, over $\mathbb{C}$, they are exactly the operators with an orthonormal basis of eigenvectors.

## Motivation

The [[self-adjoint operators|0NEGN5CRSC]] have an orthonormal basis of eigenvectors, but many useful operators with such a basis are not self-adjoint.
A rotation of $\mathbb{C}^2$ by a right angle has the orthonormal eigenvectors $(1, -i)$ and $(1, i)$, with the eigenvalues $i$ and $-i$.
If $T = U D U^*$ with $U$ unitary and $D$ diagonal, then $T^* = U \overline{D} U^*$, and diagonal matrices commute.
So $T T^* = T^* T$ is necessary for an orthonormal eigenbasis.
The complex spectral theorem says that this condition is also sufficient.

## Notation

- For operators, the condition is $T T^* = T^* T$. For matrices with the standard inner product, it is $A A^* = A^* A$, and for real matrices $A A^T = A^T A$.
- In Mathlib, `IsStarNormal` is the condition $a^* a = a a^*$ in any algebra with an involution.
- The commutator $[T^*, T] = T^* T - T T^*$ is $0$ exactly for normal $T$.

## Remarks

### Examples

- Every self-adjoint operator is normal, since $T^* T = T^2 = T T^*$.
- Every skew-adjoint operator is normal, since $T^* T = -T^2 = T T^*$.
- Every unitary or orthogonal operator is normal, since $T^* T = I = T T^*$. [[The rotation by a right angle|1CF483TZZA]] is an example.
- The matrix $\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ is normal, with $A A^* = 2I = A^* A$. It is neither Hermitian, nor skew-Hermitian, nor unitary.
- The real matrix $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$ is $I + P$ with a cyclic permutation matrix $P$. It is normal, since $P^T = P^{-1}$ commutes with $P$.
- Every diagonal matrix with complex entries is normal.

### Non-examples

- [[The shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$|BF9MKKHH4Z]]: $A A^T = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ differs from $A^T A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$.
- The nilpotent matrix $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$: $N N^T = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $N^T N = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.
- [[Differentiation on the polynomials of degree at most 2|CR3EXBJNPF]] with the inner product $\int_{-1}^{1} pq$ is not normal.
- [[The matrix with the Schur form $\begin{pmatrix} 3 & 4 \\ 0 & 3 \end{pmatrix}$|HFW74NJ8G3]] is not normal, because its Schur form is not diagonal.

### Basic properties

- [[The norm criterion|EMW3QTE3H9]]: $T$ is normal if and only if $\norm{Tv} = \norm{T^* v}$ for all $v$. Then $T$ and $T^*$ have the same eigenvectors, with conjugate eigenvalues.
- [[Orthogonality of eigenspaces|0JHGAV9H25]]: eigenvectors of a normal operator for distinct eigenvalues are orthogonal.
- [[The complex spectral theorem|04CW1P44VD]]: over $\mathbb{C}$, $T$ is normal if and only if $V$ has an orthonormal basis of eigenvectors of $T$.
- [[The real normal form|G6T1FNE3JC]]: over $\mathbb{R}$, a normal operator has a block diagonal matrix with $1 \times 1$ blocks and $2 \times 2$ scaled rotation blocks in an orthonormal basis.
- [[The spectral decomposition|D5KVBA1K9R]]: a normal operator is $T = \sum \lambda_i P_i$ with orthogonal projections $P_i$, and $T^*$ is a polynomial in $T$.
- Over $\mathbb{C}$, write $T = A + iB$ with $A$ and $B$ self-adjoint. Then $T$ is normal if and only if $AB = BA$.
- The sum and the product of two normal operators need not be normal. For example, $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}$.

### History

The Wikipedia article on normal matrices lists many conditions that are equivalent to normality.
It refers to the longer lists of Grone, Johnson, Sá and Wolkowicz from 1987, and of Elsner and Ikramov from 1998.

### Common errors

- Students think that every diagonalizable matrix is normal. [[The trap matrices|5RQ7EC5RC6]] include $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$, which is diagonalizable but not normal.
- Students test $A A^T = A^T A$ for a complex matrix. The correct test uses the conjugate transpose $A^*$.
- Students think that a normal matrix has real eigenvalues. Only the self-adjoint ones do.

## Explanations

### L1 human

A normal operator gives the same result when we apply it and its adjoint in either order.
Symmetric matrices, rotations and diagonal matrices are normal.
The reason to care: a normal operator acts on some perpendicular complex directions by multiplying each by a number.
A shear such as $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ is not normal, and it has only one special direction.

### L2 human

Worked example: we test a $3 \times 3$ real matrix.

1. Let $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$, so $A^T = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$.
2. We compute $A A^T = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix}$.
3. We compute $A^T A = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix}$. The two products agree, so $A$ is normal.
4. The eigenvalues are $2$ and $\tfrac{1}{2}(1 \pm i \sqrt{3})$. They are not all real, so $A$ is not symmetric, and they do not all have absolute value $1$, so $A$ is not orthogonal.

The typical use is to check normality first and then apply the complex spectral theorem.
A trap: normality depends on the inner product, because the adjoint does.

### L3 human

In an algebra with an involution, an element $a$ is normal when $a^* a = a a^*$.
Normal elements of a $C^*$-algebra generate commutative $C^*$-subalgebras, and the continuous functional calculus applies to them.
For bounded operators on a Hilbert space, normal operators have [[a spectral theorem with projection-valued measures|X71XRPJR7D]].
Hyponormal and subnormal operators weaken normality, and in finite dimension they are all normal.
