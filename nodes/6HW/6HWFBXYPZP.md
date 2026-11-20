---
tag: 6HWFBXYPZP
kind: concept
name: Schur complement
msc: [15A09, 15A15]
topics: [P8J6QR66TJ]
audience: ug2
uses: [CA1J41NWGS, 0ASDFEQS6P, 0EB9N0S33C, 0KA7A4ENVJ]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_complement
  - book: isbn:9780521548236
    locator: Section 0.7
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Blockwise inversion
same_as:
  wikidata: Q1778169
  wikipedia: Schur complement
---

## Summary

The Schur complement of an invertible block $A$ in a [[block matrix|0ASDFEQS6P]] $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$ is the matrix $D - C A^{-1} B$.
It is what remains of the block $D$ after block Gaussian elimination removes the block $C$.
It gives the [[determinant via the Schur complement|0KA7A4ENVJ]], the [[block inverse formula|~801e2989]], and tests for positive definiteness.
The formal definition is in [[Schur complement (definition)|CA1J41NWGS]].

## Motivation

Consider the system $Ax + By = f$ and $Cx + Dy = g$, with an [[invertible|0EB9N0S33C]] block $A$.
The first equation gives $x = A^{-1}(f - By)$.
Put this into the second equation: $(D - CA^{-1}B) y = g - CA^{-1} f$.
So the Schur complement is the matrix of the smaller system for $y$ alone.
This is elimination with whole blocks in place of single entries.

## Notation

- The Schur complement of $A$ in $M$ is written $M/A$, which recalls a quotient. Some books write $S$, $S_A$ or $(M|A)$.
- The complement of $D$ is $M/D = A - BD^{-1}C$, when $D$ is invertible.

## Remarks

### Examples

- For a $2 \times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $a \ne 0$, the Schur complement of $(a)$ is $d - bc/a$, and $ad - bc = a(d - bc/a)$.
- The [[worked $3 \times 3$ block inverse|~25fc1b6c]] has the Schur complement $S = 4$ of a $2 \times 2$ block, and it computes $M^{-1}$ from $A^{-1}$ and $S$.
- The [[Schur complement of a pivot|~48c6f2d1]] is the block that is left after one step of elimination.
- For $M = \begin{pmatrix} I_p & B \\ B^{\mathsf{T}} & I_q \end{pmatrix}$, the complement of $I_p$ is $I_q - B^{\mathsf{T}} B$.

### Non-examples

- The [[exchange matrix with a zero block|~74c14e5a]] is invertible, but the Schur complement of its upper left entry is not defined.
- The matrix $C A^{-1} B - D$ has the wrong sign. It is the negative of the Schur complement, and with it the determinant formula fails by a factor $(-1)^q$.

### Basic properties

- Block factorization: $M = \begin{pmatrix} I & 0 \\ CA^{-1} & I \end{pmatrix} \begin{pmatrix} A & 0 \\ 0 & M/A \end{pmatrix} \begin{pmatrix} I & A^{-1}B \\ 0 & I \end{pmatrix}$, by the theorem on the [[block inverse formula|~801e2989]].
- [[Determinant formula|0KA7A4ENVJ]]: $\det M = \det A \det(M/A)$.
- If $A$ is invertible, then $M$ is invertible if and only if $M/A$ is invertible, and the lower right block of $M^{-1}$ is $(M/A)^{-1}$.
- Rank additivity: $\operatorname{rank} M = \operatorname{rank} A + \operatorname{rank}(M/A)$.
- Quotient formula of Crabtree and Haynsworth: if $A$ itself has an invertible leading block $E$, then $M/A = (M/E)/(A/E)$.
- For a real symmetric $M$ with $A$ positive definite, $M$ is [[positive definite|0KX66CZMBB]] if and only if $M/A$ is positive definite.
- The last pivot in the proof of the [[existence of the LU decomposition|~8a5f1cba]] is a Schur complement.

### History

Schur used the determinant formula in a paper of 1917 on power series bounded in the unit disc.
Haynsworth introduced the name "Schur complement" and the notation $M/A$ in 1968.
Crabtree and Haynsworth proved the quotient formula in 1969.

### Common errors

- Students write $D - BA^{-1}C$. The sizes show the right order: $C$ is $q \times p$, $A^{-1}$ is $p \times p$ and $B$ is $p \times q$, so $BA^{-1}$ is not even defined unless $p = q$.
- Students treat the blocks as numbers and write $(M/A) = D - BC/A$. Block products do not commute, and $A^{-1}$ cannot be moved.

## Explanations

### L1 human

Think of a system of two vector equations in two unknown vectors $x$ and $y$.
If you solve the first equation for $x$ and put the result into the second, the matrix in front of $y$ is the Schur complement.
For numbers, take $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $a \ne 0$.
The Schur complement of $a$ is the number $d - cb/a$.
Then the determinant $ad - bc$ equals $a \cdot (d - cb/a)$.

### L2 human

Block elimination works like ordinary elimination.
Multiply the first block row by $CA^{-1}$ and subtract it from the second block row.
This is left multiplication by $\begin{pmatrix} I & 0 \\ -CA^{-1} & I \end{pmatrix}$, and it turns $M$ into $\begin{pmatrix} A & B \\ 0 & D - CA^{-1}B \end{pmatrix}$.
The new lower right block is the Schur complement.
For $M = \begin{pmatrix} 2 & 1 \\ 4 & 5 \end{pmatrix}$ the step $R_2 \to R_2 - 2R_1$ gives $\begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$, and $5 - 4 \cdot \tfrac{1}{2} \cdot 1 = 3$.

### L3 human

The Schur complement is the matrix of a quadratic form restricted after minimizing over one block of variables.
For symmetric $M$ with $A$ positive definite, $\min_x (x, y)^{\mathsf{T}} M (x, y) = y^{\mathsf{T}} (M/A) y$.
In probability, the conditional covariance of a Gaussian vector is a Schur complement of the covariance matrix.
In Mathlib, the lemma `Matrix.schur_complement_eq₁₁` expresses this quadratic form identity.
