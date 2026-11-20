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

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
An inner product space over $\mathbb{K}$ is a pair $(V, \ip{\cdot}{\cdot})$.
Here $V$ is a [[vector space|000AYPA9AJ]] over $\mathbb{K}$, and $\ip{\cdot}{\cdot}$ is an [[inner product|0NB0AWGJBW]] on $V$.
The [[formal definition|01EK923SKP]] states this.
A real inner product space of finite dimension is a Euclidean space, and a complex one is a unitary space.
Inner product spaces matter because the geometry of the plane, with lengths, angles, projections and right triangles, works in each of them.

## Motivation

Linear algebra over $\mathbb{R}$ or $\mathbb{C}$ alone has no lengths and no angles.
For example, a vector space does not say which bases are "perpendicular".
Many problems need this extra structure.
Examples are best approximation by a subspace, diagonalization of symmetric matrices, and expansion of functions in series.
The inner product space is the smallest structure where these problems make sense.
It adds to a vector space one map, with three axioms, and nothing else.

## Notation

- We write $V$ for the space when the inner product is fixed, and $(V, \ip{\cdot}{\cdot})$ when we need to name it.
- Other names: pre-Hilbert space, and, over $\mathbb{C}$, unitary space. Some books call every real inner product space of finite dimension a Euclidean space.
- In Mathlib, `InnerProductSpace 𝕜 E` is a class on a normed space `E`. It asks for an inner product with $\norm{x}^2 = \operatorname{Re}\langle x, x \rangle$, and Mathlib's `inner` is conjugate-linear in the first argument.

## Remarks

### Examples

- The space $\mathbb{R}^n$ with the [[dot product|0S52TNNTH9]] is a Euclidean space. It is the model [[Euclidean space|0XPR1E85W0]].
- The space $\mathbb{C}^n$ with the [[standard inner product|TFZ8DYVJ1J]] $\sum_k x_k \overline{y_k}$ is a unitary space.
- The space $M_2(\mathbb{C})$ with the [[trace inner product|JVH9RZ7QAB]] $\tr(B^* A)$ is a unitary space of dimension $4$.
- The space $\mathcal{P}_2(\mathbb{R})$ with the [[integral inner product|W6NJ22XGWT]] $\int_0^1 pq$ is a Euclidean space of dimension $3$.
- Every subspace $U$ of an inner product space is an inner product space with the restricted inner product. The reason is that the three axioms hold for all vectors of $V$.

### Non-examples

- The plane $\mathbb{R}^2$ with the [[maximum norm|J5V8HEYXCM]] is a normed space, but no inner product induces this norm: the parallelogram law fails.
- The space $\mathbb{C}^2$ with the [[bilinear form $x_1 y_1 + x_2 y_2$|3W8AFC4A9P]] is not an inner product space: the form gives $0$ on $(1, i)$.
- The plane $\mathbb{R}^2$ with the [[Minkowski form|TFGECQ5C32]] is not an inner product space: the form gives $0$ on $(1, 1)$.

### Basic properties

- Each inner product space has the [[induced norm|0MFJJV97RJ]] $\norm{x} = \sqrt{\ip{x}{x}}$, and so a distance $d(x, y) = \norm{x - y}$.
- The [[Cauchy-Schwarz inequality|0RFWW56Y22]], the [[triangle inequality|SRN4T2G6AM]], the [[parallelogram law|026HPGYGS4]] and the [[Pythagorean theorem|0BVTDM872V]] hold in every inner product space.
- Each inner product space of finite dimension has an [[orthonormal basis|0Y85GYEGSF]].
- So each real inner product space of dimension $n$ is isometric to $\mathbb{R}^n$ with the dot product. Each complex one is isometric to $\mathbb{C}^n$ with the standard inner product. The [[coordinates in an orthonormal basis|09DZ8CD1AK]] give the isometry.
- An inner product space that is complete for the induced norm is a [[Hilbert space|HM2HHE3J51]]. Every inner product space of finite dimension is complete, so it is a Hilbert space. Functional analysis studies the infinite-dimensional ones.

### History

The Wikipedia article on inner product spaces states that Peano first used a vector space with an inner product, in 1898.

### Common errors

- Students treat "inner product space" as a property of the set $V$ alone. The same vector space carries many inner products, with different lengths and different right angles.
- Students assume that every norm comes from an inner product. The maximum norm on $\mathbb{R}^2$ does not.
- Students use the real formula $\sum_k x_k y_k$ on $\mathbb{C}^n$. It is not an inner product there.

## Explanations

### L1 human

An inner product space is a space of vectors with a rule to measure lengths and angles.
The plane with the usual dot product is the first example.
In this plane the vector $(3, 4)$ has length $5$, and the vectors $(1, 0)$ and $(0, 1)$ make a right angle.
Other spaces, such as spaces of polynomials, also have such rules.
Then the usual facts of geometry, such as the theorem of Pythagoras, hold there too.

### L2 human

Worked example: one vector space with two inner products.

1. On $\mathbb{R}^2$ take the dot product $\ip{x}{y}_1 = x_1 y_1 + x_2 y_2$.
2. Also take $\ip{x}{y}_2 = 2x_1 y_1 + x_2 y_2$. It is an inner product, because $\ip{x}{x}_2 = 2x_1^2 + x_2^2 > 0$ for $x \neq 0$.
3. The vector $v = (1, 1)$ has length $\sqrt{2}$ in the first space and $\sqrt{3}$ in the second.
4. The vectors $(1, 1)$ and $(1, -1)$ are orthogonal in the first space, since $1 - 1 = 0$, but not in the second, since $2 - 1 = 1$.

The typical use is to choose an inner product that suits a problem, for example a weighted one in statistics.
A trap: a statement such as "the basis is orthonormal" has no meaning until we name the inner product.

### L3 human

An inner product space is a vector space with a reduction of its structure group.
The linear maps that preserve the inner product form the [[orthogonal group|0TKYAEJ8N7]] or the [[unitary group|0R9R0Y1HDK]].
In finite dimension there is only one inner product space of each dimension over each field, up to isometry.
The reason is that each one has an orthonormal basis.
So the theory in finite dimension is the study of $\mathbb{R}^n$ and $\mathbb{C}^n$ with their standard inner products.
It also studies the choice of the inner product on a given space.
In infinite dimension, completeness splits the theory.
The complete spaces are [[Hilbert spaces|HM2HHE3J51]].
The incomplete ones, such as the polynomials with $\int_0^1 pq$, are dense subspaces of Hilbert spaces.
Later sub-areas use the structure: [[orthogonal projection|0B8KZRT28M]], [[adjoints|0R9NMSM1ZP]] and the spectral theorem all need an inner product.
