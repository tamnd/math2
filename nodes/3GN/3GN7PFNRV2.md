---
tag: 3GN7PFNRV2
kind: example
name: A homogeneous system with two free variables
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
instance_of: [04KGXJG1A2, KQT68YPHD1]
uses: [04KGXJG1A2, 0WF5AQYTW6, KQT68YPHD1]
sources:
  - book: isbn:9780321982384
    locator: Section 1.5
---

## Example

Consider the [[homogeneous system|04KGXJG1A2]] over $\R$
$$x_1 + 2x_2 - x_3 + x_4 = 0, \qquad 2x_1 + 4x_2 + x_3 + 5x_4 = 0.$$

1. The coefficient matrix is $\begin{bmatrix} 1 & 2 & -1 & 1 \\ 2 & 4 & 1 & 5 \end{bmatrix}$.
2. $R_2 \leftarrow R_2 - 2R_1$ gives $(0, 0, 3, 3)$.
3. $R_2 \leftarrow \tfrac13 R_2$ gives $(0, 0, 1, 1)$.
4. $R_1 \leftarrow R_1 + R_2$ gives $(1, 2, 0, 2)$.
5. The [[reduced row echelon form|0WF5AQYTW6]] is $\begin{bmatrix} 1 & 2 & 0 & 2 \\ 0 & 0 & 1 & 1 \end{bmatrix}$, with pivot columns $1$ and $3$.
6. The free variables are $x_2 = s$ and $x_4 = t$.
7. The rows give $x_1 = -2s - 2t$ and $x_3 = -t$.
8. So the solutions are $s(-2, 1, 0, 0) + t(-2, 0, -1, 1)$, with $s, t \in \R$.
9. Check $(-2, 1, 0, 0)$: $-2 + 2 = 0$ and $-4 + 4 = 0$.
10. Check $(-2, 0, -1, 1)$: $-2 + 1 + 1 = 0$ and $-4 - 1 + 5 = 0$.

## Remarks

The two vectors in step 8 are a basis of the null space, so it has dimension $2 = 4 - 2$.
They are independent because each has a $1$ in the position of its own free variable and $0$ in the position of the other.
This agrees with [[the theorem on homogeneous systems|JPW6KVS70A]], since $4 > 2$.

## Explanations

### L1 human

There are four unknowns but only two equations.
So two unknowns are free, and the solutions form a flat two-dimensional set through the origin.
Every solution is a mix of the two basic solutions in step 8.

### L2 human

The standard way to write the [[parametric form|KQT68YPHD1]] of a homogeneous solution set is as follows.

1. Write each basic variable in terms of the free ones.
2. Write the vector $x$ with these expressions.
3. Split it as a sum, one vector for each free variable.

A trap: column $2$ has no pivot even though its entries are nonzero; pivots are found only after reduction.
