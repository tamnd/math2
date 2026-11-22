---
tag: WFM1CX5PZT
kind: statement
role: proposition
name: The columns of a square matrix form a basis iff the matrix is invertible
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [0KCQ9Y3QKA]
uses: [0VTQTPQGAV, 0EB9N0S33C, 76GG9B25A1]
proofs: [K3BWC7M959]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: The invertible matrix theorem
  - book: isbn:9780321982384
    locator: Section 2.3
---

## Statement

The bases of $F^n$ and the invertible $n \times n$ matrices are the same objects, read column by column.
Let $F$ be a field, let $n \ge 1$, and let $A$ be an $n \times n$ matrix over $F$ with columns $v_1, \dots, v_n \in F^n$.
Then $(v_1, \dots, v_n)$ is a [[basis|0VTQTPQGAV]] of $F^n$ if and only if $A$ is [[invertible|0EB9N0S33C]].
So the ordered bases of $F^n$ are exactly the lists of columns of the invertible $n \times n$ matrices over $F$.

## Remarks

### A check with numbers

Take the columns $(2, 1)$ and $(1, 1)$, so that
$$A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \qquad A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}.$$
Check: the product $A A^{-1}$ has rows $(2 - 1, -2 + 2) = (1, 0)$ and $(1 - 1, -1 + 2) = (0, 1)$, so it is $I$.
By the statement, $(2, 1), (1, 1)$ is a basis of $\mathbb{R}^2$.
The inverse also computes [[coordinates|04CYQHN6MC]]: the coordinates $c$ of a vector $x$ solve $Ac = x$, so $c = A^{-1} x$.
For $x = (3, 2)$ this gives
$$c = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 3 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix},$$
and indeed $(2, 1) + (1, 1) = (3, 2)$.
In contrast, the columns $(1, 2)$ and $(2, 4)$ of $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ are dependent, and the determinant $4 - 4 = 0$ confirms that this matrix is not invertible.

### Why each hypothesis is needed

The statement is about square matrices because both sides need them.
An invertible matrix is square by definition, and a basis of $F^n$ has exactly $n$ vectors by the [[dimension theorem|0WK0Y8RH1M]].
For a rectangular matrix, both sides fail together, but the two halves of a basis still have matrix forms, as the generalizations below say.

The field is not essential.
Over $\mathbb{Z}$, the columns $(2, 0)$ and $(0, 1)$ are independent but not a basis of $\mathbb{Z}^2$, since $a(2, 0) + b(0, 1) = (1, 0)$ would need $2a = 1$.
The matrix with these columns has determinant $2$, and it has no inverse with integer entries, so the equivalence still holds there.

### What it gives you

Any test for invertibility is a test for a basis of $F^n$: a nonzero [[determinant|0C3CFHDN6R]], or a reduced row echelon form equal to $I$, as in the [[row-reduction criterion|JXTGZPZP47]].
Counting invertible matrices counts ordered bases.
Over the field $\mathbb{F}_q$ with $q$ elements, the number of ordered bases of $\mathbb{F}_q^n$ is the [[order of the general linear group|0JQ1KNQW2K]],
$$(q^n - 1)(q^n - q) \cdots (q^n - q^{n-1});$$
for $q = 2$ and $n = 2$ this is $3 \cdot 2 = 6$; see [[vector spaces over finite fields|J9VE1X14PV]].

### The converse

The statement is an equivalence, so it has no separate converse.
The proof shows a little more: if the columns of a square $A$ span $F^n$, then a right inverse $X$ with $AX = I$ exists, and independence turns it into a two-sided inverse.

### Generalizations

For an $m \times n$ matrix $A$ over a field, the columns span $F^m$ exactly when $A$ has a right inverse, and they are independent exactly when $A$ has a left inverse.
For a commutative ring $R$, the columns of a square matrix form a basis of $R^n$ exactly when the matrix is invertible, which happens exactly when its determinant is a unit of $R$.

## Explanations

### L1 human

Write the vectors of a list as the columns of a square table of numbers.
The list is a basis exactly when the table can be undone, that is, when it has an inverse table.
For $(2, 1)$ and $(1, 1)$, the inverse exists, so these two vectors reach every point of the plane in exactly one way.

### L2 human

Here is a typical use: is $(1, 0, 1), (2, 1, 0), (0, 1, 1)$ a basis of $\mathbb{R}^3$?
Put the vectors as columns and expand the determinant along the first row:
$$\det \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} = 1 (1 \cdot 1 - 1 \cdot 0) - 2 (0 \cdot 1 - 1 \cdot 1) + 0 = 1 + 2 = 3.$$
The determinant is not zero, so the matrix is invertible and the three vectors form a basis.
One number replaced two separate checks, independence and spanning.
Watch out: the vectors go in as columns; putting them in as rows gives the transpose, which has the same determinant but a different inverse.

### L3 human

The statement identifies the set of ordered bases of $F^n$ with the group $GL_n(F)$.
The group acts on the bases by $B \mapsto BP$, and this action is free and transitive, so once one basis is fixed, every other basis corresponds to exactly one change of basis matrix.
This is the start of the sub-area on [[change of basis|0MKRHZB3WS]], and the same idea makes the set of bases of any $n$-dimensional space a torsor under $GL_n(F)$.
