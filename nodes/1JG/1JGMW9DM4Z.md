---
tag: 1JGMW9DM4Z
kind: statement
role: proposition
name: The nonzero rows of an echelon form are a basis of the row space
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
about: [069MCGX635]
uses: [0EP73HK4C4, 0F27PBRWD7, 006BHFWMAP, 0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: Basis
  - book: isbn:9780321982384
    locator: Section 4.6
---

## Statement

Let $F$ be a field, let $A$ be an $m \times n$ matrix over $F$, and let $U$ be a matrix in [[row echelon form|0F27PBRWD7]] that is [[row equivalent|006BHFWMAP]] to $A$.

1. The [[row spaces|0EP73HK4C4]] of $A$ and $U$ are equal.
2. The nonzero rows of $U$ form a [[basis|0VTQTPQGAV]] of $\operatorname{Row}(A)$.
3. So $\dim \operatorname{Row}(A)$ is the number of pivots of $U$.

## Remarks

### Why each hypothesis is needed

- $U$ must be row equivalent to $A$. A matrix obtained by column operations has, in general, a different row space.
- $U$ must be in echelon form for part 2. The matrix $\begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix}$ has two nonzero rows, but they are dependent.

### Consequences

- The number of pivots does not depend on the echelon form chosen, since it is $\dim \operatorname{Row}(A)$.
- With the [[theorem on the pivot basis|11CSKXQNG3]], $\dim \operatorname{Row}(A) = \dim \operatorname{Col}(A)$, both equal to the number of pivots. This is the [[proof of row rank equals column rank by row reduction|WK6YWCWJD0]].
- Unlike the column space, the basis of the row space comes from the reduced matrix, not from $A$.

### Converse

Two $m \times n$ matrices with the same row space are row equivalent.
The nonzero rows of the reduced row echelon form are determined by the row space, so both matrices have the same reduced form.
So the row space is a complete invariant of row equivalence.

### Generalizations

Over the integers, the Hermite normal form plays the same role for the module spanned by the rows.

## Explanations

### L1 human

Row operations only mix the rows, so they do not change the row space.
After reduction, the nonzero rows are independent, so they are a basis.

### L2 human

The proof has two parts.
First, each row operation is reversible, so the old rows and the new rows are combinations of each other.
Second, in echelon form each nonzero row has a pivot in a column where all lower rows are zero.
This staircase shape forces the coefficients of any vanishing combination to be zero, one at a time from the top.
