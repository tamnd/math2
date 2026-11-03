---
tag: KN5KTC6KNW
kind: definition
name: Hopcroft–Karp algorithm
msc: [05C70, 05C85, 68W40]
defines: PYK6XFYNQX
uses: [0ZVQKTRKVQ, 0MJ04A50QW, 03NAMV1DHJ, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm
---

## Definition

Let $G$ be a finite [[bipartite graph|0ZVQKTRKVQ]] with vertex classes $U$ and $W$, and let $M$ be a [[matching|0MJ04A50QW]] in $G$.
A vertex is *free* if it lies on no edge of $M$.
An *augmenting path* for $M$ is a [[path|03NAMV1DHJ]] between two distinct free vertices whose edges alternate between edges not in $M$ and edges in $M$.

The *Hopcroft–Karp algorithm* is the following [[algorithm|9DMSG5HAQX]].

1. Start with $M = \emptyset$.
2. Find the least length $\ell$ of an augmenting path for $M$; if there is none, return $M$.
3. Choose a maximal set $\set{P_1, \dots, P_k}$ of pairwise vertex-disjoint augmenting paths of length $\ell$.
4. Replace $M$ by the symmetric difference $M \mathbin{\triangle} (P_1 \cup \dots \cup P_k)$, where each $P_i$ is seen as a set of edges, and return to step 2.

Each pass through steps 2 to 4 is a *phase*.

## Remarks

Example: let $U = \set{u_1, u_2}$ and $W = \set{w_1, w_2}$ with edges $u_1 w_1$, $u_2 w_1$ and $u_2 w_2$.
In the first phase $\ell = 1$, and a maximal set of disjoint single edges is $\set{u_1 w_1, u_2 w_2}$, which is already a perfect matching.
If instead the first phase chooses $\set{u_2 w_1}$, the second phase uses the augmenting path $u_1, w_1, u_2, w_2$ of length $3$ and gives the same size $2$.

Non-example: the path $u_1, w_1$ is not augmenting for $M = \set{u_2 w_1}$, because $w_1$ is not free.

By Berge's theorem, a matching is maximum if and only if it has no augmenting path, so the output is a maximum matching.
Step 2 uses [[breadth-first search|52XF4HS0X3]] and step 3 uses [[depth-first search|4TE2X7N728]], so each phase takes time $O(m)$.
There are $O(\sqrt{n})$ phases, so the total time is $O(m \sqrt{n})$, where $n$ is the number of vertices and $m$ the number of edges.
