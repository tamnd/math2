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

A normal operator is one that commutes with its own adjoint.
Over the complex numbers this one equation picks out exactly the operators that act as plain multiplication along some set of perpendicular directions, so normal operators are the ones that the spectral theorem can diagonalize.
Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$.
A linear operator $T \colon V \to V$ with [[adjoint|0R9NMSM1ZP]] $T^*$ is *normal* when
$$T T^* = T^* T.$$
A square matrix $A$ is a [[normal matrix|0MR0BYF0K2]] when $A A^* = A^* A$, where $A^*$ is the conjugate transpose, and the [[formal definition|0ENZN5G4CV]] states both forms.
An equivalent condition is $\norm{Tv} = \norm{T^* v}$ for every $v \in V$.

## Motivation

The [[self-adjoint operators|0NEGN5CRSC]] have an orthonormal basis of eigenvectors, but many operators with such a basis are not self-adjoint.
The rotation of $\mathbb{C}^2$ by a right angle has the orthonormal eigenvectors $\tfrac{1}{\sqrt{2}}(1, -i)$ and $\tfrac{1}{\sqrt{2}}(1, i)$, with the eigenvalues $i$ and $-i$, and it is not self-adjoint.
So what do all operators with an orthonormal eigenbasis have in common?

Suppose $T$ has the matrix $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ in an orthonormal basis.
Then $T^*$ has the matrix $\overline{D} = \operatorname{diag}(\overline{\lambda_1}, \dots, \overline{\lambda_n})$ in the same basis, and two diagonal matrices commute.
So $T T^* = T^* T$ is necessary, and [[the complex spectral theorem|04CW1P44VD]] says that over $\mathbb{C}$ it is also sufficient.
Unitary and self-adjoint matrices, which are both normal, are the basic objects of quantum mechanics in finite dimension, and the circulant matrices of signal processing are normal too.

## Notation

For operators the condition is $T T^* = T^* T$.
For matrices with the standard inner product it is $A A^* = A^* A$, and for real matrices it reads $A A^{\mathsf{T}} = A^{\mathsf{T}} A$.
The commutator $[T^*, T] = T^* T - T T^*$ is $0$ exactly when $T$ is normal.
In Mathlib, `IsStarNormal` states $a^* a = a a^*$ for an element of any monoid with an involution, and for operators the involution is $T \mapsto T^*$.

## Remarks

### A first test

Take $A = \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$, so $A^* = \begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix}$.
Multiply in both orders:
$$A A^* = \begin{pmatrix} 1 + 1 & -i + i \\ i - i & 1 + 1 \end{pmatrix} = 2I, \qquad A^* A = \begin{pmatrix} 1 + 1 & i - i \\ -i + i & 1 + 1 \end{pmatrix} = 2I.$$
So $A$ is normal.
It is not Hermitian, since $A^* \ne A$, and it is not unitary, since $A A^* = 2I \ne I$.
Its eigenvectors $(1, 1)$ and $(1, -1)$, for the eigenvalues $1 + i$ and $1 - i$, are orthogonal, as the spectral theorem predicts.

### The three main families

Most normal operators that you meet belong to one of three families, and each passes the test for its own reason.

- A self-adjoint operator has $T^* = T$, so both products are $T^2$.
- A skew-adjoint operator has $T^* = -T$, so both products are $-T^2$.
- A unitary or orthogonal operator has $T^* = T^{-1}$, so both products are $I$, as for [[the rotation by a right angle|1CF483TZZA]].

Diagonal matrices with any complex entries are normal too, and the class is wider than these families.
For example, $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$ is $I + P$ for the cyclic permutation matrix $P$, and $P^{\mathsf{T}} = P^{-1}$ commutes with $P$, so $A$ is normal.
Its eigenvalues are $2$ and $\tfrac{1}{2}(1 \pm i\sqrt{3})$, so it is neither symmetric nor orthogonal.

### What it is not

[[The shear|BF9MKKHH4Z]] $S = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ is not normal:
$$S S^{\mathsf{T}} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \qquad S^{\mathsf{T}} S = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}.$$
The nilpotent matrix $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ fails too, with $N N^{\mathsf{T}} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $N^{\mathsf{T}} N = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.
In general a normal nilpotent operator is $0$, because it is diagonal in some orthonormal basis with only the eigenvalue $0$.
So [[differentiation on the polynomials of degree at most 2|CR3EXBJNPF]] is not normal for any inner product, and [[the matrix with Schur form $\begin{pmatrix} 3 & 4 \\ 0 & 3 \end{pmatrix}$|HFW74NJ8G3]] is not normal because its Schur form is not diagonal.

### The rules you can use

[[The norm criterion|EMW3QTE3H9]] says that $T$ is normal exactly when $\norm{Tv} = \norm{T^* v}$ for all $v$.
It follows that $T$ and $T^*$ have the same eigenvectors, with conjugate eigenvalues.
Then [[eigenvectors for distinct eigenvalues are orthogonal|0JHGAV9H25]], and over $\mathbb{C}$ the [[complex spectral theorem|04CW1P44VD]] gives an orthonormal eigenbasis.
The same eigenbasis gives [[the spectral decomposition|D5KVBA1K9R]] $T = \sum \lambda_i P_i$ with orthogonal projections $P_i$, and it shows that $T^*$ is a polynomial in $T$.
Over $\mathbb{R}$, [[the real normal form|G6T1FNE3JC]] replaces each pair of non-real eigenvalues by a $2 \times 2$ block $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$.

Over $\mathbb{C}$ every operator splits as $T = H + iK$ with $H = \tfrac{1}{2}(T + T^*)$ and $K = \tfrac{1}{2i}(T - T^*)$ self-adjoint.
A short expansion gives $T^* T - T T^* = 2i(HK - KH)$, so $T$ is normal exactly when $H$ and $K$ commute.

### Watch out

A diagonalizable matrix need not be normal.
[[The matrix $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$|5RQ7EC5RC6]] has the eigenvectors $(1, 0)$ and $(1, 1)$, but they are not orthogonal, and the matrix is not normal.
Sums and products of normal matrices need not be normal either:
$$\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix},$$
a symmetric plus an orthogonal matrix that gives a nilpotent one.
For a complex matrix, the test must use $A^*$, not $A^{\mathsf{T}}$, and a normal matrix can have eigenvalues that are not real.

### History

Long lists of conditions equivalent to normality were collected by Grone, Johnson, Sá and Wolkowicz in 1987, and extended by Elsner and Ikramov in 1998.

### Try it

Is $A = \begin{pmatrix} 2 & -3 \\ 3 & 2 \end{pmatrix}$ normal?
Yes: $A A^{\mathsf{T}} = 13 I = A^{\mathsf{T}} A$, because $A$ is $\sqrt{13}$ times a rotation.

For which real $c$ is $\begin{pmatrix} 1 & c \\ 0 & 2 \end{pmatrix}$ normal?
The $(1, 1)$ entries of $A A^{\mathsf{T}}$ and $A^{\mathsf{T}} A$ are $1 + c^2$ and $1$, so only $c = 0$ works.

## Explanations

### L1 human

A normal operator gives the same result when we apply it and its adjoint in either order.
Symmetric matrices, rotations and diagonal matrices are all normal.
The reason to care is that a normal operator, with complex numbers allowed, just multiplies each of some perpendicular directions by a number.
For example, the quarter turn of the plane multiplies two complex directions by $i$ and by $-i$.
A shear such as $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ is not normal, and it has only one special direction.

### L2 human

Here is a typical test, for the real matrix $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$.
The entries of $A A^{\mathsf{T}}$ are the dot products of the rows $(1, 1, 0)$, $(0, 1, 1)$ and $(1, 0, 1)$, and the entries of $A^{\mathsf{T}} A$ are the dot products of the columns $(1, 0, 1)$, $(1, 1, 0)$ and $(0, 1, 1)$.
Each row and each column has dot product $2$ with itself and $1$ with each of the others, so
$$A A^{\mathsf{T}} = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} = A^{\mathsf{T}} A.$$
So $A$ is normal, and the complex spectral theorem gives an orthonormal eigenbasis of $\mathbb{C}^3$.
The eigenvectors are $(1, \omega^k, \omega^{2k})$ with $\omega = e^{2\pi i/3}$, the columns of the discrete Fourier matrix of size $3$ up to a factor, for the eigenvalues $1 + \omega^k$.
The typical use is exactly this order: check normality first, then apply the spectral theorem.
Watch out: normality depends on the inner product, because the adjoint does.

### L3 human

In any algebra with an involution, an element $a$ is normal when $a^* a = a a^*$.
In a $C^*$-algebra, a normal element generates a commutative $C^*$-subalgebra, and the continuous functional calculus applies to it.
For bounded operators on a Hilbert space, normal operators have [[a spectral theorem with projection-valued measures|X71XRPJR7D]].
[[Hyponormal|35XKRHEC3Q]] and subnormal operators weaken normality, and in finite dimension both classes reduce to the normal operators.
The sub-area on isometries and the sub-area on positive operators and singular values both build on normal operators, the first through unitary matrices and the second through the spectral theorem for $A^* A$.
