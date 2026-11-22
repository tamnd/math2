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

To invert a square matrix, write the identity matrix next to it and row reduce the wide matrix until the left half is the identity; the right half is then the inverse.
In symbols, let $A$ be an $n \times n$ matrix over a field $F$, and apply [[Gauss-Jordan elimination|098D6FQN3N]] to the $n \times 2n$ [[augmented matrix|0T6MWGZSXA]] $[A \mid I_n]$.
If the left block becomes $I_n$, the result is $[I_n \mid A^{-1}]$.
If the left block gets a row of zeros, then $A$ is not [[invertible|0EB9N0S33C]], and you can stop.
So one computation answers both questions: is $A$ invertible, and if so, what is $A^{-1}$?

## Motivation

The [[formula for a 2 × 2 inverse|8XWC7RKNN1]] has no practical analogue for larger matrices, so you need a method that scales.
Think of the unknown inverse $X$ column by column.
The equation $AX = I_n$ says that column $j$ of $X$ solves the system $Ax_j = e_j$, where $e_j$ is column $j$ of $I_n$.
That is $n$ linear systems, and all of them have the same coefficient matrix $A$.
Elimination on $A$ uses the same row operations whatever the right side is, so you can carry all $n$ right sides along at once.
Writing them side by side gives exactly the block $I_n$ in $[A \mid I_n]$.

## Notation

The bar in $[A \mid I_n]$ only marks where the block $A$ ends; the matrix is the $n \times 2n$ matrix whose first $n$ columns are those of $A$ and whose last $n$ columns are those of $I_n$.
We write $R_i \to R_i + cR_j$ for adding $c$ times row $j$ to row $i$, $R_i \to cR_i$ for scaling row $i$ by a nonzero $c$, and $R_i \leftrightarrow R_j$ for exchanging two rows.

## Remarks

### A first run

Take $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ over $\mathbb{Q}$.
Clear below the first pivot with $R_2 \to R_2 - 3R_1$, scale with $R_2 \to -\tfrac{1}{2}R_2$, and clear above the second pivot with $R_1 \to R_1 - 2R_2$:
$$\left(\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 3 & 4 & 0 & 1 \end{array}\right) \to \left(\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & -2 & -3 & 1 \end{array}\right) \to \left(\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & 1 & \tfrac{3}{2} & -\tfrac{1}{2} \end{array}\right) \to \left(\begin{array}{cc|cc} 1 & 0 & -2 & 1 \\ 0 & 1 & \tfrac{3}{2} & -\tfrac{1}{2} \end{array}\right).$$
So $A^{-1} = \begin{pmatrix} -2 & 1 \\ \tfrac{3}{2} & -\tfrac{1}{2} \end{pmatrix}$.
Check:
$$AA^{-1} = \begin{pmatrix} -2 + 3 & 1 - 1 \\ -6 + 6 & 3 - 2 \end{pmatrix} = I_2.$$
For a square matrix this one product is enough, by the theorem on [[one-sided inverses|0753Y2X5K6]].

### Why the right block becomes the inverse

Each row operation is left multiplication by an [[elementary matrix|01REXW3WWE]], and left multiplication acts on the two blocks separately.
If the operations have matrices $E_1, \dots, E_k$ and $E = E_k \cdots E_1$, then
$$E\,[A \mid I_n] = [EA \mid E].$$
So at every stage the right block records the product $E$ of the operations done so far, and the left block is $EA$.
When the left block is $I_n$, the equation $EA = I_n$ says that $E$ is a left inverse of $A$, hence $E = A^{-1}$.
The theorem on [[invertibility and row reduction|1ZK55FS2BF]] makes this precise, and it also proves that the left block reaches $I_n$ exactly when $A$ is invertible.

### The three phases

The reduction runs in three phases.
First, clear the entries below each pivot, working from left to right, and exchange rows when a pivot position holds a $0$.
Second, scale each pivot to $1$.
Third, clear the entries above each pivot, working from right to left.
A zero row in the left block can only appear in the first phase, and it ends the computation: $A$ is singular.
The [[worked $3 \times 3$ inversion|743HGXHH7Q]] goes through all three phases, and the [[singular $3 \times 3$ example|6V8NDXGNJ2]] shows the zero row appearing.

### What else the method gives

The same reduction works on $[A \mid B]$ for any $n \times p$ matrix $B$, and it ends with $[I_n \mid A^{-1}B]$.
This solves $AX = B$ without ever forming $A^{-1}$.
When $A$ is singular, the right block of a zero row is a row vector $y$ with $yA = 0$, so it shows a linear relation among the rows of $A$.
The operations also factor $A$: from $E_k \cdots E_1 A = I_n$ you get $A = E_1^{-1} \cdots E_k^{-1}$, a product of elementary matrices.

### Cost

Carried out with care, inversion needs about $n^3$ multiplications for an $n \times n$ matrix, while elimination for a single system $Ax = b$ needs about $n^3/3$.
So for one system it is cheaper to eliminate than to invert, and the [[LU decomposition|0RKG5YW66Y]] stores the elimination for reuse.
The inverse pays off when you need its entries themselves, for example in a formula or a proof.

### Watch out

Every row operation acts on the whole row of $[A \mid I_n]$, both blocks at once.
An operation done only on the left block breaks the relation $E\,[A \mid I_n] = [EA \mid E]$, and the right block is then wrong.
Column operations are not allowed at all: they are right multiplications, and they mix the two blocks.
Do not stop at an echelon form either.
An echelon form with $n$ pivots already tells you that $A$ is invertible, but the right block equals $A^{-1}$ only when the left block is exactly $I_n$, as the [[echelon form non-example|CJA2QVWQCE]] shows.

### History

The name Gauss-Jordan elimination joins Gauss, who used elimination to solve the normal equations of least squares, and the geodesist Wilhelm Jordan, whose name is attached to the variant that also clears the entries above each pivot.

### Try it

First, invert $\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$.
Only the third phase is needed: $R_2 \to R_2 - R_3$ and then $R_1 \to R_1 - R_2$ give the inverse $\begin{pmatrix} 1 & -1 & 1 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix}$.
Check the last column of the product: $1 \cdot 1 + 1 \cdot (-1) + 0 = 0$, $0 - 1 + 1 = 0$ and $0 + 0 + 1 = 1$.

Second, is $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ invertible?
No: $R_2 \to R_2 - 2R_1$ gives the row $(0, 0 \mid -2, 1)$, and indeed $-2(1, 2) + (2, 4) = (0, 0)$.

## Explanations

### L1 human

We write the identity matrix next to $A$ and do row steps on the whole wide matrix.
When the left half has become the identity, the right half has become $A^{-1}$.
The reason is that the same steps that turn $A$ into the identity also turn the identity into the "undo" matrix of $A$.
If a row of zeros shows up on the left, $A$ has no inverse.

### L2 human

The working rule is to keep the two blocks together and finish the job.
Clear below the pivots, scale them to $1$, then clear above them, and only then read the right block.
At any stage, the right block is the product $E$ of the operations done so far, and the left block is $EA$; this one fact explains both the method and its traps.
For example, after the first step of the run above, the right block $\begin{pmatrix} 1 & 0 \\ -3 & 1 \end{pmatrix}$ is the matrix of $R_2 \to R_2 - 3R_1$.

### L3 human

In numerical work one rarely forms $A^{-1}$; one stores a factorization such as $PA = LU$ and solves triangular systems for each right side.
Pivoting for accuracy and the effect of rounding belong to numerical analysis, where the [[condition number|AB3S6MHJ8X]] measures how sensitive $A^{-1}$ is to errors in $A$.
Over a commutative ring such as $\mathbb{Z}$, a nonzero pivot need not have an inverse, so the scaling phase is not always available, and the test for invertibility is that $\det A$ is a unit.
