---
tag: YM0PB9F9HG
kind: example
name: Three planes meeting in one point
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
instance_of: [0GT4WWGWH2]
uses: [0GT4WWGWH2, 04XWH28452, 0ATFVE08MW]
sources:
  - book: isbn:9780321982384
    locator: Section 1.1
---

## Example

Consider the [[system of linear equations|0GT4WWGWH2]] over $\R$
$$x + y + z = 6, \qquad 2x - y + z = 3, \qquad x + 2y - z = 2.$$
We solve it with [[elementary row operations|04XWH28452]] on the augmented matrix and check the answer.

1. The augmented matrix is $\left[\begin{array}{rrr|r} 1 & 1 & 1 & 6 \\ 2 & -1 & 1 & 3 \\ 1 & 2 & -1 & 2 \end{array}\right]$.
2. $R_2 \leftarrow R_2 - 2R_1$ gives the row $(0, -3, -1 \mid -9)$.
3. $R_3 \leftarrow R_3 - R_1$ gives the row $(0, 1, -2 \mid -4)$.
4. Swap $R_2$ and $R_3$, so that the pivot of row 2 is $1$.
5. $R_3 \leftarrow R_3 + 3R_2$ gives $(0, -3, -1 \mid -9) + (0, 3, -6 \mid -12) = (0, 0, -7 \mid -21)$.
6. The matrix is now $\left[\begin{array}{rrr|r} 1 & 1 & 1 & 6 \\ 0 & 1 & -2 & -4 \\ 0 & 0 & -7 & -21 \end{array}\right]$, in echelon form.
7. [[Back substitution|0ATFVE08MW]]: $z = -21 / (-7) = 3$, then $y = -4 + 2 \cdot 3 = 2$, then $x = 6 - 2 - 3 = 1$.
8. Check: $1 + 2 + 3 = 6$, $2 - 2 + 3 = 3$ and $1 + 4 - 3 = 2$.

So the unique solution is $(x, y, z) = (1, 2, 3)$.

## Remarks

Each equation describes a plane in $\R^3$, and the three planes meet in the single point $(1, 2, 3)$.
In the column picture the same fact reads $1 \cdot (1, 2, 1) + 2 \cdot (1, -1, 2) + 3 \cdot (1, 1, -1) = (6, 3, 2)$, see [[linear systems as vector equations|E7SAHXQEVC]].
Each column of the coefficient matrix has a pivot, so the solution is unique for every right-hand side.

## Explanations

### L1 human

Three planes in space usually meet in one point, like two walls and the floor of a room meet in a corner.
Elimination removes $x$ from two equations, then $y$ from one, so that the last equation has only $z$.
Then we find $z$, then $y$, then $x$.

### L2 human

The typical use of this pattern is any $3 \times 3$ system with a unique solution.

1. Use row 1 to clear the first column below it.
2. Use row 2 to clear the second column below it.
3. Solve the last equation, then work upwards.

A trap: in step 5 it is easy to add $3R_1$ in place of $3R_2$; always name the rows you combine.
