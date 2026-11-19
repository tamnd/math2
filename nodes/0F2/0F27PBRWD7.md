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

Let $F$ be a [[field|04C5ZBG1WT]] and let $A$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] over $F$.
The *leading entry* of a nonzero row of $A$ is its first nonzero entry, from the left.
The matrix $A$ is in *row echelon form* when these two conditions hold:

1. Each zero row of $A$ is below each nonzero row of $A$.
2. For two consecutive nonzero rows, the leading entry of the lower row is strictly to the right of the leading entry of the upper row.

## Notation

Some authors, for example Anton, also require that each leading entry is $1$.
Lay calls the form defined here "echelon form" and does not require leading $1$s.

## Remarks

The matrix $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{bmatrix}$ is in row echelon form.
In row echelon form, all the entries below a leading entry are zero.
[[Gaussian elimination|0JVJ2WCXZH]] changes each matrix into a row echelon form by elementary row operations, see [[the existence theorem|FCM29NQ6DN]].

## Explanations

### L1 human

Row echelon form looks like a staircase.
Each nonzero row starts further to the right than the row above it, and the zero rows sit at the bottom.
A system in this form is easy to solve from the bottom row up.

### L2 human

We check that all entries below a leading entry are zero.

1. Let the leading entry of row $i$ be in column $p$.
2. The leading entry of row $i + 1$, if that row is nonzero, is in a column greater than $p$, so the entry $(i + 1, p)$ is $0$.
3. In the same way, each lower nonzero row has its leading entry further right, so its entry in column $p$ is $0$.
4. Zero rows have $0$ in column $p$.

A trap: the definition says nothing about the entries above a leading entry; they can be anything.
