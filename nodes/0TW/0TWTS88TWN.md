---
tag: 0TWTS88TWN
kind: definition
name: Invertible matrix
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: school
defines: 0EB9N0S33C
uses: [0CP7YY6NAG, 06DW9BAWB1, 076JGP6R3T]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.inv
    match: variant
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Definition
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-1.xml#L202
    locator: src/section3-1.xml:202
  - book: isbn:9780321982384
    locator: Section 2.2
inventory: [P2E2KV54BD]
---

## Definition

This defines when a square matrix has a two-sided inverse.
Let $R$ be a commutative ring, for example a field, and let $n \ge 1$.
Let $A$ be an $n \times n$ [[square matrix|0CP7YY6NAG]] over $R$.
An inverse of $A$ is an $n \times n$ matrix $B$ over $R$ with
$$AB = I_n \quad \text{and} \quad BA = I_n,$$
where $I_n$ is the [[identity matrix|06DW9BAWB1]] and the products are [[matrix products|076JGP6R3T]].
The matrix $A$ is *invertible* when it has an inverse.
A square matrix that is not invertible is *singular*.

## Notation

A square matrix has at most one inverse, by the [[uniqueness of the inverse|FMCX4D7RD4]].
So we write $A^{-1}$ for the inverse of an invertible matrix $A$.
Other names for invertible are *nonsingular* and *regular*.

## Remarks

The definition asks for two equations because matrix products do not commute in general, so $AB = I_n$ alone does not say what $BA$ is.
For square matrices over a field, each of the two equations implies the other, by [[one-sided inverses of square matrices|0753Y2X5K6]].
A matrix $B$ with only $AB = I$ is a right inverse of $A$, and a matrix $C$ with only $CA = I$ is a left inverse.
These one-sided notions make sense for non-square matrices too, but a non-square matrix is never called invertible.

The ring $R$ matters.
The $1 \times 1$ matrix $(2)$ is invertible over $\mathbb{Q}$, with inverse $(\tfrac{1}{2})$, but not over $\mathbb{Z}$, because $\tfrac{1}{2}$ is not an integer.
The square size matters as well: the condition $n \ge 1$ only rules out the empty matrix, and the sizes of $A$ and $B$ must match so that both products are $n \times n$.
The [[concept page|0EB9N0S33C]] gives the examples, the rules and the tests for invertibility.

Mathlib defines `Matrix.inv` for every square matrix by $A^{-1} = (\det A)^{-1} \operatorname{adj} A$ when $\det A$ is a unit, and by $A^{-1} = 0$ otherwise.
So the Mathlib inverse is a total function, and it agrees with the inverse of this definition exactly on the invertible matrices.

## Explanations

### L1 human

A matrix is invertible when another matrix undoes it, from both sides.
If $A$ sends $x$ to $y$, then $A^{-1}$ sends $y$ back to $x$.
For the $1 \times 1$ matrix $(2)$ the inverse is $(\tfrac{1}{2})$, since $2 \cdot \tfrac{1}{2} = 1$.

### L2 human

To check that $B$ is an inverse of $A$, compute $AB$ and $BA$ and compare each with $I_n$.
Take $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$.
Then
$$AB = \begin{pmatrix} 1 & -1 + 1 \\ 0 & 1 \end{pmatrix} = I_2, \qquad BA = \begin{pmatrix} 1 & 1 - 1 \\ 0 & 1 \end{pmatrix} = I_2,$$
so $A$ is invertible with $A^{-1} = B$.
Watch out: checking only one product is enough for square matrices over a field, but not for non-square matrices.
