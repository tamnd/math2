---
tag: 4WK6BCJF6D
kind: example
name: The formula det A det D − det B det C fails for block matrices
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
illustrates: [0J9TVTNB4K]
uses: [01AXG9KZQF, 016PE4VZ8Q, 09YB3WQG38, 0KA7A4ENVJ]
sources:
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Determinant
---

## Example

Let $M$ be the $4 \times 4$ matrix over $\mathbb{Q}$ whose [[blocks|01AXG9KZQF]] are $A = D = 0$ and $B = C = I_2$:
$$M = \begin{pmatrix} 0 & I_2 \\ I_2 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix}.$$
We show that $\det M \ne \det A \det D - \det B \det C$.

1. The block version of $ad - bc$ gives
$$\det A \det D - \det B \det C = 0 \cdot 0 - 1 \cdot 1 = -1.$$
2. Each row and each column of $M$ has exactly one entry $1$.
   So only one term of the [[Leibniz formula|016PE4VZ8Q]] is nonzero, the term of the permutation that sends each row to the column of its $1$.
3. That permutation sends $1 \mapsto 3$, $2 \mapsto 4$, $3 \mapsto 1$ and $4 \mapsto 2$, so it is $(1\,3)(2\,4)$.
   It is a product of two transpositions, so its sign is $+1$.
   The product of its entries is $1$, so $\det M = 1$.
4. Check by [[row swaps|09YB3WQG38]]: swapping rows 1 and 3 and then rows 2 and 4 turns $M$ into $I_4$.
   Each swap multiplies the determinant by $-1$, so $\det M = (-1)^2 \det I_4 = 1$.
5. So $\det M = 1$, while the formula gives $-1$, and the formula is false.

## Remarks

The example shows that blocks cannot be treated like numbers in the $2 \times 2$ formula.
For $1 \times 1$ blocks the formula is the true rule $ad - bc$, so the failure starts at blocks of size $2$.
With blocks of size $n$, the same matrix $\begin{pmatrix} 0 & I_n \\ I_n & 0 \end{pmatrix}$ has determinant $(-1)^n$, because it takes $n$ row swaps to reach $I_{2n}$.
So the formula, which always gives $-1$, is right for odd $n$ and wrong for even $n$.

Two correct tools replace the false formula.
Here $C = I_2$ and $D = 0$ commute, so the [[formula for commuting blocks|T4TRMJHX3S]] applies, and it gives the right value:
$$\det(AD - BC) = \det(0 - I_2) = \det(-I_2) = (-1)^2 = 1.$$
In general, when a corner block is invertible, the [[Schur complement formula|0KA7A4ENVJ]] is the right tool.
Here $B$ is invertible, so moving it to a diagonal corner by row swaps would also work.

## Explanations

### L1 human

For a $2 \times 2$ table of numbers, the determinant is $ad - bc$.
It is tempting to use the same rule when the four entries are themselves square blocks.
This example shows that the rule can then give the wrong sign: it predicts $-1$, but the true determinant is $1$.

### L2 human

The typical use of a block formula is a matrix with a zero corner block, where the [[block triangular rule|0J9TVTNB4K]] gives $\det A \det D$.
With no zero block, first ask whether a diagonal block is invertible, and then use the Schur complement.
The trap is to treat blocks like numbers.
Matrices do not commute, and the determinant of a matrix of blocks is not built from the determinants of the blocks in the same way as for entries.
