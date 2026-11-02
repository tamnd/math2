---
tag: QQ3PBZS9J8
kind: definition
name: Mesh generation
msc: [65N50, 65M50, 65D18]
defines: RTSAFF4KFJ
uses: [YH170WBQ6M, V8GZ0W1ZZ5]
sources:
  - url: https://en.wikipedia.org/wiki/Mesh_generation
---

## Definition

Let $d \in \set{2, 3}$ and let $\Omega \subset \R^d$ be a bounded open set whose closure $\overline{\Omega}$ is a polygon ($d = 2$) or a polyhedron ($d = 3$).
A *conforming mesh* of $\overline{\Omega}$ is a finite set $\mathcal{T}$ of closed cells, each a simplex or each a convex quadrilateral or hexahedron, such that:

1. the union of the cells of $\mathcal{T}$ is $\overline{\Omega}$;
2. the interiors of two distinct cells are disjoint;
3. the intersection of two distinct cells is empty or a common face of both, that is, a common vertex, edge or facet.

*Mesh generation* is the task of computing a conforming mesh of $\overline{\Omega}$ from a description of its boundary.
Usually it must meet conditions on the size $h_K = \operatorname{diam} K$ and the shape of each cell $K$.
A typical shape condition is an upper bound on $h_K / \rho_K$, where $\rho_K$ is the radius of the largest ball contained in $K$.

## Remarks

When all cells are simplices, a conforming mesh is a [[triangulation|YH170WBQ6M]] of $\overline{\Omega}$, the underlying space of a [[simplicial complex|V8GZ0W1ZZ5]].
Example: the unit square $[0,1]^2$ with the two triangles of vertices $(0,0), (1,0), (1,1)$ and $(0,0), (1,1), (0,1)$ is a conforming mesh.
The triangles cover the square, their interiors are disjoint, and they meet along the common edge from $(0,0)$ to $(1,1)$.
Non-example: cover $[0,2] \times [0,1]$ by the squares $[0,1] \times [0,1]$, $[1,2] \times [0, \tfrac12]$ and $[1,2] \times [\tfrac12, 1]$.
Clauses 1 and 2 hold, but clause 3 fails: the first and second squares meet in the segment $\set{1} \times [0, \tfrac12]$.
This segment is an edge of the second square but not of the first.
The point $(1, \tfrac12)$ is called a hanging node.
A family of meshes with $\max_K h_K \to 0$ and $h_K / \rho_K$ bounded uniformly is called shape regular.
Finite element error estimates are usually proved for such families.

## Explanations

### L1 human

A mesh cuts a region into simple pieces that fit together edge to edge.
There are no gaps, no overlaps, and no corner of one piece in the middle of a side of another.
Mesh generation is the job of producing such a cutting, with pieces that are neither too big nor too thin.
