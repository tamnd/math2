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

Let $V$ and $W$ be [[normed spaces|03J5RAKB30]] over $\R$ or $\C$.
A *linear isometry* from $V$ to $W$ is a [[linear map|0NRYHJPQG2]] $T \colon V \to W$ with $\norm{Tv} = \norm{v}$ for every $v \in V$.
When $V$ and $W$ are [[inner product spaces|0QVNCJXRY3]] with the induced norms, this condition holds exactly when $T$ keeps inner products.
For finite-dimensional inner product spaces, it holds exactly when $T^*T = I$, where $T^*$ is the [[adjoint|0R9NMSM1ZP]] of $T$.
Linear isometries are the linear maps that keep the whole geometry of a space: lengths, distances, angles and orthogonality.

## Motivation

In the plane, a rotation about the origin and a reflection in a line through the origin move figures without a change of shape or size.
Both maps are linear, and both keep the length of every vector.
Many calculations need a change of coordinates that does not distort lengths, for example a change from one orthonormal basis to another.
The linear isometries are exactly these changes of coordinates.
A bijective linear isometry is an isomorphism of inner product spaces, so it keeps every part of the structure.

## Notation

- A linear isometry from a real inner product space onto itself is also called an *orthogonal operator* or an *orthogonal transformation*.
- A linear isometry from a complex inner product space onto itself is also called a [[unitary operator|MM0EJ2GDE4]].
- Many linear algebra books use the single word *isometry* for a linear isometry.
- In metric geometry, an [[isometry|02HPP5VCZH]] is any map that keeps distances, and it need not be linear.
- Mathlib writes `LinearIsometry` with the notation `E →ₗᵢ[𝕜] F`, and `LinearIsometryEquiv` with the notation `E ≃ₗᵢ[𝕜] F` for the bijective case.

## Remarks

### Examples

- The identity map of a normed space is a linear isometry.
- The [[rotation matrix|HNY4CPEEJA]] $R(\theta)$ gives a linear isometry of $\R^2$, because $(x\cos\theta - y\sin\theta)^2 + (x\sin\theta + y\cos\theta)^2 = x^2 + y^2$.
- A [[reflection|06BRDF3F0E]] in a hyperplane of a real inner product space is a linear isometry.
- [[The inclusion of the plane in space|X132TDT8X2]], $(x, y) \mapsto (x, y, 0)$, is a linear isometry from $\R^2$ to $\R^3$ that is not surjective.
- [[The map $p(x) \mapsto p(-x)$|W4MHG5MZ1S]] on real polynomials of degree at most $2$, with $\ip{p}{q} = \int_{-1}^{1} p(x)q(x)\,dx$, is a linear isometry.
- Multiplication by a complex number $z$ with $\abs{z} = 1$ is a linear isometry of $\C$, because $\abs{zw} = \abs{z}\abs{w} = \abs{w}$.

### Non-examples

- [[Scaling by $2$|69P6G54T72]] on $\R^2$ is linear, but it doubles every length.
- The orthogonal projection of $\R^2$ onto the $x$-axis is linear, but it sends $(0, 1)$ to $0$.
- The shear $(x, y) \mapsto (x + y, y)$ is linear, but it sends $(0, 1)$, of length $1$, to $(1, 1)$, of length $\sqrt{2}$.
- A translation $v \mapsto v + a$ with $a \neq 0$ keeps distances, but it is not linear, because it moves $0$.

### Basic properties

Let $T \colon V \to W$ be a linear isometry.

- $T$ is injective, because $Tv = 0$ gives $\norm{v} = \norm{Tv} = 0$.
- $T$ keeps distances: $\norm{Tu - Tv} = \norm{T(u - v)} = \norm{u - v}$.
- Between inner product spaces, $T$ keeps inner products, by [[polarization|0R7VXTYHYZ]]. So $T$ keeps angles and orthogonality.
- For finite-dimensional inner product spaces, [[the equivalent conditions|95ST99SEW7]] say that $T$ is a linear isometry exactly when it sends an orthonormal basis to an orthonormal family, and exactly when $T^*T = I$.
- The composite of two linear isometries is a linear isometry. The inverse of a bijective linear isometry is a linear isometry.
- If $\dim V = \dim W$ is finite, then $T$ is bijective, by [[the rank-nullity theorem|0W4FSW1TVB]].
- The matrix of a linear isometry of $\R^n$ in the standard basis is an [[orthogonal matrix|0W02QESPJQ]]. The matrix of a linear isometry of $\C^n$ is a [[unitary matrix|0AR68JTMDT]].

### History

The word *isometry* comes from the Greek words *isos*, "equal", and *metron*, "measure".
Mazur and Ulam proved in 1932 that a surjective map between real normed spaces that keeps distances is affine.
So such a map is linear when it fixes $0$, see [[the Mazur-Ulam theorem|4J4EW7FXWW]].

### Common errors

- A linear isometry need not be surjective. The inclusion of $\R^2$ in $\R^3$ is an example, so $T^*T = I$ does not give $TT^* = I$ in general.
- It is not enough to check the lengths of a few vectors. The shear $(x, y) \mapsto (x + y, y)$ keeps the length of $(1, 0)$, but not of $(0, 1)$.
- It is not enough to keep right angles. Scaling by $2$ keeps right angles, but it is not a linear isometry.

## Explanations

### L1 human

A linear isometry moves vectors without a stretch or a squeeze.
A turn of the plane about the origin is an example.
The vector $(3, 4)$ has length $5$, because $3^2 + 4^2 = 25$.
After a quarter turn, it becomes $(-4, 3)$, and this vector also has length $5$.
A mirror image in a line through the origin also keeps all lengths.
To double every vector is not an isometry, because the lengths change.

### L2 human

Worked example: we check that the matrix $A = \frac{1}{5}\begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}$ gives a linear isometry of $\R^2$.

1. For $v = (x, y)$, we have $Av = \frac{1}{5}(3x - 4y, 4x + 3y)$.
2. So $\norm{Av}^2 = \frac{1}{25}\left((3x - 4y)^2 + (4x + 3y)^2\right)$.
3. We expand: $(3x - 4y)^2 + (4x + 3y)^2 = 9x^2 - 24xy + 16y^2 + 16x^2 + 24xy + 9y^2 = 25(x^2 + y^2)$.
4. So $\norm{Av}^2 = x^2 + y^2 = \norm{v}^2$, and $\norm{Av} = \norm{v}$.
5. A shorter test: the columns $\frac{1}{5}(3, 4)$ and $\frac{1}{5}(-4, 3)$ are orthonormal, so $A^TA = I$.

The typical use: in a proof, we change to an orthonormal basis, and the change of basis is a linear isometry, so no length changes.
A trap: a linear isometry need not be onto.
For the inclusion $\iota \colon \R^2 \to \R^3$, we have $\iota^*\iota = I$, but $\iota\iota^* \neq I$.

### L3 human

Linear isometries are the maps of inner product spaces that keep the full structure, and the bijective ones are the isomorphisms.
For a finite-dimensional real inner product space $V$, the bijective linear isometries of $V$ form the [[orthogonal group|WWK2E8BRGF]] $O(V)$.
In the complex case, they form the [[unitary group|VW5H9XFNJB]] $U(V)$.

In infinite dimensions, the conditions $T^*T = I$ and $TT^* = I$ differ.
The unilateral shift on $\ell^2(\N)$ satisfies the first condition and not the second, as the node on [[unitary operators|DJHVKR63H5]] shows.
Between real normed spaces, the Mazur-Ulam theorem says that linearity follows from the other conditions once $0$ is fixed and the map is onto.
Over a general field, one keeps a symmetric bilinear form instead of a norm.
This leads to the orthogonal groups of quadratic forms and to [[the Cartan-Dieudonné theorem|0VMWGYY35Q]].
