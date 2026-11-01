---
tag: GDN82Y3ATR
kind: definition
name: List coloring
msc: [05C15]
defines: VHAMHH5SPC
uses: [0JD5C82QMB, 0874138YP6, 0C5M7AM6FH]
sources:
  - url: https://en.wikipedia.org/wiki/List_coloring
---

## Definition

Let $G = (V, E)$ be a finite [[graph|0JD5C82QMB]].
A list assignment for $G$ is a map $L$ that assigns to each vertex $v$ a finite set $L(v)$ of colours.
An $L$-colouring of $G$ is a map $c$ on $V$ such that:

1. $c(v) \in L(v)$ for every vertex $v$.
2. $c(u) \ne c(v)$ for every edge $uv$.

For an integer $k \ge 1$, the graph $G$ is $k$-choosable if it has an $L$-colouring for every list assignment $L$ with $\abs{L(v)} \ge k$ for all $v$.
The choice number $\operatorname{ch}(G)$ is the least $k$ such that $G$ is $k$-choosable.

## Remarks

If all lists equal $\set{1, \dots, k}$, an $L$-colouring is a proper [[colouring|0874138YP6]] with $k$ colours, so $\operatorname{ch}(G) \ge \chi(G)$, where $\chi$ is the [[chromatic number|0C5M7AM6FH]].
Example: every tree is $2$-choosable.
Colour the vertices in an order in which each vertex after the first has exactly one earlier neighbour.
Each vertex then picks a colour of its list other than the colour of that neighbour.
Non-example: $K_{3,3}$ is not $2$-choosable, although $\chi(K_{3,3}) = 2$.
Give the vertices on each side the lists $\set{1,2}$, $\set{1,3}$ and $\set{2,3}$.
The colours used on one side meet each of these three sets, so they include at least two colours.
Two of these colours form the list of some vertex on the other side, and that vertex fails clause 2.
Thomassen proved that every planar graph is $5$-choosable.
Choice number is also called list chromatic number and written $\chi_\ell(G)$.
