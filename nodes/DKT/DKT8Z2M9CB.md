---
tag: DKT8Z2M9CB
kind: definition
name: Generalized polygon
msc: ["51E12", "51E24"]
defines: PCT2HY9AAZ
uses: [FGKNAFNHA3, 0ZVQKTRKVQ, D13K9GJT0B, 00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_polygon
---

## Definition

Let $\mathcal{S} = (P, L, I)$ be an [[incidence structure|FGKNAFNHA3]] with point set $P$, line set $L$ and incidence relation $I \subseteq P \times L$.
Its *incidence graph* is the [[bipartite graph|0ZVQKTRKVQ]] with vertex set $P \cup L$, with an edge between $p \in P$ and $\ell \in L$ when $(p, \ell) \in I$.
Let $n \ge 2$ be an integer.
The structure $\mathcal{S}$ is a *generalized $n$-gon* if its incidence graph is connected, has diameter $n$, and has [[girth|D13K9GJT0B]] $2n$.
Here the diameter is the largest distance between two vertices of the [[graph|00C0BR7D7H]].
A generalized $n$-gon is *thick* if every point lies on at least three lines and every line has at least three points.

## Remarks

Example: the [[Fano plane|QQ8GW1ASZM]] is a generalized $3$-gon.
Two points lie on a common line, and two lines meet in a point, so in both cases the distance is $2$.
A point and a line not through it are at distance $3$, so the diameter is $3$.
A cycle of length $4$ would give two points on two common lines, which is impossible.
A triangle of the plane gives a cycle of length $6$, so the girth is $6$.
It is thick, since each line has $3$ points and each point is on $3$ lines.

Non-example: the affine plane of order $2$, with $4$ points and the $6$ lines of $2$ points each.
Its girth is $6$, but two parallel lines have no common point, so they are at distance $4$; the diameter is $4 \ne 3$.

For $n \ge 3$, any two points lie on at most one line, so a generalized $n$-gon is a partial linear space.
The generalized $3$-gons with at least three points on each line and three lines on each point are exactly the [[projective planes|DANFNN8C4Y]], and the generalized $4$-gons are the generalized quadrangles.
A finite thick generalized $n$-gon has an order $(s, t)$: every line has $s + 1$ points and every point is on $t + 1$ lines.
