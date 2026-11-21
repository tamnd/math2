---
tag: 0NNR68BFRY
kind: definition
name: Reduced row echelon form
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
defines: 0WF5AQYTW6
uses: [0F27PBRWD7]
sources:
  - url: https://en.wikipedia.org/wiki/Row_echelon_form
    locator: Reduced row echelon form
  - book: isbn:9780321982384
    locator: Section 1.2
---

## Definition

A matrix is in reduced row echelon form when it is a staircase whose steps are $1$s with zeros above and below them.
Let $F$ be a [[field|04C5ZBG1WT]] and let $A$ be a matrix over $F$.
The matrix $A$ is in *reduced row echelon form* when these three conditions hold:

1. $A$ is in [[row echelon form|0VYCDGMJJJ]].
2. The leading entry of each nonzero row is $1$.
3. In each column that has a leading entry, all the other entries are $0$.

## Notation

The RREF of $A$, the unique matrix in reduced row echelon form that is row equivalent to $A$, is written $\operatorname{rref}(A)$.
Lay's textbook calls this form the "reduced echelon form".

## Remarks

### Checking the three conditions

Take $\begin{bmatrix} 1 & 0 & 4 \\ 0 & 1 & -2 \end{bmatrix}$.
The leading entries are in columns $1$ and $2$, moving right, and there are no zero rows, so condition 1 holds.
Both leading entries are $1$, so condition 2 holds.
Column $1$ is $(1, 0)$ and column $2$ is $(0, 1)$, so condition 3 holds.
Column $3$ has no leading entry, and condition 3 says nothing about it.

### What the definition makes possible

Each matrix is [[row equivalent|006BHFWMAP]] to exactly one matrix in reduced row echelon form, by the [[uniqueness theorem|BF9SMZMJZE]].
This is why the notation $\operatorname{rref}(A)$ makes sense.
[[Gauss-Jordan elimination|098D6FQN3N]] computes this matrix.
The number of nonzero rows of $\operatorname{rref}(A)$ is the [[rank|0ZC9YTXZRY]] of $A$.

### Watch out

Condition 3 concerns only the pivot columns.
In $\begin{bmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$, which is in reduced row echelon form, the entry $2$ in the non-pivot column $2$ is allowed.

## Explanations

### L1 human

Reduced row echelon form is the simplest form that row operations can reach.
Each pivot is a $1$, and it has zeros above it and below it.
From this form we can read the solutions of the system directly.

### L2 human

To bring an echelon form to reduced form, scale each pivot row so that its pivot is $1$.
Then use each pivot to clear the entries above it, starting from the bottom pivot.
For $\begin{bmatrix} 1 & 2 & 5 \\ 0 & 1 & 3 \end{bmatrix}$, one step $R_1 \leftarrow R_1 - 2R_2$ gives $\begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 3 \end{bmatrix}$.
