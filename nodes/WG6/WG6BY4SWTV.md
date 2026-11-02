---
tag: WG6BY4SWTV
kind: definition
name: Positive cone
msc: ["46A40", "06F20"]
defines: Z344RY5XX1
uses: [05EGHEQZAW, 011C29Q1S1, 0880F9EQCP]
sources:
  - url: https://en.wikipedia.org/wiki/Ordered_vector_space
---

## Definition

Let $V$ be a real [[vector space|05EGHEQZAW]].
A *positive cone* in $V$ is a subset $P \subseteq V$ such that:

1. $x + y \in P$ for all $x, y \in P$;
2. $\lambda x \in P$ for all $x \in P$ and all real $\lambda \ge 0$;
3. $P \cap (-P) = \set{0}$.

## Remarks

A positive cone $P$ defines a [[partial order|011C29Q1S1]] on $V$ by $x \le y \iff y - x \in P$.
This order satisfies $x \le y \implies x + z \le y + z$ and $x \le y \implies \lambda x \le \lambda y$ for $\lambda \ge 0$, and $P = \set{x : 0 \le x}$.
Conversely, for each partial order with these two properties, the set $\set{x : 0 \le x}$ is a positive cone.
Example: $P = \set{x \in \R^n : x_i \ge 0 \text{ for all } i}$ is a positive cone, and it gives the componentwise order.
Example: the [[positive semidefinite matrices|0880F9EQCP]] form a positive cone in the space of real symmetric $n \times n$ matrices.
Non-example: the half-plane $\set{(x, y) \in \R^2 : y \ge 0}$ satisfies clauses 1 and 2, but contains $(1, 0)$ and $(-1, 0)$, so it fails clause 3.
Some authors drop clause 3 and call $P$ a *wedge* or a convex cone; then the relation $\le$ is only a preorder.
