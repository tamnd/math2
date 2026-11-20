---
tag: H98NXA00NZ
kind: example
name: The adjugate of a singular 3 × 3 matrix
msc: ["15A09"]
topics: [DTBK11SR77]
audience: ug1
instance_of: [07W9H8QF38]
uses: [0GMPYM0NSR, 0528HKWZ1Z, 9CJME5W96T]
sources:
  - url: https://en.wikipedia.org/wiki/Adjugate_matrix
    locator: Properties
---

## Example

Let $S = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$, with $\det S = 0$ and rank $2$.

1. The cofactors of row $1$ are $C_{11} = 45 - 48 = -3$, $C_{12} = -(36 - 42) = 6$, $C_{13} = 32 - 35 = -3$.
2. Row $2$: $C_{21} = -(18 - 24) = 6$, $C_{22} = 9 - 21 = -12$, $C_{23} = -(8 - 14) = 6$.
3. Row $3$: $C_{31} = 12 - 15 = -3$, $C_{32} = -(6 - 12) = 6$, $C_{33} = 5 - 8 = -3$.
4. So $\operatorname{adj} S = \begin{pmatrix} -3 & 6 & -3 \\ 6 & -12 & 6 \\ -3 & 6 & -3 \end{pmatrix}$, which is symmetric here.
5. Each column is a multiple of $v = (1, -2, 1)$, so $\operatorname{adj} S$ has rank $1$.
6. Check: $Sv = (1 - 4 + 3, 4 - 10 + 6, 7 - 16 + 9) = 0$. So $S \operatorname{adj} S = 0 = (\det S) I_3$.

## Remarks

This agrees with the [[rank of the adjugate|9CJME5W96T]]: rank $n - 1 = 2$ gives an adjugate of rank $1$.
The columns of $\operatorname{adj} S$ span the kernel of $S$.

## Explanations

### L1 human

A singular matrix has no inverse, but it still has an adjugate.
Here the adjugate is not zero, and all its columns point along the one direction that $S$ sends to zero.

### L2 human

The adjugate gives a vector of the kernel without row reduction: any nonzero column of $\operatorname{adj} S$.
A trap: for a matrix of rank $n - 2$ or less, all columns are zero, and this method gives nothing.
