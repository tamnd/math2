---
tag: VGJRRCKZ0S
kind: definition
name: Vector optimization
msc: [90C29, 90C46]
defines: RK115S1G5T
uses: [6VE4KA12VD, HHMS3WH9T7, 0QV2JS9RJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_optimization
---

## Definition

Let $Z$ be a real vector space and let $C \subseteq Z$ be a [[convex cone|6VE4KA12VD]] that is pointed, that is, $C \cap (-C) = \set{0}$, and contains $0$.
For $y, y' \in Z$, write $y \le_C y'$ if $y' - y \in C$.
This is a [[partial order|0QV2JS9RJ3]] on $Z$ compatible with the vector operations.
Let $X$ be a nonempty set and $F \colon X \to Z$.
A *vector optimization problem* is the problem of minimizing $F$ over $X$ with respect to $\le_C$.
A point $x^* \in X$ is an *efficient* (or *minimal*) point if there is no $x \in X$ with $F(x) \le_C F(x^*)$ and $F(x) \ne F(x^*)$.
Equivalently, $(F(x^*) - C) \cap F(X) = \set{F(x^*)}$.

## Remarks

The pair $(Z, \le_C)$ is an [[ordered vector space|HHMS3WH9T7]].
When $C$ has nonempty interior, $x^*$ is *weakly efficient* if no $x \in X$ has $F(x^*) - F(x)$ in the interior of $C$.

Example: $Z = \R^k$ and $C = \R^k_{\ge 0} = \set{y : y_i \ge 0 \text{ for all } i}$.
Then $y \le_C y'$ means $y_i \le y'_i$ for all $i$, and the efficient points are the Pareto optimal points of multi-objective optimization.

Example: $Z = \R^2$ and $C = \set{(a, b) : a \ge 0, \ a + b \ge 0}$.
This cone is convex and pointed and contains $\R^2_{\ge 0}$, so fewer pairs are incomparable than in the Pareto order.

Non-example: for $C = \R^2$ the relation $\le_C$ holds between all pairs, and it is not antisymmetric, since $C$ is not pointed.
Then, if $F(X)$ has at least two points, no point of $X$ is efficient.
