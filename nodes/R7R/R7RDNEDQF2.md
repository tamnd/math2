---
tag: R7RDNEDQF2
kind: definition
name: Unital magma
msc: [20N02]
defines: KNDSJAYMSY
uses: [9689SFPVE9, 07WYQPB8E3]
sources:
  - url: https://en.wikipedia.org/wiki/Magma_(algebra)
---

## Definition

Let $(M, \cdot)$ be a [[magma|9689SFPVE9]].
It is a *unital magma* if there is an element $e \in M$ with $e \cdot x = x$ and $x \cdot e = x$ for all $x \in M$.
Such an $e$ is an [[identity element|07WYQPB8E3]] of $M$.

## Remarks

The identity is unique: if $e$ and $e'$ are identities, then $e = e \cdot e' = e'$.

Example: the set $\set{e, a, b}$ with $e \cdot x = x \cdot e = x$ for all $x$ and $u \cdot v = e$ for $u, v \in \set{a, b}$.
Both identity equations hold by construction, so this is a unital magma.
It is not associative: $(a \cdot a) \cdot b = e \cdot b = b$, but $a \cdot (a \cdot b) = a \cdot e = a$.

Non-example: $(\Z, -)$ has no identity.
If $e$ were an identity, then $e - x = x$ for all $x \in \Z$, so $e = 2x$ for every $x$, which is impossible.

In Mathlib the class `MulOneClass` is a unital magma written multiplicatively.
