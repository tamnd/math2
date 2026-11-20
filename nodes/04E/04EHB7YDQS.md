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

Let $F$ be a field and let $A$ be an $n \times n$ matrix over $F$.
The *spectrum* of $A$ is the set
$$\sigma(A) = \{\lambda \in F : A - \lambda I_n \text{ is not invertible}\}.$$
It is the set of [[eigenvalues|0BQAA2BK3Q]] of $A$.

## Notation

Other symbols are $\operatorname{spec}(A)$ and $\Lambda(A)$.
Mathlib defines `spectrum F A` for each element $A$ of an $F$-algebra, as the set of $\lambda$ with $\lambda \cdot 1 - A$ not a unit.
For the algebra of $n \times n$ matrices, this is the set above.

## Remarks

The spectrum has at most $n$ elements, because each eigenvalue is a root of the characteristic polynomial of degree $n$.
Over $\C$, the spectrum of each square matrix of size $n \ge 1$ is nonempty.
The spectrum depends on the field: the real matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has empty spectrum over $\R$ and spectrum $\{i, -i\}$ over $\C$.
Some authors count the eigenvalues with their multiplicities and call this list the spectrum.

## Explanations

### L1 human

The spectrum is the list of all eigenvalues of a matrix.
It tells us the scaling factors that the matrix shows in special directions.
For a diagonal matrix, it is the set of diagonal entries.

### L2 human

We find the spectrum of $A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$.

1. $A - \lambda I$ is lower triangular with diagonal entries $3 - \lambda$ and $5 - \lambda$.
2. A triangular matrix is invertible exactly when its diagonal entries are nonzero.
3. So $\sigma(A) = \{3, 5\}$.
4. Check: $A (0, 1)^{\mathsf{T}} = (0, 5)^{\mathsf{T}}$, and $A (1, -2)^{\mathsf{T}} = (3, 4 - 10)^{\mathsf{T}} = (3, -6)^{\mathsf{T}} = 3 (1, -2)^{\mathsf{T}}$.

The typical use is the test "$A - \lambda I$ is singular" for one candidate $\lambda$.
A trap: $A - \lambda I$ changes only the diagonal entries of $A$, not all entries.
