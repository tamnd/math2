---
tag: PRB44DTZ1P
kind: example
name: Two planes meeting in a line
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
instance_of: [0GT4WWGWH2, KQT68YPHD1, QJ0P26J9BV]
uses: [0GT4WWGWH2, 0WF5AQYTW6, KQT68YPHD1]
sources:
  - book: isbn:9780321982384
    locator: Section 1.2
---

## Example

Consider the system over $\mathbb{R}$
$$x + y + z = 3, \qquad x - y + 3z = 1.$$
It has $2$ equations and $3$ unknowns, so it is [[underdetermined|QJ0P26J9BV]].
We reduce it and write its solutions in [[parametric form|KQT68YPHD1]].

1. The augmented matrix is
$$\left[\begin{array}{rrr|r} 1 & 1 & 1 & 3 \\ 1 & -1 & 3 & 1 \end{array}\right].$$
2. The operation $R_2 - R_1$ gives $(0, -2, 2 \mid -2)$, and scaling by $-\tfrac12$ gives $(0, 1, -1 \mid 1)$.
3. The operation $R_1 - R_2$ gives $(1, 0, 2 \mid 2)$. So the [[reduced row echelon form|0WF5AQYTW6]] is
$$\left[\begin{array}{rrr|r} 1 & 0 & 2 & 2 \\ 0 & 1 & -1 & 1 \end{array}\right].$$
4. The pivot columns are columns $1$ and $2$, so $x$ and $y$ are basic variables and $z$ is free.
5. Put $z = t$. The two rows say $x + 2t = 2$ and $y - t = 1$, so $x = 2 - 2t$ and $y = 1 + t$.
6. The solution set is the line
$$\set{(2, 1, 0) + t(-2, 1, 1) : t \in \mathbb{R}}.$$
7. Check $t = 0$, the point $(2, 1, 0)$: $2 + 1 + 0 = 3$ and $2 - 1 + 0 = 1$. Check $t = 1$, the point $(0, 2, 1)$: $0 + 2 + 1 = 3$ and $0 - 2 + 3 = 1$.

## Remarks

Two planes that are not parallel meet in a line, and the example shows how elimination finds that line.
The direction $(-2, 1, 1)$ solves the homogeneous system, since $-2 + 1 + 1 = 0$ and $-2 - 1 + 3 = 0$.
So the solutions are one particular solution plus the homogeneous solutions, as the [[structure theorem|PDH3HKXWAZ]] says.
If you change the second equation to $2x + 2y + 2z = 5$, the planes become parallel and the system has no solution.
If you add a third equation that is not a combination of the first two, the line is cut down to a point.

## Explanations

### L1 human

Two planes that are not parallel cut each other along a line.
Every point of that line solves both equations, so there are infinitely many solutions.
We describe them with one number $t$ that slides along the line.

### L2 human

To describe a line of solutions, reduce the augmented matrix to reduced row echelon form and give each free variable a parameter.
Then solve each row for its basic variable, and check two different values of the parameter in the original equations.
Watch out: other choices are also correct.
If you take $x$ as the free variable, you get a different formula for the same line, and both formulas describe the same set of points.
