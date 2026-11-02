---
tag: XHWA2TEC7X
kind: statement
role: theorem
name: Beckman–Quarles theorem
msc: [51K05, 51M05]
uses: [0XPR1E85W0, 0NPPGHQNXQ, 02HPP5VCZH]
about: [02HPP5VCZH]
sources:
  - url: https://en.wikipedia.org/wiki/Beckman%E2%80%93Quarles_theorem
same_as:
  wikidata: Q2226606
  wikipedia: Beckman–Quarles theorem
---

## Statement

Let $n \ge 2$ and let $f \colon \R^n \to \R^n$ be any map.
Assume that for all $x, y \in \R^n$ with $\norm{x - y} = 1$ one has $\norm{f(x) - f(y)} = 1$.
Then $f$ is an isometry: $\norm{f(x) - f(y)} = \norm{x - y}$ for all $x, y \in \R^n$.

## Remarks

No continuity, injectivity or surjectivity of $f$ is assumed; preserving the single distance $1$ is enough.
The theorem was published by F. S. Beckman and D. A. Quarles in 1953.
The proof uses rigid configurations made of unit segments, such as unit equilateral triangles and simplices.
They show that $f$ also preserves other distances, and then that it preserves all distances.
Since an isometry of [[Euclidean space|0XPR1E85W0]] is affine, $f$ is then of the form $x \mapsto Ax + b$ with $A$ orthogonal.

The hypothesis $n \ge 2$ is necessary.
On $\R$, let $h \colon [0, 1) \to [0, 1)$ be any bijection, for instance $h(t) = t^2$, and set $f(x) = \floor{x} + h(x - \floor{x})$.
If $\abs{x - y} = 1$, then $x$ and $y$ have the same fractional part and their integer parts differ by $1$, so $\abs{f(x) - f(y)} = 1$.
But $f(0) = 0$ and $f(1/2) = 1/4$, so $f$ is not an [[isometry|02HPP5VCZH]].

## Explanations

### L1 human

Suppose a map of the plane keeps every pair of points at distance $1$ at distance $1$.
Nothing is said about other distances, and the map need not even be continuous.
The theorem says that the map must then keep all distances, so it is just a rigid motion.
In the plane, unit triangles and other rigid unit frameworks lock everything in place.

### L2 human

The theorem is a rigidity result in [[Euclidean distance|0NPPGHQNXQ]] geometry: one preserved distance forces the whole metric to be preserved.
It contrasts with the classical characterization of isometries, which assumes that all distances are preserved.
It is connected with unit distance graphs: a unit-distance-preserving map is a graph homomorphism of the unit distance graph of $\R^n$ to itself.
The one-dimensional counterexample shows that the plane's richer supply of unit triangles is what makes the result work.
