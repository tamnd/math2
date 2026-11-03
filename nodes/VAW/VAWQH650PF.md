---
tag: VAWQH650PF
kind: definition
name: Structurable algebra
msc: [17A30, 17C50, 17B60]
defines: 8RF5HXXHNY
uses: [04C5ZBG1WT, YP5TQ6WFVN, 7W52X4N3NJ, 6C2MCVB8C7]
sources:
  - url: https://en.wikipedia.org/wiki/Structurable_algebra
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] of characteristic $0$, and let $A$ be a finite-dimensional [[nonassociative|YP5TQ6WFVN]] algebra over $F$ with a unit element.
An *involution* of $A$ is a linear map $x \mapsto \bar{x}$ with $\bar{\bar{x}} = x$ and $\overline{xy} = \bar{y}\, \bar{x}$ for all $x, y \in A$.
For $x, y, z \in A$ put $\set{x, y, z} = (x \bar{y}) z + (z \bar{y}) x - (z \bar{x}) y$, and let $V_{x, y}$ be the map $z \mapsto \set{x, y, z}$.
The pair $(A, \bar{\ })$ is a *structurable algebra* if:

1. $x \mapsto \bar{x}$ is an involution of $A$;
2. $[V_{x, y}, V_{z, w}] = V_{\set{x, y, z}, w} - V_{z, \set{y, x, w}}$ for all $x, y, z, w \in A$.

Here $[S, T] = ST - TS$ is the commutator of linear maps.

## Remarks

Example: a unital associative algebra with an involution, such as $M_n(F)$ with the transpose.
Then $\set{x, y, z} = x \bar{y} z + z \bar{y} x - z \bar{x} y$, and clause 2 is checked by expanding both sides applied to a fifth element into associative words.

Example: a unital [[Jordan algebra|6C2MCVB8C7]] with the identity map as involution.
Clause 1 holds because the product is commutative, and $\set{x, y, z}$ becomes the Jordan triple product $(xy)z + (zy)x - (zx)y$.

Non-example: the octonions with the identity map fail clause 1, since $\overline{xy} = xy$ differs from $\bar{y}\, \bar{x} = yx$ for noncommuting $x$ and $y$.
With the octonion conjugation instead, the octonions form a structurable algebra.

The [[rings with involution|7W52X4N3NJ]] give the associative examples.
