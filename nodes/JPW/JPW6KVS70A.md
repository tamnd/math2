---
tag: JPW6KVS70A
kind: statement
role: theorem
name: A homogeneous system with more unknowns than equations has a nontrivial solution
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
uses: [04KGXJG1A2, 0J0BBCMJ5W, FCM29NQ6DN, P3HMRQN5KT, E4GKK727ZM]
about: [04KGXJG1A2]
proofs: [YN6BMCAVR2]
sources:
  - book: isbn:9780321982384
    locator: Section 1.5
  - url: https://en.wikipedia.org/wiki/System_of_linear_equations
    locator: Homogeneous systems
---

## Statement

When a homogeneous system has more unknowns than equations, some unknown is free, and so the system has a solution other than zero.
Let $F$ be a [[field|04C5ZBG1WT]], and let $A$ be an $m \times n$ matrix over $F$ with $n > m$.
Then the [[homogeneous system|04KGXJG1A2]] $Ax = 0$ has a solution $x \neq 0$.

More precisely, for all $m$ and $n$, the system $Ax = 0$ has a solution $x \neq 0$ if and only if some column of an echelon form of $A$ has no [[pivot|0J0BBCMJ5W]].

## Remarks

### Why each hypothesis is needed

The system must be homogeneous.
The system $x + y + z = 1$, $x + y + z = 2$ has $n = 3 > 2 = m$, and yet it has no solution at all, because the two equations contradict each other.
Without the zero right side, the free variable gives nothing, since there may be no solution to start from.

The inequality $n > m$ must be strict.
The system $x = 0$, $y = 0$ has $n = m = 2$, and its only solution is $(0, 0)$.

### What it gives you

The most used consequence is about vectors.
Any $n$ vectors $v_1, \dots, v_n$ in $F^m$ with $n > m$ are linearly dependent, because $c_1 v_1 + \cdots + c_n v_n = 0$ is a homogeneous system of $m$ equations in $n$ unknowns.
For example, $(1, 0)$, $(0, 1)$ and $(2, 3)$ in $\mathbb{R}^2$ satisfy $2(1, 0) + 3(0, 1) - (2, 3) = 0$.
This is the step that proves that two bases of a finite-dimensional space have the same size.

In matrix language, a matrix with more columns than rows has a nonzero null space.
With the [[structure theorem|PDH3HKXWAZ]], a consistent system with more unknowns than equations then has more than one solution.

### The converse

The converse of the first part is false.
The system $x + y = 0$, $2x + 2y = 0$ has $n = m = 2$ and the nontrivial solution $(1, -1)$.
So a nontrivial solution can exist without the inequality $n > m$.
The second part is an equivalence, so it contains its own converse.

### Generalizations

The result also holds over an integral domain $D$, such as $\mathbb{Z}$.
Solve the system over the field of fractions of $D$, and then multiply the solution by a common denominator to get a nonzero solution with entries in $D$.

## Explanations

### L1 human

If there are more unknowns than equations, some unknown is free.
We set that unknown to $1$ and solve for the others.
This gives a solution that is not all zeros.

### L2 human

Here is a nonzero solution of $x + y + z = 0$, $x - y + 2z = 0$ over $\mathbb{R}$.
The operation $R_2 - R_1$ gives the row $(0, -2, 1)$, so the pivots are in columns 1 and 2, and $z$ is free.
Put $z = 2$ to avoid fractions.
Then row 2 gives $-2y + 2 = 0$, so $y = 1$, and row 1 gives $x = -1 - 2 = -3$.
Check:
$$-3 + 1 + 2 = 0, \qquad -3 - 1 + 4 = 0.$$
The typical use is to show that too many vectors are dependent, or that a matrix with more columns than rows is not injective.
Watch out: the theorem gives existence only, and it says nothing about whether a non-homogeneous system with the same matrix is consistent.

### L3 human

In the language of linear maps, a linear map $F^n \to F^m$ with $n > m$ is not injective.
With the rank-nullity theorem this reads $\dim \ker A = n - \rank A \ge n - m \ge 1$.
The proof by elimination needs no dimension theory, and that is why it can be used to build dimension theory in the sub-area on [[vector spaces and bases|MVH97H8B2J]].
