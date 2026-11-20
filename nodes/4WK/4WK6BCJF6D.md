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

Let $M = \begin{pmatrix} 0 & I_2 \\ I_2 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix}$ over $\mathbb{Q}$.
So the [[blocks|01AXG9KZQF]] are $A = D = 0$ and $B = C = I_2$, all of size $2 \times 2$.

1. The false formula gives $\det A \det D - \det B \det C = 0 \cdot 0 - 1 \cdot 1 = -1$.
2. Each row and each column of $M$ has exactly one entry $1$, so only one term of the [[Leibniz formula|016PE4VZ8Q]] is nonzero.
3. That term is the permutation $1 \mapsto 3$, $2 \mapsto 4$, $3 \mapsto 1$, $4 \mapsto 2$, which is $(1\,3)(2\,4)$.
4. It is a product of two transpositions, so its sign is $+1$, and $\det M = 1$.
5. Check by [[row swaps|09YB3WQG38]]: swap rows 1 and 3, then rows 2 and 4, to get $I_4$.
6. Two swaps multiply the determinant by $(-1)^2 = 1$, so $\det M = \det I_4 = 1$.
7. So $\det M = 1 \ne -1$, and the formula is false.

## Remarks

The blocks here commute, so the [[commuting-blocks formula|T4TRMJHX3S]] applies: $\det(AD - BC) = \det(-I_2) = 1$, which is correct.
For $1 \times 1$ blocks the false formula reduces to $ad - bc$, which is correct; the error appears only for blocks of size at least $2$.
The correct general tool is the [[Schur complement formula|0KA7A4ENVJ]].

## Explanations

### L1 human

For a $2 \times 2$ matrix of numbers, the determinant is $ad - bc$.
It is tempting to use the same rule when the four entries are square blocks.
This example shows that the rule then gives the wrong sign.

### L2 human

The typical use of block formulas is a matrix with a zero block, where the [[block triangular rule|0J9TVTNB4K]] applies.
With no zero block, first check whether a corner block is invertible, and then use the Schur complement.
The trap is to treat blocks like numbers: matrices do not commute, and $\det$ is not additive.
