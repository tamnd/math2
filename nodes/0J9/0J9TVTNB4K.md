---
tag: 0J9TVTNB4K
kind: statement
role: proposition
name: Determinant of a block triangular matrix
msc: [15A15]
uses: [0C3CFHDN6R, 01AXG9KZQF]
sources:
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Determinant
---

## Statement

Let $K$ be a commutative ring, let $A$ be an $m \times m$ matrix, $B$ an $m \times n$ matrix and $D$ an $n \times n$ matrix over $K$.
Then the [[block matrix|0ASDFEQS6P]] satisfies
$$\det \begin{pmatrix} A & B \\ 0 & D \end{pmatrix} = \det A \cdot \det D,$$
where $0$ is the $n \times m$ zero matrix and $\det$ is the [[determinant|00KDZRW4C0]].

## Remarks

The same holds for the lower block triangular matrix $\begin{pmatrix} A & 0 \\ C & D \end{pmatrix}$.
It generalizes the rule for [[triangular matrices|0K1KKMFHYH]].
For a general block matrix, $\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} \ne \det A \det D - \det B \det C$ in general.

## Explanations

### L1 human

When a matrix has a block of zeros in its lower left corner, its determinant splits.
It is the product of the determinants of the two diagonal blocks.
The block $B$ does not matter, just like the entries above the diagonal of a triangular matrix.
