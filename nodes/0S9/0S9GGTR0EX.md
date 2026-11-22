---
tag: 0S9GGTR0EX
kind: concept
name: Orthonormal basis
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
specializes: [0KCQ9Y3QKA, 0RW9TNNT87]
uses: [0KCQ9Y3QKA, 0RW9TNNT87]
sources:
  - url: https://en.wikipedia.org/wiki/Orthonormal_basis
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Orthonormal_basis
    locator: Basic formula
  - url: https://en.wikipedia.org/wiki/Gram–Schmidt_process
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 6
same_as:
  wikidata: Q2365325
  wikipedia: Orthonormal basis
inventory: [ZYS2PWM983]
---

## Summary

An orthonormal basis is the best kind of basis for an inner product space: its vectors have length $1$, meet at right angles, and reach every vector of the space.
In such a basis each coordinate is one inner product, and the space computes exactly like $\mathbb{R}^n$ or $\mathbb{C}^n$ with the standard inner product.
Let $V$ be a finite-dimensional inner product space over $\mathbb{R}$ or $\mathbb{C}$.
An *orthonormal basis* of $V$ is a [[basis|0KCQ9Y3QKA]] $(e_1, \dots, e_n)$ of $V$ that is an [[orthonormal family|0RW9TNNT87]]:
$$\ip{e_i}{e_j} = \delta_{ij} \quad \text{for all } i, j.$$
The [[formal definition|0FWJ0VW561]] states the two conditions separately.

## Motivation

In a general basis, the coordinates of a vector come from a linear system.
In the standard basis of $\mathbb{R}^n$ they are just the dot products $x \cdot e_j$, and the length of $x$ is the square root of the sum of the squared coordinates.
An orthonormal basis keeps both facts in every inner product space.
So once you choose one, an abstract space of dimension $n$ with any inner product behaves like $\mathbb{K}^n$ with the standard one.

This is why orthonormal bases are everywhere in applications.
Rotated axes in mechanics and graphics, the frequency components of signal processing and the states of a quantum system are all coordinates in an orthonormal basis.
Later in the area, the spectral theorem finds an orthonormal basis of eigenvectors for a self-adjoint map, and the QR decomposition produces orthonormal bases in numerical work.

## Notation

We write $(e_1, \dots, e_n)$ for an ordered orthonormal basis, and sometimes $\{e_1, \dots, e_n\}$ when the order does not matter.
A square matrix whose columns form an orthonormal basis is called [[orthogonal|0W02QESPJQ]] over $\mathbb{R}$ and [[unitary|0AR68JTMDT]] over $\mathbb{C}$.
Watch the words: an orthogonal matrix has orthonormal columns, not merely orthogonal ones.
Mathlib writes `OrthonormalBasis ι 𝕜 E` for a finite index type `ι`, and `HilbertBasis` for the version in Hilbert spaces.
In functional analysis, "orthonormal basis" often means a maximal orthonormal family, which need not be a basis in the sense of linear algebra.

## Remarks

### Coordinates in a rotated basis

Turn the standard axes of $\mathbb{R}^2$ by $\theta = \pi/6$:
$$e_1 = \left(\tfrac{\sqrt3}{2}, \tfrac12\right), \qquad e_2 = \left(-\tfrac12, \tfrac{\sqrt3}{2}\right).$$
Both have squared length $\tfrac34 + \tfrac14 = 1$, and $e_1 \cdot e_2 = -\tfrac{\sqrt3}{4} + \tfrac{\sqrt3}{4} = 0$.
Two orthonormal vectors in a space of dimension $2$ form a basis, so this is an orthonormal basis.
For $v = (2, 0)$ the coordinates are two dot products:
$$v \cdot e_1 = \sqrt3, \qquad v \cdot e_2 = -1.$$
Check: $\sqrt3\, e_1 - e_2 = \left(\tfrac32 + \tfrac12, \tfrac{\sqrt3}{2} - \tfrac{\sqrt3}{2}\right) = (2, 0)$, and $(\sqrt3)^2 + (-1)^2 = 4 = \norm{v}^2$.
The [[rotated basis of $\mathbb{R}^2$|73MQS3Y26E]] works this out for a second vector too.

### More orthonormal bases

The standard basis of $\mathbb{R}^n$ or $\mathbb{C}^n$ is orthonormal for the standard inner product.
In $\mathbb{C}^2$, the vectors $\tfrac{1}{\sqrt2}(1, i)$ and $\tfrac{1}{\sqrt2}(1, -i)$ form an [[orthonormal basis of $\mathbb{C}^2$|V2B3V8T8TX]], and there the order of the slots in $\ip{v}{e_j}$ starts to matter.
The four [[matrix units|A4HTT7JFD1]] form an orthonormal basis of $M_2(\mathbb{C})$ for the [[trace inner product|JVH9RZ7QAB]].
On $\mathcal{P}_2(\mathbb{R})$ with $\ip{p}{q} = \int_{-1}^{1} p q$, the normalized [[Legendre polynomials|JPDVZM20EX]] form an orthonormal basis.
The columns of each [[orthogonal matrix|0W02QESPJQ]] of size $n$ form an orthonormal basis of $\mathbb{R}^n$, by the [[criterion for orthonormal columns|83QE4F4E4V]].

### What is not an orthonormal basis

The basis $(1, 1)$, $(1, -1)$ of $\mathbb{R}^2$ is orthogonal, but [[not orthonormal|72YCTDMG60]], since both vectors have norm $\sqrt2$.
The single vector $e_1$ in $\mathbb{R}^2$ is an orthonormal family, but it does not span $\mathbb{R}^2$, so it is not a basis.
The standard basis of $\mathbb{R}^2$ is not orthonormal for $\ip{x}{y} = 2x_1 y_1 + x_2 y_2$, since $\ip{e_1}{e_1} = 2$.
So the same vectors can be an orthonormal basis for one inner product and fail for another.

### What an orthonormal basis gives you

Every finite-dimensional inner product space [[has an orthonormal basis|0Y85GYEGSF]], and each orthonormal family extends to one.
To recognize one, count: an orthonormal family of $\dim V$ vectors is a basis, because it is [[linearly independent|0JWM6GJNQW]].
In the basis, $v = \sum_j \ip{v}{e_j} e_j$, by the [[coordinate formula|09DZ8CD1AK]].
[[Parseval's identity|047RFCNVSK]] gives $\ip{u}{v} = \sum_j \ip{u}{e_j}\overline{\ip{v}{e_j}}$, so the coordinate map $V \to \mathbb{K}^n$ preserves inner products.
The change-of-basis matrix between two orthonormal bases is unitary, or orthogonal over $\mathbb{R}$, so its inverse is its conjugate transpose.
In an orthonormal basis, the matrix of the [[adjoint|0R9NMSM1ZP]] of a map is the conjugate transpose of the matrix of the map.

### Watch out

Over $\mathbb{C}$, the coordinate of $v$ is $\ip{v}{e_j}$ with our convention, linear in the first slot.
The other order gives the conjugate: in the basis of $\mathbb{C}^2$ above, the wrong order turns $v = (0, 1)$ into $-v$.
A second slip is to use $\ip{v}{u_j}$ in an orthogonal basis that is not normalized.
For $u_1 = (1, 1)$, $u_2 = (1, -1)$ and $v = (3, 1)$, this gives $2v$; the correct coefficient is $\ip{v}{u_j} / \norm{u_j}^2$.
A third slip is to think that $Q^* Q = I$ gives $Q Q^* = I$ for a matrix that is not square.
For $Q = (1, 0)^{\mathsf{T}}$, $Q^{\mathsf{T}} Q = (1)$, but $Q Q^{\mathsf{T}}$ is the $2 \times 2$ matrix with a single $1$ in the corner.

### History

The [[Gram-Schmidt process|0VT6P0GNQR]], which produces orthonormal bases from any basis, is named after Jørgen Gram and Erhard Schmidt.
Laplace used the same method before either of them.

### Try it

First, show that $\tfrac{1}{\sqrt2}(1, 1)$ and $\tfrac{1}{\sqrt2}(1, -1)$ form an orthonormal basis of $\mathbb{R}^2$ and find the coordinates of $(4, 2)$.
The squared norms are $\tfrac{1 + 1}{2} = 1$, the dot product is $\tfrac{1 - 1}{2} = 0$, and the coordinates are $\tfrac{6}{\sqrt2} = 3\sqrt2$ and $\tfrac{2}{\sqrt2} = \sqrt2$.

Second, in the rotated basis above, find the coordinates of $(0, 1)$.
They are $(0, 1) \cdot e_1 = \tfrac12$ and $(0, 1) \cdot e_2 = \tfrac{\sqrt3}{2}$, and $\tfrac14 + \tfrac34 = 1 = \norm{(0, 1)}^2$.

## Explanations

### L1 human

An orthonormal basis is a set of perpendicular rulers of length $1$ that together reach every point of the space.
The usual axes of the plane are one example, and the same axes after a turn are another.
To find how far a vector goes along one ruler, take its inner product with that ruler.
For the vector $(3, 4)$ and the usual axes this gives $3$ and $4$, and $3^2 + 4^2 = 25$ is the squared length.
No equations need to be solved.

### L2 human

Here is a typical computation in $\mathbb{R}^3$.
Let $e_1 = \tfrac13(1, 2, 2)$, $e_2 = \tfrac13(2, 1, -2)$ and $e_3 = \tfrac13(2, -2, 1)$.
Each has squared entries that add to $9$, so each has norm $1$, and the three pairwise dot products are $\tfrac{2 + 2 - 4}{9}$, $\tfrac{2 - 4 + 2}{9}$ and $\tfrac{4 - 2 - 2}{9}$, all $0$.
Three orthonormal vectors in $\mathbb{R}^3$ form a basis.
For $v = (1, 0, 0)$ the coordinates are the first entries:
$$v \cdot e_1 = \tfrac13, \qquad v \cdot e_2 = \tfrac23, \qquad v \cdot e_3 = \tfrac23.$$
Check the vector:
$$\tfrac13 e_1 + \tfrac23 e_2 + \tfrac23 e_3 = \tfrac19 \left( (1, 2, 2) + (4, 2, -4) + (4, -4, 2) \right) = (1, 0, 0).$$
Check the length: $\tfrac19 + \tfrac49 + \tfrac49 = 1 = \norm{v}^2$.
In matrix terms, the coordinate vector is $Q^{\mathsf{T}} v$, where $Q$ has columns $e_1, e_2, e_3$, so a transpose replaces the inverse that a general basis would need.

### L3 human

A choice of orthonormal basis is the same as a linear isometry from $V$ onto $\mathbb{K}^n$ with the standard inner product, and Mathlib defines `OrthonormalBasis` in this way.
Two orthonormal bases differ by an element of the [[orthogonal group|0TKYAEJ8N7]] or the [[unitary group|0R9R0Y1HDK]], so these groups act simply transitively on the set of ordered orthonormal bases.
The [[QR decomposition|0ERWG4NXQ9]] is the matrix form of the Gram-Schmidt process, and it produces such bases in computation.
The [[real spectral theorem|06J4PXRG22]] says that a self-adjoint map on a real inner product space has an orthonormal basis of eigenvectors.
In an infinite-dimensional [[Hilbert space|HM2HHE3J51]], the analogue is a Hilbert basis, and the finite sums become convergent series.
