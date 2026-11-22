---
tag: VBFC9PEMPF
kind: example
name: A system of two equations as one matrix equation
msc: ["15A06", "15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [0PDVQEP0ZC]
uses: [0CCQV3884B, 0GT4WWGWH2, 0HQFZAP3ND]
sources:
  - url: https://en.wikipedia.org/wiki/System_of_linear_equations
    locator: Matrix equation
---

## Example

A system of linear equations is one matrix equation in disguise, because each left side is a row of coefficients paired with the unknowns.
Consider the [[system|0GT4WWGWH2]]
$$x + 2y = 5, \qquad 3x - y = 1.$$

1. The [[coefficient matrix|0HQFZAP3ND]] holds the coefficients row by row, and the right sides form a column:
$$A = \begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix}, \qquad b = \begin{pmatrix} 5 \\ 1 \end{pmatrix}.$$
2. For $v = (x, y)^{\mathsf{T}}$, the [[product|0CCQV3884B]] pairs each row with $v$:
$$Av = \begin{pmatrix} 1 \cdot x + 2 \cdot y \\ 3 \cdot x + (-1) \cdot y \end{pmatrix} = \begin{pmatrix} x + 2y \\ 3x - y \end{pmatrix}.$$
3. These are the two left sides, so the system is the single equation $Av = b$.
4. The vector $v = (1, 2)^{\mathsf{T}}$ gives $Av = (1 + 4, 3 - 2)^{\mathsf{T}} = (5, 1)^{\mathsf{T}} = b$, so it is a solution.
5. In the column view, the same check reads
$$1 \begin{pmatrix} 1 \\ 3 \end{pmatrix} + 2 \begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 5 \\ 1 \end{pmatrix},$$
so $b$ is a combination of the columns of $A$ with the weights $1$ and $2$.

## Remarks

The solution is unique.
The second equation gives $y = 3x - 1$, and then the first becomes $x + 6x - 2 = 5$, so $x = 1$ and $y = 2$.

The matrix form separates the coefficients from the right side.
Changing $b$ to $(0, 7)^{\mathsf{T}}$ keeps $A$, and the solution becomes $v = (2, -1)^{\mathsf{T}}$, since $2 - 2 = 0$ and $6 + 1 = 7$.
Changing the coefficient $-1$ to $6$ makes the second row three times the first, and then $Av = b$ has a solution only when $b_2 = 3b_1$.
Methods to solve $Av = b$ in general belong to the topic on [[systems of linear equations|DXSXFVDMXQ]].

## Explanations

### L1 human

A system of equations has a table of coefficients and a list of right sides.
The matrix-vector product packs the left sides into one column, so the system becomes $Av = b$.
Here the table is $\begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix}$ and the list is $(5, 1)$.

### L2 human

The two views of $Av$ match two views of the system.
The row view is the list of equations, each a line in the plane, and the solution $(1, 2)$ is where the lines meet.
The column view asks for weights that combine the columns into $b$, and here the weights are $1$ and $2$.
The trap is to put the coefficients of $x$ in a row of $A$, which gives the transposed matrix and a different system.
