---
tag: 17K9NNTCZ7
kind: example
name: Elementary matrices acting on columns, and their inverses
msc: ["15A23"]
topics: [P8J6QR66TJ]
audience: ug1
instance_of: [01REXW3WWE]
uses: [0M79HRJCRR, F7F6AA3XQ7, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_matrix
    locator: Elementary row operations
---

## Example

Let $B = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ over $\mathbb{Q}$.

1. Let $T = T_{12}(-2) = \begin{pmatrix} 1 & -2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$, a $3 \times 3$ [[elementary matrix|0M79HRJCRR]].
2. Column 2 of $BT$ is $B$ times $(-2, 1, 0)^{\mathsf{T}}$, which is $-2 \cdot (1, 4)^{\mathsf{T}} + (2, 5)^{\mathsf{T}} = (0, -3)^{\mathsf{T}}$. Columns 1 and 3 are unchanged.
3. So $BT = \begin{pmatrix} 1 & 0 & 3 \\ 4 & -3 & 6 \end{pmatrix}$: right multiplication by $T_{12}(-2)$ added $-2$ times column 1 to column 2.
4. Left multiplication by the same $T$ is not defined on $B$, because $T$ is $3 \times 3$ and $B$ is $2 \times 3$. A row operation on $B$ needs a $2 \times 2$ elementary matrix.

Now we check the inverses of the three types for $n = 3$.

5. $T_{12}(-2) T_{12}(2) = \begin{pmatrix} 1 & -2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 - 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I_3$.
6. $D_2(5) D_2(\tfrac{1}{5}) = \operatorname{diag}(1, 5 \cdot \tfrac{1}{5}, 1) = I_3$.
7. $P_{13} P_{13} = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}^2$. Row 1 of $P_{13}$ picks row 3 of $P_{13}$, which is $(1, 0, 0)$. In the same way rows 2 and 3 of the product are $(0, 1, 0)$ and $(0, 0, 1)$. So $P_{13}^2 = I_3$.
8. The products in the other order are also $I_3$, by the same computations with the factors exchanged.

## Remarks

The inverses follow the [[row operation theorem|F7F6AA3XQ7]]: each inverse matrix undoes the operation of the original one.
Step 3 shows the index rule for columns: $T_{ij}(c)$ on the right changes column $j$, using column $i$.

Column operations change different things than row operations do.
The column operation of step 3 keeps the column space of $B$, since column 2 of $BT$ is a combination of columns of $B$ and the step can be undone.
It changes the row space, though: the first row went from $(1, 2, 3)$ to $(1, 0, 3)$.
If we used $T_{21}(-2)$ on the right instead, column 1 would change, to $(1, 4) - 2(2, 5) = (-3, -6)$, and column 2 would stay.

## Explanations

### L1 human

The same elementary matrix can act on rows, from the left, or on columns, from the right.
To undo a row step, we use the opposite step: subtract instead of add, divide instead of multiply, or exchange the same rows again.

### L2 human

The point of steps 1 to 3 is the index rule for columns, which is the reverse of the rule for rows.
The point of steps 5 to 7 is that each inverse is again elementary and of the same type.
A trap: the inverse of $D_2(5)$ is $D_2(\tfrac{1}{5})$, and the inverse of $T_{12}(-2)$ is $T_{12}(2)$, not $T_{12}(-\tfrac{1}{2})$.
