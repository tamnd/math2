---
tag: 0JVJ2WCXZH
kind: concept
name: Gaussian elimination
aliases: [row-reduction]
msc: ["15A06", "65F05"]
topics: [DXSXFVDMXQ]
audience: school
uses: [04XWH28452, 0VYCDGMJJJ, 0J0BBCMJ5W]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_elimination
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Gaussian_elimination
    locator: History
  - book: isbn:9781733146678
    locator: Chapter 2
  - book: isbn:9780321982384
    locator: Section 1.2
same_as:
  wikidata: Q2658
  wikipedia: Gaussian elimination
---

## Summary

Gaussian elimination is the algorithm that changes an $m \times n$ matrix over a field into a [[row echelon form|0VYCDGMJJJ]] by [[elementary row operations|04XWH28452]].
It works column by column, from left to right, and from the top row down:

1. Find the first column, from the left, that has a nonzero entry in the current row or below it.
2. If the entry in the current row is $0$, swap the current row with a lower row whose entry in this column is nonzero; this entry is the [[pivot|0J0BBCMJ5W]].
3. For each lower row $i$, subtract $\ell_i$ times the pivot row, where $\ell_i$ is the entry of row $i$ divided by the pivot, so that the entry of row $i$ becomes $0$.
4. Move to the next row and repeat, until no rows or no nonzero entries are left.

Applied to the [[augmented matrix|0T6MWGZSXA]] of a [[system of linear equations|0GT4WWGWH2]], it gives an equivalent system in echelon form, which [[back substitution|0ATFVE08MW]] solves.
For an $n \times n$ matrix it needs about $\tfrac23 n^3$ arithmetic operations.
Gaussian elimination matters because it solves every linear system in finitely many steps, and it computes rank, null spaces, inverses and determinants.

## Motivation

To solve two equations in two unknowns, we subtract a multiple of one equation from the other to remove one unknown.
Gaussian elimination repeats this idea in an organized way, so that it works for any number of equations and unknowns.
The organization matters for a computer, and also for a person, because it guarantees termination and a correct result.
The correctness rests on the fact that row operations do not change the solution set, see [[the theorem on row operations|K41GT10YM6]].

## Notation

1. The numbers $\ell_i = a_{ij}/p$ are the multipliers, where $p$ is the pivot.
2. "Row reduction" is a common synonym; some books use it for reduction to the reduced form, which is [[Gauss-Jordan elimination|098D6FQN3N]].
3. The phase that produces the echelon form is the forward phase; the solving phase is the backward phase.

## Remarks

### Examples

1. The $3 \times 3$ system of [[the three planes example|YM0PB9F9HG]] is solved by three eliminations, one swap and back substitution.
2. [[The elimination example with a row exchange|8MW9Y8QF95]] needs a swap because a zero appears in a pivot place.
3. The system of [[the inconsistent triangle|XJX2NN45ED]] produces the row $(0, 0 \mid 1)$, which shows that it has no solution.
4. Over $\mathbb{F}_2$, the same algorithm solves the Lights Out puzzle, see [[the Lights Out example|JD8FEPHM6T]].

### Non-examples

1. Cramer's rule solves a square system with invertible coefficient matrix by determinants, not by elimination, see [[Cramer's rule|0977KZ6PQB]].
2. Iterative methods such as the Jacobi method approach the solution step by step and do not change the matrix to echelon form; they belong to numerical analysis.
3. Fourier-Motzkin elimination removes variables from systems of linear inequalities, which is a different problem, see [[Fourier-Motzkin elimination|MJQARBFG10]].

### Basic properties

1. The algorithm stops after at most $\min(m, n)$ pivot steps, and the result is in row echelon form, see [[the existence theorem|FCM29NQ6DN]].
2. The output is row equivalent to the input, so a system and its eliminated form have the same solutions.
3. Operation count for an $n \times n$ matrix, where one operation is one addition, subtraction, multiplication or division in $F$: step $j$ (with $j$ rows left below the pivot) costs $j$ divisions for the multipliers and $2j^2$ operations for the updates.
4. The total is $\sum_{j=1}^{n-1} (j + 2j^2) = \tfrac{n(n-1)}{2} + \tfrac{n(n-1)(2n-1)}{3}$, with leading term $\tfrac23 n^3$; for $n = 3$ it is $13$.
5. Updating one right-hand side costs $n(n - 1)$ more operations, and back substitution costs $n^2$; both are small compared with $\tfrac23 n^3$.
6. If no row swaps are needed, the multipliers form the lower triangular factor of an [[LU decomposition|0RKG5YW66Y]] $A = LU$; with swaps, $PA = LU$ for a permutation matrix $P$.
7. If a square matrix has $n$ pivots, its [[determinant|00KDZRW4C0]] is $(-1)^s$ times the product of the pivots, where $s$ is the number of swaps.
8. If it has fewer than $n$ pivots, its determinant is $0$ and it is not invertible.

### History

Chapter 8, "Fangcheng" (rectangular arrays), of the Chinese *Nine Chapters on the Mathematical Art* solves systems by elimination on a counting board, and Liu Hui commented on it in the 3rd century.
Newton wrote down the method in lecture notes, which were published in 1707 as *Arithmetica Universalis*.
In 1810 Gauss made a notation for symmetric elimination, and hand computers used it for the normal equations of least squares.
The school method was named after Gauss only in the 1950s, because of confusion about its history.

### Common errors

1. Arithmetic slips; always check the solution in the original equations.
2. Dividing by a zero pivot instead of swapping rows.
3. Using the old version of a row after it has been changed.

## Explanations

### L1 human

Gaussian elimination is the method of solving equations by removing one unknown at a time.
We use the first equation to remove $x_1$ from all the other equations, then the second equation to remove $x_2$, and so on.
For example, from $x + y = 3$ and $x - y = 1$, subtracting gives $-2y = -2$, so $y = 1$ and then $x = 2$.
At the end, the last equation has the fewest unknowns, and we solve upwards.

### L2 human

We solve $2x + y - z = 8$, $-3x - y + 2z = -11$, $-2x + y + 2z = -3$.

1. Pivot $2$ in column 1. $R_2 \leftarrow R_2 + \tfrac32 R_1$ gives $(0, \tfrac12, \tfrac12 \mid 1)$.
2. $R_3 \leftarrow R_3 + R_1$ gives $(0, 2, 1 \mid 5)$.
3. Pivot $\tfrac12$ in column 2. $R_3 \leftarrow R_3 - 4R_2$ gives $(0, 0, -1 \mid 1)$.
4. Back substitution: $z = -1$, then $\tfrac12 y - \tfrac12 = 1$ gives $y = 3$, then $2x + 3 + 1 = 8$ gives $x = 2$.
5. Check: $4 + 3 + 1 = 8$, $-6 - 3 - 2 = -11$ and $-4 + 3 - 2 = -3$.

The typical use is to solve a square system with one right-hand side, or to find the rank of a matrix.
A trap: in exact arithmetic any nonzero pivot works, but in floating point a tiny pivot can ruin the result; numerical analysis then chooses the pivot by size, which is partial pivoting.

### L3 human

In matrix terms, the forward phase computes $PA = LU$, with $P$ a permutation, $L$ unit lower triangular and $U$ in echelon form; see [[LU decomposition|0RKG5YW66Y]].
The count $\tfrac23 n^3$ is the leading term only; asymptotically faster methods exist, based on fast matrix multiplication, see [[big O notation|0TGV80E6A4]] for the notation of such bounds.
Over $\mathbb{Q}$ the entries can grow; fraction-free variants such as the Bareiss algorithm keep them integral.
For stability over $\R$, the analysis of pivoting strategies belongs to numerical linear algebra, see [[numerical stability|1AKB4XHMTH]].
