---
tag: T4MTXNJJ3Q
kind: statement
role: theorem
name: Nerve theorem
msc: [55U10, 55P10]
uses: [4P3S0DRZXB, ZH29VRRRJ6, 049PXYHW1T, R5WP8Z69Q8, XZG6MTSWCN]
about: [4P3S0DRZXB]
sources:
  - url: https://en.wikipedia.org/wiki/Nerve_complex
---

## Statement

Let $X$ be a [[paracompact space|ZH29VRRRJ6]] and let $\mathcal{U} = (U_i)_{i \in I}$ be an [[open cover|049PXYHW1T]] of $X$.
Assume that every nonempty intersection $U_{i_0} \cap \cdots \cap U_{i_k}$ of finitely many members of $\mathcal{U}$ is [[contractible|R5WP8Z69Q8]].
Then $X$ is [[homotopy equivalent|XZG6MTSWCN]] to the geometric realization of the [[nerve|4P3S0DRZXB]] $N(\mathcal{U})$.

## Remarks

The proof uses a partition of unity subordinate to $\mathcal{U}$ to define a map $X \to \abs{N(\mathcal{U})}$, sending $x$ to the point with barycentric coordinates $(\varphi_i(x))_{i \in I}$.
One then shows that this map is a homotopy equivalence.
A standard way compares both spaces with a common space built from the intersections, whose projections to $X$ and to $\abs{N(\mathcal{U})}$ have contractible fibres.

Example: cover $S^1$ by three open arcs, consecutive arcs overlapping in an arc, and no point in all three.
Every nonempty intersection is an arc, which is contractible, and the nerve is the boundary of a triangle, a circle, as the theorem predicts.

The contractibility hypothesis is necessary.
Cover $S^1$ by two open arcs, each a bit larger than a half circle.
Their intersection is two disjoint arcs, which is not contractible, and the nerve is a single edge, which is contractible, while $S^1$ is not.

Versions of the theorem hold for finite covers of a simplicial complex by subcomplexes whose nonempty intersections are contractible.

## Explanations

### L1 human

If a space is covered by simple pieces whose overlaps are also simple, then the overlap pattern alone determines the shape of the space up to homotopy.
The overlap pattern is recorded by the nerve, a combinatorial object.
So one can compute topological invariants of the space from a finite list of which pieces meet.

### L2 human

A cover with contractible finite intersections is called a good cover.
Every smooth manifold has a good cover by geodesically convex balls for a Riemannian metric.
So the nerve theorem shows that a compact smooth manifold has the homotopy type of a finite simplicial complex.
In topological data analysis, the Čech complex of a point cloud is the nerve of a cover by balls.
The nerve theorem shows that it recovers the homotopy type of the union of the balls.
