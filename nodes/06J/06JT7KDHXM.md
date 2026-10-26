---
tag: 06JT7KDHXM
kind: definition
name: Homogeneous system of linear equations
msc: [15A06]
defines: 04KGXJG1A2
uses: [0JTRMBQ1SA]
sources:
  - url: https://en.wikipedia.org/wiki/System_of_linear_equations
    locator: Homogeneous systems
---

## Definition

Let $F$ be a field.
A [[system of linear equations|0GT4WWGWH2]] over $F$ is *homogeneous* when each of its constant terms is $0$.
In matrix form, a homogeneous system is an equation $Ax = 0$, where $A$ is an $m \times n$ matrix over $F$ and $x = (x_1, \dots, x_n)^T$.

## Remarks

The tuple $(0, \dots, 0)$ is always a solution, the *trivial solution*.
The solution set of $Ax = 0$ is a [[linear subspace|00YC1D652K]] of $F^n$, the [[null space|0PHDYNR24D]] of $A$.
If a system $Ax = b$ has a solution $p$, then its solution set is $\{p + v : Av = 0\}$.
A homogeneous system with more unknowns than equations has a nontrivial solution.

## Explanations

### L1 human

A homogeneous system has zero on the right side of every equation.
Setting every unknown to zero always works, so the question is whether other solutions exist.
The sum of two solutions is again a solution, and so is any multiple of a solution.
