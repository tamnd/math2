---
tag: XY6CJMDY5M
kind: definition
name: Automorphism
msc: [08A35, 03C07]
defines: DSQ17TNW1C
uses: [983GZBQYT4, PZMGQMDN25]
sources:
  - url: https://en.wikipedia.org/wiki/Automorphism
---

## Definition

Let $\mathbf{A}$ be a [[structure|983GZBQYT4]] for a signature $\sigma$.
An *automorphism* of $\mathbf{A}$ is an [[isomorphism|PZMGQMDN25]] from $\mathbf{A}$ to $\mathbf{A}$.
The set of automorphisms of $\mathbf{A}$ is written $\Aut(\mathbf{A})$.

## Remarks

Example: the map $z \mapsto \bar{z}$ is an automorphism of the field $(\C, +, \cdot, 0, 1)$, because it is a bijection of $\C$ to itself with $\overline{z + w} = \bar{z} + \bar{w}$, $\overline{zw} = \bar{z}\,\bar{w}$, $\bar{0} = 0$ and $\bar{1} = 1$.

Non-example: the map $x \mapsto 2x$ on $(\Z, +, 0)$ is an injective homomorphism but not an automorphism, because it is not surjective: $1$ is not in its image.

The set $\Aut(\mathbf{A})$ is a group under composition, with the identity map as identity element.
The only automorphism of the field $\R$ is the identity.
