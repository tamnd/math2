---
tag: AN054RHT1K
kind: concept
name: Domain decomposition methods
msc: [65N55, 65F10, 65Y05]
sources:
  - url: https://en.wikipedia.org/wiki/Domain_decomposition_methods
same_as:
  wikidata: Q5289813
  wikipedia: Domain decomposition methods
---

## Summary

Domain decomposition methods solve a [[boundary value problem|TM8VQJWGHZ]] on a domain by splitting the domain into smaller subdomains.
They solve problems on the subdomains, often in parallel, and couple the local solutions through the interfaces until they fit together.
They are mainly used as [[preconditioners|KE98SW3SBD]] for Krylov methods on large parallel computers.

## Explanations

### L1 human

A big problem on a complicated region is hard to solve at once.
Cut the region into pieces, give each piece to a different processor, and solve each small problem there.
The pieces then exchange information along their common boundaries and solve again, until the pieces agree.
The classical example, due to Schwarz, solves a problem on the union of a disc and a rectangle by alternating between the two shapes.
