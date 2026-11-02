---
tag: ATJXGC4KCG
kind: definition
name: Abstract polytope
msc: [52B15, 51M20, 06A07]
defines: WREPDZG7PF
uses: [0QV2JS9RJ3, 1C7TKGTB2F, 300K6CB1KH]
sources:
  - url: https://en.wikipedia.org/wiki/Abstract_polytope
---

## Definition

Let $n \ge -1$ be an integer and let $(\mathcal{P}, \le)$ be a [[partially ordered set|0QV2JS9RJ3]], whose elements are called faces.
A *flag* of $\mathcal{P}$ is a maximal totally ordered subset.
Two flags are *adjacent* if they differ in exactly one face.
$\mathcal{P}$ is an *abstract polytope of rank $n$* if:

1. $\mathcal{P}$ has a least face $F_{-1}$ and a greatest face $F_n$;
2. every flag of $\mathcal{P}$ has exactly $n + 2$ faces;
3. $\mathcal{P}$ is strongly flag-connected: any two flags $\Phi$ and $\Psi$ are joined by flags $\Phi = \Phi_0, \Phi_1, \dots, \Phi_k = \Psi$.
   Here each $\Phi_{i-1}$ is adjacent to $\Phi_i$, and $\Phi \cap \Psi \subseteq \Phi_i$ for each $i$;
4. the diamond condition holds: if $F < G$ are faces whose ranks differ by $2$, then there are exactly two faces $H$ with $F < H < G$.

## Remarks

Conditions 1 and 2 make $\mathcal{P}$ a [[graded poset|1C7TKGTB2F]] with ranks $-1, 0, \dots, n$.
Faces of rank $0$ are vertices, faces of rank $1$ are edges, and faces of rank $n - 1$ are facets.

Example: the faces of a triangle with vertices $a, b, c$, together with $\varnothing$ as $F_{-1}$ and the triangle $T$ as $F_2$, ordered by inclusion, form an abstract polytope of rank $2$.
Every flag has the form $\varnothing < a < ab < T$, with $4 = 2 + 2$ faces.
Between $\varnothing$ and an edge there are exactly two vertices, and between a vertex and $T$ there are exactly two edges, so the diamond condition holds.
More generally, the faces of any [[convex polytope|300K6CB1KH]] of dimension $n$, with $\varnothing$ added, form an abstract polytope of rank $n$.

Non-example: take two triangles that share one vertex $c$, with all their vertices and edges, a least face, and one greatest face of rank $2$.
The vertex $c$ lies on four edges, so between $c$ and the greatest face there are four faces of rank $1$, and the diamond condition fails.

The hemicube is obtained from the cube by identifying antipodal faces.
It is an abstract polytope of rank $3$ with $4$ vertices, $6$ edges and $3$ square faces, and it is not the face lattice of any convex polytope.
