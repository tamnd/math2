---
tag: KNP5ZEQ458
kind: definition
name: H-representation and V-representation
msc: [52B11, 52B55, 90C05]
defines: W8P2G5R02N
uses: [300K6CB1KH, 0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_polytope
---

## Definition

Let $n \ge 1$, and let $P \subseteq \R^n$ be a [[convex polytope|300K6CB1KH]].

1. A *V-representation* of $P$ is a finite set $V \subseteq \R^n$ with $P = \mathrm{conv}(V)$, the [[convex hull|0FQSDC2EQ2]] of $V$.
2. An *H-representation* of $P$ is a pair $(A, b)$ of a real $m \times n$ matrix $A$ and a vector $b \in \R^m$ with $P = \set{x \in \R^n : A x \le b}$. Here $\le$ is taken coordinatewise.

Equivalently, an H-representation is a finite family of closed half-spaces whose intersection is $P$.

## Remarks

Example: for $P = [0, 1]^2$, the set $V = \set{(0, 0), (1, 0), (0, 1), (1, 1)}$ is a V-representation, and the inequalities $-x_1 \le 0$, $x_1 \le 1$, $-x_2 \le 0$, $x_2 \le 1$ form an H-representation.
Non-example: the inequalities $-x_1 \le 0$, $-x_2 \le 0$ alone are not an H-representation of $[0, 1]^2$; they define the unbounded quadrant, which contains $(2, 0) \notin P$.
Representations are not unique, since points and inequalities can be added without changing $P$.
The smallest V-representation is the set of vertices of $P$, and for a full-dimensional $P$ an irredundant H-representation has exactly one inequality for each facet, unique up to positive scaling.
Every convex polytope has both kinds of representation; this is the Minkowski–Weyl theorem.
