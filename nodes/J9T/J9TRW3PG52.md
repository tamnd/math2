---
tag: J9TRW3PG52
kind: definition
name: Invariant bilinear form
msc: [17B05, 17B20]
defines: GMB9ANSTT1
uses: [5JJYBJ6A8K, 0SQZMXB6GP, G8FEGYDSNE, TZAZ163QGK]
sources:
  - url: https://en.wikipedia.org/wiki/Killing_form
---

## Definition

Let $\mathfrak g$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $k$, and let $B \colon \mathfrak g \times \mathfrak g \to k$ be a [[bilinear form|0SQZMXB6GP]].
The form $B$ is *invariant* if
$$B([x, y], z) = B(x, [y, z]) \quad \text{for all } x, y, z \in \mathfrak g.$$

## Remarks

Using $[x, y] = -[y, x]$, the condition is equivalent to $B([y, x], z) + B(x, [y, z]) = 0$ for all $x, y, z$.
In other words, each $\operatorname{ad} y$ is skew-adjoint for $B$.
Some authors call such forms associative.
More generally, a bilinear form $B$ on a [[representation|TZAZ163QGK]] $V$ of $\mathfrak g$ is invariant if $B(x \cdot u, v) + B(u, x \cdot v) = 0$ for all $x \in \mathfrak g$ and $u, v \in V$.

Example: the trace form $B(x, y) = \tr(xy)$ on the [[general linear Lie algebra|G8FEGYDSNE]] $\mathfrak{gl}_n(k)$.
Indeed $\tr([x, y] z) = \tr(xyz) - \tr(yxz)$, and $\tr(yxz) = \tr(xzy)$ by cyclicity, so $\tr([x, y] z) = \tr(x(yz - zy)) = \tr(x [y, z])$.

Non-example: on the two-dimensional Lie algebra with basis $x, y$ and $[x, y] = y$, let $B$ be the symmetric form with $B(y, y) = 1$ and $B(x, x) = B(x, y) = 0$.
Then $B([x, y], y) = B(y, y) = 1$, while $B(x, [y, y]) = B(x, 0) = 0$, so $B$ is not invariant.

The radical $\set{x : B(x, y) = 0 \text{ for all } y}$ of an invariant form is an ideal of $\mathfrak g$.
