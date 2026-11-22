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

The Schur complement is what is left of a matrix after one step of Gaussian elimination done with whole blocks instead of single entries.
For a [[block matrix|0ASDFEQS6P]] $M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ with an invertible block $A$, it is the matrix $D - C A^{-1} B$.
It carries the rest of the information about $M$: it gives the [[determinant via the Schur complement|0KA7A4ENVJ]], the [[block inverse formula|5QTK7JWXF3]], and tests for positive definiteness.
The formal definition is in [[Schur complement (definition)|CA1J41NWGS]].

## Motivation

Consider the system $Ax + By = f$ and $Cx + Dy = g$, with an [[invertible|0EB9N0S33C]] block $A$.
The first equation gives $x = A^{-1}(f - By)$.
Putting this into the second equation gives $(D - CA^{-1}B) y = g - CA^{-1} f$.
So the Schur complement is the matrix of the smaller system for $y$ alone.
Once you solve that system, $x$ follows from the first equation.

## Notation

The Schur complement of $A$ in $M$ is written $M/A$, which recalls a quotient; some books write $S$, $S_A$ or $(M|A)$.
When $D$ is invertible, the complement of $D$ is $M/D = A - BD^{-1}C$.

## Remarks

### A first computation

Take $M = \begin{pmatrix} 2 & 1 \\ 4 & 5 \end{pmatrix}$ with $A = (2)$.
Then
$$M/A = 5 - 4 \cdot \tfrac{1}{2} \cdot 1 = 3.$$
The elimination step $R_2 \to R_2 - 2R_1$ turns $M$ into $\begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$, and the $3$ in the corner is $M/A$.
Check: $\det M = 10 - 4 = 6 = 2 \cdot 3 = \det A \cdot (M/A)$.
For a general $2 \times 2$ matrix with $a \ne 0$, the complement of $(a)$ is $d - bc/a$, and $ad - bc = a(d - bc/a)$.
The [[Schur complement of a pivot|3WRXFFFDV1]] works the same step for a $3 \times 3$ matrix.

### The block factorization

Block elimination clears $C$ with a unit lower block triangular matrix, and the same idea on the right clears $B$:
$$M = \begin{pmatrix} I & 0 \\ CA^{-1} & I \end{pmatrix} \begin{pmatrix} A & 0 \\ 0 & M/A \end{pmatrix} \begin{pmatrix} I & A^{-1}B \\ 0 & I \end{pmatrix}.$$
This identity, proved with the [[block inverse formula|5QTK7JWXF3]], is the source of every property below.
The outer factors have determinant $1$, so $\det M = \det A \det(M/A)$.
So $M$ is invertible if and only if $M/A$ is, and then the lower right block of $M^{-1}$ is $(M/A)^{-1}$.
The outer factors are invertible, so also $\operatorname{rank} M = \operatorname{rank} A + \operatorname{rank}(M/A)$.

### Where it appears

The [[worked $3 \times 3$ block inverse|DAYPSS15ET]] inverts a matrix from one $2 \times 2$ inverse and the number $S = 4$.
The last pivot in the [[existence of the LU decomposition|3PPBWG0B96]] is the Schur complement of the leading block of size $n - 1$.
For a real symmetric $M$ with $A$ [[positive definite|0KX66CZMBB]], the matrix $M$ is positive definite if and only if $M/A$ is.
For $M = \begin{pmatrix} I_p & B \\ B^{\mathsf{T}} & I_q \end{pmatrix}$, the complement of $I_p$ is $I_q - B^{\mathsf{T}} B$, so $M$ is positive definite exactly when $B^{\mathsf{T}} B$ has all eigenvalues below $1$.
Complements can be taken in stages: if $A$ has an invertible leading block $E$, then $M/A = (M/E)/(A/E)$, the quotient formula of Crabtree and Haynsworth.

### When it is not defined

The [[exchange matrix with a zero block|D31650AJ43]] $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is invertible, but the Schur complement of its upper left entry is not defined, because that entry is $0$.
This is the block version of a zero pivot, and as with a zero pivot, a row exchange removes the problem.

### Watch out

The order of the factors is $C A^{-1} B$, and the sizes force it: $C$ is $q \times p$, $A^{-1}$ is $p \times p$ and $B$ is $p \times q$.
The product $BA^{-1}C$ has the wrong size, and $BA^{-1}$ is not even defined unless $p = q$.
Blocks do not commute, so $D - BC/A$ makes no sense.
The sign matters too: $CA^{-1}B - D$ is the negative of $M/A$, and with it the determinant formula is off by the factor $(-1)^q$.

### History

Schur used the determinant formula in a paper of 1917 on power series that are bounded in the unit disc.
Haynsworth introduced the name "Schur complement" and the notation $M/A$ in 1968.
Crabtree and Haynsworth proved the quotient formula in 1969.

### Try it

Compute the Schur complement of $A = (1)$ in $M = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 5 & 1 \\ 0 & 1 & 3 \end{pmatrix}$, and decide whether $M$ is positive definite.
Answer:
$$M/A = \begin{pmatrix} 5 & 1 \\ 1 & 3 \end{pmatrix} - \begin{pmatrix} 2 \\ 0 \end{pmatrix} (2, 0) = \begin{pmatrix} 1 & 1 \\ 1 & 3 \end{pmatrix}.$$
Check: $\det M = 1 \cdot (15 - 1) - 2 \cdot (6 - 0) = 2$ and $\det(M/A) = 3 - 1 = 2$.
The matrix $M/A$ has positive diagonal and positive determinant, so it is positive definite, and so is $M$.

## Explanations

### L1 human

Think of a system of two vector equations in two unknown vectors $x$ and $y$.
If you solve the first equation for $x$ and put the result into the second, the matrix in front of $y$ is the Schur complement.
For numbers, take $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $a \ne 0$.
The Schur complement of $a$ is the number $d - cb/a$, and the determinant $ad - bc$ equals $a \cdot (d - cb/a)$.

### L2 human

Block elimination works like ordinary elimination.
Multiply the first block row by $CA^{-1}$ and subtract it from the second block row.
This is left multiplication by $\begin{pmatrix} I & 0 \\ -CA^{-1} & I \end{pmatrix}$, and it turns $M$ into $\begin{pmatrix} A & B \\ 0 & D - CA^{-1}B \end{pmatrix}$.
The new lower right block is the Schur complement, and you can keep eliminating inside it.

### L3 human

The Schur complement is the matrix of a quadratic form after minimizing over one block of variables.
For a real symmetric $M = \begin{pmatrix} A & B \\ B^{\mathsf{T}} & D \end{pmatrix}$ with $A$ positive definite, $\min_x (x, y)^{\mathsf{T}} M (x, y) = y^{\mathsf{T}} (M/A) y$, attained at $x = -A^{-1}By$.
In probability, the conditional covariance of a Gaussian vector is a Schur complement of the covariance matrix.
