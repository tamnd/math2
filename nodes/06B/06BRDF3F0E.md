---
tag: 06BRDF3F0E
kind: concept
name: Reflection
aliases: [hyperplane-reflection, linear-reflection]
msc: ["15A04", "51F15"]
topics: [AZS5BPF5H3]
audience: ug1
specializes: [07SJXTWVQW]
uses: [025158VEYZ, 0Q8HZTJC7G, 079D68S3AW]
sources:
  - url: https://en.wikipedia.org/wiki/Reflection_(mathematics)
    locator: Reflection through a hyperplane in n dimensions
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: Reflections
  - url: https://en.wikipedia.org/wiki/Householder_transformation
    locator: Properties
same_as:
  wikidata: Q426221
  wikipedia: Reflection (mathematics)
---

## Summary

Let $V$ be a real inner product space, and let $u \in V$ with $u \neq 0$.
The *reflection* in the hyperplane $u^\perp$ is the linear map
$$s_u(x) = x - 2\frac{\ip{x}{u}}{\ip{u}{u}}u.$$
It fixes each vector of the hyperplane $u^\perp$, and it sends $u$ to $-u$.
It is a [[linear isometry|07SJXTWVQW]] with $s_u^2 = \id$ and $\det s_u = -1$, by [[this theorem|~c91e3beb]].
Reflections generate the [[orthogonal group|~dc22fe40]], and the [[Cartan-Dieudonné theorem|0VMWGYY35Q]] says that $n$ of them suffice for each element of $O(n)$.

## Motivation

A plane mirror through the origin of space keeps each point of the mirror fixed.
It sends each point on the other side to the point at the same distance behind the mirror.
This map keeps all lengths, so it is an isometry, but it changes a right hand into a left hand.
Reflections are the simplest isometries that are not rotations, and every isometry is a product of them.

## Notation

- Books write $s_u$, $\sigma_u$, $R_u$ or $H_u$ for the reflection in $u^\perp$. The vector $u$ is a *normal vector* of the mirror.
- For a unit vector $u \in \R^n$, the matrix of $s_u$ is the *Householder matrix* $I - 2uu^T$, see the [[Householder transformation|JDH0THTVGM]].
- The reflection in a general subspace $W$ is $2P_W - \id$, where $P_W$ is the [[orthogonal projection|0Q8HZTJC7G]]. This topic uses "reflection" for the case of a hyperplane, unless it says otherwise.

## Remarks

### Examples

- In $\R^2$, the reflection in the line at the angle $\alpha$ to the $x$-axis is $S(\alpha) = \begin{pmatrix} \cos 2\alpha & \sin 2\alpha \\ \sin 2\alpha & -\cos 2\alpha \end{pmatrix}$, see [[the classification of O(2)|~233ca0a4]].
- [[The Householder matrix of the vector (1, 2, 2)/3|~c7e61f61]] is the reflection of $\R^3$ in the plane $x + 2y + 2z = 0$.
- [[The map p(x) ↦ p(−x) on polynomials of degree at most 2|~fcfe5c8a]] is the reflection in the even polynomials, for the inner product $\int_{-1}^{1}pq$.
- $\operatorname{diag}(1, \dots, 1, -1)$ is the reflection of $\R^n$ in the hyperplane $x_n = 0$.
- The swap $(x, y) \mapsto (y, x)$ is the reflection of $\R^2$ in the line $y = x$, with normal vector $(1, -1)$.

### Non-examples

- [[The half turn diag(−1, −1, 1)|~0a09fa5d]] is orthogonal and $Q^2 = I$, but it negates a plane, not a line. It is a rotation, not a reflection.
- [[The point reflection −I₃|~f5678826]] has determinant $-1$, but it negates all of $\R^3$, so it is not a reflection in a hyperplane.
- An orthogonal projection $P$ onto a hyperplane fixes the hyperplane, but it sends $u$ to $0$, not to $-u$. It is not invertible.

### Basic properties

- $s_u$ depends only on the line $\R u$: $s_{cu} = s_u$ for $c \neq 0$.
- $s_u$ is self-adjoint and orthogonal, so $s_u^{-1} = s_u^* = s_u$.
- $\det s_u = -1$, because in an orthogonal basis $u, e_2, \dots, e_n$ with $e_k \in u^\perp$, its matrix is $\operatorname{diag}(-1, 1, \dots, 1)$.
- If $\norm{x} = \norm{y}$ and $x \neq y$, then $s_{x - y}$ swaps $x$ and $y$, by [[this theorem|~c91e3beb]].
- The product of two reflections is a rotation. In $\R^2$, $S(\alpha)S(\beta) = R(2(\alpha - \beta))$.
- For $Q \in O(n)$, $Qs_uQ^{-1} = s_{Qu}$. So the conjugates of a reflection are reflections.

### Common errors

- A matrix with $Q^2 = I$ and $\det Q = -1$ need not be a reflection: $-I_3$ is an example. A reflection must fix a hyperplane.
- The formula needs $\ip{u}{u}$ in the denominator. With a vector $u$ that is not a unit vector, $x - 2\ip{x}{u}u$ is not a reflection.
- The vector $u$ is perpendicular to the mirror. It does not lie in the mirror.

## Explanations

### L1 human

A reflection is a mirror image.
The mirror is a line in the plane, or a plane in space, through the origin.
Points on the mirror stay where they are.
Each other point jumps straight across the mirror to the same distance on the other side.
Two mirror images in the same mirror bring every point back.

### L2 human

Worked example: the reflection of $\R^2$ in the line $y = 2x$.

1. The line $y = 2x$ is the set of $x$ with $\ip{x}{u} = 0$ for $u = (2, -1)$, and $\ip{u}{u} = 5$.
2. $s_u(1, 0) = (1, 0) - \frac{2 \cdot 2}{5}(2, -1) = \left(1 - \frac{8}{5}, \frac{4}{5}\right) = \left(-\frac{3}{5}, \frac{4}{5}\right)$.
3. $s_u(0, 1) = (0, 1) - \frac{2 \cdot (-1)}{5}(2, -1) = \left(\frac{4}{5}, \frac{3}{5}\right)$.
4. So the matrix is $\frac{1}{5}\begin{pmatrix} -3 & 4 \\ 4 & 3 \end{pmatrix}$, with determinant $\frac{1}{25}(-9 - 16) = -1$.
5. Check: $s_u(1, 2) = \frac{1}{5}(-3 + 8, 4 + 6) = (1, 2)$, so the point $(1, 2)$ on the line stays fixed.

The typical use: in numerical linear algebra, Householder reflections bring a matrix to triangular form in the QR decomposition.
A trap: $u$ is the normal vector of the mirror, not a vector along the mirror.

### L3 human

The reflections generate $O(n)$, and the finite groups generated by reflections are the finite Coxeter groups, such as the Weyl groups of root systems.
For a nondegenerate symmetric bilinear form $B$ over a field of characteristic not $2$, the same formula $s_u(x) = x - 2\frac{B(x, u)}{B(u, u)}u$ works when $B(u, u) \neq 0$.
The [[Cartan-Dieudonné theorem|0VMWGYY35Q]] then says that $O(B)$ is generated by at most $n$ such reflections.
Reflections in Euclidean geometry, in affine hyperplanes that do not pass through the origin, belong to the area of Euclidean geometry.
