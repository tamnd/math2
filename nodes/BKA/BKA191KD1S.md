---
tag: BKA191KD1S
kind: statement
role: theorem
name: Existence and uniqueness of solutions of a linear system
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
uses: [0GT4WWGWH2, 0T6MWGZSXA, 0J0BBCMJ5W, 0X6V9B1V10, 0VYCDGMJJJ, BF9SMZMJZE, P3HMRQN5KT, E4GKK727ZM]
about: [0X6V9B1V10]
proofs: [550R9YRC28]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section1-4.xml#L575
    locator: src/section1-4.xml:575
  - book: isbn:9780321982384
    locator: Section 1.2
---

## Statement

One echelon form of the augmented matrix answers both questions: whether a solution exists, and how many there are.
Let $F$ be a [[field|04C5ZBG1WT]], let $A$ be an $m \times n$ matrix over $F$, and let $b \in F^m$.
Let $E$ be any [[row echelon form|0VYCDGMJJJ]] of the [[augmented matrix|0T6MWGZSXA]] $[A \mid b]$ of the [[linear system|0GT4WWGWH2]] $Ax = b$.

1. The system is [[consistent|0X6V9B1V10]] if and only if the last column of $E$ is not a [[pivot|0J0BBCMJ5W]] column, that is, $E$ has no row $(0, \dots, 0 \mid c)$ with $c \neq 0$.
2. Assume that the system is consistent, and let $k$ be the number of columns among the first $n$ columns of $E$ that are not pivot columns.
3. Then the system has a unique solution if and only if $k = 0$, that is, every column of $A$ is a pivot column.
4. If $k \ge 1$ and $F$ is infinite, for example $F = \mathbb{R}$, the system has infinitely many solutions.
5. If $k \ge 1$ and $F$ has $q$ elements, the system has exactly $q^k$ solutions.

The pivot columns do not depend on the choice of $E$, so the number $k$ is well defined.

## Remarks

### All three cases in one family

Take $x + 2y = 3$, $2x + 4y = c$ over $\mathbb{R}$.
The step $R_2 \leftarrow R_2 - 2R_1$ gives the echelon form $\left[\begin{array}{cc|c} 1 & 2 & 3 \\ 0 & 0 & c - 6 \end{array}\right]$.
If $c \neq 6$, the last column is a pivot column, so the system is inconsistent.
If $c = 6$, the only pivot is in column 1, so $k = 1$, $y$ is free, and the solutions are $(3 - 2t, t)$; check $(3 - 2t) + 2t = 3$.
Replacing $4y$ by $5y$ gives $k = 0$ and one solution for every $c$.

### Why each hypothesis is needed

The matrix $E$ must be in echelon form: $\left[\begin{array}{cc|c} 1 & 1 & 1 \\ 1 & 1 & 2 \end{array}\right]$ is not, its last column has no leading entry, and $x + y = 1$, $x + y = 2$ is inconsistent.
$E$ must be row equivalent to $[A \mid b]$, since an echelon form of $A$ alone says nothing about consistency, by [[the augmentation principle|BE3NZP35HY]].
Parts 3 to 5 need consistency, since an inconsistent system with $k = 0$ still has no solution, as for $x = 1$, $x = 2$.
Part 4 needs an infinite field: over $\mathbb{F}_2$, the system $x + y = 0$ has $k = 1$ and only the $2$ solutions $(0, 0)$ and $(1, 1)$.

### What follows

Over any field, a linear system has no solution, exactly one solution, or more than one solution, and over $\mathbb{R}$ "more than one" means infinitely many.
At most $m$ columns have pivots, so a consistent system with more unknowns than equations has $k \ge n - m \ge 1$ and more than one solution.
A square system has a unique solution for every $b$ if and only if $A$ has $n$ pivots, that is, $A$ is invertible.
Each part is an equivalence or a count, so the converses are included: a unique solution forces $k = 0$, because $k \ge 1$ gives at least $|F| \ge 2$ solutions.

### Beyond fields

Over a commutative ring that is not a field, this test fails.
Over $\mathbb{Z}$, the equation $2x = 1$ has no solution, although $\left[\begin{array}{c|c} 2 & 1 \end{array}\right]$ looks like an echelon form with no pivot in the last column.
The [[Rouché-Capelli theorem|0HV1SKWPMS]] states the same facts in terms of rank.

### Where the name comes from

Lay states this result in Section 1.2 as the existence and uniqueness theorem.

## Explanations

### L1 human

After elimination, look for a row that says $0 = c$ with $c$ not zero.
If there is such a row, the equations contradict each other, and there is no solution.
If there is none, the system has a solution.
It is the only one when every unknown has a pivot, and otherwise some unknowns are free.

### L2 human

The typical use is to decide, before any back substitution, whether a system has none, one or many solutions.
Reduce $[A \mid b]$ to echelon form, look at the last column, and then count the columns of $A$ without a pivot.
Watch out: a zero row $(0, \dots, 0 \mid 0)$ is harmless, and only a zero row of $A$ with a nonzero right side signals inconsistency.

### L3 human

In terms of rank, part 1 says that $\operatorname{rank}[A \mid b] = \operatorname{rank} A$, and parts 2 and 3 say that $k = n - \operatorname{rank} A$.
The solution set, when it is not empty, is a coset of the null space, which has dimension $k$, by [[the structure of the solution set|PDH3HKXWAZ]].
