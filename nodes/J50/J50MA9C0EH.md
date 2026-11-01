---
tag: J50MA9C0EH
kind: definition
name: Strongly regular graph
msc: ["05E30", 05C50]
defines: C22WGRP3T8
uses: [0JD5C82QMB, 0KA4S8R39M, 01T3TMGTTE]
sources:
  - url: https://en.wikipedia.org/wiki/Strongly_regular_graph
---

## Definition

Let $v, k, \lambda, \mu$ be non-negative integers.
A finite [[graph|0JD5C82QMB]] $G$ is strongly regular with parameters $(v, k, \lambda, \mu)$, written $\mathrm{srg}(v, k, \lambda, \mu)$, if:

1. $G$ has $v$ vertices and is $k$-[[regular|0KA4S8R39M]].
2. Every two adjacent vertices have exactly $\lambda$ common [[neighbours|01T3TMGTTE]].
3. Every two distinct non-adjacent vertices have exactly $\mu$ common neighbours.

## Remarks

Many authors also require that $G$ is neither complete nor edgeless, so that both conditions 2 and 3 apply to some pair.
Counting the edges between the neighbours of a vertex $x$ and the vertices not adjacent to $x$ gives $k(k - \lambda - 1) = (v - k - 1)\mu$.
Example: the [[Petersen graph|0NR95CTFCZ]] is an $\mathrm{srg}(10, 3, 0, 1)$: it is $3$-regular, it has no triangles, so $\lambda = 0$, and two non-adjacent vertices have exactly one common neighbour.
Check of the identity: $3 \cdot (3 - 0 - 1) = 6 = (10 - 3 - 1) \cdot 1$.
Non-example: the [[cycle graph|0QQ0F12962]] $C_6$ is $2$-regular, but two vertices at distance $2$ have one common neighbour while two opposite vertices have none, so clause 3 fails.
The [[complement|0RNMP6VCR2]] of an $\mathrm{srg}(v, k, \lambda, \mu)$ is an $\mathrm{srg}(v, v - k - 1, v - 2 - 2k + \mu, v - 2k + \lambda)$.
