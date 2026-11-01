---
tag: G2RYQMGG1R
kind: conjecture
name: Cycle double cover conjecture
msc: [05C38, 05C70]
uses: [00C0BR7D7H, 0Z05VCBQ7Y, 0BANA3XYPF]
about: [0Z05VCBQ7Y]
sources:
  - url: https://en.wikipedia.org/wiki/Cycle_double_cover
history:
  posed_by: "George Szekeres and Paul Seymour"
---

## Statement

Let $G$ be a finite [[graph|00C0BR7D7H]], possibly with multiple edges, that has no [[bridge|0BANA3XYPF]].
The conjecture: there is a finite list of [[cycles|0Z05VCBQ7Y]] of $G$ such that each edge of $G$ lies in exactly two cycles of the list.
The list may contain a cycle more than once.
Such a list is called a cycle double cover of $G$.

## Remarks

The conjecture is open.
It was posed by Szekeres and, independently, by Seymour.
The hypothesis is necessary: a bridge lies on no cycle, so a graph with a bridge has no cycle double cover.
For a bridgeless planar graph, each face boundary of a plane embedding splits into edge-disjoint cycles, and each edge lies on exactly two faces.
So these cycles form a cycle double cover.
The general case reduces to cubic bridgeless graphs, and further to snarks, the cubic bridgeless graphs with no proper edge colouring with $3$ colours.
If a cubic graph has a proper edge colouring with $3$ colours, the unions of two colour classes give three families of disjoint cycles, which together cover each edge twice.

## Explanations

### L1 human

Take a network with no single link whose removal disconnects it.
The conjecture says that one can choose a collection of closed loops in the network that passes over every link exactly twice.
For a map drawn in the plane, the borders of the countries do this.
For general networks, nobody knows a proof, and nobody has found a counterexample.
