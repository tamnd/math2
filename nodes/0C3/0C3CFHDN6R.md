---
tag: 0C3CFHDN6R
kind: definition
name: Determinant
msc: [15A15]
defines: 00KDZRW4C0
uses: [0MSWYWHYF5, 0CP7YY6NAG, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: As an alternating multilinear form
---

## Definition

Let $K$ be a commutative ring and let $n \ge 1$.
There is exactly one map $\det \colon M_n(K) \to K$ with these properties:

1. $\det A$ is a multilinear function of the $n$ rows of $A$.
2. $\det A = 0$ when two rows of $A$ are equal.
3. $\det I_n = 1$, for the [[identity matrix|06DW9BAWB1]] $I_n$.

This map is the *determinant*.

## Remarks

In other words, $\det$ is the unique [[alternating multilinear map|0K6CH0MT0F]] of the rows with value $1$ on $I_n$.
The [[Leibniz formula|016PE4VZ8Q]] gives $\det A$ as a sum over permutations.
For $n = 2$, $\det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$.
The same characterization holds with columns in place of rows, because $\det A^T = \det A$.

## Explanations

### L1 human

The determinant gives one number for each square matrix.
Over the real numbers, its absolute value is the factor by which the matrix scales volume, and its sign tells if the matrix flips orientation.
A real square matrix is invertible exactly when its determinant is not zero.
