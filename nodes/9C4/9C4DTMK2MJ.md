---
tag: 9C4DTMK2MJ
kind: definition
name: Jordan pair
msc: [17C50, 17A40]
defines: CDN2B4S8YW
uses: [04C5ZBG1WT, 000AYPA9AJ, M13DZ6YXH1]
sources:
  - url: https://en.wikipedia.org/wiki/Triple_system
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] of characteristic different from $2$, and let $V^+$ and $V^-$ be [[vector spaces|000AYPA9AJ]] over $F$.
For a sign $\sigma \in \set{+, -}$, write $-\sigma$ for the other sign.
A *Jordan pair* structure on $(V^+, V^-)$ is a pair of trilinear maps $V^\sigma \times V^{-\sigma} \times V^\sigma \to V^\sigma$, for $\sigma = \pm$, both written $(x, y, z) \mapsto \set{x, y, z}$.
The conditions are, for each $\sigma$ and all $u, x, z \in V^\sigma$ and $v, y \in V^{-\sigma}$:

1. $\set{x, y, z} = \set{z, y, x}$;
2. $\set{u, v, \set{x, y, z}} = \set{\set{u, v, x}, y, z} - \set{x, \set{v, u, y}, z} + \set{x, y, \set{u, v, z}}$.

In clause 2, the inner product $\set{v, u, y}$ is the one on $V^{-\sigma}$.

## Remarks

Example: $V^+$ the $p \times q$ matrices and $V^-$ the $q \times p$ matrices over $F$, with $\set{x, y, z} = xyz + zyx$ on both sides.
Clause 1 holds by the form of the formula, and clause 2 follows by expanding both sides into products of five matrices.

Example: a [[Jordan triple system|M13DZ6YXH1]] $V$ gives the Jordan pair $(V, V)$, with the same triple product on both sides.

Non-example: the same two matrix spaces with $\set{x, y, z} = xyz$ fail clause 1, since $xyz \ne zyx$ in general.
