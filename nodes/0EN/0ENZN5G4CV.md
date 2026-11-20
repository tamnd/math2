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

Let $V$ be a finite-dimensional [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $T \colon V \to V$ be a linear [[operator|0PTF1PTJK0]] with [[adjoint|0ST8QF9T3T]] $T^*$.
The operator $T$ is *normal* when
$$T T^* = T^* T.$$
An $n \times n$ matrix $A$ over $\mathbb{K}$ is *normal* when $A A^* = A^* A$, where $A^*$ is the [[conjugate transpose|0EX045E2BP]].

## Notation

- For a real matrix, $A^* = A^T$, and the condition reads $A A^T = A^T A$.
- The Lean declaration `IsStarNormal` states $a^* a = a a^*$ for an element of any monoid with an involution. For operators, the involution is $T \mapsto T^*$.

## Remarks

- The operator $x \mapsto Ax$ on $\mathbb{K}^n$ with the standard inner product is normal if and only if the matrix $A$ is normal, by [[the matrix of the adjoint|0DBTE6HVBD]]. The same holds for the matrix of $T$ in any orthonormal basis.
- Self-adjoint, skew-adjoint and unitary operators are normal.
- An equivalent condition is $\norm{Tv} = \norm{T^* v}$ for all $v \in V$, by [[the norm criterion|~98fd04c3]].
- Normality depends on the inner product, because the adjoint does.

## Explanations

### L1 human

A normal operator gives the same result when we apply it and its adjoint in either order.
For a real matrix, we compare $A$ times its transpose with the transpose times $A$.
For the rotation $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, both products are the identity, so it is normal.

### L2 human

Worked example: we check the definition for a complex matrix.

1. Let $A = \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$. Then $A^* = \begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix}$.
2. We compute $A A^* = \begin{pmatrix} 1 + 1 & -i + i \\ i - i & 1 + 1 \end{pmatrix} = 2I$.
3. We compute $A^* A = 2I$ in the same way. So $A$ is normal.
4. Since $A^* \neq A$, the matrix is not Hermitian. So the class of normal matrices is larger than the class of Hermitian matrices.

The typical use is to check this condition before applying the complex spectral theorem.
A trap: for complex matrices, the plain transpose gives a different and wrong test.

### L3 human

The definition makes sense in every algebra with an involution, such as a $C^*$-algebra.
For bounded operators on a Hilbert space, normal operators are the setting of [[the spectral theorem for bounded normal operators|X71XRPJR7D]].
