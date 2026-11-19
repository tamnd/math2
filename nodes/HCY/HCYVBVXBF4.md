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

Consider $x + 2y = 3$, $2x + 4y = 7$ over $\R$, so $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ and $b = (3, 7)^T$.

1. Reduce $A$: $R_2 \leftarrow R_2 - 2R_1$ gives $\begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$, which is the [[RREF|0NNR68BFRY]] of $A$.
2. Reduce $[A \mid b]$: the same step gives $\left[\begin{array}{cc|c} 1 & 2 & 3 \\ 0 & 0 & 1 \end{array}\right]$.
3. $R_1 \leftarrow R_1 - 3R_2$ gives $\left[\begin{array}{cc|c} 1 & 2 & 0 \\ 0 & 0 & 1 \end{array}\right]$, the RREF of $[A \mid b]$.
4. The RREF of $A$ has $1$ pivot, and the RREF of $[A \mid b]$ has $2$ pivots.
5. So $\rank A = 1$ and $\rank [A \mid b] = 2$, and the system is inconsistent.
6. With $b = (3, 6)^T$, step 2 gives $\left[\begin{array}{cc|c} 1 & 2 & 3 \\ 0 & 0 & 0 \end{array}\right]$, already in RREF, with $1$ pivot.
7. Then the system is consistent, with solutions $(3 - 2t, t)$; check $t = 1$: $1 + 2 = 3$ and $2 + 4 = 6$.

## Remarks

The RREF of $A$ is the left block of the RREF of $[A \mid b]$, by the [[augmentation principle|BE3NZP35HY]].
But the RREF of $[A \mid b]$ is not the RREF of $A$ with a column added: step 3 also changed the entry $3$ to $0$.
Only the RREF of $[A \mid b]$ tells us whether the system is consistent.

## Explanations

### L1 human

Reducing only the left part of the table hides the right side.
The left part here becomes "$x + 2y$" and "nothing", which looks harmless.
But the right side turns the second row into $0 = 1$, an impossible equation.

### L2 human

To decide consistency, follow these steps.

1. Reduce the full augmented matrix, never only $A$.
2. Look at the last column.
3. If it holds a pivot, there is no solution.

A trap: a computer command such as `rref(A)` answers a different question from `rref([A b])`.
