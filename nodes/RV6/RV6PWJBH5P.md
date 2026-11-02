---
tag: RV6PWJBH5P
kind: statement
role: theorem
name: Almgren's regularity theorem
msc: [49Q15, 49Q05, 53A10]
uses: [EG4AJVEFT2, 4NKP73KVVW, SSNFTHZ6YJ, 7CBT4SM83Y]
about: [4NKP73KVVW]
sources:
  - url: https://en.wikipedia.org/wiki/Almgren_regularity_theorem
same_as:
  wikidata: Q4733800
  wikipedia: Almgren regularity theorem
---

## Statement

Let $m \ge 2$ and $n \ge 1$ be integers.
Let $M$ be a smooth [[Riemannian manifold|7CBT4SM83Y]] of dimension $m + n$, and let $T$ be an $m$-dimensional [[integral current|EG4AJVEFT2]] in $M$ that is [[area-minimizing|4NKP73KVVW]].
Let $\operatorname{sing} T$ be the set of points of the support of $T$, outside the support of its boundary, with this property.
Near the point, the support of $T$ is not a smooth embedded submanifold.
Then the [[Hausdorff dimension|SSNFTHZ6YJ]] of $\operatorname{sing} T$ is at most $m - 2$.

## Remarks

Frederick Almgren proved the theorem in a very long work that was published in 2000, after his death.
Camillo De Lellis and Emanuele Spadaro later gave a shorter proof.
The proof studies blow-ups at points where the tangent cone is a plane with integer multiplicity $Q \ge 2$.
Near such points the current is approximated by the graph of a $Q$-valued function that minimizes a Dirichlet energy.
A frequency function controls the rate at which the current departs from the plane.
The bound $m - 2$ is sharp in higher codimension.
By Wirtinger's inequality, complex algebraic curves in $\C^2 = \R^4$ are area-minimizing, and the curve $\set{(z, w) : z^2 = w^3}$ has a singular point at the origin, a set of dimension $0 = 2 - 2$.
In codimension $n = 1$ the singular set is much smaller: its dimension is at most $m - 7$, by the work of Federer and Simons.

## Explanations

### L1 human

An area-minimizing surface of any dimension, in a space of any dimension, can have singular points where it is not smooth.
Almgren's theorem says that these singular points form a set that is small: two dimensions smaller than the surface itself.
For two-dimensional surfaces, the singular points are isolated, as for complex curves crossing themselves.

### L2 human

In codimension one, regularity follows from De Giorgi's excess-decay method, because the tangent planes have multiplicity one.
In higher codimension a tangent plane can carry multiplicity, so branching phenomena occur, and De Giorgi's method no longer applies.
Almgren's theorem handles this with $Q$-valued functions and the frequency function, tools that have since spread to free boundary problems.
