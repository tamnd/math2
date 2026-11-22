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

A unitary matrix is the complex version of an orthogonal matrix: it moves the vectors of $\C^n$ without changing any length or any angle.
The test is the same as over $\R$, except that the transpose is replaced by the conjugate transpose.
A complex $n \times n$ matrix $U$ is *unitary* when
$$U^* U = I_n,$$
where $U^* = \overline{U}^{\mathsf{T}}$ is the [[conjugate transpose|0DXKE10PHF]]; the [[formal definition|0D6RMJ10M9]] states it.
[[Equivalently|GZ7NG7J3J8]], $U$ is invertible with $U^{-1} = U^*$, and its columns form an [[orthonormal basis|0S9GGTR0EX]] of $\C^n$ for the standard inner product $\langle x, y \rangle = \sum_k x_k \overline{y_k}$.

## Motivation

In $\C^n$ the length of a vector uses absolute values, $\lVert x \rVert^2 = \lvert x_1 \rvert^2 + \dots + \lvert x_n \rvert^2$, and $\lvert x_k \rvert^2 = x_k \overline{x_k}$ needs a complex conjugate.
The plain transpose does not see these conjugates, so the real test $Q^{\mathsf{T}} Q = I$ is the wrong test over $\C$.
The conjugate transpose is the right one, and the matrices that pass it are exactly the matrices of the [[linear isometries|07SJXTWVQW]] of $\C^n$.

Unitary matrices appear wherever complex lengths must stay the same.
The discrete Fourier transform, with the right scaling, is unitary, and so it keeps the energy of a signal.
In quantum mechanics a state is a unit vector in a complex space, and the change of a closed system over time is a unitary map.
Later the [[unitary group|VW5H9XFNJB]] collects all unitary matrices, and the [[polar decomposition|0J2C7BDJQA]] and the [[singular value decomposition|000NPTMX6J]] split every matrix into unitary and positive parts.

## Notation

The conjugate transpose is written $U^*$, $U^{\mathsf{H}}$ or $U^\dagger$; the dagger is usual in physics.
The set of unitary $n \times n$ matrices is the unitary group $U(n)$.
Mathlib writes `Matrix.unitaryGroup (Fin n) ℂ` for it, and it uses `star` for the conjugate transpose.

## Remarks

### A first check

Take
$$U = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ i & -i \end{pmatrix}, \qquad U^* = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & -i \\ 1 & i \end{pmatrix}.$$
Multiply, row of $U^*$ by column of $U$:
$$U^* U = \frac{1}{2} \begin{pmatrix} 1 + (-i)(i) & 1 + (-i)(-i) \\ 1 + i \cdot i & 1 + i(-i) \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = I_2.$$
So $U$ is unitary, and its columns $\frac{1}{\sqrt{2}}(1, i)$ and $\frac{1}{\sqrt{2}}(1, -i)$ are orthonormal in $\C^2$.
Check the real test on the same matrix: $U^{\mathsf{T}} U = \frac{1}{2} \begin{pmatrix} 1 + i^2 & 1 - i^2 \\ 1 - i^2 & 1 + i^2 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, which is not $I_2$.

### More examples

Every diagonal matrix $\operatorname{diag}(e^{i\theta_1}, \dots, e^{i\theta_n})$ is unitary, because each column is a basis vector times a number of absolute value $1$.
Every real orthogonal matrix is unitary, because for real entries $Q^* = Q^{\mathsf{T}}$.
The [[Fourier matrix of size three|SF3EBT2Z4F]] is unitary, and its fourth power is $I_3$.
The matrix [[with rows (1, i) and (i, 1) divided by the square root of two|F3P6M0A78R]] is unitary with determinant $1$, and [[the matrix with rows (0, i) and (1, 0)|6NZCDBCSKQ]] is unitary with determinant $0 \cdot 0 - i \cdot 1 = -i$.

### What it is not

The matrix $\operatorname{diag}(2, \frac{1}{2})$ is not unitary, because its first column has length $2$.
The matrix [[with rows (i, 1) and (0, 1)|RMXFKRW9WQ]] has determinant $i$, on the unit circle, but its second column $(1, 1)$ has length $\sqrt{2}$, so it is not unitary.
And a [[complex matrix with N^T N = I|JRPHE0FG7D]] is a complex orthogonal matrix, which need not be unitary.

### The rules you can use

Products and inverses of unitary matrices are unitary, since $(UW)^*(UW) = W^* U^* U W = W^* W = I_n$, so they form the group $U(n)$.
A matrix $U$ is unitary exactly when $U^*$ is, and exactly when $U^{\mathsf{T}}$ is.
[[The properties theorem|GZ7NG7J3J8]] gives the rest: $\lvert \det U \rvert = 1$, every eigenvalue $\lambda$ has $\lvert \lambda \rvert = 1$, and eigenvectors for different eigenvalues are orthogonal.
A unitary matrix is [[normal|0MR0BYF0K2]], so the [[complex spectral theorem|04CW1P44VD]] gives $U = V D V^*$ with $V$ unitary and $D$ diagonal; we say that $U$ is unitarily diagonalizable.

The determinant can be any number on the unit circle, not only $\pm 1$ as for a real orthogonal matrix.
Every $2 \times 2$ unitary matrix has the form
$$\begin{pmatrix} a & b \\ -e^{i\varphi} \overline{b} & e^{i\varphi} \overline{a} \end{pmatrix}, \qquad \lvert a \rvert^2 + \lvert b \rvert^2 = 1,$$
and its determinant is $e^{i\varphi}(a \overline{a} + b \overline{b}) = e^{i\varphi}$.

### Watch out

Eigenvalues on the unit circle do not make a matrix unitary.
The matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has the single eigenvalue $1$, but its second column has length $\sqrt{2}$.
A second trap: complex conjugation $x \mapsto \overline{x}$ keeps every length in $\C^n$, but it is not complex-linear, since $\overline{i x} = -i \overline{x}$, so it has no unitary matrix.
Last, a unitary matrix with real entries is orthogonal, but a unitary matrix with determinant $1$ need not have real entries.

### Try it

First, is $\frac{1}{5}\begin{pmatrix} 3 & 4i \\ 4i & 3 \end{pmatrix}$ unitary?
Yes: each column has squared length $\frac{9 + 16}{25} = 1$, and the inner product of the columns is $\frac{1}{25}(4i \cdot 3 + 3 \cdot \overline{4i}) = \frac{12i - 12i}{25} = 0$.

Second, find the inverse of $U = \operatorname{diag}(i, e^{i\pi/4})$.
Since $U$ is unitary, $U^{-1} = U^* = \operatorname{diag}(-i, e^{-i\pi/4})$.

## Explanations

### L1 human

A unitary matrix is a table of complex numbers that keeps all lengths in complex space.
It is the complex form of a rotation or a mirror image.
To test a matrix, swap its rows and columns and replace each entry by its complex conjugate.
If the result times the matrix is the identity, the matrix is unitary.
For example, multiplying by $i$ turns the complex plane by a quarter turn, and the $1 \times 1$ matrix $(i)$ is unitary because $\overline{i} \cdot i = 1$.

### L2 human

Here is a typical problem: diagonalize $U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ with a unitary matrix.
Apply $U$ to $(1, 1)$ and $(1, -1)$:
$$U \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1 + i}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \qquad U \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \frac{1 - i}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \end{pmatrix}.$$
Both eigenvalues have absolute value $\sqrt{\frac{1}{2} + \frac{1}{2}} = 1$, and the eigenvectors are orthogonal.
Divide each eigenvector by its length $\sqrt{2}$, and put them as the columns of $V$:
$$V = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \qquad U = V \operatorname{diag}\!\left(e^{i\pi/4}, e^{-i\pi/4}\right) V^*.$$
Check: the product of the eigenvalues is $\frac{(1 + i)(1 - i)}{2} = 1$, and $\det U = \frac{1 - i^2}{2} = 1$.
The problem shows the typical use: in the right orthonormal basis a unitary matrix only multiplies each axis by a point of the unit circle.

### L3 human

The group $U(n)$ is a compact connected Lie group of real dimension $n^2$, and it is a maximal compact subgroup of $GL_n(\C)$.
Each invertible complex matrix is a unitary matrix times a positive definite Hermitian matrix, by the polar decomposition.
In operator algebra, the unitary matrices are the unitary elements of the C*-algebra $M_n(\C)$, and on a Hilbert space they generalize to the [[unitary operators|MM0EJ2GDE4]].
In infinite dimensions the two conditions $U^* U = I$ and $U U^* = I$ are no longer equivalent, and the unilateral shift satisfies only the first.
