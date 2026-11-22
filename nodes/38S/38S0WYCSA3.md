---
tag: 38S0WYCSA3
kind: example
name: The orthogonal complement of a plane in R3 as a null space
msc: [15A63]
topics: [8GQVME4SZZ]
audience: ug1
instance_of: [0XJXTBCB2T]
uses: [079D68S3AW, 0PQ2GGY1QV, 05HQYM0R4G, T5Q51M5BAK]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: Example
  - book: isbn:9780321982384
    locator: Section 6.1
---

## Example

In $\R^3$ with the [[dot product|05HQYM0R4G]], let $U = \operatorname{span}\{u_1, u_2\}$ with $u_1 = (1, 1, 0)$ and $u_2 = (0, 1, 1)$.
We compute the [[orthogonal complement|079D68S3AW]] $U^\perp$ by solving a linear system.

1. By part 3 of the [[basic properties|T5Q51M5BAK]], a vector $x$ is in $U^\perp$ exactly when $x \cdot u_1 = 0$ and $x \cdot u_2 = 0$.
2. Written out, these two conditions are $x_1 + x_2 = 0$ and $x_2 + x_3 = 0$.
3. So $U^\perp$ is the [[null space|0PQ2GGY1QV]] of the matrix $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$, whose rows are $u_1$ and $u_2$.
4. The matrix $A$ is in echelon form with pivots in columns 1 and 2, so $x_3 = t$ is the free variable.
5. Back substitution gives $x_2 = -t$ from the second row and $x_1 = -x_2 = t$ from the first row.
6. Hence $U^\perp = \{ t(1, -1, 1) : t \in \R \} = \R(1, -1, 1)$.
7. Check: $(1, -1, 1) \cdot (1, 1, 0) = 1 - 1 + 0 = 0$ and $(1, -1, 1) \cdot (0, 1, 1) = 0 - 1 + 1 = 0$.
8. The vectors $u_1$ and $u_2$ are not parallel, so $\dim U = 2$, and $\dim U + \dim U^\perp = 2 + 1 = 3$.

So $n = (1, -1, 1)$ is a normal vector of $U$, and $U$ is the plane with equation $x_1 - x_2 + x_3 = 0$.

## Remarks

The example shows the general method for subspaces of $\R^n$ that are given by a spanning set: put the spanning vectors into the rows of a matrix and solve $Ax = 0$.
The number of free variables is the dimension of the complement, so the count $2 + 1 = 3$ is rank-nullity in disguise.

Changing the spanning set changes the answer in a predictable way.
If we add a third vector $u_3 = (1, 0, 0)$, the matrix gets a third row and becomes invertible, so the only solution is $x = 0$ and the complement of $\R^3$ is $\{0\}$.
If we drop $u_2$, then $U$ is the line $\R(1, 1, 0)$, the single equation $x_1 + x_2 = 0$ leaves two free variables, and the complement is the plane spanned by $(1, -1, 0)$ and $(0, 0, 1)$.

## Explanations

### L1 human

The plane through $(1, 1, 0)$ and $(0, 1, 1)$ is a tilted sheet through the origin.
Its complement is the one line that stands at a right angle to the sheet.
We find that line by asking which vectors have dot product zero with both given vectors, and the answer is the line through $(1, -1, 1)$.

### L2 human

In $\R^3$ there is a second way to get the normal line: the cross product of the two spanning vectors.
Compute it entry by entry:
$$u_1 \times u_2 = (1 \cdot 1 - 0 \cdot 1,\; 0 \cdot 0 - 1 \cdot 1,\; 1 \cdot 1 - 1 \cdot 0) = (1, -1, 1).$$
It gives the same line, as it must, since the cross product is orthogonal to both factors.
The null space method is the one that works in every dimension, while the cross product only exists in $\R^3$.
Watch out: if you put $u_1$ and $u_2$ into the columns of a $3 \times 2$ matrix, then $Ax = 0$ asks for the combinations $x_1 u_1 + x_2 u_2$ that vanish, which is a different question with the answer $x = 0$.
