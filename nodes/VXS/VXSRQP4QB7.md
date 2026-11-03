---
tag: VXSRQP4QB7
kind: definition
name: Cremona diagram
msc: [70C20, 74K10]
defines: 1R00A4VTW4
uses: [E5ZHQSHB97]
sources:
  - url: https://en.wikipedia.org/wiki/Cremona_diagram
---

## Definition

Let a plane [[truss|E5ZHQSHB97]] with bars $e$ and joints $i$ be in equilibrium under external loads and support reactions at the joints.
Let $t_e$ be its bar forces.
A *Cremona diagram* of the truss is a plane figure made of segments such that:

1. each external force and each reaction is drawn once, as a segment parallel to it and of the same length,
2. each bar $e$ is drawn once, as a segment parallel to $e$ of length $\abs{t_e}$, and
3. for each joint $i$, the segments of the forces acting on $i$ form a closed polygon, the force polygon of $i$.

The polygons of two joints joined by a bar share the segment of that bar.

## Remarks

Example: the triangular truss with joints $(0, 0)$, $(2, 0)$, $(1, 1)$, a load $F$ downward at the apex and vertical reactions $F/2$ at both supports.
Its diagram has a vertical segment of length $F$ for the load and two segments of slopes $\pm 1$, each of length $F/\sqrt{2}$, which close it into a triangle.
A horizontal segment of length $F/2$ for the bottom bar closes the polygons of the two supports.
Reading the lengths gives the two inclined bars in compression with force $F/\sqrt{2}$ and the bottom bar in tension with force $F/2$.

Non-example: a truss that is not in equilibrium under its loads.
Then the force polygon of some joint does not close, so clause 3 fails and no Cremona diagram exists.

Tension and compression are read from the sense in which each polygon is traversed, which is fixed by the order of the loads around the joint.
The method is also called the Maxwell–Cremona method.
