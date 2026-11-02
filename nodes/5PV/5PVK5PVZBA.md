---
tag: 5PVK5PVZBA
kind: definition
name: Barycentric subdivision
msc: [55U10, 57Q05]
defines: J5DZEYCEX2
uses: [V8GZ0W1ZZ5, 0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Barycentric_subdivision
---

## Definition

Let $K$ be a geometric simplicial complex in $\R^N$, so each simplex $\sigma$ of $K$ is the [[convex hull|0FQSDC2EQ2]] of affinely independent vertices $v_0, \dots, v_n$.
The *barycentre* of $\sigma$ is the point
$$b(\sigma) = \frac{1}{n + 1} \sum_{i=0}^{n} v_i.$$
The *barycentric subdivision* $\operatorname{sd} K$ is the geometric simplicial complex with the following simplices.
For each chain $\sigma_0 \subsetneq \sigma_1 \subsetneq \cdots \subsetneq \sigma_k$ of simplices of $K$, it has the convex hull of $\set{b(\sigma_0), \dots, b(\sigma_k)}$.

## Remarks

The union of the simplices of $\operatorname{sd} K$ equals the union of the simplices of $K$, and each simplex of $\operatorname{sd} K$ lies in a simplex of $K$.
If every simplex of $K$ has diameter at most $d$ and $K$ has dimension at most $n$, then every simplex of $\operatorname{sd} K$ has diameter at most $\frac{n}{n + 1} d$.

For an abstract [[simplicial complex|V8GZ0W1ZZ5]] $K$, the vertices of $\operatorname{sd} K$ are the nonempty faces of $K$.
The faces of $\operatorname{sd} K$ are the finite chains of nonempty faces under inclusion.

Example: let $K$ be a $2$-simplex with vertices $v_0, v_1, v_2$ and all its faces.
The maximal chains are $\set{v_i} \subsetneq \set{v_i, v_j} \subsetneq \set{v_0, v_1, v_2}$ for the $6$ ordered pairs $i \ne j$, so $\operatorname{sd} K$ has $6$ triangles, $7$ vertices and $12$ edges.

Non-example: cutting the triangle into $3$ triangles by joining its centroid to the three corners gives a subdivision, but not the barycentric one.
The barycentres of the edges are not vertices of it, though each edge is a simplex of $K$.
