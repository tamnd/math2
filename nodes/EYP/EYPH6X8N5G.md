---
tag: EYPH6X8N5G
kind: example
name: A factorization PA = LU with one row exchange
msc: ["15A23"]
topics: [P8J6QR66TJ]
audience: ug1
instance_of: [0RKG5YW66Y]
uses: [0RKG5YW66Y, 08SP3DF8NB, 3PPBWG0B96, 032Q9FB8MT]
sources:
  - book: isbn:9780321982384
    locator: Section 2.5
  - url: https://en.wikipedia.org/wiki/LU_decomposition
    locator: LU factorization with partial pivoting
---

## Example

Let $A = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 2 & 1 \\ 2 & 7 & 9 \end{pmatrix}$ over $\mathbb{Q}$.

1. The entry $a_{11}$ is $0$, so $\Delta_1 = 0$. By the theorem on [[existence of the LU decomposition|3PPBWG0B96]], the invertible matrix $A$ has no factorization $A = LU$ with $L$ unit lower triangular.
2. Exchange rows 1 and 2. This is left multiplication by the [[permutation matrix|08SP3DF8NB]] $P = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$, and $PA = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 1 & 1 \\ 2 & 7 & 9 \end{pmatrix}$.
3. $R_2 \to R_2 - 0 \cdot R_1$: nothing changes, and $\ell_{21} = 0$.
4. $R_3 \to R_3 - 2R_1$: row 3 becomes $(0, 3, 7)$, and $\ell_{31} = 2$.
5. $R_3 \to R_3 - 3R_2$: row 3 becomes $(0, 0, 4)$, and $\ell_{32} = 3$.
6. So $PA = LU$ with $L = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & 3 & 1 \end{pmatrix}$ and $U = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 4 \end{pmatrix}$.
7. Check $LU$ row by row. Row 1 is $(1, 2, 1)$ and row 2 is $(0, 1, 1)$. Row 3 is $2(1, 2, 1) + 3(0, 1, 1) + (0, 0, 4) = (2, 7, 9)$. These are the rows of $PA$.
8. Since $P^{-1} = P$, we get $A = P L U$. Also $\det A = \det P \det U = -1 \cdot 4 = -4$.

## Remarks

The leading principal minors of $PA$ are $1$, $1$ and $4$, so the existence theorem applies to $PA$.
Also, $L$ and $U$ are unique for this $P$.
Another choice of $P$ also works here, for example the exchange of rows 1 and 3, and it gives other factors.
Numerical programs choose the row with the largest entry in the pivot column; this partial pivoting belongs to numerical analysis.

## Explanations

### L1 human

If a pivot is zero, swap in a lower row first.
Do all the swaps at the start, as a permutation matrix $P$, and then eliminate as usual.
The result is $PA = LU$.

### L2 human

The determinant check is useful.
Expansion of $\det A$ along the first column gives $-1 \cdot (1 \cdot 9 - 1 \cdot 7) + 2 \cdot (1 \cdot 1 - 1 \cdot 2) = -2 - 2 = -4$.
This agrees with $\det P \det U = -4$ from step 8.
