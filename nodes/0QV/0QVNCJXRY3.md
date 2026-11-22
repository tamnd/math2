---
tag: 0QVNCJXRY3
kind: concept
name: Inner product space
aliases: [pre-hilbert-space]
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
specializes: [000AYPA9AJ]
uses: [0NB0AWGJBW]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 6
same_as:
  wikidata: Q214159
  wikipedia: Inner product space
inventory: [Z2P723Z1AG]
---

## Summary

An inner product space is a vector space together with one chosen way to measure lengths and angles.
Once the choice is made, plane geometry works in the space: right triangles, projections and the theorem of Pythagoras.
Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
An *inner product space* over $\mathbb{K}$ is a pair $(V, \ip{\cdot}{\cdot})$, where $V$ is a [[vector space|000AYPA9AJ]] over $\mathbb{K}$ and $\ip{\cdot}{\cdot}$ is an [[inner product|0NB0AWGJBW]] on $V$.
A real inner product space of finite dimension is called a *Euclidean space*, and a complex one is called a *unitary space*.
The [[formal definition|01EK923SKP]] states this.

## Motivation

A bare vector space knows sums and multiples, but it does not know lengths or right angles.
In $\mathbb{R}^2$ as a vector space, the bases $(1, 0), (0, 1)$ and $(1, 0), (1, 1)$ are equally good, and nothing says that the first one is "perpendicular".
Many problems need that extra knowledge.
Fitting a line to data asks for the closest point of a subspace, diagonalizing a symmetric matrix uses perpendicular eigenvectors, and a Fourier series expands a function along perpendicular waves.

The inner product space is the smallest structure where these problems make sense.
It adds one map with three axioms to a vector space, and nothing else.
The rest of the sub-area develops what follows from that one map, and the later sub-areas on [[orthogonal projection|0B8KZRT28M]] and [[adjoints|0R9NMSM1ZP]] build on it.

## Notation

We write $V$ alone when the inner product is fixed, and $(V, \ip{\cdot}{\cdot})$ when we need to name it.
Other names in books are *pre-Hilbert space* and, over $\mathbb{C}$, *unitary space*, and some books say Euclidean space for every real inner product space of finite dimension.
In Mathlib, `InnerProductSpace 𝕜 E` is a class on a normed space `E` that asks for an inner product with $\norm{x}^2 = \operatorname{Re}\langle x, x \rangle$.
Watch out: Mathlib's `inner` is conjugate-linear in the first slot, while math2 puts the conjugate on the second slot.

## Remarks

### Four spaces with an inner product

The model Euclidean space is $\mathbb{R}^n$ with the [[dot product|0S52TNNTH9]], the [[Euclidean space|0XPR1E85W0]] of school geometry.
The model unitary space is $\mathbb{C}^n$ with the [[standard inner product|TFZ8DYVJ1J]] $\sum_k x_k \overline{y_k}$.
The space $M_2(\mathbb{C})$ with the [[trace inner product|JVH9RZ7QAB]] $\tr(B^* A)$ is a unitary space of dimension $4$, and $\mathcal{P}_2(\mathbb{R})$ with the [[integral inner product|W6NJ22XGWT]] $\int_0^1 pq$ is a Euclidean space of dimension $3$.

Every subspace $U$ of an inner product space is again an inner product space, with the restricted inner product.
The three axioms hold for all vectors of $V$, so they hold for the vectors of $U$.
For example, the plane $U = \{x \in \mathbb{R}^3 : x_1 + x_2 + x_3 = 0\}$ with the dot product is a Euclidean space of dimension $2$.

### One space, two geometries

The inner product is part of the data, and changing it changes the geometry.
On $\mathbb{R}^2$ compare the dot product with $\ip{x}{y}_2 = 2x_1 y_1 + x_2 y_2$.
The vector $(1, 1)$ has square length $1 + 1 = 2$ for the first and $2 + 1 = 3$ for the second.
The vectors $(1, 1)$ and $(1, -1)$ give
$$1 \cdot 1 + 1 \cdot (-1) = 0, \qquad 2 \cdot 1 \cdot 1 + 1 \cdot (-1) = 1,$$
so they are perpendicular in the first space and not in the second.

### What it is not

The plane with the [[maximum norm|J5V8HEYXCM]] $\max(\abs{x_1}, \abs{x_2})$ has lengths, but no inner product gives these lengths, because the parallelogram law fails.
The space $\mathbb{C}^2$ with the [[bilinear form $x_1 y_1 + x_2 y_2$|3W8AFC4A9P]] is not an inner product space, since the form gives $0$ on $(1, i)$.
The plane with the [[Minkowski form|TFGECQ5C32]] $x_1 y_1 - x_2 y_2$ is not one either, since the form gives $0$ on $(1, 1)$.

### What every inner product space has

Each inner product space has the [[induced norm|0MFJJV97RJ]] $\norm{x} = \sqrt{\ip{x}{x}}$ and the distance $d(x, y) = \norm{x - y}$.
The [[Cauchy-Schwarz inequality|0RFWW56Y22]], the [[triangle inequality|SRN4T2G6AM]], the [[parallelogram law|026HPGYGS4]] and the [[Pythagorean theorem|0BVTDM872V]] hold in all of them, because their proofs use only the axioms.
In finite dimension there is always an [[orthonormal basis|0Y85GYEGSF]], and the [[coordinates in an orthonormal basis|09DZ8CD1AK]] turn the inner product into the standard one.
So each real inner product space of dimension $n$ is isometric to $\mathbb{R}^n$ with the dot product, and each complex one to $\mathbb{C}^n$ with the standard inner product.
An inner product space that is complete for the induced norm is a [[Hilbert space|HM2HHE3J51]], and every inner product space of finite dimension is complete.

### Watch out

An inner product space is not a property of the set $V$ alone.
A sentence such as "this basis is orthonormal" has no meaning until you name the inner product, as the two geometries above show.
A second trap is to assume that every way of measuring length comes from an inner product; the maximum norm shows that this is false.

### History

The name Hilbert space recalls Hilbert's work on integral equations in the early 1900s, where sequences with a finite sum of squares played the role of vectors.
Von Neumann gave the abstract axioms of a Hilbert space in the late 1920s, as a setting for quantum mechanics.

### Try it

First, is the line $\{(t, 2t) : t \in \mathbb{R}\}$ with the dot product an inner product space, and what is the length of $(1, 2)$?
Yes, since it is a subspace of $\mathbb{R}^2$, and the length is $\sqrt{1 + 4} = \sqrt{5}$.

Second, find a nonzero vector that is perpendicular to $(1, 1)$ for $\ip{x}{y}_2 = 2x_1 y_1 + x_2 y_2$.
You need $2y_1 + y_2 = 0$, so $(1, -2)$ works, since $2 \cdot 1 + 1 \cdot (-2) = 0$.

## Explanations

### L1 human

An inner product space is a space of vectors with a rule to measure lengths and angles.
The plane with the usual dot product is the first example.
In this plane the vector $(3, 4)$ has length $5$, and the vectors $(1, 0)$ and $(0, 1)$ make a right angle.
Other spaces, such as spaces of polynomials, also have such rules.
Then the usual facts of geometry, such as the theorem of Pythagoras, hold there too.

### L2 human

Here is a typical use: a weighted inner product for data.
Suppose two measurements are recorded as $x = (x_1, x_2)$, and the first one is twice as reliable as the second.
A statistician may then use $\ip{x}{y}_2 = 2x_1 y_1 + x_2 y_2$, which counts the first coordinate twice.
Compare the two error vectors $e = (1.5, 0)$ and $e' = (0, 2)$.
For the dot product their square sizes are
$$e \cdot e = 2.25, \qquad e' \cdot e' = 4,$$
so $e$ is the smaller error.
For the weighted inner product they are
$$\ip{e}{e}_2 = 2 \cdot 2.25 = 4.5, \qquad \ip{e'}{e'}_2 = 4,$$
so now $e$ is the larger error, because it sits in the reliable coordinate.
Choosing the inner product is part of modeling the problem.
Watch out: a statement about lengths or right angles always refers to one inner product, so name it.

### L3 human

The linear maps of $V$ that keep the inner product form the [[orthogonal group|0TKYAEJ8N7]] in the real case and the [[unitary group|0R9R0Y1HDK]] in the complex case.
In finite dimension there is, up to isometry, only one inner product space of each dimension over each of $\mathbb{R}$ and $\mathbb{C}$, because each has an orthonormal basis.
So finite-dimensional theory is the study of $\mathbb{R}^n$ and $\mathbb{C}^n$ with their standard inner products, and of the choice of an inner product on a given space.
In infinite dimension completeness splits the theory.
The complete spaces are [[Hilbert spaces|HM2HHE3J51]], and an incomplete one such as the polynomials with $\int_0^1 pq$ sits as a dense subspace of its completion.
Later sub-areas need the structure: [[orthogonal projection|0B8KZRT28M]], [[adjoints|0R9NMSM1ZP]] and the spectral theorem all use an inner product.
