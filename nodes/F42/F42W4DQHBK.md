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

A [[quadric surface|Q3Q4FF23VG]] in $\mathbb{R}^3$ is the set of zeros of a polynomial of degree $2$ in $x$, $y$ and $z$.
When the equation has the form $Q(x, y, z) = c$ with $Q$ a quadratic form, [[the principal axis theorem|0PR5P9Z4KM]] gives the shape from the eigenvalues of the matrix of $Q$.
We work out three cases.

**The surfaces $xy + yz + zx = c$.**

1. Each product $xy$, $yz$, $zx$ has coefficient $1$, which is split in half between two places.
   So the matrix of $Q = xy + yz + zx$ has $0$ on the diagonal and $\tfrac{1}{2}$ in every other place.
2. Each row of the matrix sums to $1$, so $A(1, 1, 1)^{\mathsf{T}} = (1, 1, 1)^{\mathsf{T}}$, and $1$ is an eigenvalue on the line of $(1, 1, 1)$.
3. For $v = (1, -1, 0)$ we get $Av = (-\tfrac{1}{2}, \tfrac{1}{2}, 0) = -\tfrac{1}{2} v$, and for $w = (1, 1, -2)$ we get $Aw = (-\tfrac{1}{2}, -\tfrac{1}{2}, 1) = -\tfrac{1}{2} w$.
   So $-\tfrac{1}{2}$ is an eigenvalue with multiplicity $2$.
4. Check: the trace of $A$ is $0$, and $1 - \tfrac{1}{2} - \tfrac{1}{2} = 0$.
5. The three vectors $(1, 1, 1)$, $v$ and $w$ are pairwise orthogonal.
   In orthonormal coordinates $u$, $s$, $t$ along them, $Q = u^2 - \tfrac{1}{2} s^2 - \tfrac{1}{2} t^2$.
6. For $c = 1$, the surface $u^2 - \tfrac{1}{2}(s^2 + t^2) = 1$ is a hyperboloid of two sheets, with one sheet in $u \ge 1$ and one in $u \le -1$.
7. For $c = -1$, the surface $\tfrac{1}{2}(s^2 + t^2) - u^2 = 1$ is a hyperboloid of one sheet around the $u$-axis.
8. For $c = 0$, the surface $u^2 = \tfrac{1}{2}(s^2 + t^2)$ is a circular cone with vertex at the origin.
9. All three are surfaces of revolution about the line of $(1, 1, 1)$, because the two eigenvalues $-\tfrac{1}{2}$ are equal.
   Check for $c = 1$: the point $(1, 1, 0)$ lies on the surface, and its coordinate $u = 2/\sqrt{3}$ satisfies $u^2 = \tfrac{4}{3} \ge 1$.

**The saddle $z = xy$.**

1. The rotation by $45^\circ$ in the $xy$-plane, $x = (s - t)/\sqrt{2}$ and $y = (s + t)/\sqrt{2}$, gives $xy = \tfrac{1}{2}(s^2 - t^2)$.
2. So the surface is $z = \tfrac{1}{2}s^2 - \tfrac{1}{2}t^2$, a hyperbolic paraboloid.

**An ellipsoid.** Let $2(x^2 + y^2 + z^2 + xy + yz + zx) = 4$.

1. The diagonal coefficients are $2$, and each product has coefficient $2$, which splits into $1$ and $1$.
   So the matrix is $I + J$, where $J$ is the $3 \times 3$ matrix with every entry $1$.
2. The matrix $J$ has eigenvalue $3$ on $(1, 1, 1)$ and eigenvalue $0$ on the plane $x + y + z = 0$, so $I + J$ has eigenvalues $4$, $1$ and $1$.
3. In principal axes the equation is $4u^2 + s^2 + t^2 = 4$, that is, $u^2 + s^2/4 + t^2/4 = 1$.
4. This is an ellipsoid of revolution with semi-axes $1$, $2$ and $2$, and its short axis is the line of $(1, 1, 1)$.

## Remarks

### The type from the signature

For a central quadric $Q(x) = 1$ with no zero eigenvalue, [[the signature|07EZA80NEH]] $(p, q)$ of $Q$ gives the type.

| signature $(p, q)$ | surface $Q = 1$ |
|---|---|
| $(3, 0)$ | ellipsoid |
| $(2, 1)$ | hyperboloid of one sheet |
| $(1, 2)$ | hyperboloid of two sheets |
| $(0, 3)$ | no real points |

The signs decide the type, and the sizes of the eigenvalues decide the semi-axes, $1/\sqrt{\lvert \lambda_i \rvert}$.
Watch out for the sign of $c$: $Q = 1$ and $Q = -1$ can have different types, as steps 6 and 7 of the first case show.
A hyperboloid of one sheet has one negative coefficient in the form $Q = 1$, and a hyperboloid of two sheets has two.

### The seventeen normal forms

A zero eigenvalue gives a cylinder or a paraboloid.
After an affine change of coordinates and a multiplication of the equation by a nonzero number, every equation of degree $2$ in three variables takes one of $17$ normal forms.
The six with three squares are
$$x^2 + y^2 + z^2 = 1, \quad x^2 + y^2 + z^2 = -1, \quad x^2 + y^2 + z^2 = 0, \quad x^2 + y^2 - z^2 = 1, \quad x^2 + y^2 - z^2 = -1, \quad x^2 + y^2 - z^2 = 0.$$
They are the ellipsoid, the empty imaginary ellipsoid, a single point, the hyperboloids of one and of two sheets, and the cone.
The seven with two squares are the elliptic paraboloid $z = x^2 + y^2$, the hyperbolic paraboloid $z = x^2 - y^2$, the cylinders $x^2 + y^2 = 1$ and $x^2 - y^2 = 1$, the empty $x^2 + y^2 = -1$, the line $x^2 + y^2 = 0$, and the two planes $x^2 - y^2 = 0$.
The four with one square are the parabolic cylinder $x^2 = y$, the parallel planes $x^2 = 1$, the empty $x^2 = -1$, and the double plane $x^2 = 0$.
Only five are surfaces that are not cones, cylinders or planes: the ellipsoid, the two hyperboloids and the two paraboloids.
The geometry of these surfaces, with their plane sections, is in [[the topic on quadric surfaces|F70261PW6Q]].

## Explanations

### L1 human

In three variables the method is the same as for conics in the plane.
Find the eigenvalues and eigenvectors, turn the axes to the eigenvectors, and read the shape from the signs.
The equation $xy + yz + zx = 1$ looks hard, but in the turned axes it is $u^2 - \tfrac{1}{2}(s^2 + t^2) = 1$, a surface of two separate bowls.

### L2 human

A useful shortcut: when two eigenvalues are equal, the surface is a surface of revolution about the axis of the third eigenvector.
The first and third cases both use this, with the axis along $(1, 1, 1)$.
Watch out for the matrix: the coefficient of $xy$ is split in half, so the matrix of $xy + yz + zx$ has $\tfrac{1}{2}$, not $1$, off the diagonal.
With $1$ the eigenvalues would be $2$, $-1$ and $-1$, which gives the right type but semi-axes that are wrong by a factor of $\sqrt{2}$.
