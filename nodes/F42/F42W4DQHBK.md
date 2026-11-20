---
tag: F42W4DQHBK
kind: example
name: Quadric surfaces of the form xy + yz + zx and two others, by the principal axis theorem
aliases: [classification-of-quadric-surfaces]
msc: [15A63, 51N20]
topics: [6TSCEW8QMK]
audience: ug1
instance_of: [Q3Q4FF23VG]
illustrates: [0PR5P9Z4KM]
uses: [0PR5P9Z4KM, Q3Q4FF23VG, 07EZA80NEH]
sources:
  - url: https://en.wikipedia.org/wiki/Quadric
    locator: Euclidean space
  - url: https://en.wikipedia.org/wiki/Principal_axis_theorem
---

## Example

A [[quadric|Q3Q4FF23VG]] in $\R^3$ is the zero set of a polynomial of degree $2$ in $x, y, z$.
When the equation is $Q(x, y, z) = c$ with $Q$ a quadratic form, [[the principal axis theorem|0PR5P9Z4KM]] gives its shape from the eigenvalues of the matrix of $Q$.

**The surfaces $xy + yz + zx = c$.**

1. The matrix of $Q = xy + yz + zx$ has $0$ on the diagonal and $\frac12$ in every other place.
2. $A (1, 1, 1)^T = (1, 1, 1)^T$, so $1$ is an eigenvalue, on the line of $(1, 1, 1)$.
3. For $(1, -1, 0)$ and $(1, 1, -2)$, $A v = -\frac12 v$, so $-\frac12$ is an eigenvalue with multiplicity $2$.
4. The trace is $0 = 1 - \frac12 - \frac12$, which is a check.
5. In orthonormal coordinates $u, v, w$ along these three vectors, $Q = u^2 - \frac12 v^2 - \frac12 w^2$.
6. For $c = 1$, the surface $u^2 - \frac12 (v^2 + w^2) = 1$ is a hyperboloid of two sheets, with the two sheets at $u \ge 1$ and $u \le -1$.
7. For $c = -1$, the surface $\frac12 (v^2 + w^2) - u^2 = 1$ is a hyperboloid of one sheet around the $u$-axis.
8. For $c = 0$, the surface $u^2 = \frac12 (v^2 + w^2)$ is a circular cone with vertex $0$.
9. All three are surfaces of revolution about the line of $(1, 1, 1)$, because the two eigenvalues $-\frac12$ are equal.

**The saddle $z = xy$.**

1. With $x = (s - t)/\sqrt 2$ and $y = (s + t)/\sqrt 2$, which is a rotation by $45^\circ$ in the $xy$-plane, $xy = \frac12 (s^2 - t^2)$.
2. So the surface is $z = \frac12 s^2 - \frac12 t^2$, a hyperbolic paraboloid.

**An ellipsoid.** Let $2(x^2 + y^2 + z^2 + xy + yz + zx) = 4$.

1. The matrix is $I + J$, where $J$ has every entry $1$.
2. $J$ has eigenvalue $3$ on $(1, 1, 1)$ and $0$ on the plane $x + y + z = 0$, so $I + J$ has eigenvalues $4$, $1$, $1$.
3. In the principal axes the equation is $4u^2 + v^2 + w^2 = 4$, so $u^2 + \frac{v^2}{4} + \frac{w^2}{4} = 1$.
4. This is an ellipsoid of revolution with semi-axes $1$, $2$, $2$; the short axis is the line of $(1, 1, 1)$.

## Remarks

For a central quadric $Q(x) = 1$ with nonzero eigenvalues, [[the signature|07EZA80NEH]] of $Q$ gives the type:

| signature $(p, q)$ | surface $Q = 1$ |
|---|---|
| $(3, 0)$ | ellipsoid |
| $(2, 1)$ | hyperboloid of one sheet |
| $(1, 2)$ | hyperboloid of two sheets |
| $(0, 3)$ | empty |

The exact semi-axes need the eigenvalues, and not only their signs.
A zero eigenvalue gives a cylinder or a paraboloid.
For example, $x^2 + y^2 = 1$, $x^2 - y^2 = 1$ and $x^2 = y$ are the elliptic, hyperbolic and parabolic cylinders, and $z = x^2 + y^2$ is an elliptic paraboloid.
According to Wikipedia, a general quadric in $\R^3$ is affinely equivalent to one of $17$ normal forms.
Five of them are not cones, cylinders, planes or imaginary.
These five are the ellipsoid, the elliptic and hyperbolic paraboloids, and the hyperboloids of one and two sheets.
The geometry of these surfaces, with their sections and pictures, is in [[the topic on quadric surfaces|F70261PW6Q]].

## Explanations

### L1 human

In three variables, the method is the same as for conics.
Find the eigenvalues and eigenvectors, rotate to the principal axes, and read the shape from the signs.
The equation $xy + yz + zx = 1$ looks hard, but it is a hyperboloid of two sheets.

### L2 human

A useful trick: for a matrix with a repeated eigenvalue, the surface is a surface of revolution.
A trap: the sign of $c$ matters; $Q = 1$ and $Q = -1$ can be different types, as in steps 6 and 7.
Another trap: a hyperboloid of one sheet has one negative coefficient in $Q = 1$ form, not one positive coefficient.
