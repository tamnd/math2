---
tag: WTCP8A87P1
kind: counterexample
name: Borsuk's conjecture
msc: [52A20, 52C17]
uses: [0KW3PN547K, QHJ0GBQE2E, 0BF2DE2SYK]
sources:
  - url: https://en.wikipedia.org/wiki/Borsuk%27s_conjecture
same_as:
  wikidata: Q894242
  wikipedia: Borsuk's conjecture
---

## Counterexample

Borsuk's conjecture concerns bounded sets $S \subseteq \R^n$ with more than one point, for $n \ge 1$.
It says that every such $S$ can be split into $n + 1$ sets, each of smaller [[diameter|0KW3PN547K]] than $S$.
The conjecture is false.
Kahn and Kalai proved this in 1993.
For all large $n$, they found finite sets in $\R^n$ that cannot be split into fewer than $1.2^{\sqrt{n}}$ parts of smaller diameter.
This number exceeds $n + 1$ for large $n$.

Their sets consist of the matrices $x x^T$, for $x$ in a suitable family of vectors in $\set{-1, 1}^m$.
These matrices are viewed as points of $\R^{m \times m}$ with the Euclidean norm.
For two such vectors, $\norm{x x^T - y y^T}^2 = 2 m^2 - 2 (x \cdot y)^2$.
So the diameter is attained exactly by the pairs with $x \cdot y = 0$, and a part of smaller diameter contains no orthogonal pair.
The Frankl–Wilson theorem shows that such parts are exponentially small in $m$.
So exponentially many parts are needed, while the dimension is only of order $m^2$.

## Remarks

The conjecture is true for $n = 2$ and $n = 3$, and for smooth convex bodies in every dimension.
The number $n + 1$ cannot be lowered: by the [[Borsuk–Ulam theorem|QHJ0GBQE2E]], the unit ball of $\R^n$ cannot be split into $n$ closed sets of smaller diameter.
Later work lowered the dimension of counterexamples; the smallest dimension known to admit a counterexample is $64$, found by Jenrich and Brouwer.
The vector $x x^T$ is the [[tensor product|0BF2DE2SYK]] $x \otimes x$, and the formula above uses $\norm{x \otimes x}^2 = \abs{x}^4 = m^2$ and $\langle x \otimes x, y \otimes y \rangle = (x \cdot y)^2$.

## Explanations

### L1 human

Borsuk asked whether any shape in $n$-dimensional space can be cut into $n + 1$ pieces that are all strictly smaller across.
In the plane a disc can be cut into three such pieces, and three is needed.
For a long time people believed this in every dimension.
In 1993 Kahn and Kalai found strange high-dimensional point sets where far more pieces are needed, so the conjecture fails.
