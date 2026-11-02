---
tag: YW8HBW1GJX
kind: definition
name: Deformation retract
msc: [54C15, 55P10]
defines: CEK4SC20WK
uses: [9YA6S6HD9V, 0WS9P12FQR]
sources:
  - url: https://en.wikipedia.org/wiki/Retraction_(topology)
---

## Definition

Let $X$ be a topological space and let $A \subseteq X$ carry the [[subspace topology|0WS9P12FQR]].
The subspace $A$ is a *deformation retract* of $X$ if there is a [[homotopy|9YA6S6HD9V]] $H \colon X \times [0, 1] \to X$ such that:

1. $H(x, 0) = x$ for all $x \in X$;
2. $H(x, 1) \in A$ for all $x \in X$;
3. $H(a, 1) = a$ for all $a \in A$.

The subspace $A$ is a *strong deformation retract* of $X$ if moreover $H(a, t) = a$ for all $a \in A$ and $t \in [0, 1]$.

## Remarks

The map $r = H(\cdot, 1) \colon X \to A$ is a retraction, and the inclusion $i \colon A \to X$ is a [[homotopy equivalence|XZG6MTSWCN]] with homotopy inverse $r$.
Some textbooks, such as Hatcher's, use the name deformation retraction for the strong version.
Example: $S^{n-1}$ is a strong deformation retract of $\R^n \setminus \set{0}$, via $H(x, t) = (1 - t) x + t x / \norm{x}$; clause 3 holds since $\norm{a} = 1$ for $a \in S^{n-1}$.
Non-example: a point $p$ of the circle $S^1$ is not a deformation retract of $S^1$, since otherwise $S^1$ would be [[contractible|R5WP8Z69Q8]].
