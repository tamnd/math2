---
tag: 3GZCWKX4A0
kind: concept
name: Lin–Kernighan heuristic
msc: [90C27, 90C59]
sources:
  - url: https://en.wikipedia.org/wiki/Lin%E2%80%93Kernighan_heuristic
same_as:
  wikidata: Q2835802
  wikipedia: Lin–Kernighan heuristic
---

## Summary

The Lin–Kernighan heuristic is a local search method for the symmetric [[travelling salesman problem|XJRHJX2241]], published by Shen Lin and Brian Kernighan in 1973.
It improves a tour by exchanges of a variable number of edges, built up one edge at a time while the total gain stays positive.
It gives no guarantee of optimality, but in practice it finds tours very close to optimal.
Its variants, such as Helsgaun's LKH, are among the best practical methods for large instances.

## Explanations

### L1 human

Start with any round trip through the cities.
A simple improvement removes two roads of the trip and reconnects the two pieces in the other possible way, if that is shorter.
Lin–Kernighan goes further: it removes a road, adds a shorter one, then removes and adds again, in a chain of any length.
It continues as long as the savings so far are positive, and keeps the best tour seen along the chain.
When no chain improves the tour, it stops at a tour that cannot be shortened by such moves.
