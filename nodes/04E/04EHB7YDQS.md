---
tag: 04EHB7YDQS
kind: definition
name: Spectrum of a matrix
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
defines: 0XPX5NC67E
uses: [0ZND7NQ970, 0TWTS88TWN]
formal:
  - system: lean4
    library: mathlib
    decl: spectrum
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Spectrum_of_a_matrix
    locator: Definition
inventory: [9F89D494GH]
---

## Definition

The spectrum of a square matrix is the set of scalars $\lambda$ for which $A - \lambda I$ cannot be inverted.
Let $F$ be a field, let $n \ge 1$, and let $A$ be an $n \times n$ matrix over $F$.
The *spectrum* of $A$ is the set
$$\sigma(A) = \{ \lambda \in F : A - \lambda I_n \text{ is not invertible} \}.$$
It is the set of [[eigenvalues|0BQAA2BK3Q]] of $A$.

## Notation

Other symbols are $\operatorname{spec}(A)$ and $\Lambda(A)$.
Mathlib defines `spectrum F A` for each element $A$ of an $F$-algebra, as the set of $\lambda$ for which $\lambda \cdot 1 - A$ is not a unit.
For the algebra of $n \times n$ matrices over $F$ this is the set above, since $\lambda I - A$ and $A - \lambda I$ differ only by a sign.

## Remarks

The definition uses invertibility, and the last sentence says that this gives the eigenvalues.
The reason is that a square matrix is [[invertible|0TWTS88TWN]] exactly when it is injective, so $A - \lambda I$ fails to be invertible exactly when $(A - \lambda I)v = 0$ for some $v \ne 0$.
The scalars $\lambda$ must lie in $F$, so the spectrum depends on the field.
The real matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has an empty spectrum over $\mathbb{R}$ and the spectrum $\{i, -i\}$ over $\mathbb{C}$.

The spectrum has at most $n$ elements, because each eigenvalue is a root of the characteristic polynomial, which has degree $n$.
Over $\mathbb{C}$ the spectrum of every square matrix of size $n \ge 1$ is nonempty.
Some authors count the eigenvalues with their multiplicities and call this list the spectrum.
The [[concept of the spectrum|0XPX5NC67E]] gives the rules and more examples.

## Explanations

### L1 human

The spectrum is the collection of all eigenvalues of a matrix.
It lists the stretch factors that the matrix shows in its special directions.
For a diagonal matrix, it is the set of diagonal entries.

### L2 human

We find the spectrum of $A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$.

1. The matrix $A - \lambda I$ is lower triangular, with the diagonal entries $3 - \lambda$ and $5 - \lambda$.
2. Its determinant is $(3 - \lambda)(5 - \lambda)$, so it is invertible exactly when both diagonal entries are nonzero.
3. So $\sigma(A) = \{3, 5\}$.
4. Check: $A(0, 1) = (0, 5) = 5(0, 1)$, and $A(1, -2) = (3, 4 - 10) = (3, -6) = 3(1, -2)$.

The typical use is the test "is $A - \lambda I$ singular?" for one candidate $\lambda$.
Watch out: forming $A - \lambda I$ changes only the diagonal entries of $A$, not the others.
