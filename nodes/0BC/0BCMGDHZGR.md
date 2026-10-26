---
tag: 0BCMGDHZGR
kind: definition
name: Pivot
msc: [15A06]
defines: 0J0BBCMJ5W
uses: [0F27PBRWD7]
sources:
  - url: https://en.wikipedia.org/wiki/Pivot_element
    locator: lead section
---

## Definition

Let $F$ be a field and let $A$ be a matrix over $F$ in [[row echelon form|0VYCDGMJJJ]].
A *pivot* of $A$ is the leading entry of a nonzero row of $A$, that is, the first nonzero entry of that row.
A *pivot column* of $A$ is a column that contains a pivot.
For a general matrix $B$, take a row echelon form of $B$ that is row equivalent to $B$.
The pivot positions of $B$ are the positions of the pivots of this form.

## Remarks

The pivot positions do not depend on the choice of the row echelon form.
The number of pivots is the [[rank|0ZC9YTXZRY]] of the matrix.
In the system $Ax = b$, the unknowns of the pivot columns are the *basic variables*, and the other unknowns are the *free variables*.
In numerical work, partial pivoting chooses as pivot an entry of largest absolute value in its column, to reduce rounding errors.

## Explanations

### L1 human

A pivot is the first nonzero number in a row of a staircase matrix.
During elimination we divide by the pivot and use it to clear the entries below it.
Each pivot fixes one unknown, and each column without a pivot gives a free unknown.
