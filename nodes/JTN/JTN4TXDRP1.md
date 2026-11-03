---
tag: JTN4TXDRP1
kind: definition
name: Holonomic constraint
msc: [70F20, 70G10]
defines: AXA8HN8Y45
uses: [0XPR1E85W0, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Holonomic_constraints
---

## Definition

Consider a system of $N$ point particles with positions $x_1, \dots, x_N \in \R^3$, and write $x = (x_1, \dots, x_N) \in \R^{3N}$.
Let $f$ be a real-valued [[smooth function|0V33BNKZ9S]] on an open subset of $\R^{3N} \times \R$.
A *holonomic constraint* on the system is a condition $f(x, t) = 0$ that the positions must satisfy at every time $t$.
Holonomic constraints $f_1 = 0, \dots, f_k = 0$ are *independent* when the gradients of $f_1, \dots, f_k$ in $x$ are linearly independent wherever all the constraints hold.

## Remarks

Example: a pendulum of length $\ell > 0$ with pivot at the origin of $\R^3$ satisfies $f(x) = \abs{x}^2 - \ell^2 = 0$.
Its gradient $2x$ is nonzero on the sphere $\abs{x} = \ell$, so the constraint is independent.
Non-example: a particle that must stay in the half-space $z \ge 0$ is restricted by an inequality, not by an equation, so the restriction is not a holonomic constraint.
A constraint linear in the velocities is also called holonomic when it is equivalent to a constraint on positions.
For instance, $\dot z = 0$ is equivalent to $z = c$ for a constant $c$.
