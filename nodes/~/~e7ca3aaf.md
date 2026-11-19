---
tag: ~e7ca3aaf
kind: example
name: The three row operations on a 2 by 2 matrix and their inverses
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
instance_of: [04XWH28452]
uses: [0DE5R5EB4D, 01REXW3WWE, ~6410ee51]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_matrix
    locator: Elementary row operations
---

## Example

Let $M = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ over $\R$.
We apply one [[elementary row operation|0DE5R5EB4D]] of each type and undo it.

1. Swap: $R_1 \leftrightarrow R_2$ gives $\begin{bmatrix} 3 & 4 \\ 1 & 2 \end{bmatrix}$. The same swap gives back $M$.
2. Scale: $R_1 \leftarrow 5R_1$ gives $\begin{bmatrix} 5 & 10 \\ 3 & 4 \end{bmatrix}$. Then $R_1 \leftarrow \tfrac15 R_1$ gives back $M$.
3. Add: $R_2 \leftarrow R_2 - 3R_1$ gives $\begin{bmatrix} 1 & 2 \\ 0 & -2 \end{bmatrix}$. Then $R_2 \leftarrow R_2 + 3R_1$ gives back $M$.
4. The [[elementary matrix|01REXW3WWE]] of step 3 is $E = \begin{bmatrix} 1 & 0 \\ -3 & 1 \end{bmatrix}$, the result of the same step on $I_2$.
5. Check: $EM = \begin{bmatrix} 1 & 2 \\ 3 - 3 & 4 - 6 \end{bmatrix} = \begin{bmatrix} 1 & 2 \\ 0 & -2 \end{bmatrix}$.
6. The inverse step gives $E^{-1} = \begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix}$, and $E^{-1}E = \begin{bmatrix} 1 & 0 \\ 3 - 3 & 1 \end{bmatrix} = I_2$.

## Remarks

The example illustrates [[the theorem on row operations|~6410ee51]]: each inverse is an operation of the same type.
If the scale factor in step 2 were $0$, the first row would become zero and no operation could bring back $(1, 2)$.

## Explanations

### L1 human

Every row move has an "undo" button.
A swap is undone by the same swap.
Multiplying by $5$ is undone by dividing by $5$.
Subtracting three times row 1 is undone by adding three times row 1.

### L2 human

To find the elementary matrix of a row operation on $m$ rows:

1. Start with the identity matrix $I_m$.
2. Apply the operation to it.
3. The result $E$ satisfies $EM = $ (the operation applied to $M$) for every $M$ with $m$ rows.

A trap: the order matters; $E_2E_1M$ means that the operation of $E_1$ is done first.
