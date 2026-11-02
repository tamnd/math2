---
tag: 5DFMMGGD9Y
kind: statement
role: theorem
name: Minkowski–Weyl theorem
msc: [52B11, 90C05]
uses: [0FQSDC2EQ2, 6VE4KA12VD, 300K6CB1KH, W8P2G5R02N]
about: [300K6CB1KH, W8P2G5R02N]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_polytope
---

## Statement

Let $n \ge 1$, and let $P \subseteq \R^n$ be nonempty.
The following are equivalent.

1. There are a real $m \times n$ matrix $A$ and $b \in \R^m$, for some $m \ge 0$, with $P = \set{x \in \R^n : A x \le b}$, where $\le$ is taken coordinatewise.
2. There are finite sets $V, W \subseteq \R^n$ with $V \ne \emptyset$ and $P = \mathrm{conv}(V) + \mathrm{cone}(W)$.

Here $\mathrm{conv}(V)$ is the [[convex hull|0FQSDC2EQ2]] of $V$, and $\mathrm{cone}(W)$ is the [[convex cone|6VE4KA12VD]] of all nonnegative linear combinations of $W$, with $\mathrm{cone}(\emptyset) = \set{0}$.
In particular, $P$ is a [[convex polytope|300K6CB1KH]] if and only if it is a bounded set of the form in 1.

## Remarks

For 2 implies 1, write $P$ as the projection to $\R^n$ of the set of all $(x, \lambda, \mu)$ with $x = \sum_v \lambda_v v + \sum_w \mu_w w$, $\lambda, \mu \ge 0$ and $\sum_v \lambda_v = 1$.
Fourier–Motzkin elimination shows that the projection of a set given by finitely many linear inequalities is again such a set.
For 1 implies 2, one can apply the first direction to a suitable polar cone.
The polytope case follows, because a bounded set $\mathrm{conv}(V) + \mathrm{cone}(W)$ must have $\mathrm{cone}(W) = \set{0}$.
Example: the square $[0, 1]^2$ is $\set{x : 0 \le x_1 \le 1, \ 0 \le x_2 \le 1}$, given by four inequalities, and also $\mathrm{conv}\set{(0, 0), (1, 0), (0, 1), (1, 1)}$.
The quadrant $\set{x : x_1 \ge 0, x_2 \ge 0}$ is $\mathrm{conv}\set{0} + \mathrm{cone}\set{(1, 0), (0, 1)}$.
Finiteness is needed: the closed unit disc is an intersection of infinitely many half-planes and the convex hull of infinitely many points, but of neither form above.

## Explanations

### L1 human

There are two ways to describe a convex polytope: by its corners, or by the flat walls that bound it.
The theorem says that both ways describe the same shapes.
Any finite list of points spans a shape that can be cut out by finitely many walls.
Any bounded region cut out by finitely many walls is spanned by finitely many corners.

### L2 human

The two descriptions are the [[V-representation and H-representation|W8P2G5R02N]] of a polytope.
Linear programming uses both: the feasible region is given by inequalities, while the simplex method moves between vertices.
Changing from one description to the other is the vertex and facet enumeration problem.
The sizes can differ a lot: the cube $[0, 1]^n$ needs $2n$ inequalities but has $2^n$ vertices.
The theorem is a finite-dimensional cousin of Farkas' lemma, and the two can be derived from each other.
