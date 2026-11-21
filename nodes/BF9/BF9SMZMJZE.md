---
tag: BF9SMZMJZE
kind: statement
role: theorem
name: Uniqueness of the reduced row echelon form
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
uses: [0WF5AQYTW6, 095DDGZF16, 0NNR68BFRY, E4GKK727ZM, FCM29NQ6DN, P3HMRQN5KT]
about: [0WF5AQYTW6]
proofs: [Y80F8462DG]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section1-2.xml#L1343
    locator: src/section1-2.xml:1343
  - url: https://en.wikipedia.org/wiki/Row_echelon_form
    locator: Reduced row echelon form
  - book: isbn:9780321982384
    locator: Section 1.2
---

## Statement

However you row reduce a matrix, the fully reduced result is always the same.
Let $F$ be a [[field|04C5ZBG1WT]] and let $A$ be an $m \times n$ matrix over $F$.
Then there is exactly one matrix in [[reduced row echelon form|0WF5AQYTW6]] that is [[row equivalent|095DDGZF16]] to $A$.
Equivalently: if two $m \times n$ matrices $R$ and $S$ in reduced row echelon form are row equivalent, then $R = S$.

## Remarks

### Two routes, one result

We reduce $A = \begin{bmatrix} 2 & 4 \\ 1 & 3 \end{bmatrix}$ in two orders.
First route: $R_1 \leftarrow \tfrac12 R_1$ gives $(1, 2)$, then $R_2 \leftarrow R_2 - R_1$ gives $(0, 1)$, and $R_1 \leftarrow R_1 - 2R_2$ gives $(1, 0)$.
Second route: $R_1 \leftrightarrow R_2$ gives the rows $(1, 3)$ and $(2, 4)$, then $R_2 \leftarrow R_2 - 2R_1$ gives $(0, -2)$.
Continuing, $R_2 \leftarrow -\tfrac12 R_2$ gives $(0, 1)$, and $R_1 \leftarrow R_1 - 3R_2$ gives $(1, 0)$.
Both routes end at $I_2$, as the theorem predicts.

### Why "reduced" is needed

Row echelon forms are not unique.
The matrix $\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ is row equivalent to the two different echelon forms $\begin{bmatrix} 1 & 2 \\ 0 & -2 \end{bmatrix}$ and $\begin{bmatrix} 3 & 4 \\ 0 & \tfrac23 \end{bmatrix}$, as [[two echelon forms|19FNDHJ181]] shows.
Leading $1$s alone are not enough either.
The matrices $\begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$ and $I_2$ both have leading $1$s and are row equivalent, but only $I_2$ has zeros above its pivots.
Existence of the reduced form is the [[existence theorem|FCM29NQ6DN]], and the content here is uniqueness.

### What follows

The RREF of a matrix is well defined, and it is written $\operatorname{rref}(A)$.
Two matrices of the same size are row equivalent if and only if they have the same RREF.
The pivot positions of any row echelon form of $A$ are those of $\operatorname{rref}(A)$, so they do not depend on the choices made in elimination.
So the number of pivots, the rank, is well defined, and so are the basic and free variables, as the page on [[pivots|0J0BBCMJ5W]] explains.
The RREF of an augmented matrix $[A \mid B]$ begins with the RREF of $A$, by the [[augmentation principle|BE3NZP35HY]].

### The easy converse

If $R = S$, then $R$ and $S$ are row equivalent, by the empty sequence of operations.

### Beyond fields

Over a Euclidean domain such as $\mathbb{Z}$, the Hermite normal form plays the same role, and it is also unique.
For column operations, the reduced column echelon form is unique in the same way, by transposition.

### Watch out

The theorem says nothing about echelon forms that are not reduced.
If your echelon form differs from the one in a book, both may be right, and only the RREFs must agree.

## History

Lay's textbook states the theorem in Section 1.2 and puts its proof in an appendix.
A short proof by induction on the number of columns was published by Thomas Yuster in *Mathematics Magazine* in 1984.

## Explanations

### L1 human

Different people can row reduce a matrix in different orders.
If they all go on to the fully reduced form, they always end with the same matrix.
So the fully reduced form is a reliable fingerprint of the matrix.

### L2 human

The typical use is to test row equivalence, or to speak of "the" rank, "the" pivot columns and "the" free variables of a matrix.
Without the theorem, these words would depend on the route taken through the elimination.
To test whether two matrices are row equivalent, reduce both fully and compare entry by entry.

### L3 human

The RREF is a canonical form for the orbits of $\mathrm{GL}_m(F)$ acting on $m \times n$ matrices from the left.
The orbit of $A$ is determined by its row space, and the nonzero rows of $\operatorname{rref}(A)$ are the unique reduced echelon basis of this space.
In the Grassmannian of $r$-dimensional subspaces of $F^n$, the pivot set of the RREF picks a Schubert cell, and the free entries of the RREF are coordinates on that cell.
