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

Let $R$ be a commutative ring, for example a field, and let $n \ge 1$.
Let $A$ be an $n \times n$ [[square matrix|0CP7YY6NAG]] over $R$.
An inverse of $A$ is an $n \times n$ matrix $B$ over $R$ with
$$AB = I_n \quad \text{and} \quad BA = I_n,$$
where $I_n$ is the [[identity matrix|06DW9BAWB1]] and the products are [[matrix products|076JGP6R3T]].
The matrix $A$ is *invertible* when it has an inverse.
A square matrix that is not invertible is *singular*.

## Notation

A square matrix has at most one inverse, as the concept page shows.
So we write $A^{-1}$ for the inverse of an invertible matrix $A$.
Other names for invertible are *nonsingular* and *regular*.

## Remarks

The definition asks for two equations, because matrix products do not commute in general.
For square matrices over a field, each one of the two equations implies the other one; the concept page links the theorem.
A matrix $B$ with only $AB = I$ is a right inverse of $A$, and a matrix $C$ with only $CA = I$ is a left inverse.
These one-sided notions also make sense for non-square matrices, but a non-square matrix is never called invertible.
Mathlib defines `Matrix.inv` for every square matrix by $A^{-1} = (\det A)^{-1} \operatorname{adj} A$ when $\det A$ is a unit, and by $A^{-1} = 0$ otherwise.
So the Mathlib inverse is a total function, and it agrees with the inverse of this definition exactly on the invertible matrices.

## Explanations

### L1 human

A matrix is invertible when another matrix undoes it, from both sides.
If $A$ sends $x$ to $y$, then $A^{-1}$ sends $y$ back to $x$.
For the $1 \times 1$ matrix $(2)$ the inverse is $(\tfrac{1}{2})$, since $2 \cdot \tfrac{1}{2} = 1$.

### L2 human

To check that $B$ is an inverse of $A$, we compute $AB$ and $BA$ and compare each with $I_n$.
For $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$ we get $AB = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ and $BA = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.
So $A$ is invertible with $A^{-1} = B$.
A trap: over the ring $\mathbb{Z}$, the matrix $(2)$ is not invertible, because $\tfrac{1}{2}$ is not an integer.
