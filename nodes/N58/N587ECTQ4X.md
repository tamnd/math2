---
tag: N587ECTQ4X
kind: concept
name: Order polytope
msc: [06A07, 52B05, 52B20]
sources:
  - url: https://en.wikipedia.org/wiki/Order_polytope
same_as:
  wikidata: Q85791185
  wikipedia: Order polytope
---

## Summary

The order polytope of a finite poset $P$ is the set of functions $f \colon P \to [0, 1]$ that are [[order-preserving|0A7KV2WB7A]], seen as points of $\R^P$.
It is a convex polytope with integer vertices, namely the indicator functions of the upper sets of $P$.
Its volume is the number of [[linear extensions|W8DZ5KGGHN]] of $P$ divided by $\abs{P}!$, and its lattice point counts are given by the [[order polynomial|VDBDJZWPEA]].
It was introduced by Richard Stanley, together with the chain polytope of the poset.

## Explanations

### L1 human

Give each element of a poset a real number between $0$ and $1$, so that larger elements get numbers at least as large.
All such assignments fill a convex region in space, one coordinate per element.
For two unrelated elements you get the whole unit square.
For a chain $x < y$ you get the triangle where $0 \le f(x) \le f(y) \le 1$, which is half of the square.
