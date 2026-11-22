---
tag: B61PAXBBHQ
kind: example
name: LU decomposition of a 3 × 3 matrix and its use to solve a system
msc: ["15A23"]
topics: [P8J6QR66TJ]
audience: ug1
instance_of: [0RKG5YW66Y]
uses: [0RKG5YW66Y, 3PPBWG0B96, R424G32KFA, 0ATFVE08MW, 032Q9FB8MT]
sources:
  - book: isbn:9780321982384
    locator: Section 2.5
  - url: https://en.wikipedia.org/wiki/LU_decomposition
---

## Example

Elimination on a $3 \times 3$ matrix, with its multipliers written down, gives the factors $L$ and $U$, and these then solve a system by two substitutions.
Let
$$A = \begin{pmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{pmatrix}$$
over $\mathbb{Q}$.
We eliminate below the pivots without row exchanges, and we keep each multiplier.

1. The step $R_2 \to R_2 - 2R_1$ turns row 2 into $(0, 1, 1)$, so $\ell_{21} = 2$.
2. The step $R_3 \to R_3 - 4R_1$ turns row 3 into $(0, 3, 5)$, so $\ell_{31} = 4$.
3. The step $R_3 \to R_3 - 3R_2$ turns row 3 into $(0, 0, 2)$, so $\ell_{32} = 3$.

So
$$L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{pmatrix}, \qquad U = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}.$$
Check: row 2 of $LU$ is $2(2, 1, 1) + (0, 1, 1) = (4, 3, 3)$, and row 3 is $4(2, 1, 1) + 3(0, 1, 1) + (0, 0, 2) = (8, 7, 9)$.
The pivots $2, 1, 2$ agree with the [[leading principal minors|3PPBWG0B96]] $\Delta_1 = 2$, $\Delta_2 = 2$ and $\Delta_3 = 4$, since $2 = 2/1$, $1 = 2/2$ and $2 = 4/2$.

Now solve $Ax = b$ for $b = (4, 10, 24)^{\mathsf{T}}$.
Forward substitution in $Ly = b$ and [[back substitution|0ATFVE08MW]] in $Ux = y$ give
$$y_1 = 4, \quad y_2 = 10 - 2 \cdot 4 = 2, \quad y_3 = 24 - 4 \cdot 4 - 3 \cdot 2 = 2; \qquad x_3 = \tfrac{2}{2} = 1, \quad x_2 = 2 - x_3 = 1, \quad x_1 = \tfrac{4 - x_2 - x_3}{2} = 1.$$
Check: $A(1, 1, 1)^{\mathsf{T}}$ is the vector of row sums $(4, 10, 24)^{\mathsf{T}} = b$.

Finally, the [[LDU form|R424G32KFA]] divides each row of $U$ by its pivot:
$$D = \operatorname{diag}(2, 1, 2), \qquad V = D^{-1} U = \begin{pmatrix} 1 & 1/2 & 1/2 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}.$$
Check: $DV$ multiplies the rows of $V$ by $2$, $1$ and $2$, which gives $U$ back, so $LDV = LU = A$.

## Remarks

### The inverse from the factors

The inverses of the factors are
$$L^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 2 & -3 & 1 \end{pmatrix}, \qquad U^{-1} = \begin{pmatrix} 1/2 & -1/2 & 0 \\ 0 & 1 & -1/2 \\ 0 & 0 & 1/2 \end{pmatrix}.$$
Then
$$A^{-1} = U^{-1} L^{-1} = \begin{pmatrix} 3/2 & -1/2 & 0 \\ -3 & 5/2 & -1/2 \\ 1 & -3/2 & 1/2 \end{pmatrix}.$$
Check: row 1 of $A^{-1}$ times column 1 of $A$ is $3 - 2 + 0 = 1$, and row 3 of $A^{-1}$ times column 1 of $A$ is $2 - 6 + 4 = 0$.

### Watch out

Entry $(3, 1)$ of $L^{-1}$ is $2$, not $-4$.
The inverse of $L$ is not found by changing the signs of all the multipliers, because $L^{-1} = T_{32}(-3)\,T_{31}(-4)\,T_{21}(-2)$ and the product mixes them: $-4 + 3 \cdot 2 = 2$.
Check: row 3 of $L$ times column 1 of $L^{-1}$ is $4 - 6 + 2 = 0$.
Only $L$ itself has the simple form, with each multiplier in its place.

### Try it

Use the same factors to solve $Ax = (1, 3, 9)^{\mathsf{T}}$.
Answer: forward substitution gives $y = (1, 1, 2)$, since $3 - 2 = 1$ and $9 - 4 - 3 = 2$.
Back substitution gives $x_3 = 1$, $x_2 = 1 - 1 = 0$ and $x_1 = (1 - 0 - 1)/2 = 0$.
Check: $x = (0, 0, 1)^{\mathsf{T}}$, and $A x$ is column 3 of $A$, which is $(1, 3, 9)^{\mathsf{T}}$.

## Explanations

### L1 human

We do elimination once and write down the multipliers.
They form the lower triangular matrix $L$, and the result of the elimination is the upper triangular matrix $U$.
Then each system $Ax = b$ is solved by two quick substitutions.

### L2 human

The multipliers go into $L$ with a plus sign, because $L$ undoes the elimination.
For example, row 3 of $A$ is rebuilt from the rows of $U$ as $4$ times row 1 plus $3$ times row 2 plus row 3.
This is why entry $(3, 1)$ of $L$ is $4$ and entry $(3, 2)$ is $3$.
