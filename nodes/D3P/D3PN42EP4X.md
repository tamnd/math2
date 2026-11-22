---
tag: "D3PN42EP4X"
kind: statement
role: proposition
name: Vectors span F^m iff the matrix of columns has a pivot in every row
msc: ["15A03", "15A06"]
topics: [MVH97H8B2J]
audience: ug1
uses: [0DTY8B9HMS, 0BCMGDHZGR, 0XM8BZD76G, 0BJKVF90Z6]
about: [088RYKAWK9]
proofs: [AVT1JV7PDX]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section2-3.xml#L1347
    locator: src/section2-3.xml:1347
  - book: isbn:9780321982384
    locator: Section 1.4
---

## Statement

Row reduction decides whether a list of vectors spans $F^m$: look for a pivot in every row.
Let $F$ be a field, and let $v_1, \dots, v_n$ be vectors in the [[coordinate space|713F6AM1X1]] $F^m$.
Let $A$ be the $m \times n$ matrix whose columns are $v_1, \dots, v_n$, and let $R$ be a row echelon form of $A$.

1. The vectors $v_1, \dots, v_n$ [[span|0BJKVF90Z6]] $F^m$ if and only if every row of $R$ contains a [[pivot|0BCMGDHZGR]].
2. In particular, if $v_1, \dots, v_n$ span $F^m$, then $n \ge m$.

## Remarks

### A check in three dimensions

Take $v_1 = (1, 0, 1)$, $v_2 = (0, 1, 1)$ and $v_3 = (1, 1, 0)$ in $\mathbb{R}^3$.
Subtract row 1 from row 3, then row 2 from row 3:
$$\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & -2 \end{pmatrix}.$$
Every row has a pivot, so the vectors span $\mathbb{R}^3$.
If you replace $v_3$ by $(1, 1, 2)$, the last entry becomes $2 - 1 - 1 = 0$ and the third row is zero.
Then the vectors span only the plane $z = x + y$, since $(1, 1, 2) = v_1 + v_2$.

### Why each hypothesis is needed

The pivots must be read from an echelon form, not from $A$ itself.
The matrix with columns $(0, 1)$ and $(1, 0)$ has the entry $0$ in its top left corner, yet its columns span $F^2$; one row swap shows a pivot in each row.

The target must be all of $F^m$.
For a proper subspace $W$ of $F^m$, a spanning set of $W$ never passes the test, because its echelon form has a zero row.
For example, $(1, 0, 0)$ and $(0, 1, 0)$ span the plane $z = 0$, and their matrix has a zero third row.

The scalars must form a field.
Over the ring $\mathbb{Z}$, the $1 \times 1$ matrix $(2)$ is already in echelon form with a nonzero entry in its only row, but $2$ does not generate $\mathbb{Z}$, since $1$ is not an integer multiple of $2$.
The proof divides by pivots, and that needs inverses.

### What it gives you

Each pivot sits in its own column, so an echelon form of an $m \times n$ matrix has at most $n$ pivots.
If $n < m$, some row has no pivot, which is part 2: you need at least $m$ vectors to span $F^m$.
A row without a pivot also produces a concrete vector $b$ outside the span, as the [[proof|AVT1JV7PDX]] shows.
Together with the [[column test for independence|76GG9B25A1]], which needs a pivot in every column, the theorem shows that a basis of $F^m$ has exactly $m$ vectors: a square matrix with a pivot in every row and every column.

### The converse

Part 1 is already an equivalence.
The converse of part 2 is false: $(1, 1)$ and $(2, 2)$ are two vectors in $F^2$, but every combination of them is a multiple of $(1, 1)$, so they do not span.

### Generalizations

In a space $V$ of dimension $m$, choose a basis and replace each vector by its coordinate vector in $F^m$.
Then $n$ vectors span $V$ exactly when their matrix of coordinates has a pivot in every row.
In matrix language, the theorem says that the columns of $A$ span $F^m$ exactly when $A$ has rank $m$.

## Explanations

### L1 human

Put the vectors side by side as the columns of a table and simplify the table by row reduction.
If each row of the simplified table has a leading entry, then every target vector can be reached, so the vectors span.
If one row is all zeros, some target cannot be reached.
Since each column gives at most one leading entry, you need at least as many vectors as rows.

### L2 human

Do $(1, 2)$, $(2, 3)$ and $(3, 5)$ span $\mathbb{R}^2$?
The matrix has rows $(1, 2, 3)$ and $(2, 3, 5)$.
Subtract twice row 1 from row 2:
$$\begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 5 \end{pmatrix} \to \begin{pmatrix} 1 & 2 & 3 \\ 0 & -1 & -1 \end{pmatrix}.$$
Both rows have a pivot, so the three vectors span $\mathbb{R}^2$.
The test says nothing about waste: here $(3, 5) = (1, 2) + (2, 3)$, so one vector is redundant, and the [[column test|76GG9B25A1]] detects that from the third column, which has no pivot.

### L3 human

The theorem is the statement that the linear map $x \mapsto Ax$ from $F^n$ to $F^m$ is surjective exactly when its rank is $m$.
Row operations multiply $A$ on the left by an invertible matrix, which changes the target space by an isomorphism and so keeps surjectivity.
The dual statement, a pivot in every column, is injectivity, and the two together are the invertible matrix theorem for square matrices.
