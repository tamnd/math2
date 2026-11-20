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

In $\R^3$ with the [[dot product|05HQYM0R4G]], let $U = \operatorname{span}\set{u_1, u_2}$ with $u_1 = (1, 1, 0)$ and $u_2 = (0, 1, 1)$.
We compute the [[orthogonal complement|079D68S3AW]] $U^\perp$.

1. By the [[basic properties|T5Q51M5BAK]], $x \in U^\perp$ exactly when $x \cdot u_1 = 0$ and $x \cdot u_2 = 0$.
2. These conditions are $x_1 + x_2 = 0$ and $x_2 + x_3 = 0$.
3. So $U^\perp$ is the [[null space|0PQ2GGY1QV]] of $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$, whose rows are $u_1$ and $u_2$.
4. $A$ is in echelon form with pivots in columns 1 and 2, so $x_3 = t$ is free.
5. Back substitution gives $x_2 = -t$ and $x_1 = -x_2 = t$.
6. Hence $U^\perp = \set{t(1, -1, 1) : t \in \R} = \R(1, -1, 1)$.
7. Check: $(1, -1, 1) \cdot (1, 1, 0) = 1 - 1 + 0 = 0$ and $(1, -1, 1) \cdot (0, 1, 1) = 0 - 1 + 1 = 0$.
8. The vectors $u_1$ and $u_2$ are not parallel, so $\dim U = 2$, and $\dim U + \dim U^\perp = 2 + 1 = 3$.

So $U$ is the plane $x_1 - x_2 + x_3 = 0$, and $n = (1, -1, 1)$ is a normal vector of this plane.

## Remarks

The method works for every subspace of $\R^n$ given by a spanning set: put the spanning vectors into the rows of a matrix and solve $Ax = 0$.
If we add a third vector $u_3 = (1, 0, 0)$, the matrix gets a third row, the only solution is $x = 0$, and the complement of $\R^3$ is $\set{0}$.
If we drop $u_2$, then $U$ is the line $\R(1, 1, 0)$, and its complement is the plane $x_1 + x_2 = 0$, spanned by $(1, -1, 0)$ and $(0, 0, 1)$.

## Explanations

### L1 human

The plane through $(1, 1, 0)$ and $(0, 1, 1)$ is a tilted sheet through the origin.
The complement is the one line that stands at right angles to the sheet.
We find it by asking which vectors have dot product zero with both given vectors.

### L2 human

The two conditions are two linear equations in three unknowns.
Two independent equations in $\R^3$ leave one free variable, so the answer is a line.
The typical use is to find the normal vector of a plane from two vectors in the plane.
In $\R^3$ the cross product $u_1 \times u_2 = (1 \cdot 1 - 0 \cdot 1, 0 \cdot 0 - 1 \cdot 1, 1 \cdot 1 - 1 \cdot 0) = (1, -1, 1)$ gives the same line.
The trap is to put $u_1$ and $u_2$ in the columns of the matrix: then $Ax = 0$ asks for a different thing.
