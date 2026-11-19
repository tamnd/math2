---
tag: 5MGKEK1K42
kind: statement
role: corollary
name: Uniqueness of solutions of a consistent linear system by pivot columns
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
uses: [0X6V9B1V10, 0GT4WWGWH2, 0BCMGDHZGR, BKA191KD1S]
proofs: [~69961e16]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section1-4.xml#L917
    locator: src/section1-4.xml:917
---

## Statement

Let $F$ be a [[field|04C5ZBG1WT]], and take a [[system of linear equations|0GT4WWGWH2]] $Ax = b$ over $F$ that is [[consistent|0X6V9B1V10]].
Look at the [[pivot positions|0BCMGDHZGR]] of its coefficient matrix $A$.

1. If each column of $A$ holds a pivot position, then the system has exactly one solution.
2. If at least one column of $A$ holds no pivot position, then the system has more than one solution.
3. In case 2, if $F$ is infinite, for example $F = \R$, the system has infinitely many solutions.

## Remarks

A column with a pivot position gives a basic variable.
A column without one gives a free variable.
So the cases say: no free variable means one solution, and at least one free variable means more than one solution.

### Why each hypothesis is needed

1. Consistency is needed. An inconsistent system has no solution, whatever its pivot columns are; for example $x = 1$, $x = 2$ has a pivot in its only column.
2. Part 3 needs an infinite field. Over $\mathbb{F}_2$ the system $x + y = 1$ has a free variable and exactly $2$ solutions, $(1, 0)$ and $(0, 1)$.

### Consequences

1. A consistent system with more unknowns than equations has more than one solution, because $A$ has at most $m$ pivots.
2. Over $\R$, a linear system has no solution, exactly one, or infinitely many; it never has exactly two.

### Converse

Both parts together give a converse: if a consistent system has exactly one solution, every column of $A$ has a pivot position.

### Generalizations

The count of solutions over a field with $q$ elements is $q^k$, with $k$ the number of free variables, see [[the theorem on finite fields|~b461276f]].
The [[parametric form|~dc297165]] describes all the solutions with $k$ parameters.

## Explanations

### L1 human

If every unknown has a pivot, the equations fix each unknown, so there is one answer.
If some unknown has no pivot, we can choose it freely, so there are many answers.

### L2 human

We look at $x + y + z = 3$, $y + 2z = 3$ over $\R$.

1. The augmented matrix $\left[\begin{array}{rrr|r} 1 & 1 & 1 & 3 \\ 0 & 1 & 2 & 3 \end{array}\right]$ is in echelon form, with no pivot in the last column, so the system is consistent.
2. Column 3 of $A$ has no pivot, so $z$ is free.
3. With $z = t$, back substitution gives $y = 3 - 2t$ and $x = 3 - (3 - 2t) - t = t$.
4. So the solutions $(t, 3 - 2t, t)$ are infinitely many; check $t = 1$: $1 + 1 + 1 = 3$ and $1 + 2 = 3$.

The typical use is to decide quickly whether a consistent system has one solution or many.
A trap: the pivots must be those of the coefficient matrix $A$; a pivot in the last column of $[A \mid b]$ means no solution.

### L3 human

The number of free variables is $n - \operatorname{rank} A$, the dimension of the null space.
So the statement is the case "$\dim N(A) = 0$ or not" of [[the structure of the solution set|~a01a76ca]].
