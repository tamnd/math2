---
tag: 1NX95TTMFT
kind: definition
name: Semisimple Lie group
msc: ["22E46", "22E15", "22E10"]
defines: XJS07AJ50Y
uses: [7JBRGCVJRB]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_Lie_group
---

## Definition

Let $G$ be a connected real or complex [[Lie group|7JBRGCVJRB]], and let $\mathfrak{g}$ be its [[Lie algebra|WKVBS76432]].
The group $G$ is a *semisimple Lie group* if $\mathfrak{g}$ is a [[semisimple Lie algebra|EY9DN7QAX1]], that is, the only solvable ideal of $\mathfrak{g}$ is $0$.

## Remarks

Let $\mathfrak{g}$ be a finite-dimensional Lie algebra over a field of characteristic $0$.
The following are equivalent:

1. the only solvable ideal of $\mathfrak{g}$ is $0$;
2. $\mathfrak{g}$ is a direct sum of simple ideals;
3. the Killing form $B(x, y) = \tr(\operatorname{ad} x \operatorname{ad} y)$ is nondegenerate (Cartan's criterion).

Example: $G = SO(4)$.
Its Lie algebra $\mathfrak{so}(4)$ is isomorphic to $\mathfrak{so}(3) \oplus \mathfrak{so}(3)$, a direct sum of two simple ideals, so $G$ is semisimple.
It is not simple, since each summand is a proper nonzero ideal.

Non-example: $G = GL_n(\R)^+$, the invertible real $n \times n$ matrices with positive determinant, for $n \ge 1$.
Its Lie algebra $\mathfrak{gl}_n(\R)$ contains the ideal $\R I_n$ of scalar matrices, which is abelian, hence solvable, and nonzero.
So the condition fails.

Some authors do not require $G$ to be connected and ask only that $\mathfrak{g}$ be semisimple; some also ask for a finite centre.
