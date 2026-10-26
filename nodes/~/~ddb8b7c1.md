---
tag: ~ddb8b7c1
kind: statement
role: theorem
name: A matrix is diagonalisable iff it has a basis of eigenvectors
msc: [15A20]
uses: [~bc4ca369, ~20152ff2, ~6c1abb8a]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonalizable_matrix
    locator: Characterization
---

## Statement

Let $F$ be a field and let $A$ be an $n \times n$ matrix over $F$.
Then $A$ is [[diagonalisable|~e1050cd7]] if and only if $F^n$ has a [[basis|~4af6ac42]] of [[eigenvectors|~606eab95]] of $A$.
If $v_1, \dots, v_n$ is such a basis with $A v_i = \lambda_i v_i$, and $P$ has the columns $v_1, \dots, v_n$, then $P^{-1} A P$ is the diagonal matrix with entries $\lambda_1, \dots, \lambda_n$.

## Remarks

The equation $AP = PD$ says column by column that $A v_i = \lambda_i v_i$.
Equivalently, $F^n$ is the direct sum of the eigenspaces of $A$.
Equivalently, the sum of the [[geometric multiplicities|~5fe59876]] of the eigenvalues is $n$.

## Explanations

### L1 human

To diagonalise a matrix, we need $n$ independent eigenvectors.
We put them as columns into a matrix $P$.
Then $P^{-1} A P$ is diagonal, with the eigenvalues on the diagonal.
