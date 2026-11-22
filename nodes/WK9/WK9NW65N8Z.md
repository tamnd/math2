---
tag: WK9NW65N8Z
kind: example
name: Column space of a matrix map and the consistency of a system
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
instance_of: [03AJKXH1AV]
uses: [0F0RPPJ2TT, 0X6V9B1V10, 0PDVQEP0ZC]
sources:
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: Column space
---

## Example

The column space of a $3 \times 2$ matrix of rank $2$ is a plane, and its equation tells us which systems can be solved.
Let
$$A = \begin{pmatrix} 1 & -1 \\ 2 & 0 \\ 0 & 1 \end{pmatrix}$$
over $\mathbb{R}$, with columns $a_1 = (1, 2, 0)$ and $a_2 = (-1, 0, 1)$.

1. By the [[matrix-vector product|0PDVQEP0ZC]], $A(x, y) = x a_1 + y a_2 = (x - y, 2x, y)$, so the [[column space|0F0RPPJ2TT]] is the set of all these vectors.
2. The columns are independent: if $x a_1 + y a_2 = 0$, the third entry gives $y = 0$, and then the second entry gives $x = 0$.
3. So $\dim \operatorname{Col}(A) = 2$, and the column space is a plane through the origin in $\mathbb{R}^3$.
4. A vector $(u, v, w)$ has the form $(x - y, 2x, y)$ exactly when $y = w$, $x = v/2$ and $u = v/2 - w$, so the plane is
$$\operatorname{Col}(A) = \{(u, v, w) : 2u - v + 2w = 0\}.$$
5. Check on the columns: $2 \cdot 1 - 2 + 2 \cdot 0 = 0$ and $2 \cdot (-1) - 0 + 2 \cdot 1 = 0$.
6. Take $b = (1, 4, 1)$; then $2 - 4 + 2 = 0$, so $Ax = b$ is [[consistent|0X6V9B1V10]], and indeed $A(2, 1) = (2 - 1, 4, 1) = (1, 4, 1)$.
7. Take $b' = (1, 0, 0)$; then $2 - 0 + 0 = 2 \ne 0$, so $Ax = b'$ has no solution.

## Remarks

The example shows that a description of the column space by equations is a test for consistency.
Here one equation is enough, because the plane has codimension $3 - 2 = 1$ in $\mathbb{R}^3$.

The coefficients of that equation form the normal vector $(2, -1, 2)$, and this vector lies in the null space of $A^{\mathsf{T}}$:
$$A^{\mathsf{T}} \begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix} = \begin{pmatrix} 2 - 2 + 0 \\ -2 + 0 + 2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}.$$
So $b$ is in the column space exactly when $b$ is orthogonal to the null space of $A^{\mathsf{T}}$, which is the [[Fredholm alternative|4HH8C9V8JQ]] in a small case.

If we drop the second column, the column space shrinks to the line through $(1, 2, 0)$, and two equations, such as $v = 2u$ and $w = 0$, are needed to describe it.

## Explanations

### L1 human

The column space is the set of all outputs of the matrix.
A system has a solution exactly when its right side is one of these outputs.
Here the outputs fill a flat plane in space, and the right side $(1, 0, 0)$ lies off that plane, so it can never come out.

### L2 human

To find the equation of the plane, write a general output $(x - y, 2x, y)$ and remove $x$ and $y$.
The last entry gives $y$, the middle entry gives $x$, and the first entry then must equal $v/2 - w$.
Multiplying by $2$ gives $2u - v + 2w = 0$.
Watch out: this equation is a condition on the right side $b$, so it lives in $\mathbb{R}^3$, not in the plane $\mathbb{R}^2$ of the unknowns.
