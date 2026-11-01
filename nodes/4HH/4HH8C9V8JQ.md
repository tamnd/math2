---
tag: 4HH8C9V8JQ
kind: statement
role: theorem
name: Fredholm alternative
msc: [15A06, 47A53]
uses: [0JTRMBQ1SA, 06JT7KDHXM, 0W809K6AW0, 0QA8CHH8MG]
about: [0GT4WWGWH2, 04KGXJG1A2]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_alternative
---

## Statement

Let $F$ be a [[field|04C5ZBG1WT]], let $n \ge 1$ and let $A$ be an $n \times n$ matrix over $F$, with [[transpose|09DXWYRD43]] $A^{T}$.
Then exactly one of the following two cases holds.

1. For every $b \in F^n$, the [[system|0GT4WWGWH2]] $Ax = b$ has exactly one solution $x \in F^n$.
2. The [[homogeneous system|04KGXJG1A2]] $Ax = 0$ has a solution $x \ne 0$.

In case 2, for $b \in F^n$, the system $Ax = b$ has a solution if and only if $y^{T} b = 0$ for every $y \in F^n$ with $A^{T} y = 0$.

## Remarks

The first part follows from the [[rank–nullity theorem|0W4FSW1TVB]]: the map $x \mapsto Ax$ on $F^n$ is injective if and only if it is surjective.
For the solvability condition, the [[column space|03AJKXH1AV]] of $A$ and the solution space of $A^{T} y = 0$ have dimensions $r$ and $n - r$, where $r$ is the [[rank|0ZC9YTXZRY]] of $A$.
Every column $a$ of $A$ satisfies $y^{T} a = 0$ for such $y$.
So the column space lies in the space of all $b$ with $y^{T} b = 0$ for all such $y$.
Both spaces have dimension $r$, so they are equal.
Example: for $A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, case 2 holds with $x = (1, -1)$.
The solutions of $A^{T} y = 0$ are the multiples of $y = (1, -1)$, so $Ax = b$ is solvable exactly when $b_1 = b_2$.
The name comes from Fredholm's theory of integral equations, where the same alternative holds for compact perturbations of the identity on Banach spaces.

## Explanations

### L1 human

A square linear system behaves in one of two ways.
Either it is perfect: every right-hand side has one and only one solution.
Or the homogeneous system has a nonzero solution, and then some right-hand sides have no solution at all.
In the second case, a simple test tells which right-hand sides work: $y^{T} b$ must be $0$ for every solution $y$ of the transposed homogeneous system $A^{T} y = 0$.

### L2 human

The theorem says that for square systems, uniqueness and existence go together.
To show that $Ax = b$ is always solvable, it is enough to show that $Ax = 0$ has only the zero solution.
The solvability condition in case 2 is the statement that the column space of $A$ is the annihilator of the null space of $A^{T}$.
It is the finite-dimensional model for the Fredholm alternative for integral equations and for elliptic boundary value problems.
