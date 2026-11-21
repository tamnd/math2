---
tag: 5MGKEK1K42
kind: statement
role: corollary
name: Uniqueness of solutions of a consistent linear system by pivot columns
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
uses: [0X6V9B1V10, 0GT4WWGWH2, 0BCMGDHZGR, BKA191KD1S]
proofs: [DBEVX34DZJ]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section1-4.xml#L917
    locator: src/section1-4.xml:917
---

## Statement

Once a system is known to have a solution, the pivots of the coefficient matrix alone decide whether there is just one.
Let $F$ be a [[field|04C5ZBG1WT]], and take a [[system of linear equations|0GT4WWGWH2]] $Ax = b$ over $F$ that is [[consistent|0X6V9B1V10]].
Look at the [[pivot positions|0BCMGDHZGR]] of its coefficient matrix $A$.

1. If each column of $A$ holds a pivot position, then the system has exactly one solution.
2. If at least one column of $A$ holds no pivot position, then the system has more than one solution.
3. In case 2, if $F$ is infinite, for example $F = \mathbb{R}$, the system has infinitely many solutions.

## Remarks

### Reading the cases

A column with a pivot position gives a basic variable, and a column without one gives a free variable.
So the cases say: no free variable means one solution, and at least one free variable means more than one solution.

### A case with a free variable

Take $x + y + z = 3$, $y + 2z = 3$ over $\mathbb{R}$.
The augmented matrix $\left[\begin{array}{rrr|r} 1 & 1 & 1 & 3 \\ 0 & 1 & 2 & 3 \end{array}\right]$ is in echelon form, with no pivot in the last column, so the system is consistent.
Column 3 of $A$ has no pivot, so $z$ is free.
With $z = t$, back substitution gives $y = 3 - 2t$ and $x = 3 - (3 - 2t) - t = t$.
So the solutions $(t, 3 - 2t, t)$ are infinitely many, and $t = 1$ checks: $1 + 1 + 1 = 3$ and $1 + 2 = 3$.

### Why each hypothesis is needed

Consistency is needed, since an inconsistent system has no solution whatever its pivot columns are; for example $x = 1$, $x = 2$ has a pivot in its only column.
Part 3 needs an infinite field: over $\mathbb{F}_2$ the system $x + y = 1$ has a free variable and exactly $2$ solutions, $(1, 0)$ and $(0, 1)$.

### What follows

A consistent system with more unknowns than equations has more than one solution, because $A$ has at most $m$ pivots.
Over $\mathbb{R}$, a linear system has no solution, exactly one, or infinitely many, and never exactly two.
Parts 1 and 2 together give the converse: if a consistent system has exactly one solution, every column of $A$ has a pivot position.

### Counting exactly

Over a field with $q$ elements the number of solutions is $q^k$, with $k$ the number of free variables, by [[the theorem on finite fields|8QM2Y41P69]].
The [[parametric form|KQT68YPHD1]] describes all the solutions with $k$ parameters.

## Explanations

### L1 human

If every unknown has a pivot, the equations fix each unknown, so there is one answer.
If some unknown has no pivot, we can choose it freely, so there are many answers.

### L2 human

The typical use is to decide quickly whether a consistent system has one solution or many.
First check consistency, then count the columns of $A$ without a pivot.
Watch out: the pivots must be those of the coefficient matrix $A$, and a pivot in the last column of $[A \mid b]$ means no solution.

### L3 human

The number of free variables is $n - \operatorname{rank} A$, the dimension of the null space.
So the statement is the case "$\dim N(A) = 0$ or not" of [[the structure of the solution set|PDH3HKXWAZ]].
