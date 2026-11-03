---
tag: 9NR5VKEJ51
kind: object
name: Bethe lattice
msc: [82B20, 82B23, 05C05]
instance_of: [062D9KXJB1, 0Q70YFB6ZM]
uses: [062D9KXJB1, 0Q70YFB6ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Bethe_lattice
same_as:
  wikidata: Q794168
  wikipedia: Bethe lattice
---

## Description

Let $q \ge 2$ be an integer.
The *Bethe lattice* of coordination number $q$ is the infinite connected [[tree|062D9KXJB1]] in which every vertex has degree exactly $q$.
It is unique up to graph isomorphism, and it is a [[regular graph|0Q70YFB6ZM]] of degree $q$.
For $q = 2$ it is the graph $\Z$ with edges between consecutive integers.

## Remarks

Fix a vertex $o$, the root.
For $n \ge 1$ there are exactly $q (q - 1)^{n - 1}$ vertices at distance $n$ from $o$, so the number of vertices grows exponentially in the distance when $q \ge 3$.
As a result, for $q \ge 3$, in a finite ball the boundary vertices make up a fixed positive fraction of all vertices.
So statistical models on it are studied deep inside the tree, away from the boundary.
Since the tree has no cycles, models such as the [[Ising model|R0KGM32QN6]] can be solved exactly on it by recursion from the leaves.
For the ferromagnetic Ising model with coupling $J > 0$ and no field, the critical inverse temperature $\beta_c$ satisfies $\tanh(\beta_c J) = 1/(q - 1)$.
This solution coincides with the Bethe–Peierls approximation for a lattice with coordination number $q$, which is the origin of the name.
For $q \ge 3$ it is the Cayley graph of a free product of $q$ copies of $\Z/2\Z$.

## Explanations

### L1 human

Start at one point and draw $q$ branches; at the end of each branch draw $q - 1$ new branches, and continue forever.
The result is a tree in which every point looks the same and there are no loops.
Without loops, a spin model can be solved by passing information from the outside in, which makes this tree a standard testing ground for approximations.
