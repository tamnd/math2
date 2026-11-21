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

A plane in space is pinned down by one point on it and one arrow sticking straight out of it, and the dot product turns that picture into a single linear equation.
Let $a \in \mathbb{R}^3$ be a point and let $n \in \mathbb{R}^3$ be a nonzero vector.
The [[plane|0V3XAMF3C1]] through $a$ with [[normal vector|0WQJJCCTC8]] $n$ is the set of the points $r$ with
$$n \cdot (r - a) = 0,$$
that is, the points $r$ for which the arrow $r - a$ is [[perpendicular|03NK6RSRQ1]] to $n$.
Expanding the dot product gives the general form $n_1 x + n_2 y + n_3 z = d$ with $d = n \cdot a$.
Conversely, every equation $n_1 x + n_2 y + n_3 z = d$ with $n \neq 0$ describes a plane with normal $n$.
So one linear equation in three unknowns is a plane, and its coefficients are the normal.

## Motivation

A line is fixed by a point and one direction, but a plane contains a whole family of directions, and no single one of them describes it.
What a plane does have is exactly one direction perpendicular to it, up to scale.
A point $r$ lies on the plane through $a$ exactly when the arrow $r - a$ lies flat in the plane, and that happens exactly when $r - a$ is perpendicular to the normal.
The [[dot product|0S52TNNTH9]] writes "perpendicular" as "dot product zero", and the condition becomes one linear equation.

The plane can also be described from the inside, by a point and two directions $u$ and $v$ that lie in it and are not parallel.
Then the points are $r = a + s u + t v$ for real $s$ and $t$, and the cross product $u \times v$ supplies a normal.

## Notation

With $n = (n_1, n_2, n_3)$ and $a = (x_0, y_0, z_0)$, the equation $n \cdot (r - a) = 0$ reads
$$n_1(x - x_0) + n_2(y - y_0) + n_3(z - z_0) = 0,$$
the point-normal form.
Multiplied out it is the general form $n_1 x + n_2 y + n_3 z = d$, which many books write as $ax + by + cz = d$; in vector form this is $n \cdot r = d$.
The parametric form is $r = a + s u + t v$ with $s, t \in \mathbb{R}$.
Dividing by $\|n\|$ gives the unit normal $\hat n = n / \|n\|$ and the Hesse normal form $\hat n \cdot r = p$, where the sign of $\hat n$ is chosen so that $p \geq 0$.

## Remarks

### A first computation

The plane through $(1, 2, 3)$ with normal $(2, -1, 4)$ has the equation $2x - y + 4z = d$, where $d = 2 \cdot 1 - 2 + 4 \cdot 3 = 12$.

The plane through $a = (1, 1, 0)$ with directions $u = (1, 0, 1)$ and $v = (0, 1, 1)$ needs a normal first.
The cross product gives
$$n = u \times v = (0 \cdot 1 - 1 \cdot 1, \; 1 \cdot 0 - 1 \cdot 1, \; 1 \cdot 1 - 0 \cdot 0) = (-1, -1, 1),$$
and $d = n \cdot a = -2$, so the plane is $-x - y + z = -2$, or $x + y - z = 2$.
As a check, $a + u = (2, 1, 1)$ gives $2 + 1 - 1 = 2$, and $a + v = (1, 2, 1)$ gives $1 + 2 - 1 = 2$.

Three points not on one line work the same way, with $u$ and $v$ the edges from one of them.
The [[three-point example|B1N13NEAJQ]] finds the plane $6x + 3y + 2z = 6$ through $(1, 0, 0)$, $(0, 2, 0)$ and $(0, 0, 3)$.

### The rules you can use

Two equations $n \cdot r = d$ and $n' \cdot r = d'$ describe the same plane exactly when $(n', d') = c\,(n, d)$ for some $c \neq 0$.
Two planes are parallel or equal exactly when their normals are multiples of each other.

The angle between two planes is the angle between their normals, taken acute:
$$\cos \varphi = \frac{|n_1 \cdot n_2|}{\|n_1\| \, \|n_2\|}, \qquad 0 \leq \varphi \leq \tfrac{\pi}{2}.$$
For $x + y = 1$ and $y + z = 2$ this gives $\cos \varphi = \tfrac{1}{2}$ and $\varphi = \tfrac{\pi}{3}$, as the [[angle example|P0VS33VRSR]] shows.
A line with direction $d$ makes with the plane the angle $\psi$ with $\sin \psi = |d \cdot n| / (\|d\| \, \|n\|)$, and it meets the plane in exactly one point when $n \cdot d \neq 0$.
The distance from a point $q$ to the plane $n \cdot r = d$ is $|n \cdot q - d| / \|n\|$, by the [[distance formulas|C6GAS92QHX]].

### What a plane equation is not

The equation $0x + 0y + 0z = d$ is not a plane: it has no solutions when $d \neq 0$ and every point is a solution when $d = 0$.
The [[non-example|3BV88R6A66]] treats this case, together with three points on one line.
In $\mathbb{R}^3$ the equation $x + y = 1$ is a plane, the one standing upright over the line $x + y = 1$ of the $xy$-plane.
And $a + s u + t v$ with $u$ parallel to $v$ is only a line.

### Watch out

The normal is the coefficient vector of the general form, not a vector you read off the parametric form.
In $a + s u + t v$ the vectors $u$ and $v$ lie in the plane, so neither of them is a normal.

The constant $d$ is $n \cdot a$, and it is $0$ only for planes through the origin.
For the angle between planes, take the absolute value; without it you may get the obtuse angle between the normals instead.

### History

The equation of a plane in coordinates comes from the analytic geometry of space of the eighteenth century.
The vector form $n \cdot (r - a) = 0$ belongs to the vector analysis of Gibbs and Heaviside in the 1880s.

### Try it

Find the plane through $(2, 0, -1)$ parallel to $3x - y + z = 7$.
It has the same normal $(3, -1, 1)$, and $d = 6 - 0 - 1 = 5$, so it is $3x - y + z = 5$.

Where does the line $(0, 0, 0) + t(1, 1, 1)$ meet the plane $x + y - z = 2$?
Substituting gives $t + t - t = 2$, so $t = 2$ and the point is $(2, 2, 2)$.

## Explanations

### L1 human

Hold a book flat and push a pencil straight through it.
The pencil is the normal vector of the plane of the book.
A point is on the plane when the arrow from a fixed point of the plane to it makes a right angle with the pencil.
For the floor $z = 0$ the pencil is $(0, 0, 1)$, and a point is on the floor when its height is $0$.

### L2 human

The typical uses are intersections of lines and planes, angles between planes, and distances to planes.
For each of them, first bring the plane into the general form $n \cdot r = d$ so that the normal can be read off.
If the plane is given by a point and two directions, compute $n = u \times v$ and then $d = n \cdot a$, and check the answer with one more point of the plane.
Watch out: the parametric form needs two directions that are not parallel, while the general form needs one normal that is not zero.

### L3 human

A plane is a two-dimensional affine subspace of $\mathbb{R}^3$, and the general form describes it as a level set of the linear functional $r \mapsto n \cdot r$.
The sub-area on [[duality|9K7FFF26QR]] treats such functionals in general; a plane is a shifted copy of the kernel of one of them.
In $\mathbb{R}^n$ the same equation $n \cdot r = d$ describes a hyperplane, of dimension $n - 1$.
