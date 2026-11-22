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
This is the [[permutation matrix|08SP3DF8NB]] with $p_{12} = p_{21} = p_{34} = p_{43} = 1$ and all other entries $0$.
A naive "$4 \times 4$ Sarrus scheme" copies the first three columns to the right and uses four diagonals in each direction, with a plus sign going down and a minus sign going up.
We show that this scheme gives the wrong value for $P$.

1. The down diagonals are the products $p_{1, 1+k}\, p_{2, 2+k}\, p_{3, 3+k}\, p_{4, 4+k}$ for $k = 0, 1, 2, 3$, with the column indices read modulo $4$.
2. Each down product contains a zero entry.
   For $k = 0$ it contains $p_{11} = 0$, for $k = 1$ it contains $p_{23} = 0$, for $k = 2$ it contains $p_{13} = 0$, and for $k = 3$ it contains $p_{14} = 0$.
   So the down sum is $0$.
3. The up diagonals are the products $p_{1, m}\, p_{2, m-1}\, p_{3, m-2}\, p_{4, m-3}$ for $m = 1, 2, 3, 4$, again modulo $4$.
4. For $m = 2$ the column indices are $2, 1, 4, 3$, and the product is $p_{12} p_{21} p_{34} p_{43} = 1$.
   For $m = 1, 3, 4$ the product contains $p_{11}$, $p_{13}$ or $p_{14}$, which are $0$.
   So the up sum is $1$.
5. The scheme gives $0 - 1 = -1$.
6. Now the true value.
   The matrix $P$ comes from $I_4$ by two row swaps: rows $1$ and $2$, then rows $3$ and $4$.
7. Each swap changes the sign of the determinant, by the [[effect of row operations|09YB3WQG38]], and $\det I_4 = 1$ by the [[determinant of the identity matrix|0Z4BWARC38]].
8. So $\det P = (-1)^2 \cdot 1 = 1$, and the scheme, which gave $-1$, fails.

## Remarks

The [[Leibniz formula|016PE4VZ8Q]] for $n = 4$ has $4! = 24$ terms, and the scheme lists only $8$ of them.
For $P$ the only nonzero Leibniz term belongs to the permutation $(1\,2)(3\,4)$, which is a product of two transpositions and so is even.
The scheme does list this term, as an up diagonal, but it gives it the minus sign, which is wrong.

For other matrices the scheme fails because it misses terms.
For the permutation matrix of the $3$-cycle $(1\,2\,3)$, which keeps $4$ fixed, the only nonzero Leibniz term is not on any of the $8$ diagonals, so the scheme gives $0$ while the determinant is $1$.
For $I_4$, on the other hand, the scheme gives the correct value $1$, so a test on the identity cannot show the error.

## Explanations

### L1 human

The diagonal trick for $3 \times 3$ matrices does not work for $4 \times 4$ matrices.
For this matrix of zeros and ones the trick gives $-1$.
The true determinant is $1$, because the matrix comes from the identity by two swaps of rows, and two sign changes cancel.

### L2 human

To compute a $4 \times 4$ determinant, use row reduction or a [[Laplace expansion|0C08BQ3M05]].
The example also teaches how to test a rule.
A matrix with a single nonzero term in the Leibniz formula isolates one permutation, so it shows at once whether the rule has that term with the right sign.
Diagonal matrices are bad tests, because the false scheme gets them right.
