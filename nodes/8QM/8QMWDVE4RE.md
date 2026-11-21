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

Consider the [[homogeneous system|04KGXJG1A2]] over $\mathbb{R}$
$$x + y + z = 0, \qquad 2x - y + z = 0, \qquad x + 2y - z = 0.$$
We show that $(0, 0, 0)$ is its only solution.

1. Clear the first column: $R_2 - 2R_1$ gives $(0, -3, -1)$, and $R_3 - R_1$ gives $(0, 1, -2)$.
2. Swap the new rows 2 and 3, and clear the second column with $R_3 + 3R_2$:
$$\begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & -2 \\ 0 & -3 & -1 \end{pmatrix} \to \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & -2 \\ 0 & 0 & -7 \end{pmatrix}.$$
3. Every column has a pivot, so there are no free variables.
4. Back substitution gives $-7z = 0$, so $z = 0$, then $y = 2z = 0$, then $x = -y - z = 0$.
5. So the only solution is the [[trivial|Y0HXCJRB9B]] solution $(0, 0, 0)$.

## Remarks

The row operations are the same as in [[three planes meeting in one point|YM0PB9F9HG]], because they depend only on the coefficient matrix.
Since the homogeneous system has only the solution $0$, the system there with right side $(6, 3, 2)$ has exactly one solution, by the [[structure theorem|PDH3HKXWAZ]].
If you change the last equation to $3x + 0y + 2z = 0$, which is the sum of the first two, one column loses its pivot and a whole line of solutions appears.

## Explanations

### L1 human

Three planes through the origin often meet only at the origin.
Here they do: elimination leaves one pivot in each column, so no unknown is free.

### L2 human

To test whether $Ax = 0$ has only the trivial solution, reduce $A$ to echelon form and count the pivots.
If the count equals the number of unknowns, only $x = 0$ solves the system.
Watch out: a square matrix does not always pass this test.
The matrix $\begin{bmatrix} 1 & 1 \\ 2 & 2 \end{bmatrix}$ has only one pivot, and $(1, -1)$ is a nontrivial solution.
