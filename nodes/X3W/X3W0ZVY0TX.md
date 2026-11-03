---
tag: X3W0ZVY0TX
kind: definition
name: Poisson algebra
msc: [17B63, 53D17]
defines: 45VKBM65QZ
uses: [3CTW1P4HBP, 5JJYBJ6A8K, 3J89REV9WQ]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_algebra
---

## Definition

Let $k$ be a field.
Let $P$ be a vector space over $k$ with two bilinear maps $P \times P \to P$, a product $(a, b) \mapsto ab$ and a bracket $(a, b) \mapsto \set{a, b}$.
Then $P$ is a *Poisson algebra* over $k$ if:

1. the product makes $P$ an [[associative algebra|3CTW1P4HBP]] over $k$;
2. the bracket makes $P$ a [[Lie algebra|5JJYBJ6A8K]] over $k$;
3. $\set{a, bc} = \set{a, b} c + b \set{a, c}$ for all $a, b, c \in P$ (Leibniz rule).

## Remarks

Clause 3 says that each map $b \mapsto \set{a, b}$ is a [[derivation|3J89REV9WQ]] of the associative product.
Many authors, especially in geometry, also require the product to be commutative.

Example: $P = \R[x, y]$, or the smooth functions on $\R^2$, with the usual product and $\set{f, g} = \frac{\partial f}{\partial x}\frac{\partial g}{\partial y} - \frac{\partial f}{\partial y}\frac{\partial g}{\partial x}$.
The bracket is antisymmetric and satisfies the Jacobi identity, and the product rule for derivatives gives $\set{f, gh} = \set{f, g} h + g \set{f, h}$.
Another example: every associative algebra with the commutator $\set{a, b} = ab - ba$ is a Poisson algebra, since $a(bc) - (bc)a = (ab - ba)c + b(ac - ca)$.

Non-example: $P = k[x]$ with the usual product and the bracket $\set{f, g} = f g' - g f'$, where $'$ is the derivative.
This bracket is a Lie bracket, but clause 3 fails.
With $b = c = 1$, clause 3 would give $\set{a, 1} = 2\set{a, 1}$, so $\set{a, 1} = 0$; yet $\set{x, 1} = x \cdot 0 - 1 \cdot 1 = -1$.
