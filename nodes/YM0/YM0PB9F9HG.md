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

Consider the [[system of linear equations|0GT4WWGWH2]] over $\mathbb{R}$
$$x + y + z = 6, \qquad 2x - y + z = 3, \qquad x + 2y - z = 2.$$
We solve it with [[elementary row operations|04XWH28452]] on the augmented matrix, and then we check the answer.

1. The augmented matrix is
$$\left[\begin{array}{rrr|r} 1 & 1 & 1 & 6 \\ 2 & -1 & 1 & 3 \\ 1 & 2 & -1 & 2 \end{array}\right].$$
2. Clear the first column below row 1. The operation $R_2 - 2R_1$ gives the row $(0, -3, -1 \mid -9)$, and $R_3 - R_1$ gives $(0, 1, -2 \mid -4)$.
3. Swap the new rows 2 and 3, so that row 2 starts with the entry $1$. This avoids fractions in the next step.
4. Clear the second column below row 2 with $R_3 + 3R_2$:
$$(0, -3, -1 \mid -9) + (0, 3, -6 \mid -12) = (0, 0, -7 \mid -21).$$
5. The matrix is now in echelon form:
$$\left[\begin{array}{rrr|r} 1 & 1 & 1 & 6 \\ 0 & 1 & -2 & -4 \\ 0 & 0 & -7 & -21 \end{array}\right].$$
6. [[Back substitution|0ATFVE08MW]] from the last row up gives $z = -21 / (-7) = 3$, then $y = -4 + 2 \cdot 3 = 2$, then $x = 6 - 2 - 3 = 1$.
7. Check in the original equations: $1 + 2 + 3 = 6$, $2 - 2 + 3 = 3$ and $1 + 4 - 3 = 2$.

So the system has exactly one solution, $(x, y, z) = (1, 2, 3)$.

## Remarks

In the row picture, each equation is a plane in $\mathbb{R}^3$, and the three planes meet in the single point $(1, 2, 3)$.
In the column picture, the same fact says that the right side is a combination of the columns:
$$1 \cdot (1, 2, 1) + 2 \cdot (1, -1, 2) + 3 \cdot (1, 1, -1) = (6, 3, 2),$$
as in [[linear systems as vector equations|E7SAHXQEVC]].
Every column of the coefficient matrix has a pivot, so the solution is unique, and it stays unique if you change the right side $(6, 3, 2)$ to any other vector.
If instead you change the last equation to $3x + 0y + 2z = 9$, which is $R_1 + R_2$, the planes share a whole line and the solution is no longer unique.

## Explanations

### L1 human

Three planes in space often meet in one point, as two walls and the floor of a room meet in a corner.
Elimination removes $x$ from two equations and then $y$ from one, so that the last equation has only $z$.
Then we find $z$, then $y$, then $x$.

### L2 human

The same three moves solve any $3 \times 3$ system with a unique solution.
Use row 1 to clear the first column below it, use row 2 to clear the second column below it, and then solve from the bottom up.
Watch out in step 4: it is easy to add $3R_1$ in place of $3R_2$.
Name the rows that you combine at every step, and check the final answer in the original equations.
