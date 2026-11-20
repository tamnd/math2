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

Let $F$ be a [[field|04C5ZBG1WT]] and let $A$ be a matrix over $F$.
The matrix $A$ is in *reduced row echelon form* when these three conditions hold:

1. $A$ is in [[row echelon form|0VYCDGMJJJ]].
2. The leading entry of each nonzero row is $1$.
3. In each column that has a leading entry, all the other entries are $0$.

## Notation

The RREF of $A$, the unique matrix in reduced row echelon form that is row equivalent to $A$, is written $\operatorname{rref}(A)$.
Lay calls this form the "reduced echelon form".

## Remarks

The matrix $\begin{bmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$ is in reduced row echelon form.
Each matrix is [[row equivalent|006BHFWMAP]] to exactly one matrix in reduced row echelon form, see [[the uniqueness theorem|BF9SMZMJZE]].
[[Gauss-Jordan elimination|098D6FQN3N]] computes this matrix.
The number of nonzero rows of the reduced row echelon form of $A$ is the [[rank|0ZC9YTXZRY]] of $A$.

## Explanations

### L1 human

Reduced row echelon form is the simplest form that row operations can reach.
Each pivot is a $1$, and it has zeros above it and below it.
From this form we can read the solutions of the system directly.

### L2 human

We check the conditions for $\begin{bmatrix} 1 & 0 & 4 \\ 0 & 1 & -2 \end{bmatrix}$.

1. The leading entries are in columns $1$ and $2$, moving right, and there are no zero rows. So condition 1 holds.
2. Both leading entries are $1$. So condition 2 holds.
3. Column $1$ is $(1, 0)$ and column $2$ is $(0, 1)$. So condition 3 holds.

A trap: condition 3 concerns only the pivot columns; column $3$ may contain any numbers.
