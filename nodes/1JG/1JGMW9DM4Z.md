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

Row reduction keeps the row space, and the rows that survive it are a basis.
Let $F$ be a field, let $A$ be an $m \times n$ matrix over $F$, and let $U$ be a matrix in [[row echelon form|0F27PBRWD7]] that is [[row equivalent|006BHFWMAP]] to $A$.

1. The [[row spaces|0EP73HK4C4]] of $A$ and $U$ are equal.
2. The nonzero rows of $U$ form a [[basis|0VTQTPQGAV]] of $\operatorname{Row}(A)$.
3. Hence $\dim \operatorname{Row}(A)$ is the number of pivots of $U$.

## Remarks

### Why each hypothesis is needed

The matrix $U$ must be row equivalent to $A$, because other operations move the row space.
For $A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$, subtracting column 1 from column 2 gives the echelon matrix $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, whose nonzero row $(1, 0)$ does not lie in $\operatorname{Row}(A)$, the line through $(1, 1)$.

The matrix $U$ must be in echelon form for part 2, because nonzero rows alone need not be independent.
The matrix $\begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix}$ has two nonzero rows, but the second is twice the first.
The staircase of pivots is what makes the rows independent.

### What it gives you

The number of pivots is the same for every echelon form of $A$, because it equals $\dim \operatorname{Row}(A)$, which does not depend on the form.
Together with the [[pivot basis theorem|11CSKXQNG3]], it shows that the row space and the column space both have dimension equal to the number of pivots, which is the [[proof of row rank equals column rank by row reduction|WK6YWCWJD0]].

For a worked use, take $A$ with rows $(0, 2, 4)$, $(1, 1, 1)$ and $(1, 3, 5)$.
An echelon form has the nonzero rows $(1, 1, 1)$ and $(0, 2, 4)$, so these are a basis, and the [[example with a non-reduced form|NZ8PF59MTJ]] shows that the row space is the plane $x - 2y + z = 0$.
Notice the contrast with the column space: the basis of the row space comes from the reduced matrix, while the basis of the column space must come from $A$.

### The converse

Two $m \times n$ matrices with the same row space are row equivalent.
The reason is that the nonzero rows of the reduced row echelon form are determined by the row space alone, so both matrices reduce to the same matrix.
So the row space is a complete invariant of row equivalence.

### Generalizations

Over the integers, division by a pivot is not allowed, and the Hermite normal form plays the role of the reduced form for the group spanned by the rows.

## Explanations

### L1 human

Row operations only mix the rows, so they do not change the row space.
After reduction, the nonzero rows form a staircase, and a staircase of rows cannot cancel to zero.
So these rows are a basis, and counting them gives the dimension.

### L2 human

The [[proof|JVTHT2561H]] has two parts.
First, each row operation can be undone, so the old rows and the new rows are combinations of each other, and the spans agree.
Second, in echelon form each nonzero row has its pivot in a column where all lower rows are zero.
In a combination that equals zero, the entry at the first pivot column involves only the first coefficient, so that coefficient is zero, and the argument continues down the staircase.
Watch out: the rows of $A$ in the positions of the nonzero rows of $U$ need not be a basis, because row exchanges can move the rows.
For $A$ with rows $(0, 0)$ and $(1, 1)$, the echelon form has the nonzero row $(1, 1)$ in position 1, but row 1 of $A$ is zero.
