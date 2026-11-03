---
tag: CPKPXCT3Q7
kind: definition
name: Hosoya index
msc: [05C70, 05C92, 05C31]
defines: 1P57E5E03M
uses: [0JD5C82QMB, 0MJ04A50QW, AE724Y8CQX, 0GA9K57A39]
sources:
  - url: https://en.wikipedia.org/wiki/Hosoya_index
---

## Definition

Let $G$ be a finite [[graph|0JD5C82QMB]].
The *Hosoya index* $Z(G)$ is the number of [[matchings|0MJ04A50QW]] of $G$, the empty matching included.
Here a matching is a set of edges of $G$ no two of which share a vertex.
Equivalently, $Z(G) = \sum_{k \ge 0} m_k(G)$, where $m_k(G)$ is the number of matchings with exactly $k$ edges.

## Remarks

Example: the path $P_3$ with edges $e_1, e_2$ sharing a vertex has the matchings $\emptyset$, $\set{e_1}$, $\set{e_2}$, so $Z(P_3) = 3$.
The cycle $C_3$ has the empty matching and three one-edge matchings, so $Z(C_3) = 4$.
For the path $P_n$ on $n$ vertices, $Z(P_n) = F_{n+1}$, a term of the [[Fibonacci sequence|0GA9K57A39]] with $F_1 = F_2 = 1$, since deleting the last vertex or its edge gives $Z(P_n) = Z(P_{n-1}) + Z(P_{n-2})$.
Non-example: the set $\set{e_1, e_2}$ in $P_3$ is not a matching, because $e_1$ and $e_2$ share a vertex, so it is not counted.
The recurrence $Z(G) = Z(G - e) + Z(G - u - v)$ for an edge $e = uv$ computes $Z$ in general.
Among trees on $n$ vertices, the star has the smallest Hosoya index, $n$, and the path the largest.
