---
tag: KXG0P38NCE
kind: example
name: Counting nonzero rows or diagonal entries does not give the rank
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
not_instance_of:
  - target: 0ZC9YTXZRY
    note: the number of nonzero rows of a matrix that is not in echelon form, and the number of nonzero diagonal entries, are not the rank
uses: [0EWQEYRVA8, 0F27PBRWD7]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Computing the rank of a matrix
---

## Example

Two quick counts look like the rank but are not: the number of nonzero rows of a matrix, and the number of nonzero entries on its diagonal.
Three small matrices show the failures.

1. Let $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$.
Both rows are nonzero, but the second column is twice the first, so the column space is the line spanned by $(1, 2)$ and the [[rank|0EWQEYRVA8]] is $1$, not $2$.
2. Subtract $2$ times row 1 from row 2 of $A$:
$$\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \to \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix}.$$
This is an [[echelon form|0F27PBRWD7]], and only now does the count of nonzero rows give the rank $1$.
3. Let $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
Both diagonal entries are $0$, but the second column $(1, 0)$ is nonzero, so the column space is spanned by $(1, 0)$ and $\rank N = 1$, not $0$.
4. Let $M = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.
Both diagonal entries are nonzero, but the two columns are equal, so $\rank M = 1$, not $2$.

## Remarks

Each count works only for a special shape of matrix.
The number of nonzero rows is the rank for a matrix in echelon form, because there the nonzero rows are independent: each one has its leading entry in a column where the rows below it are zero.
The number of nonzero diagonal entries is the rank for a diagonal matrix, and it is also the rank for an upper triangular matrix whose diagonal entries are all nonzero.
For a general triangular matrix the count is only a lower bound.
If $k$ diagonal entries are nonzero, the rows and columns through them form a triangular $k \times k$ submatrix with nonzero diagonal, so its minor is nonzero and the rank is at least $k$.
The rank can be larger: $N$ above has count $0$ and rank $1$, and $\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$ has count $0$ and rank $2$.
For a matrix that is not triangular, such as $M$, the count can also be too large.

## Explanations

### L1 human

The rank counts independent rows, not nonzero rows.
Two nonzero rows can still be multiples of each other, like $(1, 2)$ and $(2, 4)$, and then together they give only one direction.
Zeros on the diagonal do not mean a small rank either, since the nonzero entries can sit off the diagonal.

### L2 human

The safe method is to row reduce first and count afterwards.
Row operations do not change the row space, so they do not change the rank, and in echelon form the count of nonzero rows is correct.
Watch out for triangular matrices: the diagonal of a triangular matrix gives its determinant, but it does not give its rank unless all diagonal entries are nonzero.
