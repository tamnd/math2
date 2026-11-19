---
tag: KEV3SBST22
kind: example
name: Matrices that fail the row echelon conditions
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
not_instance_of:
  - target: 0VYCDGMJJJ
    note: the first matrix has a zero row above a nonzero row, and the second has two leading entries in the same column
uses: [0F27PBRWD7]
sources:
  - url: https://en.wikipedia.org/wiki/Row_echelon_form
    locator: lead section
---

## Example

Let $M_1 = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 4 & 5 \end{bmatrix}$ and $M_2 = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 6 & 7 \end{bmatrix}$ over $\R$.

1. In $M_1$, row $2$ is zero and row $3$ is nonzero. So condition 1 of [[row echelon form|0F27PBRWD7]] fails.
2. Swapping $R_2$ and $R_3$ of $M_1$ gives $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 0 \end{bmatrix}$, which is in row echelon form.
3. In $M_2$, rows $2$ and $3$ both have their leading entry in column $2$. So condition 2 fails.
4. $R_3 \leftarrow R_3 - \tfrac32 R_2$ in $M_2$ gives $(0, 6 - 6, 7 - \tfrac{15}{2}) = (0, 0, -\tfrac12)$.
5. The result $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & -\tfrac12 \end{bmatrix}$ is in row echelon form.

## Remarks

Each failure is repaired by one more row operation, as in the [[existence proof|48XDCB74Q4]].
A matrix with a zero row in the middle has a swap still to do; a matrix with two leading entries in one column has an elimination still to do.

## Explanations

### L1 human

In the first table, an empty row sits in the middle; it must go to the bottom.
In the second table, two rows start in the same column; one of them must be cleared first.

### L2 human

1. If a zero row is not at the bottom, swap it down.
2. If two rows start in the same column, subtract a multiple of the upper row from the lower one.

A trap: leading entries that are not $1$ do not break the definition used here; they matter only in books that require leading $1$s.
