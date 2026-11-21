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

Consider the [[homogeneous system|04KGXJG1A2]] over $\mathbb{R}$
$$x_1 + 2x_2 - x_3 + x_4 = 0, \qquad 2x_1 + 4x_2 + x_3 + 5x_4 = 0.$$
We find all its solutions in [[parametric form|KQT68YPHD1]].

1. Apply $R_2 - 2R_1$, then $\tfrac13 R_2$, then $R_1 + R_2$ to the coefficient matrix:
$$\begin{bmatrix} 1 & 2 & -1 & 1 \\ 2 & 4 & 1 & 5 \end{bmatrix} \to \begin{bmatrix} 1 & 2 & -1 & 1 \\ 0 & 0 & 3 & 3 \end{bmatrix} \to \begin{bmatrix} 1 & 2 & -1 & 1 \\ 0 & 0 & 1 & 1 \end{bmatrix} \to \begin{bmatrix} 1 & 2 & 0 & 2 \\ 0 & 0 & 1 & 1 \end{bmatrix}.$$
2. The last matrix is the [[reduced row echelon form|0WF5AQYTW6]]. Its pivot columns are $1$ and $3$, so $x_2$ and $x_4$ are free.
3. Put $x_2 = s$ and $x_4 = t$. The rows say $x_1 + 2s + 2t = 0$ and $x_3 + t = 0$, so $x_1 = -2s - 2t$ and $x_3 = -t$.
4. Split the solution into one vector for each free variable:
$$x = s(-2, 1, 0, 0) + t(-2, 0, -1, 1), \qquad s, t \in \mathbb{R}.$$
5. Check $(-2, 1, 0, 0)$: $-2 + 2 = 0$ and $-4 + 4 = 0$. Check $(-2, 0, -1, 1)$: $-2 + 1 + 1 = 0$ and $-4 - 1 + 5 = 0$.

## Remarks

The two vectors in step 4 form a basis of the null space, so it has dimension $2 = 4 - 2$.
They are independent because each has a $1$ in the position of its own free variable and a $0$ in the position of the other one.
The example agrees with the [[theorem on homogeneous systems|JPW6KVS70A]], since there are $4$ unknowns and only $2$ equations.
If you add a third equation such as $x_2 = 0$, one free variable disappears, and the solution set shrinks to the line spanned by $(-2, 0, -1, 1)$.

## Explanations

### L1 human

There are four unknowns but only two equations.
So two unknowns are free, and the solutions form a flat two-dimensional set through the origin.
Every solution is a mix of the two basic solutions in step 4.

### L2 human

The standard way to write a homogeneous solution set is in three moves.
Write each basic variable in terms of the free ones, write the vector $x$ with these expressions, and split it as a sum with one vector for each free variable.
Watch out: column $2$ has no pivot even though its entries are nonzero.
Pivots are found only after reduction, because the entry $2$ in column 2 is cleared by the pivot in column 1 of the same row.
