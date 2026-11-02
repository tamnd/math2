---
tag: Q93QR7EJKY
kind: definition
name: Near-ring
msc: [16Y30]
defines: ARAEEM8CVF
uses: [G5S1M9, 0V3CFG1KK9]
sources:
  - url: https://en.wikipedia.org/wiki/Near-ring
---

## Definition

A *(right) near-ring* is a set $N$ with two binary operations $+$ and $\cdot$ such that:

1. $(N, +)$ is a [[group|G5S1M9]], not necessarily abelian, with identity element $0$.
2. $(N, \cdot)$ is a [[semigroup|0V3CFG1KK9]]: $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ for all $a, b, c \in N$.
3. $(a + b) \cdot c = a \cdot c + b \cdot c$ for all $a, b, c \in N$.

## Remarks

A *left near-ring* asks instead $c \cdot (a + b) = c \cdot a + c \cdot b$; the two notions are mirror images.
Every ring is a near-ring.
Example: for a group $(G, +)$, let $M(G)$ be the set of all maps $G \to G$, with $(f + g)(x) = f(x) + g(x)$ and $f \cdot g = f \circ g$.
Clause 1 holds pointwise, clause 2 because composition is associative, and clause 3 because $((f + g) \circ h)(x) = f(h(x)) + g(h(x))$.
The other distributive law fails in $M(\Z)$: for the constant map $f = 1$, $f \circ (g + h) = 1$ but $f \circ g + f \circ h = 2$.
Non-example: $\N = \set{0, 1, 2, \ldots}$ with the usual operations satisfies clauses 2 and 3, but fails clause 1, since $1$ has no additive inverse.
