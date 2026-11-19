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

Let $F$ be a [[field|04C5ZBG1WT]] and let $A$ be an $m \times n$ matrix over $F$.
Then there is exactly one matrix in [[reduced row echelon form|0WF5AQYTW6]] that is [[row equivalent|095DDGZF16]] to $A$.
Equivalently: if two $m \times n$ matrices $R$ and $S$ in reduced row echelon form are row equivalent, then $R = S$.

## Remarks

### Why each hypothesis is needed

1. The word "reduced" is needed. The matrix $\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ is row equivalent to the two different row echelon forms $\begin{bmatrix} 1 & 2 \\ 0 & -2 \end{bmatrix}$ and $\begin{bmatrix} 3 & 4 \\ 0 & \tfrac23 \end{bmatrix}$, see [[two echelon forms|19FNDHJ181]].
2. Both conditions of the reduced form are needed. The matrices $\begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$ and $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ have leading $1$s and are row equivalent, but only the second has zeros above its pivots.
3. Over a field, existence is [[the existence theorem|FCM29NQ6DN]]; the content here is uniqueness.

### Consequences

1. The RREF of a matrix is well defined, and it is written $\operatorname{rref}(A)$.
2. Two matrices of the same size are row equivalent if and only if they have the same RREF.
3. The pivot positions of any row echelon form of $A$ are the pivot positions of $\operatorname{rref}(A)$, so they do not depend on the choices made in elimination.
4. So the number of pivots, the rank, is well defined, and so are the basic and free variables, see [[pivots|0J0BBCMJ5W]].
5. The RREF of an augmented matrix $[A \mid B]$ begins with the RREF of $A$, see [[the augmentation principle|BE3NZP35HY]].

### Converse

The converse is true and easy: if $R = S$, then $R$ and $S$ are row equivalent, by the empty sequence of operations.

### Generalizations

1. Over a Euclidean domain such as $\mathbb{Z}$, the Hermite normal form plays the same role, and it is also unique.
2. For column operations, the reduced column echelon form is unique in the same way, by transposition.

## History

The statement is classical and appears in all modern textbooks, for example Lay, Section 1.2, where the proof is put in an appendix.
A short proof by induction on the number of columns was published by Yuster in *Mathematics Magazine* in 1984.

## Explanations

### L1 human

Different people can row reduce a matrix in different orders.
If they all go on to the fully reduced form, they always end with the same matrix.
So the fully reduced form is a reliable fingerprint of the matrix.

### L2 human

We reduce $A = \begin{bmatrix} 2 & 4 \\ 1 & 3 \end{bmatrix}$ in two orders.

1. Order 1: $R_1 \leftarrow \tfrac12 R_1$ gives $(1, 2)$; $R_2 \leftarrow R_2 - R_1$ gives $(0, 1)$; $R_1 \leftarrow R_1 - 2R_2$ gives $(1, 0)$.
2. Order 2: $R_1 \leftrightarrow R_2$ gives rows $(1, 3)$, $(2, 4)$; $R_2 \leftarrow R_2 - 2R_1$ gives $(0, -2)$.
3. Then $R_2 \leftarrow -\tfrac12 R_2$ gives $(0, 1)$, and $R_1 \leftarrow R_1 - 3R_2$ gives $(1, 0)$.
4. Both orders give $I_2$, as the theorem predicts.

The typical use is to test row equivalence, or to say "the" rank, "the" pivot columns and "the" free variables of a matrix.
A trap: the theorem says nothing about echelon forms that are not reduced; those are not unique.

### L3 human

The RREF is a canonical form for the orbits of $\mathrm{GL}_m(F)$ acting on $m \times n$ matrices from the left.
The orbit of $A$ is determined by its row space, and the nonzero rows of $\operatorname{rref}(A)$ are the unique reduced echelon basis of this space.
In the Grassmannian of $r$-dimensional subspaces of $F^n$, the pivot set of the RREF picks a Schubert cell, and the free entries of the RREF are coordinates on that cell.
