---
tag: ZQVQTP6E2K
kind: definition
name: Kruskal's algorithm
msc: [05C85, 05C05, 90C27]
defines: 5FPWTYFJRA
uses: [00C0BR7D7H, 0KWFFMDF8T, 0Z05VCBQ7Y, 0S4ZEZM7KE, 0JW7KT6PQW, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
---

## Definition

Let $G = (V, E)$ be a finite [[connected graph|0KWFFMDF8T]] and let $w \colon E \to \R$ be a weight function on its edges.
*Kruskal's algorithm* is the following [[algorithm|9DMSG5HAQX]].

1. List the edges as $e_1, \dots, e_m$ with $w(e_1) \le w(e_2) \le \dots \le w(e_m)$.
2. Start with the empty set $F = \emptyset$.
3. For $i = 1, \dots, m$ in turn, add $e_i$ to $F$ if the graph $(V, F \cup \set{e_i})$ has no [[cycle|0Z05VCBQ7Y]].

It returns $F$, which is the edge set of a [[minimum spanning tree|0JW7KT6PQW]] of $G$.

## Remarks

Example: let $G$ be the triangle on $\set{a, b, c}$ with $w(ab) = 1$, $w(bc) = 2$ and $w(ac) = 3$.
The algorithm adds $ab$ and $bc$, and it rejects $ac$ because $ab, bc, ac$ form a cycle.
The tree $\set{ab, bc}$ has weight $3$, the least weight of a [[spanning tree|0S4ZEZM7KE]] of $G$.

Non-example: if $G$ is not connected, no spanning tree exists.
The same steps then return a minimum spanning forest, that is, a minimum spanning tree of each connected component.

Correctness follows from the cut property: a lightest edge crossing any partition of $V$ into two parts lies in some minimum spanning tree.
With a disjoint-set (union-find) structure for the cycle test, the running time is $O(m \log m)$.
