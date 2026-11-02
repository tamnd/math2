---
tag: FRFYHJGAN3
kind: object
name: Simplex category
msc: [18N50, 55U10]
instance_of: [A2DE66937D]
uses: [0A7KV2WB7A, 0FRXBVVR03]
sources:
  - url: https://en.wikipedia.org/wiki/Simplex_category
same_as:
  wikidata: Q10906333
  wikipedia: Simplex category
---

## Description

For each natural number $n$, let $[n]$ be the [[totally ordered|0FRXBVVR03]] set $\set{0, 1, \dots, n}$ with the usual order.
The *simplex category* $\Delta$ has the sets $[n]$ for $n \ge 0$ as objects.
A morphism $[m] \to [n]$ is an order-preserving ([[monotone|0A7KV2WB7A]]) map, that is, a map $f$ with $f(i) \le f(j)$ whenever $i \le j$.
Composition is the composition of maps.
A composite of order-preserving maps is order-preserving, and identity maps are order-preserving, so $\Delta$ is a [[category|A2DE66937D]].

## Remarks

Every morphism of $\Delta$ is a composite of two kinds of basic maps.
The face map $\delta_i \colon [n-1] \to [n]$, for $0 \le i \le n$, is the injective order-preserving map whose image misses $i$.
The degeneracy map $\sigma_i \colon [n+1] \to [n]$, for $0 \le i \le n$, is the surjective order-preserving map that takes the value $i$ twice.
For example, the map $[2] \to [1]$ with $0 \mapsto 0$, $1 \mapsto 0$, $2 \mapsto 1$ is $\sigma_0$.
One pictures $[n]$ as the standard $n$-simplex with vertices $0, \dots, n$: face maps include a face, and degeneracy maps collapse an edge.
Functors from the opposite category $\Delta^{\mathrm{op}}$ are the [[simplicial objects|WK0A32TZHB]], and functors $\Delta^{\mathrm{op}} \to \mathbf{Set}$ are the [[simplicial sets|WW81ARB8K9]].

## Explanations

### L1 human

The simplex category is a small list of shapes: a point, an edge, a triangle, a tetrahedron, and so on.
The arrows between shapes say how one shape sits in another as a face, or how a shape can be squashed onto a smaller one.
For example, there are two maps $[0] \to [1]$, which pick the two endpoints of an edge, and three maps $[1] \to [1]$: the identity and the two constant maps.
