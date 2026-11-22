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

Let
$$S = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}.$$
Row $2$ minus row $1$ is $(3, 3, 3)$, and row $3$ minus row $2$ is also $(3, 3, 3)$, so the rows are dependent, $\det S = 0$, and $S$ has rank $2$.
We compute the adjugate of $S$ and see that it is not zero.

1. The cofactors of row $1$ are
$$C_{11} = 45 - 48 = -3, \qquad C_{12} = -(36 - 42) = 6, \qquad C_{13} = 32 - 35 = -3.$$
2. The cofactors of row $2$ are
$$C_{21} = -(18 - 24) = 6, \qquad C_{22} = 9 - 21 = -12, \qquad C_{23} = -(8 - 14) = 6.$$
3. The cofactors of row $3$ are
$$C_{31} = 12 - 15 = -3, \qquad C_{32} = -(6 - 12) = 6, \qquad C_{33} = 5 - 8 = -3.$$
4. The cofactor matrix is symmetric here, so transposing it changes nothing, and by the [[definition of the adjugate|0GMPYM0NSR]]
$$\operatorname{adj} S = \begin{pmatrix} -3 & 6 & -3 \\ 6 & -12 & 6 \\ -3 & 6 & -3 \end{pmatrix}.$$
5. Each column is a multiple of $v = (1, -2, 1)$: the columns are $-3v$, $6v$ and $-3v$.
   So $\operatorname{adj} S$ is not zero, and its rank is $1$.
6. Check: $S v = (1 - 4 + 3, \ 4 - 10 + 6, \ 7 - 16 + 9) = (0, 0, 0)$.
   So $S \operatorname{adj} S = 0 = (\det S) I_3$, as the [[adjugate identity|0528HKWZ1Z]] requires.

## Remarks

The example fits the [[rank of the adjugate|9CJME5W96T]]: a matrix of rank $n - 1 = 2$ has an adjugate of rank exactly $1$.
Step 6 shows more: every column of $\operatorname{adj} S$ lies in the kernel of $S$, and since the kernel is a line, the nonzero columns span it.
In the same way, the rows of $\operatorname{adj} S$ are multiples of $(1, -2, 1)$, and $(1, -2, 1) S = (1 - 8 + 7, \ 2 - 10 + 8, \ 3 - 12 + 9) = 0$.

The picture changes when the rank drops further.
For $\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{pmatrix}$, of rank $1$, any two rows are proportional, so every $2 \times 2$ minor is $0$ and the adjugate is the zero matrix.
In the other direction, changing the entry $9$ to $10$ gives the invertible matrix of the [[worked example|BDHT6DBGC9]], whose adjugate has rank $3$.

## Explanations

### L1 human

A singular matrix has no inverse, but it still has an adjugate.
For this matrix the adjugate is not zero.
All its columns point along one direction, $(1, -2, 1)$, and that is exactly the direction that $S$ sends to zero.

### L2 human

The example gives a way to find the kernel of a matrix of rank $n - 1$ without row reduction: compute the adjugate and take any nonzero column.
Here the first column $(-3, 6, -3)$ is a multiple of $(1, -2, 1)$, and $S(1, -2, 1) = 0$.
Watch out: when the rank is $n - 2$ or less, every column of the adjugate is $0$, and the method gives nothing.
