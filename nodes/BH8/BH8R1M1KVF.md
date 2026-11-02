---
tag: BH8R1M1KVF
kind: statement
role: theorem
name: Upper bound theorem
msc: [52B05, 52B11]
uses: [300K6CB1KH, 872BAKDQQK, M6YBMXKJYD, R7V3S9V891, 6DXF1T506B, 4WKHF5BCTA, 4CZMWQVC30]
about: [872BAKDQQK, M6YBMXKJYD]
sources:
  - url: https://en.wikipedia.org/wiki/Upper_bound_theorem
same_as:
  wikidata: Q17104455
  wikipedia: Upper bound theorem
---

## Statement

Let $n > d \ge 2$, and let $P$ be a [[convex polytope|300K6CB1KH]] of dimension $d$ with $n$ [[vertices|R7V3S9V891]].
Let $C(n, d)$ be the [[cyclic polytope|M6YBMXKJYD]] of dimension $d$ with $n$ vertices.
Then for every $i$ with $0 \le i \le d - 1$,
$$f_i(P) \le f_i(C(n, d)),$$
where $f_i$ is the number of $i$-dimensional faces, the $i$-th entry of the [[f-vector|872BAKDQQK]].

## Remarks

The theorem was proved by Peter McMullen in 1970, after Theodore Motzkin had conjectured it.
Proof idea: a small perturbation of the vertices makes $P$ simplicial without lowering any $f_i$, so one may assume $P$ simplicial.
Then one passes to the h-vector of the boundary, uses the [[Dehn–Sommerville equations|4WKHF5BCTA]] $h_i = h_{d-i}$, and proves $h_i \le \binom{n - d + i - 1}{i}$ for $i \le d/2$ with a shelling of the boundary.
Cyclic polytopes attain all these bounds, because they are neighborly.

The number of facets of $C(n, d)$ is
$$f_{d-1}(C(n,d)) = \frac{n}{n - m} \binom{n - m}{m} \text{ if } d = 2m, \qquad 2 \binom{n - m - 1}{m} \text{ if } d = 2m + 1.$$
For $d = 3$ this gives $2n - 4$, the number of triangles of any simplicial $3$-polytope with $n$ vertices.
For $d = 4$ and $n = 8$ it gives $8 \cdot 15 / 6 = 20$ facets.

By [[polar polytope|6DXF1T506B]] duality, the theorem also bounds the number of vertices of a $d$-polytope with $n$ facets.

## Explanations

### L1 human

Among all polytopes with a given dimension and a given number of corners, which one has the most faces?
The upper bound theorem says: the cyclic polytope, and it wins in every dimension of face at once.
So there is a single shape that is the champion for edges, for two-dimensional faces, and so on.

### L2 human

In the dual form, a polytope with $n$ facets in dimension $d$ has at most about $n^{\floor{d/2}}$ vertices.
This bounds the number of vertices that the simplex method or a vertex enumeration algorithm may meet, and the size of convex hulls in computational geometry.
The theorem was extended to simplicial spheres by Richard Stanley using commutative algebra.
Its lower-bound partner, for simplicial polytopes, is the lower bound theorem, and both are contained in the [[g-theorem|4CZMWQVC30]].
