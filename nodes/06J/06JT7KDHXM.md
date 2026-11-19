---
tag: 06JT7KDHXM
kind: definition
name: Homogeneous system of linear equations
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
defines: 04KGXJG1A2
uses: [0JTRMBQ1SA]
sources:
  - url: https://en.wikipedia.org/wiki/System_of_linear_equations
    locator: Homogeneous systems
  - book: isbn:9780321982384
    locator: Section 1.5
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]].
A [[system of linear equations|0GT4WWGWH2]] over $F$ is *homogeneous* when each of its constant terms is $0$.
In matrix form, a homogeneous system is an equation $Ax = 0$, where $A$ is an $m \times n$ matrix over $F$ and $x = (x_1, \dots, x_n)^T$.
For any system $Ax = b$, the system $Ax = 0$ is its *associated homogeneous system*.

## Remarks

The tuple $(0, \dots, 0)$ is always a solution, the *trivial solution*.
The solution set of $Ax = 0$ is a [[linear subspace|00YC1D652K]] of $F^n$, the [[null space|0PHDYNR24D]] of $A$.
If a system $Ax = b$ has a solution $p$, then its solution set is $\set{p + v : Av = 0}$, see [[the structure theorem|~a01a76ca]].
A homogeneous system with more unknowns than equations has a nontrivial solution, see [[the theorem|~37f18967]].

## Explanations

### L1 human

A homogeneous system has zero on the right side of every equation.
Setting every unknown to zero always works, so the question is whether other solutions exist.
The sum of two solutions is again a solution, and so is any multiple of a solution.

### L2 human

The system $x + y = 0$, $2x + 2y = 0$ is homogeneous.

1. The pair $(0, 0)$ is a solution.
2. The pair $(1, -1)$ is also a solution: $1 - 1 = 0$ and $2 - 2 = 0$.
3. So is $(3, -3) = 3(1, -1)$.

A trap: "homogeneous" refers to the right side only; the coefficients can be any numbers.
