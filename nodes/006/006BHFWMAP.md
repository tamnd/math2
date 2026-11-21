---
tag: 006BHFWMAP
kind: concept
name: Row equivalence
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
uses: [04XWH28452, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Row_equivalence
    locator: lead section
  - book: isbn:9780135367971
    locator: Chapter 1
  - book: isbn:9780321982384
    locator: Section 1.1
same_as:
  wikidata: Q3444264
  wikipedia: Row equivalence
---

## Summary

Two matrices are row equivalent when row operations turn one into the other.
For $m \times n$ [[matrices|0VD9ZSWWJG]] $A$ and $B$ over a field, $A$ is row equivalent to $B$ when a finite sequence of [[elementary row operations|04XWH28452]] changes $A$ into $B$.
Row equivalence is an equivalence relation, and row equivalent matrices have the same row space and the same null space, by the [[theorem on row equivalence|E4GKK727ZM]].
This is what makes elimination work: a system may be replaced by a simpler row equivalent one with the same solutions.
The [[formal definition|095DDGZF16]] is short.

## Motivation

Elimination changes a system step by step until the solutions can be read off.
We need a word for "reachable by such steps", and we need to know what stays the same along the way.
Row equivalence is that word.

The answer to the second question is a list of invariants.
The solution set, the row space, the null space and the rank all survive every step.
So any question about these can be asked of the simplest matrix in the class, the reduced row echelon form, instead of the original one.

## Notation

Common notations are $A \sim B$, $A \sim_R B$ and $A \xrightarrow{\text{row}} B$.
Lay's textbook writes $\sim$ between the stages of a row reduction.

## Remarks

### A system and its solved form

The augmented matrix $\left[\begin{array}{cc|c} 1 & 1 & 3 \\ 1 & -1 & 1 \end{array}\right]$ of $x + y = 3$, $x - y = 1$ is row equivalent to $\left[\begin{array}{cc|c} 1 & 0 & 2 \\ 0 & 1 & 1 \end{array}\right]$.
The second matrix is the system $x = 2$, $y = 1$, so both systems have the single solution $(2, 1)$.
[[The reversing example|HASTW7ARPD]] goes from the first matrix to the second and back again.

### Testing with the RREF

Every matrix is row equivalent to exactly one matrix in [[reduced row echelon form|0WF5AQYTW6]], by the [[existence theorem|FCM29NQ6DN]] and the [[uniqueness theorem|BF9SMZMJZE]].
So $A \sim B$ exactly when $A$ and $B$ have the same RREF.
For instance, $\begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 7 \end{bmatrix}$ and $\begin{bmatrix} 1 & 2 & 0 \\ 1 & 2 & 1 \end{bmatrix}$ both reduce to $\begin{bmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix}$, as [[the test example|13RPZZFD43]] shows.
In particular, every invertible $n \times n$ matrix is row equivalent to $I_n$.

### Row equivalence as a matrix product

A sequence of row operations is left multiplication by a product of [[elementary matrices|01REXW3WWE]].
So $A \sim B$ implies $B = PA$ for an invertible matrix $P$.
Over a field the converse holds too, since every invertible matrix is a product of elementary matrices.

### What it does not keep

Row operations can change the column space.
The matrices $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ and $\begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ have the same column space but are not row equivalent, as [[the non-example|A6P6MMDQBF]] shows.
The matrices $\begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 7 \end{bmatrix}$ and $\begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$ are not row equivalent either, since their ranks are $2$ and $1$.
Matrices of different sizes are never row equivalent.

### Watch out

Row equivalent matrices need not be equal up to scaling of rows, since row additions change rows in other ways.
And two different echelon forms do not prove that matrices are not row equivalent, because echelon forms are not unique.
Only the reduced forms can be compared.

### Try it

Are $\begin{bmatrix} 1 & 3 \\ 2 & 7 \end{bmatrix}$ and $I_2$ row equivalent?
Yes: $R_2 \leftarrow R_2 - 2R_1$ gives the rows $(1, 3)$ and $(0, 1)$, and $R_1 \leftarrow R_1 - 3R_2$ gives $I_2$.

## Explanations

### L1 human

Two tables are row equivalent when row moves turn one into the other.
Since every move can be undone, it does not matter which table we start from.
If the tables come from two systems of equations, the two systems have the same solutions.
For example, the system $x + y = 3$, $x - y = 1$ is row equivalent to the system $x = 2$, $y = 1$.

### L2 human

We test whether $A = \begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix}$ and $B = \begin{bmatrix} 2 & 4 \\ 1 & 2 \end{bmatrix}$ are row equivalent.

1. For $A$, the step $R_2 \leftarrow R_2 - 3R_1$ gives $\begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$.
2. For $B$, the swap $R_1 \leftrightarrow R_2$ gives $\begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$, and then $R_2 \leftarrow R_2 - 2R_1$ gives $\begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$.
3. The RREFs agree, so $A \sim B$.
4. For a sequence from $A$ to $B$, reduce $A$, then undo the steps for $B$ in reverse order: $R_2 \leftarrow R_2 + 2R_1$, then $R_1 \leftrightarrow R_2$.
5. Check: from $\begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$ the first step gives $\begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$, and the swap gives $B$.

### L3 human

Row equivalence classes of $m \times n$ matrices correspond to subspaces of $F^n$ of dimension at most $m$, through the row space.
So the set of classes of rank $r$ is the Grassmannian of $r$-dimensional subspaces of $F^n$.
Column equivalence is the dual notion, with the column space in place of the row space.
Over the integers, the classes under invertible row operations have the Hermite normal form as canonical representatives.
