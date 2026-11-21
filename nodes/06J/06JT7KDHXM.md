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

A homogeneous system is a system of linear equations with zero on every right side.
Let $F$ be a [[field|04C5ZBG1WT]].
A [[system of linear equations|0GT4WWGWH2]] over $F$ is *homogeneous* when each of its constant terms is $0$.
In matrix form, a homogeneous system is an equation $Ax = 0$, where $A$ is an $m \times n$ matrix over $F$ and $x = (x_1, \dots, x_n)^{\mathsf{T}}$.
For any system $Ax = b$, the system $Ax = 0$ is its *associated homogeneous system*.

## Remarks

The condition is about the right sides only, and the coefficients can be any elements of $F$.
Because every right side is zero, the tuple $(0, \dots, 0)$ is always a solution, called the *trivial solution*.
For example, $x + y = 0$, $2x + 2y = 0$ is homogeneous, with the trivial solution $(0, 0)$ and also the solution $(1, -1)$.
The system $x + y = 1$, $x - y = 0$ fails the condition, and $(0, 0)$ is not a solution of it.

The associated homogeneous system matters because it controls the shape of the solutions of $Ax = b$.
If $Ax = b$ has a solution $p$, then its solution set is $\set{p + v : Av = 0}$, by the [[structure theorem|PDH3HKXWAZ]].
The solution set of $Ax = 0$ itself is a [[linear subspace|00YC1D652K]] of $F^n$, the [[null space|0PHDYNR24D]] of $A$.
The concept page on the [[homogeneous system|04KGXJG1A2]] proves this and shows when nontrivial solutions exist.

## Explanations

### L1 human

A homogeneous system has zero on the right side of every equation.
Setting every unknown to zero always works, so the question is whether other solutions exist.
The sum of two solutions is again a solution, and so is any multiple of a solution.

### L2 human

The system $x + y = 0$, $2x + 2y = 0$ is homogeneous.
The pair $(0, 0)$ is a solution, and so is $(1, -1)$, since
$$1 + (-1) = 0, \qquad 2 \cdot 1 + 2 \cdot (-1) = 0.$$
Then $(3, -3) = 3(1, -1)$ is also a solution, because a multiple of a solution of a homogeneous system is a solution.
Watch out: "homogeneous" refers to the right side only, so a system with zero coefficients and a nonzero right side is not homogeneous.
