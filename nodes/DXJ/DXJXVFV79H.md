---
tag: DXJXVFV79H
kind: concept
name: Expander graph
msc: [05C48, 05C50]
sources:
  - url: https://en.wikipedia.org/wiki/Expander_graph
same_as:
  wikidata: Q776602
  wikipedia: Expander graph
---

## Summary

An expander graph is a sparse graph in which every set of at most half of the vertices has many edges leaving it.
One usually means a family of [[regular graphs|0KA4S8R39M]] of fixed degree whose [[Cheeger constant|Y7S6W12N64]] stays above a fixed positive bound.
Expanders combine few edges with strong connectivity, and they are used in network design, error-correcting codes, derandomization and group theory.

## Explanations

### L1 human

Picture a network of computers in which each machine has only three cables.
In a good expander, any group of up to half the machines is joined to the rest by many cables, in proportion to the size of the group.
So the network has no bottleneck, although it is cheap to build.
A long cycle is the opposite: half of the cycle is cut off from the other half by just $2$ edges.
