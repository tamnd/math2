---
tag: DMXAX32B4R
kind: definition
name: Composition algebra
msc: [17A75]
defines: 1Q9G6AST10
uses: [1SENAHZW5A, 0RBQS1JJCR, 01NHFZF2SK]
sources:
  - url: https://en.wikipedia.org/wiki/Composition_algebra
---

## Definition

Let $K$ be a field and let $A$ be an [[algebra|1SENAHZW5A]] over $K$, not necessarily associative or unital.
Let $N \colon A \to K$ be a [[quadratic form|0RBQS1JJCR]] with polar form $b(x, y) = N(x + y) - N(x) - N(y)$.
The pair $(A, N)$ is a *composition algebra* if:

1. the bilinear form $b$ is [[nondegenerate|01NHFZF2SK]], and
2. $N(xy) = N(x) N(y)$ for all $x, y \in A$.

## Remarks

$N$ is called the norm of $A$.
A composition algebra with a unit is called a Hurwitz algebra or a unital composition algebra.
In a unital composition algebra each $x$ satisfies $x^2 - b(x, 1)x + N(x)1 = 0$.
Example: $\C$ over $\R$ with $N(z) = \abs{z}^2$; the polar form is $2\operatorname{Re}(z\bar{w})$, which is nondegenerate, and $\abs{zw}^2 = \abs{z}^2\abs{w}^2$.
Non-example: $\R^3$ with the cross product and $N(v) = v \cdot v$ fails clause 2, since $N(e_1 \times e_1) = 0$ while $N(e_1)N(e_1) = 1$.
Two unital composition algebras are isomorphic if and only if their norms are isometric.
