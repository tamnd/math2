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

Let $A = \begin{pmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{pmatrix}$ over $\mathbb{Q}$.
We eliminate below the pivots without row exchanges, and we keep each multiplier.

1. $R_2 \to R_2 - 2R_1$: row 2 becomes $(0, 1, 1)$. The multiplier is $\ell_{21} = 2$.
2. $R_3 \to R_3 - 4R_1$: row 3 becomes $(0, 3, 5)$. The multiplier is $\ell_{31} = 4$.
3. $R_3 \to R_3 - 3R_2$: row 3 becomes $(0, 0, 2)$. The multiplier is $\ell_{32} = 3$.
4. So $U = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}$ and $L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{pmatrix}$.
5. Check $LU$ row by row. Row 1 is $(2, 1, 1)$. Row 2 is $2(2, 1, 1) + (0, 1, 1) = (4, 3, 3)$. Row 3 is $4(2, 1, 1) + 3(0, 1, 1) + (0, 0, 2) = (8, 7, 9)$. So $LU = A$.
6. The pivots $2, 1, 2$ agree with the [[leading principal minors|3PPBWG0B96]] $\Delta_1 = 2$, $\Delta_2 = 2$ and $\Delta_3 = 4$: $2 = 2/1$, $1 = 2/2$ and $2 = 4/2$.

Now solve $Ax = b$ for $b = (4, 10, 24)^{\mathsf{T}}$.

7. Forward substitution in $Ly = b$: $y_1 = 4$, then $y_2 = 10 - 2 \cdot 4 = 2$, then $y_3 = 24 - 4 \cdot 4 - 3 \cdot 2 = 2$.
8. [[Back substitution|0ATFVE08MW]] in $Ux = y$: $2x_3 = 2$ gives $x_3 = 1$, then $x_2 + x_3 = 2$ gives $x_2 = 1$, then $2x_1 + x_2 + x_3 = 4$ gives $x_1 = 1$.
9. Check: $A(1, 1, 1)^{\mathsf{T}}$ is the vector of row sums $(4, 10, 24)^{\mathsf{T}} = b$.

The [[LDU form|R424G32KFA]]:

10. $D = \operatorname{diag}(2, 1, 2)$, and $V = D^{-1} U = \begin{pmatrix} 1 & 1/2 & 1/2 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$, by dividing the rows of $U$ by $2$, $1$ and $2$.
11. Check: $DV$ multiplies the rows of $V$ by $2$, $1$ and $2$, which gives $U$ back. So $LDV = LU = A$.

## Remarks

The inverses of the factors are $L^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 2 & -3 & 1 \end{pmatrix}$ and $U^{-1} = \begin{pmatrix} 1/2 & -1/2 & 0 \\ 0 & 1 & -1/2 \\ 0 & 0 & 1/2 \end{pmatrix}$.
Check: $L L^{-1} = I_3$; for example, row 3 of $L$ times column 1 of $L^{-1}$ is $4 - 6 + 2 = 0$.
Note that entry $(3, 1)$ of $L^{-1}$ is $2$, not $-4$: the inverse of $L$ is not found by changing the signs of all multipliers.
Only $L$ itself has the simple form, with the multipliers in their places.
Then $A^{-1} = U^{-1} L^{-1} = \begin{pmatrix} 3/2 & -1/2 & 0 \\ -3 & 5/2 & -1/2 \\ 1 & -3/2 & 1/2 \end{pmatrix}$.
Multiplying out gives $A^{-1} A = I_3$; for example, row 1 of $A^{-1}$ times column 1 of $A$ is $3 - 2 + 0 = 1$.

## Explanations

### L1 human

We do elimination once and write down the multipliers.
They form the lower triangular matrix $L$, and the result of the elimination is the upper triangular matrix $U$.
Then each system $Ax = b$ is solved by two quick substitutions.

### L2 human

The multipliers go into $L$ with a plus sign, because $L$ undoes the elimination.
For example, row 3 of $A$ is rebuilt from the rows of $U$.
It is $4$ times row 1 plus $3$ times row 2 plus row 3.
This is why entry $(3, 1)$ of $L$ is $4$ and entry $(3, 2)$ is $3$.
