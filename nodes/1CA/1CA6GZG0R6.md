---
tag: 1CA6GZG0R6
kind: concept
name: Tate cohomology
msc: [20J06, 11R34]
sources:
  - url: https://en.wikipedia.org/wiki/Tate_cohomology_group
same_as:
  wikidata: Q7687974
  wikipedia: Tate cohomology group
---

## Summary

Tate cohomology joins the cohomology and the [[homology|CFAG3VRXEA]] of a finite group $G$ into one sequence of groups $\hat H^n(G, M)$ indexed by all integers $n$.
It agrees with ordinary cohomology in positive degrees and with homology in degrees at most $-2$.
In the two middle degrees it is modified with the norm map.
A short exact sequence of modules gives a long exact sequence infinite in both directions.
Tate cohomology is a basic tool of class field theory and of [[Galois cohomology|9MPCZ3EAJM]], and for cyclic groups it is periodic of period $2$.

## Explanations

### L1 human

For a finite group, cohomology runs upward from degree $0$ and homology runs downward.
Tate noticed that the two can be glued into a single sequence that runs in both directions, after a small correction at the junction.
The correction uses the norm, the sum of all the group elements acting on a module.
Let a cyclic group of order $m$ act on $\Z$ with every element fixing every integer.
Then the groups alternate between $\Z/m\Z$ and $0$.
