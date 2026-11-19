---
tag: 0BCMGDHZGR
kind: definition
name: Pivot
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
defines: 0J0BBCMJ5W
uses: [0F27PBRWD7]
sources:
  - url: https://en.wikipedia.org/wiki/Pivot_element
    locator: lead section
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section1-4.xml#L30
    locator: src/section1-4.xml:30
  - book: isbn:9780321982384
    locator: Section 1.2
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] and let $A$ be a matrix over $F$ in [[row echelon form|0VYCDGMJJJ]].
A *pivot* of $A$ is the leading entry of a nonzero row of $A$, that is, the first nonzero entry of that row.
A *pivot column* of $A$ is a column that contains a pivot.
For a general matrix $B$, take a row echelon form of $B$ that is row equivalent to $B$.
The *pivot positions* of $B$ are the positions of the pivots of this form, and the *pivot columns* of $B$ are the columns of $B$ that contain them.
In a system $Bx = b$, the unknowns of the pivot columns of $B$ are the *basic variables*, and the other unknowns are the *free variables*.

## Notation

Some books, such as Strang, use "pivot" for the nonzero number used in an elimination step.
Others, such as Lay, use "pivot position" for the place of a leading $1$ in the reduced form.

## Remarks

The pivot positions do not depend on the choice of the row echelon form, by the [[uniqueness of the RREF|BF9SMZMJZE]].
The number of pivots is the [[rank|0ZC9YTXZRY]] of the matrix.
In numerical work, partial pivoting chooses as pivot an entry of largest absolute value in its column, to reduce rounding errors.

## Explanations

### L1 human

A pivot is the first nonzero number in a row of a staircase matrix.
During elimination we divide by the pivot and use it to clear the entries below it.
Each pivot fixes one unknown, and each column without a pivot gives a free unknown.

### L2 human

The echelon form $\begin{bmatrix} 3 & 1 & 2 \\ 0 & 0 & 5 \end{bmatrix}$ of a system in $x_1, x_2, x_3$ has pivots $3$ and $5$.

1. The pivot positions are $(1, 1)$ and $(2, 3)$.
2. The pivot columns are $1$ and $3$, so $x_1$ and $x_3$ are basic.
3. Column $2$ has no pivot, so $x_2$ is free.

A trap: the pivot columns of $B$ are columns of the original matrix $B$, at the same places as in the echelon form; their entries differ.
