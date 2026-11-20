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

Let $V$ be a finite-dimensional inner product space over $\mathbb{R}$ or $\mathbb{C}$.
An orthonormal basis of $V$ is a [[basis|0KCQ9Y3QKA]] $(e_1, \dots, e_n)$ of $V$ that is an [[orthonormal family|0RW9TNNT87]]: $\ip{e_i}{e_j} = \delta_{ij}$ for all $i, j$.
The [[formal definition|0FWJ0VW561]] states this.
Orthonormal bases matter because in them coordinates are inner products, and inner products of vectors are the standard inner products of their coordinates.

## Motivation

In a general basis, the coordinates of a vector come from a linear system.
In the standard basis of $\mathbb{R}^n$ they are just the dot products $x \cdot e_j$.
An orthonormal basis is a basis that keeps this property in every inner product space.
With it, an abstract inner product space of dimension $n$ behaves exactly like $\mathbb{R}^n$ or $\mathbb{C}^n$ with the standard inner product.

## Notation

- We write $(e_1, \dots, e_n)$ for an ordered orthonormal basis, and sometimes $\set{e_1, \dots, e_n}$.
- In matrix language, a square matrix with orthonormal columns is called [[orthogonal|0W02QESPJQ]] over $\mathbb{R}$ and [[unitary|0AR68JTMDT]] over $\mathbb{C}$. An "orthogonal matrix" has orthonormal columns, not only orthogonal ones.
- Mathlib writes `OrthonormalBasis ι 𝕜 E` for a finite index type `ι`, and `HilbertBasis` for the version in Hilbert spaces.
- In functional analysis, "orthonormal basis" often means a maximal orthonormal family, which need not be a basis in the sense of linear algebra.

## Remarks

### Examples

- The standard basis of $\mathbb{R}^n$ or $\mathbb{C}^n$ is orthonormal for the standard inner product.
- For each angle $\theta$, the vectors $(\cos\theta, \sin\theta)$ and $(-\sin\theta, \cos\theta)$ form an orthonormal basis of $\mathbb{R}^2$. The [[rotated basis for $\theta = \pi/6$|73MQS3Y26E]] computes coordinates in it.
- The vectors $\frac{1}{\sqrt2}(1, i)$ and $\frac{1}{\sqrt2}(1, -i)$ form an [[orthonormal basis of $\mathbb{C}^2$|V2B3V8T8TX]].
- The four [[matrix units|A4HTT7JFD1]] form an orthonormal basis of $M_2(\mathbb{C})$ for the [[trace inner product|JVH9RZ7QAB]].
- The normalized [[Legendre polynomials|JPDVZM20EX]] $e_0, e_1, e_2$ form an orthonormal basis of $\mathcal{P}_2(\mathbb{R})$ for $\int_{-1}^1 pq$.
- The columns of each [[orthogonal matrix|0W02QESPJQ]] of size $n$ form an orthonormal basis of $\mathbb{R}^n$, by the [[criterion for orthonormal columns|83QE4F4E4V]].

### Non-examples

- The basis $(1, 1)$, $(1, -1)$ of $\mathbb{R}^2$ is orthogonal, but [[not orthonormal|72YCTDMG60]], since both vectors have norm $\sqrt2$.
- The single vector $e_1$ in $\mathbb{R}^2$ is an orthonormal family, but it does not span $\mathbb{R}^2$. So it is not a basis.
- The standard basis of $\mathbb{R}^2$ is not orthonormal for $\ip{x}{y} = 2x_1 y_1 + x_2 y_2$, since $\ip{e_1}{e_1} = 2$.

### Basic properties

- Every finite-dimensional inner product space [[has an orthonormal basis|0Y85GYEGSF]], and each orthonormal family extends to one.
- In an orthonormal basis, $v = \sum_j \ip{v}{e_j} e_j$, by the [[coordinate formula|09DZ8CD1AK]].
- [[Parseval's identity|047RFCNVSK]] gives $\ip{u}{v} = \sum_j \ip{u}{e_j}\overline{\ip{v}{e_j}}$, so the coordinate map is an isometry onto $\mathbb{K}^n$.
- An orthonormal family of $\dim V$ vectors is an orthonormal basis, because it is [[linearly independent|0JWM6GJNQW]].
- The change-of-basis matrix between two orthonormal bases is unitary, or orthogonal over $\mathbb{R}$.
- In an orthonormal basis, the matrix of the [[adjoint|0R9NMSM1ZP]] of a map is the conjugate transpose of the matrix of the map.

### History

The [[Gram-Schmidt process|0VT6P0GNQR]], which produces orthonormal bases, is named after Gram and Schmidt.
According to the Wikipedia article on the process, Laplace knew the method before Gram and Schmidt.

### Common errors

- Over $\mathbb{C}$, students compute the coordinate as $\ip{e_j}{v}$. With our convention the coordinate is $\ip{v}{e_j}$, and the other order gives its conjugate.
- Students use $a_j = \ip{v}{u_j}$ in an orthogonal basis that is not normalized. The correct formula is $a_j = \ip{v}{u_j} / \norm{u_j}^2$.
- Students think that $Q^* Q = I$ implies $Q Q^* = I$ for a non-square $Q$. This holds only for square matrices.

## Explanations

### L1 human

An orthonormal basis is a set of perpendicular arrows of length $1$ that reaches every vector of the space.
The usual axes of the plane are one example, and the same axes after a rotation are another.
To find how far a vector goes along one axis, take its inner product with that axis.
No equations need to be solved.

### L2 human

Worked example: we find coordinates in an orthonormal basis of $\mathbb{R}^3$.

1. Let $e_1 = \frac13(1, 2, 2)$, $e_2 = \frac13(2, 1, -2)$ and $e_3 = \frac13(2, -2, 1)$. These three vectors are orthonormal, so they form a basis of $\mathbb{R}^3$.
2. Let $v = (1, 0, 0)$. Its coordinates are $v \cdot e_1 = \frac13$, $v \cdot e_2 = \frac23$ and $v \cdot e_3 = \frac23$.
3. Check: $\frac13 e_1 + \frac23 e_2 + \frac23 e_3 = \frac19\left((1, 2, 2) + (4, 2, -4) + (4, -4, 2)\right) = (1, 0, 0)$.
4. Check the norm: $\frac19 + \frac49 + \frac49 = 1 = \norm{v}^2$.

The typical use is to change coordinates with a transpose instead of an inverse.
A trap: an "orthogonal matrix" must have unit columns, not only orthogonal columns.

### L3 human

A choice of orthonormal basis is the same as a linear isometry $V \to \mathbb{K}^n$ onto the standard space, and Mathlib defines `OrthonormalBasis` in this way.
Two orthonormal bases differ by an element of the [[orthogonal group|0TKYAEJ8N7]] or the [[unitary group|0R9R0Y1HDK]].
The [[QR decomposition|0ERWG4NXQ9]] is the matrix form of the Gram-Schmidt process, and it produces such bases in computation.
The [[spectral theorem|06J4PXRG22]] says that a self-adjoint map has an orthonormal basis of eigenvectors.
In an infinite-dimensional [[Hilbert space|HM2HHE3J51]], the analogue is a Hilbert basis, and the sums become convergent series.
