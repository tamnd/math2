---
tag: ZAKCAS4GC7
kind: concept
name: Prim's algorithm
msc: [05C85, 05C05, 90C27]
specializes: [PSM6NKYJB8]
sources:
  - url: https://en.wikipedia.org/wiki/Prim%27s_algorithm
same_as:
  wikidata: Q470813
  wikipedia: Prim's algorithm
---

## Summary

Prim's algorithm finds a [[minimum spanning tree|0JW7KT6PQW]] of a connected graph with weighted edges.
It grows a single tree from a start vertex, adding at each step the lightest edge that joins the tree to a vertex outside it.
It is a [[greedy algorithm|PSM6NKYJB8]], and with a binary heap it runs in time $O(m \log n)$ on $n$ vertices and $m$ edges.

## Explanations

### L1 human

Start at one town and build roads outward, one at a time.
At every step, look at all roads that lead from a town already reached to a town not yet reached, and build the cheapest one.
Stop when every town is reached.
Take a triangle with road costs $1$ between $a$ and $b$, $2$ between $b$ and $c$, and $3$ between $a$ and $c$.
Starting from $a$ gives the roads $ab$ and then $bc$.
Unlike [[Kruskal's algorithm|5FPWTYFJRA]], the roads built so far always form one connected piece.
