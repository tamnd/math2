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

Consider the system over $\R$
$$x + y + z = 3, \qquad x - y + 3z = 1.$$
It has $2$ equations and $3$ unknowns, so it is underdetermined.

1. The augmented matrix is $\left[\begin{array}{rrr|r} 1 & 1 & 1 & 3 \\ 1 & -1 & 3 & 1 \end{array}\right]$.
2. $R_2 \leftarrow R_2 - R_1$ gives $(0, -2, 2 \mid -2)$.
3. $R_2 \leftarrow -\tfrac12 R_2$ gives $(0, 1, -1 \mid 1)$.
4. $R_1 \leftarrow R_1 - R_2$ gives $(1, 0, 2 \mid 2)$.
5. The [[reduced row echelon form|0WF5AQYTW6]] is $\left[\begin{array}{rrr|r} 1 & 0 & 2 & 2 \\ 0 & 1 & -1 & 1 \end{array}\right]$.
6. The pivot columns are $1$ and $2$, so $x$ and $y$ are basic and $z$ is free.
7. Put $z = t$. The rows give $x = 2 - 2t$ and $y = 1 + t$.
8. So the solution set is $\set{(2, 1, 0) + t(-2, 1, 1) : t \in \R}$, a line in [[parametric form|KQT68YPHD1]].
9. Check $t = 0$: $2 + 1 + 0 = 3$ and $2 - 1 + 0 = 1$.
10. Check $t = 1$, the point $(0, 2, 1)$: $0 + 2 + 1 = 3$ and $0 - 2 + 3 = 1$.

## Remarks

The direction $(-2, 1, 1)$ solves the homogeneous system: $-2 + 1 + 1 = 0$ and $-2 - 1 + 3 = 0$.
This illustrates [[the structure theorem|PDH3HKXWAZ]]: solutions are one particular solution plus homogeneous solutions.

## Explanations

### L1 human

Two planes that are not parallel cut each other along a line.
Every point of that line solves both equations, so there are infinitely many solutions.
We describe them with one parameter $t$ that slides along the line.

### L2 human

To describe a line of solutions, follow these steps.

1. Reduce the augmented matrix to reduced row echelon form.
2. Name each free variable with a parameter.
3. Solve each row for its basic variable.
4. Check two different values of the parameter in the original equations.

A trap: choosing $x$ as the free variable is also correct, but it gives a different-looking parametrization of the same line.
