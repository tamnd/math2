---
tag: FCM29NQ6DN
kind: statement
role: theorem
name: Every matrix is row equivalent to a matrix in row echelon form and to one in reduced row echelon form
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
uses: [0F27PBRWD7, 0NNR68BFRY, 095DDGZF16, 0DE5R5EB4D]
about: [0VYCDGMJJJ, 0WF5AQYTW6]
proofs: [48XDCB74Q4]
sources:
  - url: https://en.wikipedia.org/wiki/Row_echelon_form
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 1.2
  - book: isbn:9780135367971
    locator: Chapter 1
---

## Statement

Row reduction always succeeds: every matrix over a field can be brought to echelon form, and further to reduced echelon form.
Let $F$ be a [[field|04C5ZBG1WT]] and let $A$ be an $m \times n$ matrix over $F$.

1. $A$ is [[row equivalent|006BHFWMAP]] to a matrix in [[row echelon form|0VYCDGMJJJ]].
2. $A$ is row equivalent to a matrix in [[reduced row echelon form|0WF5AQYTW6]].

The proof is an algorithm: [[Gaussian elimination|0JVJ2WCXZH]] gives part 1, and [[Gauss-Jordan elimination|098D6FQN3N]] gives part 2.

## Remarks

### The algorithm on one matrix

Take $A = \begin{bmatrix} 0 & 2 & 4 \\ 1 & 1 & 1 \\ 2 & 4 & 6 \end{bmatrix}$.
The top-left entry is $0$, so first swap $R_1 \leftrightarrow R_2$, which gives the rows $(1, 1, 1)$, $(0, 2, 4)$, $(2, 4, 6)$.
Then $R_3 \leftarrow R_3 - 2R_1$ makes row 3 equal to $(0, 2, 4)$, and $R_3 \leftarrow R_3 - R_2$ makes it $(0, 0, 0)$.
The matrix is now in row echelon form.
For the reduced form, $R_2 \leftarrow \tfrac12 R_2$ gives $(0, 1, 2)$, and $R_1 \leftarrow R_1 - R_2$ gives $(1, 0, -1)$.
So the RREF is
$$\begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{bmatrix}.$$

### Why the scalars must form a field

The algorithm divides by nonzero entries.
Over $\mathbb{Z}$, the $1 \times 2$ matrix $\begin{bmatrix} 2 & 1 \end{bmatrix}$ cannot be given a leading entry $1$ by an invertible row operation, since the only invertible scalars are $\pm 1$.
So part 2 fails over $\mathbb{Z}$ if row operations must stay inside the integers.

### What follows

Every [[system of linear equations|0GT4WWGWH2]] is equivalent to a system in RREF, from which the solutions can be read, by the [[lemma on systems in RREF|P3HMRQN5KT]].
Together with the [[uniqueness theorem|BF9SMZMJZE]], every matrix has exactly one RREF, so the RREF is a canonical form for row equivalence.
Every square matrix is row equivalent to an upper triangular matrix, since a square matrix in echelon form is upper triangular.

### Existence is the easy half

A matrix already in echelon form is row equivalent to itself, by the empty sequence, so there is no interesting converse.
The real question is uniqueness.
It fails for row echelon forms, as [[two echelon forms|19FNDHJ181]] shows, and it holds for the reduced form.

### Watch out

The swap in the example is needed only because the top-left entry is $0$, which cannot serve as a pivot.
Some other row operation that puts a nonzero entry there, such as $R_1 \leftarrow R_1 + R_2$, would also work.
What never works is dividing by the $0$.

## History

Elimination to a triangular array is described in the "Fangcheng" chapter of the *Nine Chapters on the Mathematical Art*.
Gauss described elimination for the normal equations of least squares in 1810.
The reduction to the reduced form was described in geodesy by Wilhelm Jordan in 1888.

## Explanations

### L1 human

However messy a table of numbers is, row moves can turn it into a staircase shape.
First clear everything below the first useful number of the first column, then do the same for the rows below.
Then scale each staircase step to $1$ and clear above it too.
This always works, and it always stops after a finite number of moves.

### L2 human

The typical use is the first step of every computation with a matrix: rank, null space, inverse, solutions.
Each of these is read off the RREF, and the theorem guarantees that the RREF exists.
In practice you follow the steps of the example: find a pivot, clear below it, move one row down, and repeat.

### L3 human

Part 1 is the existence half of the statement that the orbits of $\mathrm{GL}_m(F)$ on $m \times n$ matrices have canonical representatives.
Combined with uniqueness, it shows that the orbits are classified by the RREF, and thus by the row space.
Over a Euclidean domain, the same induction with division with remainder in place of division gives the Hermite normal form.
In matrix terms, part 1 gives $PA = U$ with $P$ invertible and $U$ in echelon form.
Organizing the row swaps first gives the factorization $PA = LU$ with a permutation matrix $P$, as the page on [[LU decomposition|0RKG5YW66Y]] explains.
