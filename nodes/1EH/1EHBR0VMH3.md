---
tag: 1EHBR0VMH3
kind: definition
name: Busemann G-space
msc: [53C70, 51F99]
defines: EKXQFD7EMF
uses: [063W5JMY85, 0Z4V98VN5E, 0DC3MPR7C9]
sources:
  - url: https://en.wikipedia.org/wiki/Busemann_G-space
---

## Definition

Let $(X, d)$ be a [[metric space|063W5JMY85]].
For points $x, y, z \in X$, say that $y$ lies *between* $x$ and $z$ when $y \ne x$, $y \ne z$ and $d(x, y) + d(y, z) = d(x, z)$.
The space $X$ is a *Busemann G-space* when it satisfies these four conditions.

1. Finite compactness: every bounded closed subset of $X$ is compact.
2. Menger convexity: for all distinct $x, z \in X$ there is a point between $x$ and $z$.
3. Local prolongability: each $p \in X$ has a radius $r_p > 0$ with this property. For distinct $x, y$ in the [[open ball|0DC3MPR7C9]] $B(p, r_p)$, some $z \in X$ has $y$ between $x$ and $z$.
4. Uniqueness of prolongation: if $y$ lies between $x$ and $z_1$ and between $x$ and $z_2$, and $d(y, z_1) = d(y, z_2)$, then $z_1 = z_2$.

## Remarks

Condition 1 says that $X$ is a [[proper metric space|0Z4V98VN5E]].
Example: the Euclidean plane $\R^2$.
It is proper, the midpoint lies between any two distinct points, and a segment from $x$ through $y$ extends along its line.
The extension of length $t$ beyond $y$ is unique, since equality in the triangle inequality forces $z$ onto the ray from $x$ through $y$.

Non-example: $\R^2$ with the taxicab distance $d_1$ fails condition 4.
Take $x = (0, 0)$, $y = (1, 0)$, $z_1 = (2, 0)$ and $z_2 = (\frac{3}{2}, \frac{1}{2})$.
Then $d_1(y, z_1) = d_1(y, z_2) = 1$ and $d_1(x, z_1) = d_1(x, z_2) = 2$, so $y$ lies between $x$ and both points, but $z_1 \ne z_2$.
