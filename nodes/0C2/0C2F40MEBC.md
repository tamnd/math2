---
tag: 0C2F40MEBC
kind: statement
role: theorem
name: Determinant is the product of the eigenvalues
msc: [15A15, 15A18]
uses: [0T0X8GTYYS, 0ZND7NQ970, 0S7A0EMPF4]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Eigenvalues and characteristic polynomial
---

## Statement

Let $F$ be a field and let $A$ be an $n \times n$ matrix over $F$.
Assume that the characteristic polynomial of $A$ splits over $F$ as $p_A(t) = (t - \lambda_1) \cdots (t - \lambda_n)$.
Then
$$\det A = \lambda_1 \lambda_2 \cdots \lambda_n.$$

## Remarks

The $\lambda_i$ are the [[eigenvalues|0BQAA2BK3Q]] of $A$, each repeated according to its [[algebraic multiplicity|0FY42N02DV]].
The statement follows by comparing the constant coefficients, see [[the determinant as a coefficient|0T0X8GTYYS]].
For example, $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ has eigenvalues $1$ and $3$, and determinant $3$.

## Explanations

### L1 human

The determinant of a matrix is the product of its eigenvalues, counted with multiplicity.
This agrees with the volume picture: in a basis of eigenvectors, the map stretches each direction by its eigenvalue.
The volume then changes by the product of these factors.
