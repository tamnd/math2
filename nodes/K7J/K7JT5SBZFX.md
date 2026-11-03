---
tag: K7JT5SBZFX
kind: statement
role: theorem
name: Edmonds' matching polytope theorem
msc: [90C27, 05C70, 52B12]
uses: [0MJ04A50QW, 0NHK9MFFW9, 0FQSDC2EQ2, 300K6CB1KH, 0RCQZ36MME, JYBHEDWB6X, DKNC3NS0YH]
about: [0NHK9MFFW9, 300K6CB1KH]
sources:
  - url: https://en.wikipedia.org/wiki/Matching_polytope
---

## Statement

Let $G = (V, E)$ be a finite graph.
For $F \subseteq E$, let $\chi^F \in \R^E$ be its incidence vector, the [[indicator function|0RCQZ36MME]] of $F$ on $E$.
For $x \in \R^E$ and $A \subseteq E$, write $x(A) = \sum_{e \in A} x_e$.
For $U \subseteq V$, let $\delta(U)$ be the set of edges with exactly one end in $U$.
Let $E[U]$ be the set of edges with both ends in $U$.
Write $\delta(v) = \delta(\set{v})$.

Let $P_1$ be the set of all $x \in \R^E$ such that
$$x_e \ge 0 \ (e \in E), \quad x(\delta(v)) = 1 \ (v \in V), \quad x(\delta(U)) \ge 1 \ (U \subseteq V, \ \abs{U} \text{ odd}).$$
Let $P_2$ be the set of all $x \in \R^E$ such that
$$x_e \ge 0 \ (e \in E), \quad x(\delta(v)) \le 1 \ (v \in V), \quad x(E[U]) \le \frac{\abs{U} - 1}{2} \ (U \subseteq V, \ \abs{U} \text{ odd}).$$

1. The [[convex hull|0FQSDC2EQ2]] of the vectors $\chi^M$, where $M$ runs over the [[perfect matchings|0NHK9MFFW9]] of $G$, is $P_1$.
2. The convex hull of the vectors $\chi^M$, where $M$ runs over the [[matchings|0MJ04A50QW]] of $G$, is $P_2$.

## Remarks

The inequalities are valid.
A perfect matching must use an edge leaving each set $U$ with an odd number of vertices.
A matching has at most $(\abs{U} - 1)/2$ edges inside such a set $U$.
The hard part is that every vertex of the polytope defined by the inequalities is integral.
Edmonds proved this with the primal-dual analysis of his weighted [[blossom algorithm|JYBHEDWB6X]].
Another proof takes a vertex $x$ that is not integral and uses a tight odd set constraint to split the graph into two smaller graphs, then applies induction.

Example: let $G$ be two disjoint triangles, with $x_e = 1/2$ on every edge.
Then $x(\delta(v)) = 1$ for every vertex, but for $U$ the vertex set of one triangle, $x(\delta(U)) = 0 < 1$.
Indeed $G$ has no perfect matching, and the odd set constraints are needed to exclude this $x$.
If $G$ is bipartite, the constraints with $\abs{U} \ge 3$ are not needed, and the degree constraints alone give the polytope, as in Birkhoff's theorem on doubly stochastic matrices.

## Explanations

### L1 human

Each matching of a graph can be written as a list of zeros and ones, one entry per edge.
These lists are the corners of a geometric solid, the matching polytope.
The theorem describes the solid by simple linear inequalities.
Besides the obvious ones, each vertex is used at most once, one needs a rule for each odd set of vertices.
This makes it possible to optimize over matchings with the tools of linear programming.

### L2 human

The theorem is a basic result of [[polyhedral combinatorics|DKNC3NS0YH]].
Its number of inequalities is exponential, yet weighted matching can be solved in polynomial time by the weighted blossom algorithm.
The odd set constraints can also be separated in polynomial time, by a minimum odd cut computation due to Padberg and Rao.
With the ellipsoid method, this gives a second polynomial-time approach.
The degree constraints alone give the right polytope for bipartite graphs, because their constraint matrix is totally unimodular.
For general graphs that matrix is not totally unimodular, and the odd set constraints repair the defect.
