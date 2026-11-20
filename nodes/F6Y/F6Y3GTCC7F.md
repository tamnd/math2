---
tag: F6Y3GTCC7F
kind: example
name: The diagonal scheme of Sarrus fails for a 4 × 4 matrix
msc: ["15A15"]
topics: [DTBK11SR77]
audience: school
instance_of: [08SP3DF8NB]
not_instance_of:
  - target: 7H2P40X0MV
    note: the diagonal scheme gives -1 for this 4 × 4 permutation matrix, but the determinant is 1, so the scheme is not a rule for n = 4
uses: [7H2P40X0MV, 08SP3DF8NB, 09YB3WQG38, 0Z4BWARC38, 016PE4VZ8Q]
sources:
  - url: https://en.wikipedia.org/wiki/Rule_of_Sarrus
    locator: lead section
---

## Example

Let $P = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$.
This is the [[permutation matrix|08SP3DF8NB]] with $p_{12} = p_{21} = p_{34} = p_{43} = 1$.
The "4 × 4 Sarrus scheme" copies the first three columns to the right and uses four diagonals in each direction.

1. The down diagonals are the products $p_{1, 1+k}\, p_{2, 2+k}\, p_{3, 3+k}\, p_{4, 4+k}$ for $k = 0, 1, 2, 3$, with column indices read modulo $4$.
2. For $k = 0$ the product contains $p_{11} = 0$. For $k = 1$ it contains $p_{23} = 0$. For $k = 2$ it contains $p_{13} = 0$. For $k = 3$ it contains $p_{14} = 0$. So the down sum is $0$.
3. The up diagonals are the products $p_{1, j}\, p_{2, j-1}\, p_{3, j-2}\, p_{4, j-3}$ for $j = 1, 2, 3, 4$, modulo $4$.
4. For $j = 2$ the product is $p_{12} p_{21} p_{34} p_{43} = 1$. For $j = 1, 3, 4$ the product contains $p_{11}$, $p_{13}$ or $p_{14}$, which are $0$.
5. So the scheme gives $0 - 1 = -1$.
6. The true value: $P$ comes from $I_4$ by two row swaps, rows $1, 2$ and rows $3, 4$.
7. Each swap changes the sign, by the [[effect of row operations|09YB3WQG38]], and $\det I_4 = 1$ by the [[determinant of the identity|0Z4BWARC38]].
8. So $\det P = (-1)^2 \cdot 1 = 1 \neq -1$. The scheme fails.

## Remarks

The [[Leibniz formula|016PE4VZ8Q]] for $n = 4$ has $24$ terms, and the scheme lists only $8$ of them.
For this $P$ the only nonzero Leibniz term belongs to the permutation $(1\,2)(3\,4)$, which is even.
The scheme does list this term, but with the sign of an up diagonal, which is wrong.
For $I_4$ the scheme gives the correct value $1$, so a single test matrix can hide the error.

## Explanations

### L1 human

The diagonal trick for $3 \times 3$ matrices does not work for $4 \times 4$ matrices.
For this matrix of zeros and ones the trick gives $-1$.
The true determinant is $1$, because the matrix comes from the identity by two swaps of rows.

### L2 human

To compute a $4 \times 4$ determinant, use row reduction or a [[Laplace expansion|0C08BQ3M05]].
A trap: the scheme gives the right answer for some matrices, such as $I_4$ or diagonal matrices, so a test on those matrices does not show the error.
