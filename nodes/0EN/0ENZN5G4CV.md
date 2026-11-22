---
tag: 0ENZN5G4CV
kind: definition
name: Normal operator
msc: ["47B15", "15A04"]
topics: [3YM9EK6VMB]
audience: ug1
defines: 0C8BR8XRTR
uses: [0ST8QF9T3T, 0PTF1PTJK0, 01EK923SKP, 0EX045E2BP]
formal:
  - system: lean4
    library: mathlib
    decl: IsStarNormal
    match: variant
sources:
  - url: https://en.wikipedia.org/wiki/Normal_operator
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780134860244
    locator: Section 6.4
inventory: [3TQD4SG7V4]
---

## Definition

A normal operator is an operator that commutes with its adjoint.
Let $V$ be a finite-dimensional [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $T \colon V \to V$ be a linear [[operator|0PTF1PTJK0]] with [[adjoint|0ST8QF9T3T]] $T^*$.
The operator $T$ is *normal* when
$$T T^* = T^* T.$$
An $n \times n$ matrix $A$ over $\mathbb{K}$ is *normal* when $A A^* = A^* A$, where $A^*$ is the [[conjugate transpose|0EX045E2BP]] of $A$.

## Notation

For a real matrix $A^* = A^{\mathsf{T}}$, and the condition reads $A A^{\mathsf{T}} = A^{\mathsf{T}} A$.
The Lean declaration `IsStarNormal` states $a^* a = a a^*$ for an element of any monoid with an involution; it is a variant because it is not tied to operators, and for operators the involution is $T \mapsto T^*$.

## Remarks

The definition has two ingredients, and each one matters.
The adjoint is taken for the given inner product, so normality depends on the inner product, and the same linear map can be normal for one inner product and not for another.
The space is finite-dimensional, so the adjoint always exists, and $T T^*$ and $T^* T$ are operators on the same space $V$.

The operator and the matrix forms agree in orthonormal bases.
By [[the matrix of the adjoint|0DBTE6HVBD]], the matrix of $T^*$ in an orthonormal basis is the conjugate transpose of the matrix of $T$.
So $T$ is normal exactly when its matrix in one, or every, orthonormal basis is a normal matrix.

For a small example, the rotation $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has $R^{\mathsf{T}} = -R$, so $R R^{\mathsf{T}} = I = R^{\mathsf{T}} R$, and $R$ is normal.
A case that fails is $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, with $N N^{\mathsf{T}} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ but $N^{\mathsf{T}} N = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.
An equivalent condition is $\norm{Tv} = \norm{T^* v}$ for all $v \in V$, by [[the norm criterion|EMW3QTE3H9]].
The concept page on [[normal operators|0C8BR8XRTR]] gives the main families: self-adjoint, skew-adjoint and unitary operators.

## Explanations

### L1 human

A normal operator gives the same result when we apply it and its adjoint in either order.
For a real matrix, we compare the matrix times its transpose with the transpose times the matrix.
For the quarter turn $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, both products are the identity, so the quarter turn is normal.

### L2 human

Here is the test for a complex matrix, $A = \begin{pmatrix} 2 & i \\ i & 2 \end{pmatrix}$ with $A^* = \begin{pmatrix} 2 & -i \\ -i & 2 \end{pmatrix}$.
Multiply in both orders:
$$A A^* = \begin{pmatrix} 4 + 1 & -2i + 2i \\ 2i - 2i & 1 + 4 \end{pmatrix} = 5I, \qquad A^* A = \begin{pmatrix} 4 + 1 & 2i - 2i \\ -2i + 2i & 1 + 4 \end{pmatrix} = 5I.$$
So $A$ is normal, although $A^* \neq A$ and $A$ is not Hermitian.
The typical use is to run this test before applying the complex spectral theorem.
Watch out: the test with the plain transpose is wrong over $\mathbb{C}$.
Every complex symmetric matrix passes it, but $B = \begin{pmatrix} 1 & i \\ i & -1 \end{pmatrix}$ has $B^2 = 0$ with $B \neq 0$, and a nonzero nilpotent matrix is never normal.

### L3 human

The definition makes sense in every algebra with an involution, such as a $C^*$-algebra, where the involution plays the part of the adjoint.
For bounded operators on a Hilbert space, normal operators are the setting of [[the spectral theorem for bounded normal operators|X71XRPJR7D]].
