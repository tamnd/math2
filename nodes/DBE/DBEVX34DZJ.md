---
tag: DBEVX34DZJ
kind: proof
name: Proof of uniqueness of solutions by pivot columns
proves: 5MGKEK1K42
methods: [0NTF6DMVAP, 0WCP0PVET6]
uses: [BKA191KD1S, 0BCMGDHZGR]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section1-4.xml#L917
    locator: src/section1-4.xml:917
---

## Proof

We read the pivots of $A$ from an echelon form of $[A \mid b]$ and then apply the existence and uniqueness theorem.
Let $A$ be $m \times n$, and let $E$ be an echelon form of $[A \mid b]$.

1. The first $n$ columns of $E$ form an echelon form of $A$, because deleting the last column of an echelon matrix keeps the staircase pattern.
2. So the pivot columns of $A$ are the pivot columns of $E$ among its first $n$ columns.
3. Let $k$ be the number of columns of $A$ without a pivot position.
4. The system is consistent, so [[the existence and uniqueness theorem|BKA191KD1S]], part 3, applies.
5. Part 1: if each column of $A$ holds a pivot position, then $k = 0$, and the solution is unique by part 3 of that theorem.
6. Part 2: if some column holds no pivot position, then $k \ge 1$, and the solution is not unique by part 3 of that theorem.
7. Part 3: if, in addition, $F$ is infinite, part 4 of that theorem gives infinitely many solutions.

## Idea

The statement is the special case of the existence and uniqueness theorem for consistent systems.

## Variants

A direct proof over $\mathbb{R}$ uses the solution formula from the RREF: a free variable can take every real value, and each value gives a different solution.
