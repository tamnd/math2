---
tag: 0K1KKMFHYH
kind: statement
role: proposition
name: Determinant of a triangular matrix
msc: [15A15]
uses: [0C3CFHDN6R, 0MKABWDRNC]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Properties
---

## Statement

Let $K$ be a commutative ring and let $A = (a_{ij})$ be an $n \times n$ upper or lower [[triangular matrix|0N4XY7Z3NN]] over $K$.
Then
$$\det A = a_{11} a_{22} \cdots a_{nn},$$
where $\det$ is the [[determinant|00KDZRW4C0]].

## Remarks

In the [[Leibniz formula|016PE4VZ8Q]], all terms except the term of the identity permutation contain an entry below, or above, the diagonal, so they are zero.
Row reduction to a triangular matrix, with this rule, is a practical way to compute determinants.
A triangular matrix over a field is invertible if and only if all its diagonal entries are nonzero.

## Explanations

### L1 human

For a triangular matrix, the determinant is the product of the diagonal entries.
The entries above the diagonal do not matter.
For example, $\det \begin{pmatrix} 2 & 7 \\ 0 & 3 \end{pmatrix} = 6$.
