---
tag: HQVWQBHQSC
kind: example
name: Pivot positions, basic variables and free variables of a 3 by 5 matrix
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
instance_of: [0J0BBCMJ5W]
uses: [0BCMGDHZGR, 0NNR68BFRY]
sources:
  - book: isbn:9780321982384
    locator: Section 1.2
---

## Example

Pivots need not sit on the diagonal, and a zero column always gives a free variable.
Let
$$A = \begin{bmatrix} 0 & 1 & 2 & 0 & 3 \\ 0 & 2 & 4 & 1 & 7 \\ 0 & 0 & 0 & 1 & 1 \end{bmatrix}$$
over $\mathbb{R}$, the coefficient matrix of $Ax = 0$ in $x_1, \dots, x_5$.

1. Column 1 is zero, so the first pivot is in column 2, and the entry $1$ at $(1, 2)$ is nonzero.
2. The step $R_2 \leftarrow R_2 - 2R_1$ makes row 2 equal to $(0, 0, 0, 1, 1)$.
3. The step $R_3 \leftarrow R_3 - R_2$ makes row 3 equal to $(0, 0, 0, 0, 0)$.
4. The result $\begin{bmatrix} 0 & 1 & 2 & 0 & 3 \\ 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$ is in echelon form, and in fact in [[reduced row echelon form|0NNR68BFRY]].
5. The [[pivot positions|0BCMGDHZGR]] are $(1, 2)$ and $(2, 4)$, so the pivot columns are $2$ and $4$, and the rank is $2$.
6. The basic variables are $x_2, x_4$, and the free variables are $x_1, x_3, x_5$.
7. The rows give $x_2 = -2x_3 - 3x_5$ and $x_4 = -x_5$.
8. Check the solution $(0, -2, 1, 0, 0)$ in $A$: $-2 + 2 = 0$, $-4 + 4 = 0$ and $0 = 0$.
9. Check the solution $(0, -3, 0, -1, 1)$ in $A$: $-3 + 3 = 0$, $-6 - 1 + 7 = 0$ and $-1 + 1 = 0$.

## Remarks

The null space has dimension $5 - 2 = 3$, with one basis vector for each free variable.
Setting one free variable to $1$ and the others to $0$ gives $e_1$, $(0, -2, 1, 0, 0)$ and $(0, -3, 0, -1, 1)$.

The pivot columns $2$ and $4$ of $A$ itself, the vectors $(1, 2, 0)$ and $(0, 1, 1)$, form a basis of the column space of $A$.
The pivot columns of the reduced matrix, $(1, 0, 0)$ and $(0, 1, 0)$, do not, since $(0, 1, 1)$ is not in their span.

## Explanations

### L1 human

Here the first column is all zeros, so the unknown $x_1$ does not appear at all and is free.
After two moves only two rows start a step, so only two unknowns are fixed.
The other three unknowns can be chosen freely.

### L2 human

1. Reduce to echelon form.
2. Mark the pivots and list their columns.
3. All other columns give free variables.

Watch out: in step 1 the first pivot is not in column 1, because pivots need not be on the diagonal.
