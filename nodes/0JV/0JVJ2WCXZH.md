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

Gaussian elimination removes one unknown at a time until the system is a staircase that we can solve from the bottom up.
In matrix terms, it changes an $m \times n$ matrix over a field into a [[row echelon form|0VYCDGMJJJ]] by [[elementary row operations|04XWH28452]].
It works column by column, from left to right, and from the top row down:

1. Find the first column, from the left, that has a nonzero entry in the current row or below it.
2. If the entry in the current row is $0$, swap the current row with a lower row whose entry in this column is nonzero; the entry now in the current row is the [[pivot|0J0BBCMJ5W]].
3. For each lower row $i$, subtract $\ell_i$ times the pivot row, where $\ell_i$ is the entry of row $i$ divided by the pivot, so that the entry of row $i$ becomes $0$.
4. Move to the next row and repeat, until no rows or no nonzero entries are left.

Applied to the [[augmented matrix|0T6MWGZSXA]] of a [[system of linear equations|0GT4WWGWH2]], it gives an equivalent system in echelon form, which [[back substitution|0ATFVE08MW]] solves.
For an $n \times n$ matrix it needs about $\tfrac23 n^3$ arithmetic operations.
It solves every linear system in finitely many steps, and the same steps compute rank, null spaces, inverses and determinants.

## Motivation

To solve $x + y = 3$ and $x - y = 1$, we subtract the first equation from the second and get $-2y = -2$, an equation without $x$.
Then $y = 1$, and the first equation gives $x = 2$.
Gaussian elimination repeats this idea in a fixed order, so that it works for any number of equations and unknowns.
The fixed order matters for a computer and also for a person, because it guarantees that the process stops with a correct result.
The correctness rests on the fact that row operations do not change the solution set, by [[the theorem on row operations|K41GT10YM6]].

## Notation

The numbers $\ell_i = a_{ij}/p$, where $p$ is the pivot, are the multipliers.
"Row reduction" is a common synonym, and some books use it for the reduction to the reduced form, which is [[Gauss-Jordan elimination|098D6FQN3N]].
The phase that produces the echelon form is the forward phase, and the solving phase is the backward phase.

## Remarks

### A worked system

We solve $2x + y - z = 8$, $-3x - y + 2z = -11$, $-2x + y + 2z = -3$.

1. The pivot is $2$ in column 1. $R_2 \leftarrow R_2 + \tfrac32 R_1$ gives $(0, \tfrac12, \tfrac12 \mid 1)$.
2. $R_3 \leftarrow R_3 + R_1$ gives $(0, 2, 1 \mid 5)$.
3. The pivot is $\tfrac12$ in column 2. $R_3 \leftarrow R_3 - 4R_2$ gives $(0, 0, -1 \mid 1)$.
4. Back substitution gives $z = -1$, then $\tfrac12 y - \tfrac12 = 1$ gives $y = 3$, then $2x + 3 + 1 = 8$ gives $x = 2$.
5. Check: $4 + 3 + 1 = 8$, $-6 - 3 - 2 = -11$ and $-4 + 3 - 2 = -3$.

### More examples

The system of [[the three planes example|YM0PB9F9HG]] is solved by three eliminations, one swap and back substitution.
[[The elimination example with a row exchange|8MW9Y8QF95]] needs a swap because a zero appears in a pivot place.
The system of [[the inconsistent triangle|XJX2NN45ED]] produces the row $(0, 0 \mid 1)$, which shows that it has no solution.
Over $\mathbb{F}_2$, the same algorithm solves the Lights Out puzzle, as in [[the Lights Out example|JD8FEPHM6T]].

### Other ways to solve, which are not elimination

Cramer's rule solves a square system with invertible coefficient matrix by determinants, see [[Cramer's rule|0977KZ6PQB]].
Iterative methods such as the Jacobi method approach the solution step by step and do not change the matrix to echelon form; they belong to numerical analysis.
[[Fourier-Motzkin elimination|MJQARBFG10]] removes variables from systems of linear inequalities, which is a different problem.

### What the algorithm guarantees

The algorithm stops after at most $\min(m, n)$ pivot steps, and the result is in row echelon form, by [[the existence theorem|FCM29NQ6DN]].
The output is row equivalent to the input, so a system and its eliminated form have the same solutions.
If no row swaps are needed, the multipliers form the lower triangular factor of an [[LU decomposition|0RKG5YW66Y]] $A = LU$, and with swaps, $PA = LU$ for a permutation matrix $P$.
If a square matrix has $n$ pivots, its [[determinant|00KDZRW4C0]] is $(-1)^s$ times the product of the pivots, where $s$ is the number of swaps.
If it has fewer than $n$ pivots, its determinant is $0$ and it is not invertible.

### Counting the work

Count one addition, subtraction, multiplication or division in $F$ as one operation, and take an $n \times n$ matrix.
At the step with $j$ rows left below the pivot, there are $j$ divisions for the multipliers and $2j^2$ operations for the updates.
The total is $\sum_{j=1}^{n-1} (j + 2j^2) = \tfrac{n(n-1)}{2} + \tfrac{n(n-1)(2n-1)}{3}$, with leading term $\tfrac23 n^3$.
For $n = 3$ it is $3 + 10 = 13$.
Updating one right side costs $n(n - 1)$ more operations, and back substitution costs $n^2$, both small compared with $\tfrac23 n^3$.

### History

Chapter 8, "Fangcheng" (rectangular arrays), of the Chinese *Nine Chapters on the Mathematical Art* solves systems by elimination on a counting board, and Liu Hui commented on it in the 3rd century.
Newton wrote down the method in lecture notes, which were published in 1707 as *Arithmetica Universalis*.
In 1810 Gauss made a notation for symmetric elimination, and hand computers used it for the normal equations of least squares.
The school method was named after Gauss only in the 1950s, because of confusion about its history.

### Watch out

Always check the solution in the original equations, since one arithmetic slip spoils every later step.
Never divide by a zero pivot; swap rows instead.
After a row has changed, use only its new version.

### Try it

Solve $x + 2y = 5$, $3x + 4y = 11$ by elimination.
The step $R_2 \leftarrow R_2 - 3R_1$ gives $-2y = -4$, so $y = 2$ and $x = 5 - 4 = 1$, and $3 + 8 = 11$ checks.

## Explanations

### L1 human

Gaussian elimination is the method of solving equations by removing one unknown at a time.
We use the first equation to remove $x_1$ from all the other equations, then the second equation to remove $x_2$, and so on.
For example, from $x + y = 3$ and $x - y = 1$, subtracting gives $-2y = -2$, so $y = 1$ and then $x = 2$.
At the end, the last equation has the fewest unknowns, and we solve upwards.

### L2 human

The typical use is to solve a square system with one right side, or to find the rank of a matrix.
Watch out: in exact arithmetic any nonzero pivot works, but in floating point a tiny pivot can ruin the result.
Numerical analysis then chooses the pivot by size, which is partial pivoting.

### L3 human

In matrix terms, the forward phase computes $PA = LU$, with $P$ a permutation, $L$ unit lower triangular and $U$ in echelon form; see [[LU decomposition|0RKG5YW66Y]].
The count $\tfrac23 n^3$ is for this algorithm, and asymptotically faster methods exist, based on fast matrix multiplication; see [[big O notation|0TGV80E6A4]] for the notation of such bounds.
Over $\mathbb{Q}$ the entries can grow, and fraction-free variants such as the Bareiss algorithm keep them integral.
For stability over $\mathbb{R}$, the analysis of pivoting strategies belongs to numerical linear algebra, see [[numerical stability|1AKB4XHMTH]].
