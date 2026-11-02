---
tag: D39NBQH3H6
kind: statement
role: theorem
name: Euler's formula for polytopes
msc: [52B05, 52B11]
uses: [300K6CB1KH, 872BAKDQQK, RNDDWDAFJ5, 09HT3P35YP, 4WKHF5BCTA]
about: [872BAKDQQK, 300K6CB1KH]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_characteristic
---

## Statement

Let $P$ be a [[convex polytope|300K6CB1KH]] of dimension $d \ge 1$, with [[f-vector|872BAKDQQK]] $(f_0, \dots, f_{d-1})$.
Then
$$\sum_{i=0}^{d-1} (-1)^i f_i = f_0 - f_1 + f_2 - \cdots + (-1)^{d-1} f_{d-1} = 1 - (-1)^d.$$

## Remarks

With $f_{-1} = 1$ for the empty face and $f_d = 1$ for $P$, the relation reads $\sum_{i=-1}^{d} (-1)^i f_i = 0$.
One proof is topological: the boundary of $P$ is homeomorphic to the sphere $S^{d-1}$, and its faces form a cell decomposition.
So the alternating sum is the [[Euler characteristic|RNDDWDAFJ5]] $1 + (-1)^{d-1}$ of the sphere.
A combinatorial proof builds the boundary facet by facet in a shelling order and checks that the alternating sum changes correctly at each step.

For $d = 3$ the formula is [[Euler's polyhedron formula|09HT3P35YP]] $f_0 - f_1 + f_2 = 2$.
For $d = 4$ the alternating sum is $0$; the $4$-cube has $16 - 32 + 24 - 8 = 0$.
For a polygon with $n$ vertices, $n - n = 0 = 1 - (-1)^2$.

It is the only linear equation satisfied by the f-vectors of all $d$-polytopes, up to scaling.
For simplicial polytopes there are further linear relations, the [[Dehn–Sommerville equations|4WKHF5BCTA]].

## Explanations

### L1 human

Count the faces of each dimension of a convex polytope and add them with alternating signs.
The answer does not depend on the polytope, only on its dimension: it is $2$ in odd dimensions and $0$ in even dimensions.
In three dimensions this is the classical rule vertices minus edges plus faces equals $2$.

### L2 human

The relation $\sum (-1)^i f_i = 1 - (-1)^d$ is the Euler–Poincaré relation.
It is the first constraint any candidate f-vector must meet, and in dimension $3$ together with the inequalities $f_2 \le 2 f_0 - 4$ and $f_0 \le 2 f_2 - 4$ it characterises the f-vectors of $3$-polytopes.
Its proof by shellings was historically delicate: early arguments assumed that the boundary of a polytope can be shelled, which was proved only later by Bruggesser and Mani.
The same alternating sum, for general cell complexes, is the Euler characteristic of algebraic topology.
