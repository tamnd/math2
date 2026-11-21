---
tag: 0XYP2KKSPC
kind: definition
name: Normal vector
msc: ["51N20"]
topics: [VKVAJ94SKZ]
audience: school
defines: 0WQJJCCTC8
uses: [0V3XAMF3C1, 0MP9BCF6DP, 03NK6RSRQ1, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_(geometry)
    locator: Normal to planes and polygons
inventory: [R7N8FHPH16]
---

## Definition

Let $H$ be a [[line|0MP9BCF6DP]] in $\mathbb{R}^2$ or a [[plane|0V3XAMF3C1]] in $\mathbb{R}^3$, and let $\cdot$ be the [[dot product|0S52TNNTH9]].
A normal vector of $H$ is a nonzero vector $n$ such that
$$n \cdot (x - y) = 0 \quad \text{for all points } x, y \in H.$$
In words, $n$ is [[perpendicular|03NK6RSRQ1]] to every vector between two points of $H$.

## Notation

A normal is written $n$ or $\mathbf{n}$.
A unit normal vector is a normal vector of length $1$, written $\hat n$.

## Remarks

The condition $n \neq 0$ is part of the definition, because the zero vector is perpendicular to everything and carries no direction.
Once one normal $n$ is known, the normals of $H$ are exactly the vectors $c n$ with $c \neq 0$.

The definition is easy to apply to the usual descriptions of lines and planes.
The plane $\{(x, y, z) : a x + b y + c z = d\}$ with $(a, b, c) \neq (0, 0, 0)$ has the normal $(a, b, c)$: for two points $x$ and $y$ on it, $(a, b, c) \cdot x = d = (a, b, c) \cdot y$, so the dot product with $x - y$ is $0$.
In the same way the line $\{(x, y) : a x + b y = c\}$ with $(a, b) \neq (0, 0)$ has the normal $(a, b)$.
For the plane $\{p + s u + t v : s, t \in \mathbb{R}\}$ with $u$ and $v$ not parallel, the [[cross product|0N5N15HWZ7]] $u \times v$ is a normal.

## Explanations

### L1 human

A normal vector sticks straight out of a flat object.
Each arrow that lies in the object makes a right angle with it, so its dot product with the normal is $0$.
For the floor $z = 0$, the arrow $(0, 0, 1)$ pointing straight up is a normal.

### L2 human

To check that $n$ is a normal of a plane, it is enough to check $n \cdot u = 0$ and $n \cdot v = 0$ for two non-parallel vectors $u$ and $v$ in the plane.
Every vector between two points of the plane is a combination $s u + t v$, and the dot product is linear, so $n \cdot (s u + t v) = 0$ as well.
For example, $(1, 1, 1)$ is a normal of the plane spanned by $(1, -1, 0)$ and $(0, 1, -1)$, since both dot products are $0$.
Watch out: one dot product is not enough, since a vector perpendicular to $u$ alone can still lean along $v$.
