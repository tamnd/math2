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

Let $F$ be a field and let $A$ and $B$ be $m \times n$ matrices over $F$.
The matrix $A$ is row equivalent to $B$ when a finite sequence of [[elementary row operations|04XWH28452]] changes $A$ into $B$.
The exact definition is in [[the definition node|095DDGZF16]].
Row equivalence is an equivalence relation, and row equivalent matrices have the same row space and the same null space, see [[the theorem|~e3949f1c]].
It matters because two systems with row equivalent augmented matrices have the same solutions, so row reduction may replace a system by a simpler one.

## Motivation

Elimination changes a system step by step until we can read off the solutions.
We need a name for "reachable by such steps", and we need to know what stays the same along the way.
Row equivalence is that name, and the theorem on it lists what stays the same: the solution set, the row space, the null space and the rank.

## Notation

Common notations are $A \sim B$, $A \sim_R B$ and $A \xrightarrow{\text{row}} B$.
Lay writes $A \sim B$ in examples of row reduction.

## Remarks

### Examples

1. $\begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 7 \end{bmatrix}$ and $\begin{bmatrix} 1 & 2 & 0 \\ 1 & 2 & 1 \end{bmatrix}$ are row equivalent, since both reduce to the same RREF, see [[the test example|~1cd380f5]].
2. Every invertible $n \times n$ matrix is row equivalent to $I_n$.
3. The augmented matrix $\left[\begin{array}{cc|c} 1 & 1 & 3 \\ 1 & -1 & 1 \end{array}\right]$ is row equivalent to $\left[\begin{array}{cc|c} 1 & 0 & 2 \\ 0 & 1 & 1 \end{array}\right]$, and the reverse sequence is in [[the reversing example|~e06fbfe4]].
4. Any matrix is row equivalent to the same matrix with two rows swapped.

### Non-examples

1. $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ and $\begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ have the same column space, but they are not row equivalent, see [[the non-example|~698f64c0]].
2. $\begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 7 \end{bmatrix}$ and $\begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$ are not row equivalent, since their ranks are $2$ and $1$.
3. Matrices of different sizes are never row equivalent.

### Basic properties

1. Row equivalence is reflexive, symmetric and transitive, see [[the theorem|~e3949f1c]].
2. $A \sim B$ implies $B = PA$ for an invertible matrix $P$; over a field the converse also holds, since every invertible matrix is a product of [[elementary matrices|01REXW3WWE]].
3. Row equivalent matrices have the same row space and the same null space, see [[the theorem|~e3949f1c]].
4. Every matrix is row equivalent to exactly one matrix in [[reduced row echelon form|0WF5AQYTW6]], see [[the existence theorem|~d9e684c6]] and [[the uniqueness theorem|BF9SMZMJZE]].
5. So $A \sim B$ if and only if $A$ and $B$ have the same RREF.

### History

Row equivalence as a named relation became standard in the textbooks of the 20th century; Hoffman and Kunze treat it in Chapter 1.

### Common errors

1. Thinking that row equivalent matrices have the same column space.
2. Thinking that row equivalent matrices are equal "up to scaling of rows"; row additions change rows in other ways.

## Explanations

### L1 human

Two tables are row equivalent when row moves turn one into the other.
Since every move can be undone, it does not matter which table we start from.
If the tables come from two systems of equations, the two systems have the same solutions.
For example, the system $x + y = 3$, $x - y = 1$ is row equivalent to the system $x = 2$, $y = 1$.

### L2 human

We test whether $A = \begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix}$ and $B = \begin{bmatrix} 2 & 4 \\ 1 & 2 \end{bmatrix}$ are row equivalent.

1. For $A$: $R_2 \leftarrow R_2 - 3R_1$ gives $\begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$.
2. For $B$: $R_1 \leftrightarrow R_2$ gives $\begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$, then $R_2 \leftarrow R_2 - 2R_1$ gives $\begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$.
3. The RREFs agree, so $A \sim B$.
4. A sequence from $A$ to $B$: reduce $A$, then undo the steps for $B$ in reverse order: $R_2 \leftarrow R_2 + 2R_1$, then $R_1 \leftrightarrow R_2$.
5. Check: from $\begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$ the first step gives $\begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$, and the swap gives $B$.

The typical use is the RREF test of step 3.
A trap: two different echelon forms do not show that matrices are not row equivalent, because echelon forms are not unique; compare the RREFs.

### L3 human

Row equivalence classes of $m \times n$ matrices correspond to subspaces of $F^n$ of dimension at most $m$, through the row space.
So the set of classes of rank $r$ is the Grassmannian of $r$-dimensional subspaces of $F^n$.
Column equivalence is the dual notion, with the column space in place of the row space.
Over a ring such as $\mathbb{Z}$, the classes under invertible row operations have the Hermite normal form as canonical representatives.
