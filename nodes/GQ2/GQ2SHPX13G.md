---
tag: GQ2SHPX13G
kind: definition
name: Mathematical programming with equilibrium constraints
msc: [90C33, 90C30]
defines: 5J7796V5GT
uses: [6QS7X5GVMY, JMTCEQ2J3Q, 02AS45T3H9, 2WGB8R9SAD]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_programming_with_equilibrium_constraints
---

## Definition

Let $f \colon \R^n \times \R^m \to \R$, let $Z \subseteq \R^n \times \R^m$, and let $F \colon \R^n \times \R^m \to \R^m$.
For each $x \in \R^n$ let $C(x) \subseteq \R^m$ be a closed [[convex set|02AS45T3H9]], and let $S(x)$ be the set of solutions $y$ of the [[variational inequality|6QS7X5GVMY]]
$$y \in C(x), \qquad (v - y)^T F(x, y) \ge 0 \quad \text{for all } v \in C(x).$$
A *mathematical program with equilibrium constraints* (MPEC) is the problem: minimise $f(x, y)$ over $(x, y)$ subject to $(x, y) \in Z$ and $y \in S(x)$.

## Remarks

When $C(x) = \R^m_{\ge 0}$, the condition $y \in S(x)$ is the [[complementarity problem|JMTCEQ2J3Q]] $y \ge 0$, $F(x, y) \ge 0$, $y^T F(x, y) = 0$.
The resulting problems are *mathematical programs with complementarity constraints*.

Example: minimise $(x - 1)^2 + (y - 1)^2$ over $(x, y) \in \R^2$ subject to $y \ge 0$, $y - x \ge 0$ and $y (y - x) = 0$.
Here $C(x) = [0, \infty)$ and $F(x, y) = y - x$, so the constraint is $y \in S(x)$.
For $x \ge 0$ the solution set is $S(x) = \set{x}$, and for $x < 0$ it is $S(x) = \set{0}$; the minimum is $0$ at $(1, 1)$.

Non-example: minimise $f(x, y)$ subject to $y \ge 0$ and $y - x \ge 0$, without $y (y - x) = 0$, is an ordinary nonlinear program: $y$ need not solve the equilibrium problem.

With complementarity constraints, the Mangasarian–Fromovitz [[constraint qualification|2WGB8R9SAD]] fails at every feasible point, so the standard Karush–Kuhn–Tucker theory does not apply directly.
