---
tag: 07SDJ5DNE4
kind: concept
name: Normal vector and equation of a plane
aliases: [point-normal-form]
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
uses: [0V3XAMF3C1, 0WQJJCCTC8, 0S52TNNTH9, 03NK6RSRQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_planes_in_three-dimensional_space
    locator: Point–normal form and general form of the equation of a plane
  - url: https://en.wikipedia.org/wiki/Euclidean_planes_in_three-dimensional_space
    locator: Angle between two planes
---

## Summary

Let $a \in \mathbb{R}^3$ be a point and let $n \in \mathbb{R}^3$ be a nonzero vector.
The [[plane|0V3XAMF3C1]] through $a$ with the [[normal vector|0WQJJCCTC8]] $n$ is the set of the points $r$ with
$$n \cdot (r - a) = 0,$$
that is, the points $r$ such that $r - a$ is [[perpendicular|03NK6RSRQ1]] to $n$.
With $n = (n_1, n_2, n_3)$ and $a = (x_0, y_0, z_0)$, it is the point-normal form $n_1(x - x_0) + n_2(y - y_0) + n_3(z - z_0) = 0$.
Expanded, it is the general form $n_1 x + n_2 y + n_3 z = d$ with $d = n \cdot a$.
Conversely, each equation $n_1 x + n_2 y + n_3 z = d$ with $n \neq 0$ is a plane with the normal vector $n$.
A plane also has the parametric form $r = a + s u + t v$, where $u$ and $v$ are non-parallel vectors in the plane, and then $n = u \times v$.

## Motivation

A plane in space has many directions, so one direction vector cannot describe it as for a line.
But it has exactly one direction perpendicular to it, up to scale.
A point $r$ is on the plane through $a$ when the arrow $r - a$ lies flat in the plane, that is, when it is perpendicular to the normal.
The [[dot product|0S52TNNTH9]] turns this condition into one linear equation.
This is why one linear equation in three unknowns describes a plane.

## Notation

- Vector form: $n \cdot (r - a) = 0$, or $n \cdot r = d$.
- Point-normal form: $n_1(x - x_0) + n_2(y - y_0) + n_3(z - z_0) = 0$.
- General form: $n_1 x + n_2 y + n_3 z = d$; many books write $ax + by + cz = d$.
- Parametric form: $r = a + s u + t v$, with $s, t \in \mathbb{R}$.
- Unit normal: $\hat n = n / \|n\|$, and the Hesse normal form $\hat n \cdot r = p$ with $p \geq 0$.

## Remarks

### Examples

- The plane $z = 0$ has the normal vector $(0, 0, 1)$ and the parametric form $s(1, 0, 0) + t(0, 1, 0)$.
- The plane through $(1, 0, 0)$, $(0, 2, 0)$ and $(0, 0, 3)$ is $6x + 3y + 2z = 6$. The [[three-point example|~305ce7fa]] derives it.
- The plane through $(1, 2, 3)$ with the normal $(2, -1, 4)$ is $2x - y + 4z = 2 - 2 + 12 = 12$.
- The planes $x + y = 1$ and $y + z = 2$ make the angle $\tfrac{\pi}{3}$. The [[angle example|~49200a35]] computes it.

### Non-examples

- The equation $0x + 0y + 0z = d$ is not a plane: it is empty for $d \neq 0$ and all of $\mathbb{R}^3$ for $d = 0$. The [[non-example|~b7a5de3d]] treats this and three collinear points.
- In $\mathbb{R}^3$, the equation $x + y = 1$ is a plane, not a line; it is a line only in $\mathbb{R}^2$.
- The set $\{a + s u + t v\}$ with $u \parallel v$ is a line, not a plane.

### Basic properties

- Two equations $n \cdot r = d$ and $n' \cdot r = d'$ give the same plane if and only if $(n', d') = c(n, d)$ for some $c \neq 0$.
- Two planes are parallel or equal if and only if their normals are multiples of each other.
- Plane through three points $A$, $B$, $C$ not on one line: $n = (B - A) \times (C - A)$ and $n \cdot (r - A) = 0$.
- Angle between two planes: the angle $\varphi \in [0, \tfrac{\pi}{2}]$ with $\cos \varphi = \dfrac{|n_1 \cdot n_2|}{\|n_1\| \, \|n_2\|}$.
- Angle between a line with direction $d$ and a plane: $\sin \psi = \dfrac{|d \cdot n|}{\|d\| \, \|n\|}$.
- The line $a + t d$ meets the plane $n \cdot r = e$ in one point if and only if $n \cdot d \neq 0$.
- The distance from a point $q$ to the plane $n \cdot r = d$ is $\dfrac{|n \cdot q - d|}{\|n\|}$, by the [[distance formulas|~1297517b]].

### History

The equation of a plane in coordinates comes from the analytic geometry of space of the 18th century.
The vector form $n \cdot (r - a) = 0$ belongs to the vector analysis of Gibbs and Heaviside in the 1880s.

### Common errors

- Students read the normal vector from the wrong equation, such as from the parametric form; the normal is the coefficient vector of the general form.
- Students forget that $d$ is $n \cdot a$, and write $d = 0$ for every plane.
- Students take the obtuse angle between the normals as the angle between the planes. The absolute value in the formula gives the acute angle.

## Explanations

### L1 human

Hold a book flat and push a pencil straight through it.
The pencil is the normal vector of the plane of the book.
A point is on the plane when the arrow from a fixed point of the plane to it makes a right angle with the pencil.
For the floor $z = 0$, the pencil is $(0, 0, 1)$, and a point is on the floor when its height is $0$.

### L2 human

Worked example: the plane through $a = (1, 1, 0)$ with the directions $u = (1, 0, 1)$ and $v = (0, 1, 1)$.

1. Normal: $n = u \times v = (0 \cdot 1 - 1 \cdot 1, \; 1 \cdot 0 - 1 \cdot 1, \; 1 \cdot 1 - 0 \cdot 0) = (-1, -1, 1)$.
2. Constant: $d = n \cdot a = -1 - 1 + 0 = -2$.
3. Equation: $-x - y + z = -2$, or $x + y - z = 2$.
4. Check: $a + u = (2, 1, 1)$ gives $2 + 1 - 1 = 2$, and $a + v = (1, 2, 1)$ gives $1 + 2 - 1 = 2$.

The typical uses are intersections of lines and planes, angles between planes, and distances.
A trap: the parametric form needs two non-parallel directions; the general form needs one nonzero normal.

### L3 human

A plane is a two-dimensional affine subspace of $\mathbb{R}^3$, and the general form describes it as a level set of the linear functional $r \mapsto n \cdot r$.
The sub-area on [[duality|9K7FFF26QR]] treats such functionals in general, and a plane is the kernel of one of them, shifted.
In $\mathbb{R}^n$ the same equation $n \cdot r = d$ describes a hyperplane, of dimension $n - 1$.
