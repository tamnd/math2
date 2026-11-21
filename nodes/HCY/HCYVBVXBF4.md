---
tag: HCYVBVXBF4
kind: example
name: The reduced row echelon forms of A and of the augmented matrix differ
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
instance_of: [0T6MWGZSXA, 0WF5AQYTW6]
uses: [0YCDZ7N8VD, 0NNR68BFRY, 0EWQEYRVA8]
sources:
  - book: isbn:9780321982384
    locator: Section 1.2
---

## Example

Reducing only the coefficient matrix can hide the fact that a system has no solution.
Consider over $\mathbb{R}$ the system
$$x + 2y = 3, \qquad 2x + 4y = 7,$$
so $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ and $b = (3, 7)^{\mathsf{T}}$.

1. Reduce $A$. The step $R_2 \leftarrow R_2 - 2R_1$ gives $\begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$, which is the [[RREF|0NNR68BFRY]] of $A$. It has $1$ pivot.
2. Reduce $[A \mid b]$ with the same step. It gives $\left[\begin{array}{cc|c} 1 & 2 & 3 \\ 0 & 0 & 1 \end{array}\right]$.
3. The new pivot in the last column needs zeros above it, so $R_1 \leftarrow R_1 - 3R_2$ gives $\left[\begin{array}{cc|c} 1 & 2 & 0 \\ 0 & 0 & 1 \end{array}\right]$. This is the RREF of $[A \mid b]$, and it has $2$ pivots.
4. So $\rank A = 1$ and $\rank [A \mid b] = 2$. The second row says $0 = 1$, and the system is inconsistent.
5. Change the right side to $b = (3, 6)^{\mathsf{T}}$. Then step 2 gives $\left[\begin{array}{cc|c} 1 & 2 & 3 \\ 0 & 0 & 0 \end{array}\right]$, already in RREF, with $1$ pivot.
6. Now the system is consistent, with the solutions $(3 - 2t, t)$ for $t \in \mathbb{R}$. Check $t = 1$, the point $(1, 1)$: $1 + 2 = 3$ and $2 + 4 = 6$.

## Remarks

The RREF of $A$ is always the left block of the RREF of $[A \mid b]$, by the [[augmentation principle|BE3NZP35HY]].
Here that block is $\begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$ in both cases.
But the RREF of $[A \mid b]$ is not the RREF of $A$ with a column added at the end: step 3 also changed the entry $3$ to $0$.

The two right sides give the same RREF of $A$, but one system is inconsistent and the other has infinitely many solutions.
So the RREF of $A$ alone cannot decide consistency, and only the RREF of $[A \mid b]$ can.

## Explanations

### L1 human

The two equations have the same left side up to a factor $2$, since $2x + 4y = 2(x + 2y)$.
So the second equation asks $x + 2y$ to equal $\tfrac72$, while the first asks it to equal $3$.
Reducing only the left part of the table hides this conflict.
The right side turns the second row into $0 = 1$, an impossible equation.

### L2 human

To decide consistency, follow these steps.

1. Reduce the full augmented matrix, never only $A$.
2. Look at the last column.
3. If it holds a pivot, there is no solution.

Watch out: a computer command such as `rref(A)` answers a different question from `rref([A b])`.
