---
tag: QF0E0X7AQG
kind: statement
role: theorem
name: Fundamental theorem of linear programming
msc: [90C05, 52B55]
uses: [957S7V3JW8, VNMXB0J2KA, 0ZC9YTXZRY, 3MSGFJM2NX, 0CRMGPAH83, FYZC634H2D]
about: [957S7V3JW8, VNMXB0J2KA]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_linear_programming
same_as:
  wikidata: Q57498
  wikipedia: Fundamental theorem of linear programming
---

## Statement

Let $A$ be a real $m \times n$ matrix of [[rank|0ZC9YTXZRY]] $m$, let $b \in \R^m$ and let $c \in \R^n$.
Consider the [[linear program|VNMXB0J2KA]]: maximize $c^T x$ subject to $A x = b$ and $x \ge 0$.

1. If the program has a feasible solution, then it has a [[basic feasible solution|957S7V3JW8]].
2. If the program has an optimal solution, then it has an optimal solution that is a basic feasible solution.

## Remarks

Proof idea: take a feasible (or optimal) $x$ with the fewest nonzero coordinates.
If the columns $A_j$ with $x_j > 0$ were [[linearly dependent|0CRMGPAH83]], a dependence $\sum_j d_j A_j = 0$ would give a direction $d$ with $A d = 0$.
Moving along $\pm d$ until a coordinate reaches $0$ keeps feasibility and removes a nonzero coordinate, a contradiction.
For an optimal $x$, one has $c^T d = 0$, so the move also keeps the objective value.

Since basic feasible solutions are the vertices, that is, the [[extreme points|3MSGFJM2NX]], of the feasible region, part 2 says that an optimum, when it exists, is attained at a vertex.
There are finitely many bases, so in principle an optimum can be found by checking them all; the simplex algorithm does this search cleverly.

Example: maximize $x_1$ subject to $x_1 + x_2 = 1$, $x \ge 0$.
The optimal solution $(1, 0)$ is the basic feasible solution of the basis $\set{1}$.
For $c = (1, 1)$, every feasible point is optimal, including the non-basic $(1/2, 1/2)$, but the basic $(1, 0)$ and $(0, 1)$ are optimal too, as part 2 requires.

The rank hypothesis is a normalization: redundant equations can be deleted without changing the feasible region, when the system is consistent.
Part 2 needs the existence of an optimum.
For "maximize $x_1$ subject to $x_1 - x_2 = 0$, $x \ge 0$" the basic feasible solution $0$ exists, but the program is unbounded and has no optimal solution.

## Explanations

### L1 human

The feasible region of a linear program is a shape with flat sides and corners.
The theorem says that if a best point exists, then one of the corners is a best point.
So the search for an optimum can be restricted to the finitely many corners.

### L2 human

The theorem reduces linear programming to a finite search over bases, and it is the reason the simplex algorithm can work with basic feasible solutions only.
Together with [[Farkas' lemma|FYZC634H2D]] or duality theory it gives the trichotomy: a linear program is infeasible, unbounded, or has an optimal basic feasible solution.
In the language of polyhedra, a linear function bounded above on a nonempty pointed polyhedron attains its maximum at a vertex.
