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

A normal vector is the one direction that sticks straight out of a flat object, and knowing it is often the shortest way to know the object.
A normal vector of a [[line|0MP9BCF6DP]] in $\mathbb{R}^2$ or of a [[plane|0V3XAMF3C1]] in $\mathbb{R}^3$ is a nonzero vector that is [[perpendicular|03NK6RSRQ1]] to every vector between two of its points.
The [[definition|0XYP2KKSPC]] states this with the dot product.
The normal gives the [[equation of a plane|07SDJ5DNE4]] $n \cdot (r - a) = 0$, and it is the tool for angles between planes and for distances to planes.
For a curved surface, a normal at a point is a vector perpendicular to the tangent plane there.

## Motivation

A plane in space contains infinitely many directions, and to describe it from the inside you need two of them.
But only one direction, up to scale, is perpendicular to all of them at once.
This single direction carries the same information with less data, and it turns the plane into one equation.
In $\mathbb{R}^2$ a line has a normal direction in the same way, and the equation $ax + by = c$ is the statement that the normal $(a, b)$ has a fixed dot product with each point of the line.

## Notation

A normal is usually written $n$ or $\mathbf{n}$, and a unit normal $\hat n$ or $\nu$.
For the plane $ax + by + cz = d$ the coefficient vector $(a, b, c)$ is a normal, so the notation of the equation already names it.

## Remarks

### A first computation

The plane $6x + 3y + 2z = 6$ has the normal $(6, 3, 2)$.
Its length is $\sqrt{36 + 9 + 4} = 7$, so $\tfrac{1}{7}(6, 3, 2)$ is a unit normal.

For a plane given by two directions, the cross product finds a normal.
The plane through $0$ that contains $u = (1, 2, 0)$ and $v = (0, 1, 3)$ has the normal
$$n = u \times v = (2 \cdot 3 - 0 \cdot 1, \; 0 \cdot 0 - 1 \cdot 3, \; 1 \cdot 1 - 2 \cdot 0) = (6, -3, 1),$$
and indeed $n \cdot u = 6 - 6 + 0 = 0$ and $n \cdot v = 0 - 3 + 3 = 0$.
This always works when $u$ and $v$ are not parallel, by the [[perpendicularity of the cross product|0T4QHJXSD4]].

In the plane $\mathbb{R}^2$, the line $2x + 3y = 6$ has the normal $(2, 3)$, and its direction $(-3, 2)$ is perpendicular to it.
On the unit sphere $x^2 + y^2 + z^2 = 1$, the outward unit normal at a point $p$ is $p$ itself.

### The rules you can use

If $n$ is a normal of $H$, then the normals of $H$ are exactly the vectors $c n$ with $c \neq 0$.
So every line in $\mathbb{R}^2$ and every plane in $\mathbb{R}^3$ has exactly two unit normals, $\pm n / \|n\|$.
Choosing one of the two is choosing a side of the plane, which is what an orientation of the plane means.
To test whether $n$ is a normal of a plane, it suffices to check $n \cdot u = 0$ and $n \cdot v = 0$ for two non-parallel directions $u$ and $v$ in it.

### What a normal is not

The zero vector is perpendicular to everything, but it is not a normal, because it points nowhere.
A line in $\mathbb{R}^3$ has no single normal direction: every vector in a whole plane is perpendicular to it.
So "the normal of a line" makes sense in $\mathbb{R}^2$ but not in $\mathbb{R}^3$.

### Watch out

A vector that lies in the plane is not a normal, even if it appears in the description of the plane.
And a normal must be perpendicular to every direction in the plane, not just to one; a vector perpendicular to $u$ alone can still lean along $v$.
When you compute a normal as $(B - A) \times (C - A)$ from three points, check that the answer is nonzero, since three points on one line give $0$.

### History

The word comes from the Latin "norma", the carpenter's square used to draw right angles.

### Try it

Find a unit normal of the plane $x - 2y + 2z = 4$.
The coefficient vector $(1, -2, 2)$ has length $3$, so $\tfrac{1}{3}(1, -2, 2)$ is one, and its negative is the other.

Is $(1, 1, 1)$ a normal of the plane through $0$ containing $(1, -1, 0)$ and $(0, 1, -1)$?
Both dot products are $0$, and the two directions are not parallel, so it is.

## Explanations

### L1 human

A normal vector sticks straight out of a flat object.
A pencil that stands upright on a table is normal to the table.
Each arrow that lies on the table makes a right angle with the pencil, so its dot product with the pencil is $0$.

### L2 human

In practice a normal comes from one of two places.
If the plane is given by an equation $ax + by + cz = d$, read off $(a, b, c)$.
If it is given by a point and two directions, or by three points, take a cross product of two directions.
Then the normal does the work: angles between planes are angles between normals, and the distance to a plane is measured along the normal.
Watch out: the normal must be perpendicular to every vector in the plane, so check it against two directions, not one.

### L3 human

For a surface given as a level set $F(x, y, z) = c$, the gradient $\nabla F$ is a normal at each point where it is nonzero; this belongs to [[calculus|RX2DPD6V6M]].
For a hyperplane $n \cdot r = d$ in $\mathbb{R}^n$ the normal is again $n$, and the direction space of the hyperplane is the orthogonal complement of $n$.
