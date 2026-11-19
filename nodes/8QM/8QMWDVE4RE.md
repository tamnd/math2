---
tag: 8QMWDVE4RE
kind: example
name: A homogeneous system with only the trivial solution
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
instance_of: [04KGXJG1A2]
uses: [04KGXJG1A2, Y0HXCJRB9B]
sources:
  - book: isbn:9780321982384
    locator: Section 1.5
---

## Example

Consider the [[homogeneous system|04KGXJG1A2]] over $\R$
$$x + y + z = 0, \qquad 2x - y + z = 0, \qquad x + 2y - z = 0.$$

1. $R_2 \leftarrow R_2 - 2R_1$ gives $(0, -3, -1)$.
2. $R_3 \leftarrow R_3 - R_1$ gives $(0, 1, -2)$.
3. Swap $R_2$ and $R_3$.
4. $R_3 \leftarrow R_3 + 3R_2$ gives $(0, 0, -7)$.
5. Every column has a pivot, so there are no free variables.
6. Back substitution: $-7z = 0$ gives $z = 0$, then $y = 2z = 0$, then $x = -y - z = 0$.
7. So the only solution is the [[trivial|Y0HXCJRB9B]] solution $(0, 0, 0)$.

## Remarks

The row operations are the same as in [[the three planes example|YM0PB9F9HG]], because they depend only on the coefficient matrix.
So the system there, with right side $(6, 3, 2)$, has exactly one solution, by [[the structure theorem|PDH3HKXWAZ]].

## Explanations

### L1 human

Three planes through the origin usually meet only at the origin.
Here they do: elimination leaves one pivot in each column, so nothing is free.

### L2 human

To test whether $Ax = 0$ has only the trivial solution:

1. Reduce $A$ to echelon form.
2. Count the pivots.
3. If the count equals the number of unknowns, only $x = 0$ solves the system.

A trap: a square matrix does not always pass this test; the matrix $\begin{bmatrix} 1 & 1 \\ 2 & 2 \end{bmatrix}$ has only one pivot.
