---
tag: E4GKK727ZM
kind: statement
role: theorem
name: Row equivalence is an equivalence relation that keeps the row space and the null space
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
uses: [095DDGZF16, K41GT10YM6, 0G8VEZ3WTK, 0EP73HK4C4, 0PQ2GGY1QV]
about: [006BHFWMAP]
proofs: [Q7BEFA0ETV]
sources:
  - url: https://en.wikipedia.org/wiki/Row_equivalence
    locator: lead section
  - book: isbn:9780135367971
    locator: Chapter 1
  - book: isbn:9780321982384
    locator: Section 1.1
---

## Statement

Row equivalence behaves like equality for everything that elimination cares about.
Let $F$ be a [[field|04C5ZBG1WT]] and fix integers $m, n \ge 1$.
Write $A \sim B$ when the $m \times n$ matrix $A$ is [[row equivalent|006BHFWMAP]] to $B$.

1. The relation $\sim$ is an [[equivalence relation|0G8VEZ3WTK]] on the set of $m \times n$ matrices over $F$.
2. If $A \sim B$, then $B = PA$ for an invertible $m \times m$ matrix $P$.
3. If $A \sim B$, then $A$ and $B$ have the same [[row space|069MCGX635]], the span in $F^n$ of their rows.
4. If $A \sim B$, then $A$ and $B$ have the same [[null space|0PHDYNR24D]] $\set{x \in F^n : Ax = 0}$.
5. If $[A \mid b] \sim [A' \mid b']$, then the systems $Ax = b$ and $A'x = b'$ have the same solution set.

## Remarks

### A check on a small matrix

Take $A = \begin{bmatrix} 1 & 2 \\ 2 & 5 \end{bmatrix}$.
The step $R_2 \leftarrow R_2 - 2R_1$ gives $\begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$, and $R_1 \leftarrow R_1 - 2R_2$ gives $I_2$.
So $A \sim I_2$, and the inverse steps $R_1 \leftarrow R_1 + 2R_2$, then $R_2 \leftarrow R_2 + 2R_1$, lead back to $A$.
The null space of $I_2$ is $\set{0}$, so part 4 says the null space of $A$ is $\set{0}$ too.
Directly: $x + 2y = 0$ and $2x + 5y = 0$ give $y = 0$ after subtracting twice the first, and then $x = 0$.

### Why each hypothesis is needed

The relation uses only elementary operations.
If scaling by $0$ were allowed, every matrix could reach the zero matrix but not come back, and symmetry would fail.

Part 3 is about rows, and the [[column space|03AJKXH1AV]] can change.
The matrices $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ and $\begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}$ are row equivalent by a swap, but their column spaces are spanned by $e_1$ and by $e_2$.

The matrices must have the same size, because row operations never change the number of rows or columns.

### What follows

Row operations never change the rank, since the row space stays the same.
To test whether $A \sim B$, compare their reduced row echelon forms, which works by the [[uniqueness of the RREF|BF9SMZMJZE]], as [[the test example|13RPZZFD43]] shows.
The nonzero rows of an echelon form of $A$ span the row space of $A$.

### The converses

Part 4 has a true converse over a field: two $m \times n$ matrices with the same null space are row equivalent.
The reason is that the null space determines the row space, which in turn determines the RREF.
Part 3 also has a true converse: matrices of the same size with the same row space are row equivalent.
Equal column spaces do not imply row equivalence, as [[the non-example|A6P6MMDQBF]] shows.

### Watch out

Row equivalent matrices usually have different column spaces.
So a basis of the column space of $A$ must be taken from the columns of $A$, not from the columns of its RREF.
The RREF only tells you which columns of $A$ to take.

## Explanations

### L1 human

Two tables of numbers are row equivalent when row moves turn one into the other.
Every row move can be undone, so you can always walk back.
The moves never change which equations are hidden in the rows, so the solutions stay the same.

### L2 human

The typical use is to replace a matrix by its RREF when we study its null space, its row space or its rank.
All three can be read off the RREF, and the theorem says they are the same for the original matrix.
The column space is the exception, and for it we go back to the original columns.

### L3 human

Row equivalence classes are the orbits of $\mathrm{GL}_m(F)$ acting on $m \times n$ matrices by left multiplication.
Each orbit is determined by the row space, a subspace of $F^n$ of dimension at most $m$, so the orbits correspond to such subspaces.
The RREF is a canonical representative of the orbit, and its pivot positions give the Schubert cell of the row space in the Grassmannian.
Over $\mathbb{F}_q$ with $r \le m$, the number of row equivalence classes of rank $r$ is therefore the [[Gaussian binomial coefficient|YS09Z1YNEK]] $\binom{n}{r}_q$.
