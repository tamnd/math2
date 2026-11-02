---
tag: 1QS5A6XNXA
kind: definition
name: Direct limit of rings
msc: [16S10, 18A30, 13B02]
defines: Q5T05ET56S
uses: [0B1261B5ED, 0VTH8KPCG2, X9HEQ29Q49, 0G8VEZ3WTK, 0670T59HGE]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_limit
---

## Definition

Let $(I, \le)$ be a directed set: a nonempty preordered set in which any two elements have a common upper bound.
A *directed system of rings* over $I$ consists of [[rings|0B1261B5ED]] $R_i$ for $i \in I$ and [[ring homomorphisms|0VTH8KPCG2]] $f_{ij} \colon R_i \to R_j$ for $i \le j$, such that:

1. $f_{ii}$ is the identity of $R_i$ for every $i$.
2. $f_{jk} \circ f_{ij} = f_{ik}$ whenever $i \le j \le k$.

On the disjoint union $\bigsqcup_i R_i$, let $a \in R_i$ and $b \in R_j$ be [[equivalent|0G8VEZ3WTK]] if $f_{ik}(a) = f_{jk}(b)$ for some $k$ with $i \le k$ and $j \le k$.
The *direct limit* $\varinjlim R_i$ is the set of equivalence classes $[a]$.
For $a \in R_i$ and $b \in R_j$, choose $k \ge i, j$ and set $[a] + [b] = [f_{ik}(a) + f_{jk}(b)]$ and $[a][b] = [f_{ik}(a) f_{jk}(b)]$.

## Remarks

These operations do not depend on the choices, and they make $\varinjlim R_i$ a ring; the maps $\varphi_i \colon R_i \to \varinjlim R_i$, $a \mapsto [a]$, are ring homomorphisms with $\varphi_j \circ f_{ij} = \varphi_i$.
It is the [[direct limit|X9HEQ29Q49]] of the system in the category of rings: for every ring $S$ and homomorphisms $g_i \colon R_i \to S$ with $g_j \circ f_{ij} = g_i$, there is exactly one homomorphism $g \colon \varinjlim R_i \to S$ with $g \circ \varphi_i = g_i$.
Example: let $I = \N$, $R_n = k[x_1, \dots, x_n]$ and let $f_{mn}$ be the inclusion for $m \le n$.
The direct limit is the polynomial ring $k[x_1, x_2, \dots]$ in countably many variables, since each polynomial involves only finitely many variables.
This ring is not [[Noetherian|0670T59HGE]], although every $R_n$ is, as the chain of ideals $(x_1) \subset (x_1, x_2) \subset \cdots$ shows.
Non-example: if $I$ is not directed, say two incomparable indices $1, 2$ with rings $\Z$ and $\Z/2$ and no common upper bound.
Then the sum $[a] + [b]$ for $a \in R_1$ and $b \in R_2$ is not defined, and the construction does not give a ring.
A direct limit of fields is a field, and a direct limit of local rings along local homomorphisms is a local ring.
