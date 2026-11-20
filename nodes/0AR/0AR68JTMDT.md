---
tag: 0AR68JTMDT
kind: concept
name: Unitary matrix
aliases: [complex-unitary-matrix]
msc: ["15B57", "15A21"]
topics: [AZS5BPF5H3]
audience: ug1
specializes: [0EB9N0S33C, 0MR0BYF0K2]
uses: [0D6RMJ10M9, 0DXKE10PHF, 0S9GGTR0EX]
sources:
  - url: https://en.wikipedia.org/wiki/Unitary_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Unitary_matrix
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Unitary_matrix
    locator: Equivalent conditions
  - book: isbn:9780521839402
    locator: Chapter 2
same_as:
  wikidata: Q727103
  wikipedia: Unitary matrix
inventory: [YNRSTBKDN5]
---

## Summary

A complex $n \times n$ matrix $U$ is *unitary* when $U^*U = I_n$, where $U^*$ is the [[conjugate transpose|0DXKE10PHF]].
[[Equivalently|~2220a569]], $U$ is invertible with $U^{-1} = U^*$, and its columns form an [[orthonormal basis|0S9GGTR0EX]] of $\C^n$ for the standard inner product $\ip{x}{y} = \sum_k x_k\overline{y_k}$.
Unitary matrices are the matrices of the [[linear isometries|07SJXTWVQW]] of $\C^n$, and they are the complex analogue of [[orthogonal matrices|0W02QESPJQ]].
Their determinants and eigenvalues lie on the unit circle, and each unitary matrix can be diagonalized by another unitary matrix.

## Motivation

In $\C^n$, lengths and angles come from the inner product $\ip{x}{y} = \sum_k x_k\overline{y_k}$, which uses complex conjugates.
The transpose alone does not see these conjugates, so the condition $Q^TQ = I$ is the wrong test over $\C$.
The right test uses the conjugate transpose, and it gives the unitary matrices.
Unitary matrices appear wherever complex lengths must stay the same, for example in the discrete Fourier transform and in quantum mechanics.

## Notation

- The conjugate transpose is written $U^*$, $U^H$ or $U^\dagger$.
- The set of unitary $n \times n$ matrices is the [[unitary group|~4244c18b]] $U(n)$. Mathlib writes `Matrix.unitaryGroup (Fin n) ℂ`.

## Remarks

### Examples

- [[The matrix with rows (1, i) and (i, 1) divided by the square root of two|~ee8e12f5]] is unitary with determinant $1$.
- [[The Fourier matrix of size three|~3dc0ee36]] is unitary, and its fourth power is $I_3$.
- Each diagonal matrix $\operatorname{diag}(e^{i\theta_1}, \dots, e^{i\theta_n})$ is unitary.
- Each real orthogonal matrix is unitary, because then $Q^* = Q^T$.
- [[The unitary matrix with rows (0, i) and (1, 0)|~24dc021c]] has determinant $-i$.

### Non-examples

- [[A complex matrix with $N^TN = I$|~83b36d34]] need not be unitary: the plain transpose is the wrong test over $\C$.
- [[The matrix with rows (i, 1) and (0, 1)|~b46dc950]] has determinant $i$, on the unit circle, but it is not unitary.
- $\operatorname{diag}(2, \frac{1}{2})$ is not unitary: its first column has length $2$.

### Basic properties

- $U$ is unitary exactly when $U^*$ is unitary, and exactly when $U^T$ is unitary.
- Products and inverses of unitary matrices are unitary, so they form the group $U(n)$.
- $\abs{\det U} = 1$, and every eigenvalue $\lambda$ of $U$ has $\abs{\lambda} = 1$, see [[the properties|~2220a569]].
- $U$ is [[normal|0MR0BYF0K2]], so $U = VDV^*$ with $V$ unitary and $D$ diagonal, by the [[complex spectral theorem|04CW1P44VD]].
- A $2 \times 2$ unitary matrix has the form $\begin{pmatrix} a & b \\ -e^{i\varphi}\overline{b} & e^{i\varphi}\overline{a} \end{pmatrix}$ with $\abs{a}^2 + \abs{b}^2 = 1$, and its determinant is $e^{i\varphi}$.

### Common errors

- A complex matrix with $U^TU = I$ is a complex orthogonal matrix, not a unitary matrix. The two notions differ.
- A matrix with all eigenvalues on the unit circle need not be unitary. The upper triangular matrix with rows $(1, 1)$ and $(0, 1)$ has the only eigenvalue $1$, but it is not unitary.
- A unitary matrix with real entries is orthogonal, but a unitary matrix with determinant $1$ need not be real.

## Explanations

### L1 human

A unitary matrix is a table of complex numbers that keeps all lengths in complex space.
It is the complex form of a rotation or a mirror image.
To test a matrix, swap its rows and columns and replace each entry by its complex conjugate.
If the result times the matrix is the identity, the matrix is unitary.

### L2 human

Worked check for $U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ i & -i \end{pmatrix}$:

1. $U^* = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & -i \\ 1 & i \end{pmatrix}$, the conjugate of the transpose.
2. $U^*U = \frac{1}{2}\begin{pmatrix} 1 \cdot 1 + (-i)(i) & 1 \cdot 1 + (-i)(-i) \\ 1 \cdot 1 + i \cdot i & 1 \cdot 1 + i(-i) \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = I_2$.
3. So $U$ is unitary. Its columns $\frac{1}{\sqrt{2}}(1, i)$ and $\frac{1}{\sqrt{2}}(1, -i)$ are orthonormal in $\C^2$.

The typical use: a change between two orthonormal bases of $\C^n$ is a unitary matrix.
A trap: $U^TU = \frac{1}{2}\begin{pmatrix} 0 & 2 \\ 2 & 0 \end{pmatrix} \neq I_2$, so the real test fails here even though $U$ is unitary.

### L3 human

$U(n)$ is the group of linear isometries of $\C^n$, a compact connected Lie group of real dimension $n^2$.
It is a maximal compact subgroup of $GL_n(\C)$, and each element of $GL_n(\C)$ is a product of a unitary matrix and a positive definite Hermitian matrix, by the [[polar decomposition|0J2C7BDJQA]].
The unitary matrices are the unitary elements of the C*-algebra $M_n(\C)$, and they generalize to the [[unitary operators|MM0EJ2GDE4]] of a Hilbert space.
