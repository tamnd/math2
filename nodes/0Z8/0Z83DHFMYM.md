---
tag: 0Z83DHFMYM
kind: concept
name: Computing the inverse by row reduction
msc: [15A09, 65F05]
topics: [P8J6QR66TJ]
audience: ug1
uses: [0T6MWGZSXA, 098D6FQN3N, 0EB9N0S33C, 01REXW3WWE]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_elimination
    locator: Finding the inverse of a matrix
  - book: isbn:9780321982384
    locator: Section 2.2
  - url: https://hefferon.net/linearalgebra/
    locator: Chapter Three, Section IV.4, Inverses
  - url: https://understandinglinearalgebra.org/
    locator: Section 3.1, Invertibility
---

## Summary

Row reduction computes the inverse of a square matrix, or shows that no inverse exists.
Let $A$ be an $n \times n$ matrix over a field $F$, and form the $n \times 2n$ [[augmented matrix|0T6MWGZSXA]] $[A \mid I_n]$.
Apply [[Gauss-Jordan elimination|098D6FQN3N]] to it.
If the left block becomes $I_n$, then the result is $[I_n \mid A^{-1}]$, and the right block is the inverse.
If the left block gets a row of zeros, then $A$ is not [[invertible|0EB9N0S33C]].
The method rests on the theorem on [[invertibility and row reduction|1ZK55FS2BF]].

## Motivation

The [[2 × 2 formula|8XWC7RKNN1]] does not extend to larger matrices in a practical way.
The columns $x_1, \dots, x_n$ of $A^{-1}$ are the solutions of the $n$ systems $Ax_j = e_j$, because $AX = I_n$ means $Ax_j = e_j$ for each column.
These $n$ systems have the same coefficient matrix $A$, so the same row operations solve all of them.
The augmented matrix $[A \mid I_n]$ carries all $n$ right-hand sides at once.

## Notation

- The vertical bar in $[A \mid I_n]$ only separates the two blocks; the matrix is the $n \times 2n$ block matrix with blocks $A$ and $I_n$.
- We write $R_i \to R_i + cR_j$ for "add $c$ times row $j$ to row $i$", $R_i \to cR_i$ for a scaling, and $R_i \leftrightarrow R_j$ for an exchange.

## Remarks

### Examples

- For $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, four row operations give $A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$; the steps are in the L2 explanation of [[invertibility and row reduction|1ZK55FS2BF]].
- The [[worked $3 \times 3$ inversion|743HGXHH7Q]] inverts $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}$ with five row operations.
- The [[singular $3 \times 3$ example|6V8NDXGNJ2]] shows how a zero row appears in the left block.

### Non-examples

- Stopping at an echelon form does not give the inverse: the right block is then not $A^{-1}$, as the [[echelon form non-example|CJA2QVWQCE]] shows.
- Column operations on $[A \mid I_n]$ are not allowed, because they mix the blocks; they would correspond to multiplication on the right.

### Basic properties

- The method is correct because each row operation is left multiplication by an [[elementary matrix|01REXW3WWE]]. If $E = E_k \cdots E_1$ and $EA = I_n$, then $E = A^{-1}$, and $E[A \mid I_n] = [I_n \mid E]$.
- The same reduction decides invertibility: $A$ is invertible exactly when the left block reaches $I_n$.
- The method also works on $[A \mid B]$ for an $n \times p$ matrix $B$, and it then ends with $[I_n \mid A^{-1}B]$.
- For a general $n \times n$ matrix, the method needs about $n^3$ multiplications, while elimination for one system $Ax = b$ needs about $n^3/3$. So for one system, it is cheaper to solve than to invert, as the [[LU decomposition|0RKG5YW66Y]] shows.

### History

Jordan, a German geodesist, described the full reduction that also clears the entries above the pivots, in 1888.
The name Gauss-Jordan elimination comes from this work.

### Common errors

- Students do a row operation only on the left block. Each operation must act on the whole row of $[A \mid I_n]$.
- Students forget to check the result. One product $AX$ is enough, by the theorem on [[one-sided inverses|0753Y2X5K6]].
- Students divide by a zero pivot. If a pivot position has a $0$, exchange with a lower row that has a nonzero entry in that column.

## Explanations

### L1 human

We write the identity matrix next to $A$ and row reduce the whole wide matrix.
When the left half becomes the identity, the right half has become $A^{-1}$.
The same row operations that turn $A$ into $I$ turn $I$ into $A^{-1}$.

### L2 human

The method has three phases.
First, clear the entries below each pivot, from left to right.
Second, scale each pivot to $1$.
Third, clear the entries above each pivot, from right to left.
If the left block gets a zero row in the first phase, stop: the matrix is singular.
A trap: the second and third phases are not optional, since the right block equals $A^{-1}$ only at the end.

### L3 human

In numerical work one rarely computes $A^{-1}$; one stores a factorization such as $PA = LU$ and solves triangular systems.
The choice of pivots for accuracy, and the effect of rounding, belong to numerical analysis, where the [[condition number|AB3S6MHJ8X]] measures the sensitivity.
