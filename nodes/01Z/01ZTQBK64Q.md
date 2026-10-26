---
tag: 01ZTQBK64Q
kind: statement
role: proposition
name: Adding a multiple of one row to another preserves the determinant
msc: [15A15]
uses: [0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Statement

Let $K$ be a commutative ring, let $A$ be an $n \times n$ matrix over $K$, and let $c \in K$.
Let $i \ne j$, and let $B$ be the matrix that results when $c$ times row $j$ of $A$ is added to row $i$.
Then $\det B = \det A$, where $\det$ is the [[determinant|00KDZRW4C0]].

## Remarks

By linearity in row $i$, $\det B = \det A + c \det A'$, where $A'$ has two equal rows; so $\det A' = 0$.
This is the reason why [[Gaussian elimination|0JVJ2WCXZH]] computes determinants efficiently.
The same holds for columns.

## Explanations

### L1 human

Adding a multiple of one row to another row shears the box spanned by the rows.
A shear does not change the volume.
So this row operation keeps the determinant.
