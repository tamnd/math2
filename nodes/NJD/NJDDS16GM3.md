---
tag: NJDDS16GM3
kind: definition
name: Lie algebra
msc: [17B05, 17B01]
defines: 5JJYBJ6A8K
uses: [04C5ZBG1WT, 000AYPA9AJ, 0443XNARDV]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebra
    locator: Definition
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]].
A *Lie algebra* over $k$ is a [[vector space|000AYPA9AJ]] $\mathfrak g$ over $k$ together with a [[bilinear map|0443XNARDV]] $[\cdot, \cdot] \colon \mathfrak g \times \mathfrak g \to \mathfrak g$, called the *Lie bracket*, such that:

1. $[x, x] = 0$ for all $x \in \mathfrak g$.
2. $[x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0$ for all $x, y, z \in \mathfrak g$ (the Jacobi identity).

## Remarks

Example: $\R^3$ with the cross product $[x, y] = x \times y$ is a real Lie algebra.
The cross product is bilinear and $x \times x = 0$.
The Jacobi identity follows from the rule $x \times (y \times z) = (x \cdot z)\, y - (x \cdot y)\, z$: summing over the three cyclic permutations, the six terms cancel in pairs.

Non-example: $\R$ with the bracket $[x, y] = xy$ is bilinear, but it fails clause 1, since $[1, 1] = 1 \ne 0$.

Clause 1 and bilinearity give anticommutativity, $[x, y] = -[y, x]$, by expanding $[x + y, x + y] = 0$.
If the characteristic of $k$ is not $2$, anticommutativity implies clause 1.
The same definition with a commutative ring in place of $k$ and a module in place of the vector space gives Lie algebras over a commutative ring.
Lie algebras are usually written in Fraktur letters such as $\mathfrak g$, $\mathfrak h$ and $\mathfrak{sl}_2$.
