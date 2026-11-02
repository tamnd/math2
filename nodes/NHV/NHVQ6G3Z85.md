---
tag: NHVQ6G3Z85
kind: definition
name: Regular polytope
msc: [51M20, 52B15]
defines: F60PD912D5
uses: [300K6CB1KH, KY7SB854VH, 0ZG3Z5JZ85, 02GK6HZYBT]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_polytope
---

## Definition

Let $P \subseteq \R^d$ be a [[convex polytope|300K6CB1KH]] of dimension $d$.
A *flag* of $P$ is a sequence $(F_0, F_1, \dots, F_{d-1})$ of [[faces|KY7SB854VH]] of $P$ with $F_0 \subset F_1 \subset \cdots \subset F_{d-1}$ and $\dim F_i = i$ for each $i$.
The [[symmetry group|0ZG3Z5JZ85]] of $P$ is the group of isometries of $\R^d$ that map $P$ onto itself.
It acts on the set of flags of $P$.
The polytope $P$ is *regular* if this action is [[transitive|02GK6HZYBT]].
That is, for any two flags $\Phi$ and $\Psi$ of $P$ there is a symmetry $g$ of $P$ with $g(\Phi) = \Psi$.

## Remarks

Example: the cube $[0,1]^3$ has $8$ vertices, each vertex lies on $3$ edges, and each edge lies on $2$ square faces, so it has $8 \cdot 3 \cdot 2 = 48$ flags.
Its symmetry group has order $48$.
It can move any vertex to any vertex and then permute the three edges at a vertex freely, so it acts transitively on flags.
So the cube is regular.

Non-example: the rectangle $[0,2] \times [0,1]$ has $8$ flags but only $4$ symmetries.
No symmetry maps a flag whose edge has length $2$ to a flag whose edge has length $1$, so the action is not transitive.

For a convex polytope, a symmetry that fixes one flag is the identity, so the action of the symmetry group on the flags of a regular polytope is simply transitive.
In dimension $2$ the regular polytopes are the [[regular polygons|01KJJ9A400]], and in dimension $3$ they are the [[Platonic solids|017E5PRS1Q]].
The same flag condition defines regular star polytopes, which are not convex.
It also defines regular abstract polytopes, where the symmetry group is replaced by the automorphism group of a partially ordered set.
