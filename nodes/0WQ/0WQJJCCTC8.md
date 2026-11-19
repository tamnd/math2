---
tag: 0WQJJCCTC8
kind: concept
name: Normal vector
aliases: [normal]
msc: ["51N20"]
topics: [VKVAJ94SKZ]
audience: school
uses: [0MP9BCF6DP, 0V3XAMF3C1, 03NK6RSRQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_(geometry)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Normal_(geometry)
    locator: Normal to planes and polygons
same_as:
  wikidata: Q273176
  wikipedia: Normal (geometry)
inventory: [R7N8FHPH16]
---

## Summary

A normal vector of a [[line|0MP9BCF6DP]] in $\mathbb{R}^2$ or of a [[plane|0V3XAMF3C1]] in $\mathbb{R}^3$ is a nonzero vector that is [[perpendicular|03NK6RSRQ1]] to every vector between two of its points.
The [[definition|0XYP2KKSPC]] states this with the dot product.
For a curved surface, a normal vector at a point is perpendicular to the tangent plane at that point.
The normal gives the [[equation of a plane|07SDJ5DNE4]] $n \cdot (r - a) = 0$, and it is the tool for angles between planes and distances to planes.

## Motivation

A plane in space contains many directions, but only one direction, up to scale, is perpendicular to all of them.
This one direction describes the plane with less data than two direction vectors.
In the plane $\mathbb{R}^2$, a line has one normal direction in the same way.

## Notation

- A normal is often written $n$ or $\mathbf{n}$, and a unit normal $\hat n$ or $\nu$.
- For the plane $a x + b y + c z = d$, the normal $(a, b, c)$ is the coefficient vector.

## Remarks

### Examples

- The plane $z = 0$ has the normal vectors $(0, 0, c)$ with $c \neq 0$.
- The plane $6x + 3y + 2z = 6$ has the normal $(6, 3, 2)$ and the unit normal $\tfrac{1}{7}(6, 3, 2)$.
- The line $2x + 3y = 6$ in $\mathbb{R}^2$ has the normal $(2, 3)$; its direction $(-3, 2)$ is perpendicular to it.
- The sphere $x^2 + y^2 + z^2 = 1$ has at the point $p$ the outward unit normal $p$.

### Non-examples

- The zero vector is perpendicular to every vector, but it is not a normal vector, by definition.
- A direction vector of a line in $\mathbb{R}^3$ is not a normal of the line. A line in space has a whole plane of perpendicular directions, so "the" normal of a line in $\mathbb{R}^3$ is not defined.

### Basic properties

- If $n$ is a normal of $H$, then the normals of $H$ are exactly the vectors $c n$ with $c \neq 0$.
- The plane $a x + b y + c z = d$ with $(a, b, c) \neq 0$ has the normal $(a, b, c)$.
- The plane $p + s u + t v$ with $u \not\parallel v$ has the normal $u \times v$, by the [[perpendicularity of the cross product|0T4QHJXSD4]].
- Exactly two unit normals exist, $\pm n / \|n\|$; a choice between them is an orientation of the plane.

### History

The word comes from the Latin "norma", a carpenter's square.

### Common errors

- Students take a vector in the plane as its normal.
- Students forget to check that a computed normal is nonzero; three points on one line give $n = 0$.

## Explanations

### L1 human

A normal vector sticks straight out of a flat object.
A pencil that stands upright on a table is normal to the table.
Each arrow that lies on the table makes a right angle with the pencil, so its dot product with the pencil is $0$.

### L2 human

Worked example: find a normal of the plane through $0$ that contains $u = (1, 2, 0)$ and $v = (0, 1, 3)$.

1. $n = u \times v = (2 \cdot 3 - 0 \cdot 1, \; 0 \cdot 0 - 1 \cdot 3, \; 1 \cdot 1 - 2 \cdot 0) = (6, -3, 1)$.
2. Check: $n \cdot u = 6 - 6 + 0 = 0$ and $n \cdot v = 0 - 3 + 3 = 0$.

A trap: a normal must be perpendicular to every vector in the plane, not only to one of them.

### L3 human

For a surface given as a level set $F(x, y, z) = c$, the gradient $\nabla F$ is a normal at each point where it is nonzero; this is treated in [[calculus|RX2DPD6V6M]].
For a hyperplane $n \cdot r = d$ in $\mathbb{R}^n$, the normal is again $n$, and its orthogonal complement is the direction space of the hyperplane.
