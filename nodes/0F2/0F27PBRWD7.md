---
tag: 0F27PBRWD7
kind: definition
name: Row echelon form
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
defines: 0VYCDGMJJJ
uses: [0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Row_echelon_form
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 1.2
---

## Definition

A matrix is in row echelon form when its nonzero rows form a staircase and its zero rows sit at the bottom.
Let $F$ be a [[field|04C5ZBG1WT]] and let $A$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] over $F$.
The *leading entry* of a nonzero row of $A$ is its first nonzero entry, from the left.
The matrix $A$ is in *row echelon form* when these two conditions hold:

1. Each zero row of $A$ is below each nonzero row of $A$.
2. For two consecutive nonzero rows, the leading entry of the lower row is strictly to the right of the leading entry of the upper row.

## Notation

Some books also require that each leading entry is $1$.
Lay's textbook calls the form defined here "echelon form" and does not require leading $1$s.

## Remarks

### An example and the zeros it forces

The matrix $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{bmatrix}$ is in row echelon form, with leading entries in columns $1$ and $3$.
In row echelon form, all the entries below a leading entry are zero.
To see this, let the leading entry of row $i$ be in column $p$.
Every lower nonzero row has its leading entry in a column greater than $p$, by condition 2 used repeatedly, so its entry in column $p$ is $0$.
The zero rows have $0$ in column $p$ as well.

### What the definition leaves open

The definition says nothing about the entries above a leading entry, and they can be anything.
So a matrix usually has many row echelon forms.
The [[reduced row echelon form|0WF5AQYTW6]] adds conditions that make the form unique.

### Where it comes from

[[Gaussian elimination|0JVJ2WCXZH]] changes each matrix into a row echelon form by elementary row operations, by the [[existence theorem|FCM29NQ6DN]].

## Explanations

### L1 human

Row echelon form looks like a staircase.
Each nonzero row starts further to the right than the row above it, and the zero rows sit at the bottom.
A system in this form is easy to solve from the bottom row up.

### L2 human

To check a matrix, mark the leading entry of each row.
The marks must move strictly right as you go down, and the zero rows must come last.
For $\begin{bmatrix} 0 & 2 & 1 \\ 0 & 0 & 3 \end{bmatrix}$, the marks are in columns $2$ and $3$, so the matrix is in row echelon form.
Watch out: an empty first column is allowed, since the staircase may start anywhere.
