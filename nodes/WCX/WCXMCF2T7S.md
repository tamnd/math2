---
tag: WCXMCF2T7S
kind: example
name: Matrices in row echelon form that are not reduced
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
not_instance_of:
  - target: 0WF5AQYTW6
    note: the first matrix has a leading entry 3, and the second has a nonzero entry above a leading 1
uses: [0NNR68BFRY, 0F27PBRWD7]
sources:
  - url: https://en.wikipedia.org/wiki/Row_echelon_form
    locator: Reduced row echelon form
---

## Example

Let $N_1 = \begin{bmatrix} 1 & 2 & 0 \\ 0 & 3 & 1 \end{bmatrix}$ and $N_2 = \begin{bmatrix} 1 & 2 & 5 \\ 0 & 1 & 3 \end{bmatrix}$ over $\R$.

1. Both are in [[row echelon form|0F27PBRWD7]]: their leading entries are in columns $1$ and $2$, and they have no zero rows.
2. The leading entry of row 2 of $N_1$ is $3 \ne 1$. So condition 2 of [[reduced row echelon form|0NNR68BFRY]] fails.
3. In $N_2$, column 2 has a leading entry in row 2, and the entry $2$ above it is nonzero. So condition 3 fails.
4. Reduce $N_1$: $R_2 \leftarrow \tfrac13 R_2$ gives $(0, 1, \tfrac13)$, then $R_1 \leftarrow R_1 - 2R_2$ gives $(1, 0, -\tfrac23)$.
5. Reduce $N_2$: $R_1 \leftarrow R_1 - 2R_2$ gives $(1, 0, -1)$.
6. The RREFs are $\begin{bmatrix} 1 & 0 & -\tfrac23 \\ 0 & 1 & \tfrac13 \end{bmatrix}$ and $\begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 3 \end{bmatrix}$.

## Remarks

The two RREFs differ, so $N_1$ and $N_2$ are not row equivalent, by the uniqueness theorem.
Their pivot positions agree, which shows that pivot positions alone do not decide row equivalence.

## Explanations

### L1 human

A staircase is not yet fully reduced if a step starts with a number other than $1$, or if there is a nonzero number above a step.

### L2 human

1. Scale each pivot row so that its pivot is $1$.
2. Use each pivot to clear the entries above it.

A trap: entries in non-pivot columns, such as the $\tfrac13$ and $-\tfrac23$ in step 6, are allowed to be nonzero.
