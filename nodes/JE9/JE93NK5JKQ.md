---
tag: JE93NK5JKQ
kind: definition
name: Nilpotent Lie algebra
msc: [17B30]
defines: MEJ9PGMJ9H
uses: [5JJYBJ6A8K, 3Z22XPB6H5, W7A2R0GR3T, HBVZGRKCWQ]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_Lie_algebra
---

## Definition

Let $\mathfrak g$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $k$, with [[lower central series|3Z22XPB6H5]] $\mathfrak g^1 = \mathfrak g$ and $\mathfrak g^{i+1} = [\mathfrak g, \mathfrak g^i]$.
The Lie algebra $\mathfrak g$ is *nilpotent* if $\mathfrak g^n = 0$ for some $n \ge 1$.

## Remarks

Equivalently, there is $n$ such that $[x_1, [x_2, [\cdots [x_{n-1}, x_n] \cdots]]] = 0$ for all $x_1, \dots, x_n \in \mathfrak g$.
Abelian Lie algebras are nilpotent, with $\mathfrak g^2 = 0$.
By induction, the derived series satisfies $\mathfrak g^{(i)} \subseteq \mathfrak g^{i+1}$, so a nilpotent Lie algebra is [[solvable|W7A2R0GR3T]].

Example: the [[Heisenberg algebra|HBVZGRKCWQ]] with basis $x, y, z$, $[x, y] = z$ and $z$ central.
Here $\mathfrak g^2 = kz$ and $\mathfrak g^3 = 0$.

Non-example: the two-dimensional Lie algebra with basis $x, y$ and $[x, y] = y$.
Here $\mathfrak g^2 = ky$ and $\mathfrak g^3 = [\mathfrak g, ky] = ky$ because $[x, y] = y$, so $\mathfrak g^i = ky$ for all $i \ge 2$.
This algebra is solvable but not nilpotent.
