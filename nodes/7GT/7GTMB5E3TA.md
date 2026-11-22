---
tag: 7GTMB5E3TA
kind: example
name: The four fundamental subspaces of a 3 × 4 matrix
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
illustrates: [73DVECPAT6]
uses: [0F0RPPJ2TT, 0EP73HK4C4, 0PQ2GGY1QV, 05HQYM0R4G]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_linear_algebra
    locator: lead section
---

## Example

One $3 \times 4$ matrix of rank $2$ shows all four subspaces, their dimensions and their orthogonality at once.
Let
$$A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 3 & 6 & 1 & 5 \end{pmatrix}$$
over $\mathbb{R}$, so $m = 3$ and $n = 4$.
By the [[column space example|AGHYPF25CY]], its reduced row echelon form has the nonzero rows $(1, 2, 0, 1)$ and $(0, 0, 1, 2)$, with pivots in columns 1 and 3, so $r = 2$.

1. [[Column space|0F0RPPJ2TT]]: columns 1 and 3 of $A$, namely $(1, 2, 3)$ and $(0, 1, 1)$, form a basis, so $\dim \operatorname{Col}(A) = 2 = r$.
2. [[Null space|0PQ2GGY1QV]]: by the [[null space example|GG03BSSZ43]], the vectors $(-2, 1, 0, 0)$ and $(-1, 0, -2, 1)$ form a basis, so $\dim \operatorname{Null}(A) = 2 = n - r$.
3. [[Row space|0EP73HK4C4]]: the nonzero rows $(1, 2, 0, 1)$ and $(0, 0, 1, 2)$ of the reduced form are a basis, so $\dim \operatorname{Row}(A) = 2 = r$.
4. Left null space: by the [[left null space example|KJ7X8CZWNT]], the vector $(-1, -1, 1)$ is a basis, so $\dim \operatorname{Null}(A^{\mathsf{T}}) = 1 = m - r$.
5. Row space against null space, with the [[dot product|05HQYM0R4G]]: $(1, 2, 0, 1) \cdot (-2, 1, 0, 0) = -2 + 2 = 0$ and $(1, 2, 0, 1) \cdot (-1, 0, -2, 1) = -1 + 1 = 0$.
6. Also $(0, 0, 1, 2) \cdot (-2, 1, 0, 0) = 0$ and $(0, 0, 1, 2) \cdot (-1, 0, -2, 1) = -2 + 2 = 0$, so $\operatorname{Null}(A)$ is orthogonal to $\operatorname{Row}(A)$.
7. Column space against left null space: $(1, 2, 3) \cdot (-1, -1, 1) = -1 - 2 + 3 = 0$ and $(0, 1, 1) \cdot (-1, -1, 1) = -1 + 1 = 0$.
8. The dimensions add up: $2 + 2 = 4 = n$ in $\mathbb{R}^4$, and $2 + 1 = 3 = m$ in $\mathbb{R}^3$.
9. Row space to column space: for $u_1 = (1, 2, 0, 1)$, we get $Au_1 = (1 + 4 + 0 + 1,\ 2 + 8 + 0 + 4,\ 3 + 12 + 0 + 5) = (6, 14, 20)$.
10. For $u_2 = (0, 0, 1, 2)$, we get $Au_2 = (0 + 2,\ 1 + 8,\ 1 + 10) = (2, 9, 11)$.
11. The column space is the plane $b_3 = b_1 + b_2$, and $6 + 14 = 20$ and $2 + 9 = 11$, so both images lie in $\operatorname{Col}(A)$.
12. The images $(6, 14, 20)$ and $(2, 9, 11)$ are not proportional, so $A$ carries the basis $u_1, u_2$ of $\operatorname{Row}(A)$ to a basis of $\operatorname{Col}(A)$, as part 4 of the [[theorem|73DVECPAT6]] says.
13. Adding a null vector does not change the image: $A(u_1 + (-2, 1, 0, 0)) = Au_1 + 0 = (6, 14, 20)$.

## Remarks

The example shows every part of the theorem with explicit vectors.
The four basis vectors of $\operatorname{Row}(A)$ and $\operatorname{Null}(A)$ are independent, because the two planes are orthogonal, so together they form a basis of $\mathbb{R}^4$.
The left null space vector $(-1, -1, 1)$ gives the condition $b_3 = b_1 + b_2$ for $Ax = b$ to have a solution.

The basis of the column space must be taken from $A$, not from its reduced form.
Columns 1 and 3 of the reduced form are $(1, 0, 0)$ and $(0, 1, 0)$, and $(1, 0, 0)$ is not in $\operatorname{Col}(A)$, since $0 \ne 1 + 0$.
The row space is different: the nonzero rows of the reduced form do span $\operatorname{Row}(A)$, because row operations do not change the row space.

If we change the corner entry $5$ to $6$, the reduced form gets a third pivot in column 4, and the rank becomes $3$.
Then $\operatorname{Col}(A) = \mathbb{R}^3$, the left null space is $\{0\}$, the row space has dimension $3$ and the null space is the line through $(-2, 1, 0, 0)$, with $3 + 1 = 4$ and $3 + 0 = 3$.

## Explanations

### L1 human

This matrix has rank $2$, so its row space and its column space are planes.
The null space is a plane in $\mathbb{R}^4$, and the left null space is a line in $\mathbb{R}^3$.
Each pair of subspaces in the same space is orthogonal, and every dot product above comes out to $0$.

### L2 human

In $\mathbb{R}^4$, the row space and the null space are orthogonal planes, and together they span $\mathbb{R}^4$.
In $\mathbb{R}^3$, the column space is a plane, and the left null space is its normal line.
The matrix sends the row space onto the column space, one to one, and it sends the null space to $0$.
Watch out: the column space and the row space are both planes, but they live in different spaces, $\mathbb{R}^3$ and $\mathbb{R}^4$, so they cannot be compared.
