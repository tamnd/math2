---
tag: 07SJXTWVQW
kind: concept
name: Linear isometry
aliases: [norm-preserving-linear-map, isometric-linear-map]
msc: ["15A04", "46B04"]
topics: [AZS5BPF5H3]
audience: ug1
specializes: [0NRYHJPQG2]
uses: [00A0RPAQ8A, 0RJF668P1T, 01EK923SKP, 0ST8QF9T3T]
sources:
  - url: https://en.wikipedia.org/wiki/Isometry
    locator: Linear isometry
  - url: https://en.wikipedia.org/wiki/Mazur%E2%80%93Ulam_theorem
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Summary

A linear isometry is a linear map that moves vectors without stretching or squeezing any of them.
Rotations and mirror reflections are the first examples, and together with their relatives in higher dimensions they are the maps that keep the whole geometry of a space.
Let $V$ and $W$ be [[normed spaces|03J5RAKB30]] over $\R$ or $\C$.
A *linear isometry* from $V$ to $W$ is a [[linear map|0NRYHJPQG2]] $T \colon V \to W$ with
$$\norm{Tv} = \norm{v} \qquad \text{for every } v \in V.$$
The [[formal definition|0717XXPWM6]] states this.
When $V$ and $W$ are [[inner product spaces|0QVNCJXRY3]] with the induced norms, the condition holds exactly when $T$ keeps inner products.
When they are also finite-dimensional, it holds exactly when $T^*T = I$, where $T^*$ is the [[adjoint|0R9NMSM1ZP]] of $T$.

## Motivation

A change of coordinates should not change the answer to a geometric question.
If you pass from one orthonormal basis of a plane to another, a segment of length $5$ must still have length $5$, and a right angle must stay a right angle.
The maps that guarantee this are the linear isometries, so they are the maps that you may apply freely in a proof about lengths and angles.

The same maps appear in physics and in computing.
The motions of a rigid body about a fixed point are rotations, and a rotation of space is a linear isometry.
In numerical linear algebra, the QR algorithm and least squares solvers multiply by orthogonal matrices because these matrices do not amplify rounding errors.
The [[orthogonal group|WWK2E8BRGF]] and the [[unitary group|VW5H9XFNJB]] collect the linear isometries of $\R^n$ and $\C^n$ onto themselves, and the theory of rotations and reflections grows out of these two groups.

## Notation

Many linear algebra books use the single word *isometry* for a linear isometry.
A linear isometry of a real inner product space onto itself is also called an *orthogonal operator* or an *orthogonal transformation*, and in the complex case a [[unitary operator|MM0EJ2GDE4]].
Watch out: some books, mostly in physics, use "orthogonal transformation" for rotations only, and leave out the reflections.
In metric geometry an [[isometry|02HPP5VCZH]] is any map that keeps distances, linear or not.
Mathlib writes `LinearIsometry` with the notation `E →ₗᵢ[𝕜] F`, and `LinearIsometryEquiv` with the notation `E ≃ₗᵢ[𝕜] F` for the bijective ones.

## Remarks

### A first check by hand

Take the matrix $A = \frac{1}{5}\begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}$ acting on $\R^2$.
For $v = (x, y)$ we get $Av = \frac{1}{5}(3x - 4y, 4x + 3y)$, and we expand the squared length:
$$(3x - 4y)^2 + (4x + 3y)^2 = 9x^2 - 24xy + 16y^2 + 16x^2 + 24xy + 9y^2 = 25(x^2 + y^2).$$
Divide by $25$ to get $\norm{Av}^2 = x^2 + y^2 = \norm{v}^2$.
So $A$ is a linear isometry, and it is the [[rotation|HNY4CPEEJA]] by the angle $\theta$ with $\cos \theta = \tfrac{3}{5}$ and $\sin \theta = \tfrac{4}{5}$.
Check: for $v = (1, 2)$, $Av = (-1, 2)$, and both vectors have length $\sqrt{5}$.

### More examples

A [[reflection|06BRDF3F0E]] in a hyperplane of a real inner product space keeps lengths, since it only reverses the component along one unit normal.
Multiplication by a complex number $z$ with $\abs{z} = 1$ is a linear isometry of $\C$, because $\abs{zw} = \abs{z}\abs{w} = \abs{w}$.
The [[inclusion of the plane in space|X132TDT8X2]], $(x, y) \mapsto (x, y, 0)$, is a linear isometry from $\R^2$ to $\R^3$ that is not onto.
Function spaces have isometries too: on the polynomials of degree at most $2$ with $\ip{p}{q} = \int_{-1}^{1} p q \, dx$, the [[substitution $p(x) \mapsto p(-x)$|W4MHG5MZ1S]] keeps every norm, because the interval is symmetric about $0$.

### What it is not

[[Scaling by $2$|69P6G54T72]] on $\R^2$ is linear and keeps right angles, but it doubles every length.
The orthogonal projection of $\R^2$ onto the $x$-axis is linear, but it sends $(0, 1)$ to $0$.
The shear $(x, y) \mapsto (x + y, y)$ is linear, but it sends $(0, 1)$, of length $1$, to $(1, 1)$, of length $\sqrt{2}$.
A translation $v \mapsto v + a$ with $a \ne 0$ keeps distances, but it is not linear, because it moves $0$.
Each of the first three fails the norm condition, and the last fails linearity.

### The rules you can use

Let $T \colon V \to W$ be a linear isometry.
It is injective, because $Tv = 0$ gives $\norm{v} = \norm{Tv} = 0$.
It keeps distances, because $\norm{Tu - Tv} = \norm{T(u - v)} = \norm{u - v}$.
Between inner product spaces it keeps inner products, by [[polarization|0R7VXTYHYZ]], and so it keeps angles and orthogonality.
For finite-dimensional inner product spaces, [[the equivalent conditions|95ST99SEW7]] reduce the test to a finite check: $T$ is a linear isometry exactly when it sends one orthonormal basis to an orthonormal family, and exactly when $T^*T = I$.
Composites of linear isometries are linear isometries, and so is the inverse of a bijective one.
When $\dim V = \dim W$ is finite, an injective linear map is bijective by the [[rank-nullity theorem|0W4FSW1TVB]], so $T$ is invertible.
In the standard basis, a linear isometry of $\R^n$ has an [[orthogonal matrix|0W02QESPJQ]] and a linear isometry of $\C^n$ has a [[unitary matrix|0AR68JTMDT]].

### Watch out

A linear isometry need not be onto.
For the inclusion $\iota \colon \R^2 \to \R^3$ we have $\iota^*\iota = I$, but $\iota\iota^*$ is the projection onto the plane $z = 0$, not $I$.
Checking a few lengths is not enough either: the shear $(x, y) \mapsto (x + y, y)$ keeps the length of $(1, 0)$ and fails at $(0, 1)$.
Over $\C$, a map can keep all distances and fix $0$ without being complex-linear.
Complex conjugation $z \mapsto \bar z$ on $\C$ keeps $\abs{z - w}$, yet $\overline{i \cdot 1} = -i \ne i \cdot \bar 1$.
It is only real-linear.

### History

The word *isometry* comes from the Greek *isos*, "equal", and *metron*, "measure".
Mazur and Ulam proved in 1932 that a surjective map between real normed spaces that keeps distances is affine.
So such a map is linear when it fixes $0$, by the [[Mazur-Ulam theorem|4J4EW7FXWW]].

### Try it

First, is $T(x, y) = (y, -x)$ a linear isometry of $\R^2$?
Yes: $\norm{T(x, y)}^2 = y^2 + x^2 = \norm{(x, y)}^2$, and $T$ is the rotation by $-90$ degrees.

Second, for which real $c$ is $T(x, y) = (cx, y)$ a linear isometry?
The vector $(1, 0)$ goes to $(c, 0)$, so we need $\abs{c} = 1$, that is $c = 1$ or $c = -1$, and both values work.

## Explanations

### L1 human

A linear isometry moves arrows without changing their lengths.
A quarter turn of the plane about the origin is one.
The arrow $(3, 4)$ has length $5$, since $3^2 + 4^2 = 25$.
After the quarter turn it becomes $(-4, 3)$, and $(-4)^2 + 3^2 = 25$ again.
A mirror in a line through the origin also keeps every length, but doubling every arrow does not.

### L2 human

Here is a typical use: a change of orthonormal basis keeps all lengths.
In $\R^2$ take the orthonormal basis $f_1 = \tfrac{1}{\sqrt 2}(1, 1)$ and $f_2 = \tfrac{1}{\sqrt 2}(-1, 1)$, and the map $T$ that sends a vector to its coordinates in this basis.
The coordinates of $v$ are $(v \cdot f_1, v \cdot f_2)$, so for $v = (3, 1)$ we get
$$T v = \left(\tfrac{3 + 1}{\sqrt 2}, \tfrac{-3 + 1}{\sqrt 2}\right) = \left(2\sqrt 2, -\sqrt 2\right).$$
Check: $\norm{Tv}^2 = 8 + 2 = 10 = 3^2 + 1^2 = \norm{v}^2$.
The matrix of $T$ has rows $f_1$ and $f_2$, which are orthonormal, so $T$ is a linear isometry for every $v$ and not only for this one.
This is why proofs may pass to an adapted orthonormal basis: no length and no angle changes on the way.

### L3 human

The bijective linear isometries are the isomorphisms of inner product spaces.
For a finite-dimensional real inner product space $V$ they form the [[orthogonal group|WWK2E8BRGF]] $O(V)$, and in the complex case the [[unitary group|VW5H9XFNJB]] $U(V)$.
In infinite dimensions $T^*T = I$ no longer gives $TT^* = I$: the unilateral shift on $\ell^2(\N)$ satisfies the first and not the second, as the page on [[unitary operators|DJHVKR63H5]] shows.
Between real normed spaces the Mazur-Ulam theorem makes linearity automatic for surjective distance-preserving maps that fix $0$.
Over a general field one keeps a symmetric bilinear form in place of a norm, and this leads to the orthogonal groups of quadratic forms and to the [[Cartan-Dieudonné theorem|0VMWGYY35Q]].
