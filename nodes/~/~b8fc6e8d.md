---
tag: ~b8fc6e8d
kind: definition
name: Spectrum of a matrix
msc: [15A18]
defines: ~4e9e4286
uses: [~0aea559b]
sources:
  - url: https://en.wikipedia.org/wiki/Spectrum_of_a_matrix
    locator: Definition
---

## Definition

Let $F$ be a field and let $A$ be an $n \times n$ matrix over $F$.
The *spectrum* of $A$ is the set
$$\sigma(A) = \{\lambda \in F : A - \lambda I_n \text{ is not invertible}\}.$$
It is the set of [[eigenvalues|~13fe038c]] of $A$.

## Remarks

The spectrum has at most $n$ elements, because each eigenvalue is a root of the characteristic polynomial of degree $n$.
Over $\C$, the spectrum of each square matrix is nonempty.
The spectrum depends on the field: the real matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has empty spectrum over $\R$ and spectrum $\{i, -i\}$ over $\C$.
Some authors count the eigenvalues with their multiplicities and call this list the spectrum.

## Explanations

### L1 human

The spectrum is the list of all eigenvalues of a matrix.
It tells us the scaling factors that the matrix shows in special directions.
For a diagonal matrix, it is the set of diagonal entries.
