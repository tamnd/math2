---
tag: 8G30AFBZNQ
kind: problem
name: Linear complementarity problem
msc: [90C33]
uses: [JMTCEQ2J3Q, 0VD9ZSWWJG, ERSZ4ADRCY, HDWEPH4YG4]
about: [JMTCEQ2J3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_complementarity_problem
same_as:
  wikidata: Q783105
  wikipedia: Linear complementarity problem
history:
  posed_by: Richard W. Cottle and George B. Dantzig
  first_stated: "1968"
---

## Problem

Let $M$ be a real $n \times n$ [[matrix|0VD9ZSWWJG]] and let $q \in \R^n$.
The *linear complementarity problem* $\mathrm{LCP}(q, M)$ is to find vectors $w, z \in \R^n$ such that
$$w = M z + q, \quad w \ge 0, \quad z \ge 0, \quad z^T w = 0,$$
where $\ge$ holds componentwise.

## Remarks

It is the [[complementarity problem|JMTCEQ2J3Q]] for the affine map $z \mapsto M z + q$.
If $q \ge 0$, then $z = 0$, $w = q$ is a solution.

The [[Karush–Kuhn–Tucker conditions|HDWEPH4YG4]] of a convex [[quadratic program|ERSZ4ADRCY]] "minimise $\tfrac12 x^T Q x + c^T x$ subject to $A x \ge b$, $x \ge 0$" form an LCP with
$$M = \begin{pmatrix} Q & -A^T \\ A & 0 \end{pmatrix}, \qquad q = \begin{pmatrix} c \\ -b \end{pmatrix}.$$
Finding a Nash equilibrium of a bimatrix game can also be written as an LCP.

The problem $\mathrm{LCP}(q, M)$ has exactly one solution for every $q \in \R^n$ if and only if $M$ is a P-matrix, that is, all its principal minors are positive.
Deciding whether a given LCP has a solution is NP-complete in general.
Lemke's algorithm and other pivoting methods solve it for important classes of matrices, such as positive semidefinite ones.

## Explanations

### L1 human

There are $n$ pairs of unknown numbers $z_i$ and $w_i$, tied together by linear equations.
All of them must be nonnegative, and in each pair at least one must be zero.
For $n = 1$, $M = 1$ and $q = -2$, one needs $w = z - 2$, $w, z \ge 0$ and $z w = 0$; the solution is $z = 2$, $w = 0$.
