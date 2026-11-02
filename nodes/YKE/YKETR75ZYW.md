---
tag: YKETR75ZYW
kind: problem
name: Discrete Dirichlet problem
msc: [31C20, 05C81]
uses: [00C0BR7D7H, WRY0M7SW59]
about: [WRY0M7SW59]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_Laplace_operator
history:
  posed_by: "H. B. Phillips and Norbert Wiener"
  first_stated: "1923"
  notes: "Phillips and Wiener studied it in Nets and the Dirichlet problem, J. Math. Phys. 2 (1923). Courant, Friedrichs and Lewy used it in 1928."
---

## Problem

Let $G = (V, E)$ be a finite connected [[graph|00C0BR7D7H]] with symmetric positive edge weights $c(x, y)$.
Let $B \subseteq V$ be a nonempty set of boundary vertices, and let $I = V \setminus B$ be the set of interior vertices.
Let $g \colon B \to \R$ be a function.
Find a function $f \colon V \to \R$ that is [[harmonic|WRY0M7SW59]] at every vertex of $I$ and satisfies $f = g$ on $B$.

## Remarks

The problem always has exactly one solution.
Uniqueness follows from the maximum principle: the difference $h$ of two solutions is harmonic on $I$ and zero on $B$.
At an interior vertex where $h$ is largest, harmonicity forces the same value at all neighbours.
Connectedness spreads this value to a vertex of $B$, so $\max h = 0$, and in the same way $\min h = 0$.
The conditions form a square system of $\abs{I}$ linear equations in the $\abs{I}$ unknowns $f(x)$, $x \in I$, so uniqueness gives existence.
The solution has the probabilistic form $f(x) = \mathbb{E}_x\big[g(X_\tau)\big]$, where $(X_n)$ is the random walk with $p(x, y) = c(x, y)/c(x)$ started at $x$ and $\tau$ is its first hitting time of $B$.
Example: on the path with vertices $0, 1, \dots, n$, unit weights and $B = \set{0, n}$, the solution is the linear interpolation $f(k) = g(0) + \tfrac{k}{n}\big(g(n) - g(0)\big)$.
Connectedness matters: if a component of the graph does not meet $B$, any constant can be added to $f$ on that component, and the solution is not unique.

## Explanations

### L1 human

Fix numbers on some vertices of a graph, the boundary.
The task is to fill in the other vertices so that each of them carries the average of its neighbours.
Think of the boundary numbers as fixed voltages, or fixed temperatures, and of the filled-in numbers as the equilibrium state.
On a connected finite graph there is always exactly one way to do it.
It can be found by solving a linear system or by running random walks to the boundary.
