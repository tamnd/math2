---
tag: ~1a0caa3d
kind: example
name: A right eigenvector that is not a left eigenvector
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
not_instance_of:
  - target: ~d0c39701
    note: The row vector (1, 0) is the transpose of a right eigenvector of A, but (1, 0)A = (1, 1) is not a multiple of (1, 0)
uses: [~d0c39701, 0B5H4208Z9]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Left and right eigenvectors
---

## Example

Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$, as in [[left and right eigenvectors of a triangular matrix|~4dea89e6]].

1. $A(1, 0)^{\mathsf T} = (1, 0)^{\mathsf T}$. So $(1, 0)^{\mathsf T}$ is a right [[eigenvector|0B5H4208Z9]] for the eigenvalue $1$.
2. As a row vector, $(1, 0)A = (1 \cdot 1 + 0 \cdot 0,\ 1 \cdot 1 + 0 \cdot 2) = (1, 1)$.
3. $(1, 1)$ is not a multiple of $(1, 0)$. So $(1, 0)$ is not a [[left eigenvector|~d0c39701]] of $A$.
4. The left eigenvector for $1$ is $(1, -1)$: $(1, -1)A = (1, 1 - 2) = (1, -1)$.

## Remarks

- The left eigenvectors of $A$ are the transposes of the right eigenvectors of $A^{\mathsf T}$, not of $A$.
- For a symmetric matrix, $A^{\mathsf T} = A$, and the two kinds of eigenvectors agree up to transpose.

## Explanations

### L1 human

Multiplying a row vector by $A$ from the left uses the columns of $A$, not its rows.
So the right eigenvector $(1, 0)$ need not work from the left.
Here it does not.

### L2 human

The typical lesson is to compute left eigenvectors from $A^{\mathsf T}$.
A trap is to transpose a right eigenvector of a nonsymmetric matrix and use it as a left eigenvector.
