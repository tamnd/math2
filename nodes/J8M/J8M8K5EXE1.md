---
tag: J8M8K5EXE1
kind: example
name: Elementary matrices of the three types acting on rows
msc: ["15A23"]
topics: [P8J6QR66TJ]
audience: ug1
instance_of: [01REXW3WWE]
uses: [0M79HRJCRR, F7F6AA3XQ7, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_matrix
    locator: Elementary row operations
  - book: isbn:9780321982384
    locator: Section 2.2
---

## Example

Let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}$ over $\mathbb{Q}$.
We multiply $A$ on the left by one $3 \times 3$ [[elementary matrix|0M79HRJCRR]] of each type.

1. Row exchange $R_1 \leftrightarrow R_3$, with $P_{13} = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}$. Then $P_{13} A = \begin{pmatrix} 5 & 6 \\ 3 & 4 \\ 1 & 2 \end{pmatrix}$: rows 1 and 3 changed places.
2. Row scaling $R_2 \to -2R_2$, with $D_2(-2) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$. Then $D_2(-2) A = \begin{pmatrix} 1 & 2 \\ -6 & -8 \\ 5 & 6 \end{pmatrix}$.
3. Row replacement $R_3 \to R_3 - 5R_1$, with $T_{31}(-5) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -5 & 0 & 1 \end{pmatrix}$. Row 3 of the product is $-5 \cdot (1, 2) + 1 \cdot (5, 6) = (0, -4)$, so $T_{31}(-5) A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 0 & -4 \end{pmatrix}$.
4. A full elimination: after step 3, the operation $R_2 \to R_2 - 3R_1$ with $T_{21}(-3)$ gives $\begin{pmatrix} 1 & 2 \\ 0 & -2 \\ 0 & -4 \end{pmatrix}$.
5. Then $R_3 \to R_3 - 2R_2$ with $T_{32}(-2)$ gives $R = \begin{pmatrix} 1 & 2 \\ 0 & -2 \\ 0 & 0 \end{pmatrix}$, an echelon form.
6. So $R = T_{32}(-2)\, T_{21}(-3)\, T_{31}(-5)\, A$, and the product of the three elementary matrices is $E = \begin{pmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ 1 & -2 & 1 \end{pmatrix}$.
7. Check: row 3 of $EA$ is $1 \cdot (1, 2) - 2 \cdot (3, 4) + 1 \cdot (5, 6) = (0, 0)$, and row 2 is $-3 \cdot (1, 2) + (3, 4) = (0, -2)$. So $EA = R$.

## Remarks

Each product in steps 1 to 3 follows the rule of the [[row operation theorem|F7F6AA3XQ7]].
Row $k$ of $EA$ is the combination of the rows of $A$ given by row $k$ of $E$.
Step 7 shows that the whole elimination is a single left multiplication by the invertible matrix $E$.
Row 3 of $E$ records the dependence $a_1 - 2a_2 + a_3 = 0$ among the rows of $A$.

## Explanations

### L1 human

Each elementary matrix does one row step to the matrix $A$.
We can do several steps one after another, or we can first multiply the elementary matrices together and then do all steps at once.

### L2 human

The point is that the order of the factors matters: the first operation is the rightmost factor, next to $A$.
A typical use is step 7: the last row of $E$ gives a combination of the rows of $A$ that is zero.
A trap: $T_{31}(-5)$ has its entry $-5$ in row $3$, column $1$, and it changes row $3$, not row $1$.
