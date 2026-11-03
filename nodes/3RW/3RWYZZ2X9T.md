---
tag: 3RWYZZ2X9T
kind: definition
name: Lemke–Howson algorithm
msc: [91A68, 91A05, 90C33]
defines: 1FSR0S8E45
uses: [5MZTZRC3CZ, P01KKHB155, 745WYP9YJ0, QP7GEKDTYX]
sources:
  - url: https://en.wikipedia.org/wiki/Lemke%E2%80%93Howson_algorithm
---

## Definition

Let $A$ and $B$ be real $m \times n$ matrices with positive entries, the payoffs of a two-player [[normal-form game|5MZTZRC3CZ]].
Consider the [[polytopes|QP7GEKDTYX]]
$$P = \set{x \in \R^m : x \ge 0,\ B^T x \le \mathbf{1}}, \qquad Q = \set{y \in \R^n : A y \le \mathbf{1},\ y \ge 0}.$$
Use the labels $1, \dots, m + n$.

1. A point $x \in P$ has label $i \le m$ if $x_i = 0$, and label $m + j$ if $(B^T x)_j = 1$.
2. A point $y \in Q$ has label $m + j$ if $y_j = 0$, and label $i \le m$ if $(A y)_i = 1$.
3. A pair $(x, y)$ is *completely labeled* if each of the $m + n$ labels is a label of $x$ or of $y$.

Assume the game is nondegenerate: vertices of $P$ have at most $m$ labels, and vertices of $Q$ at most $n$ labels.
The *Lemke–Howson algorithm* with missing label $k$ starts at the vertex $(0, 0)$ of $P \times Q$.
It drops label $k$ by moving along an edge of $P \times Q$.
It then repeats: the new vertex has one duplicate label, and it moves along the edge that drops the old copy of that label.
It stops at the first completely labeled vertex.

## Remarks

A completely labeled pair $(x, y) \ne (0, 0)$ gives a [[Nash equilibrium|745WYP9YJ0]] $(x / \sum_i x_i,\ y / \sum_j y_j)$ in [[mixed strategies|P01KKHB155]], and every equilibrium arises this way.
The vertices that have all labels except possibly $k$ form disjoint paths and cycles, whose path endpoints are the completely labeled vertices.
So the walk from $(0, 0)$ is well defined and ends at an equilibrium.
The other equilibria are paired up by the paths, so a nondegenerate game has an odd number of equilibria.
Example: let $A = B = I_2$, the identity matrix, and drop label $1$.
Then $x$ moves from $0$ to $(1, 0)$ and gains label $3$, which $y = 0$ already has.
So $y$ moves to $(1, 0)$ and gains label $1$; now all labels appear, and both players play their first strategy.
Non-example: in the same game, the pair $x = (1, 0)$, $y = (0, 0)$ reached after the first step has the labels $\set{2, 3}$ and $\set{3, 4}$.
Label $1$ is missing, so it is not completely labeled, and the algorithm goes on.
Payoffs can be made positive by adding a constant, which does not change the equilibria.
Savani and von Stengel showed that the algorithm can take exponentially many steps.
