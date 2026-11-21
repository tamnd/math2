---
tag: XJX2NN45ED
kind: example
name: Three lines without a common point
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
instance_of: [0X6V9B1V10, 0JVJ2WCXZH, QJ0P26J9BV]
uses: [0X6V9B1V10, 0JVJ2WCXZH, 04XWH28452]
sources:
  - url: https://en.wikipedia.org/wiki/Overdetermined_system
    locator: lead section
---

## Example

Consider the system over $\mathbb{R}$
$$x + y = 2, \qquad x - y = 0, \qquad x + 2y = 4.$$
It has $3$ equations and $2$ unknowns, so it is [[overdetermined|QJ0P26J9BV]].
We show by [[Gaussian elimination|0JVJ2WCXZH]] that it is [[inconsistent|0X6V9B1V10]].

1. The augmented matrix is
$$\left[\begin{array}{rr|r} 1 & 1 & 2 \\ 1 & -1 & 0 \\ 1 & 2 & 4 \end{array}\right].$$
2. Clear the first column: $R_2 - R_1$ gives $(0, -2 \mid -2)$, and $R_3 - R_1$ gives $(0, 1 \mid 2)$.
3. Scale row 2 by $-\tfrac12$ to get $(0, 1 \mid 1)$.
4. Clear the second column below row 2: $R_3 - R_2$ gives $(0, 0 \mid 1)$.
5. The last row says $0x + 0y = 1$. No pair of numbers satisfies it, so the system has no solution.

## Remarks

The surprise is that any two of the three lines do meet.
The first two meet at $(1, 1)$, which fails the third equation, since $1 + 2 = 3 \ne 4$.
The first and third meet at $(0, 2)$, which fails the second, since $0 - 2 \ne 0$.
The second and third meet at $(\tfrac43, \tfrac43)$, which fails the first, since $\tfrac83 \ne 2$.
So the lines form a triangle, and no point lies on all three.

A small change makes the system consistent.
If the third equation is $x + 2y = 3$, the last row becomes $(0, 0 \mid 0)$, and all three lines pass through $(1, 1)$.

## Explanations

### L1 human

Draw the three lines and you see a small triangle.
Each corner lies on two lines but not on the third.
So no point is on all three lines, and the system has no solution.

### L2 human

This pattern appears when measured data should fit a model exactly.
Reduce the augmented matrix and look for a row $(0, \dots, 0 \mid c)$ with $c \ne 0$.
If you find one, the data do not fit exactly, and [[least squares|0BYTQ4X1HC]] gives the best fit instead.
Watch out: if you check only the first two equations, you would wrongly accept $(1, 1)$ as a solution.
