---
tag: WVZ7F41S9Q
kind: definition
name: Medial magma
msc: [20N02, 20N05]
defines: VZHN6GA3TA
uses: [9689SFPVE9]
sources:
  - url: https://en.wikipedia.org/wiki/Medial_magma
---

## Definition

Let $(M, \cdot)$ be a [[magma|9689SFPVE9]].
It is *medial* if
$$(x \cdot y) \cdot (u \cdot v) = (x \cdot u) \cdot (y \cdot v)$$
for all $x, y, u, v \in M$.

## Remarks

Example: $\Q$ with $x \circ y = (x + y)/2$.
Both $(x \circ y) \circ (u \circ v)$ and $(x \circ u) \circ (y \circ v)$ equal $(x + y + u + v)/4$.
This magma is medial but not associative.

Example: every commutative semigroup is medial, since $(xy)(uv) = x(yu)v = x(uy)v = (xu)(yv)$.

Non-example: $\Z$ with $x \cdot y = xy + 1$.
Take $x = y = 1$ and $u = v = 0$.
Then $1 \cdot 1 = 2$ and $0 \cdot 0 = 1$, so the left side is $2 \cdot 1 = 3$.
Also $1 \cdot 0 = 1$, so the right side is $1 \cdot 1 = 2 \ne 3$.

A magma is medial if and only if the map $M \times M \to M$, $(x, y) \mapsto x \cdot y$, is a homomorphism from the product magma $M \times M$ to $M$.
