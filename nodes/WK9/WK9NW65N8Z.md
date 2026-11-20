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

Let $A = \begin{pmatrix} 1 & -1 \\ 2 & 0 \\ 0 & 1 \end{pmatrix}$ over $\R$, with columns $a_1 = (1, 2, 0)$ and $a_2 = (-1, 0, 1)$.

1. By the [[matrix-vector product|0PDVQEP0ZC]], $A(x, y) = x a_1 + y a_2 = (x - y,\ 2x,\ y)$.
2. So the [[column space|0F0RPPJ2TT]] is the set of these vectors, the image of the map $(x, y) \mapsto A(x, y)$ of $\R^2$ into $\R^3$.
3. The columns are independent: if $x a_1 + y a_2 = 0$, then the third entry gives $y = 0$ and the second gives $x = 0$. So $\dim \operatorname{Col}(A) = 2$.
4. A vector $(u, v, w)$ lies in $\operatorname{Col}(A)$ if and only if $u = x - y$ with $x = v/2$ and $y = w$. That is, $2u - v + 2w = 0$.
5. Check on the columns: $2 \cdot 1 - 2 + 0 = 0$ and $2 \cdot (-1) - 0 + 2 \cdot 1 = 0$.
6. Take $b = (1, 4, 1)$. Then $2 - 4 + 2 = 0$, so the system $Ax = b$ is [[consistent|0X6V9B1V10]]. The solution is $x = 2$, $y = 1$: $A(2, 1) = (1, 4, 1)$.
7. Take $b' = (1, 0, 0)$. Then $2 - 0 + 0 = 2 \ne 0$, so $Ax = b'$ has no solution.

## Remarks

- The column space here is a plane through the origin in $\R^3$, with normal vector $(2, -1, 2)$.
- The normal vector spans the left null space: $A^\top (2, -1, 2) = (2 - 2 + 0,\ -2 + 0 + 2) = (0, 0)$. This is the [[Fredholm alternative|4HH8C9V8JQ]] in a small case.

## Explanations

### L1 human

The column space is the set of all outputs of the matrix.
A system has a solution exactly when its right side is one of these outputs.

### L2 human

The column space of a $3 \times 2$ matrix of rank $2$ is a plane in $\R^3$, so it is cut out by one linear equation.
That equation is a test for consistency of $Ax = b$, and its coefficients form a vector in the null space of $A^\top$.
