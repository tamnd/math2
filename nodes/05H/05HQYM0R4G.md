---
tag: 05HQYM0R4G
kind: definition
name: Dot product
msc: ["15A63"]
topics: [VKVAJ94SKZ]
audience: school
defines: 0S52TNNTH9
uses: [0XM8BZD76G]
formal:
  - system: lean4
    library: mathlib
    decl: dotProduct
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Dot_product
    locator: Coordinate definition
---

## Definition

Let $n \geq 1$ and let $x = (x_1, \dots, x_n)$ and $y = (y_1, \dots, y_n)$ be vectors of the [[coordinate space|0XM8BZD76G]] $\mathbb{R}^n$.
The dot product of $x$ and $y$ is the real number
$$x \cdot y = \sum_{i=1}^{n} x_i y_i = x_1 y_1 + x_2 y_2 + \dots + x_n y_n.$$

## Notation

Other notations are $\langle x, y \rangle$ and $(x, y)$.
In matrix notation, $x \cdot y = x^{\mathsf{T}} y$ for column vectors $x$ and $y$.
In Mathlib the dot product of two vectors $x, y : \text{Fin } n \to R$ is `dotProduct x y`, written `x ⬝ᵥ y`, for any commutative semiring $R$.

## Remarks

The dot product is symmetric, bilinear and positive definite, so it is an [[inner product|0NB0AWGJBW]] on $\mathbb{R}^n$.
In the plane and in space, $x \cdot y = \|x\| \, \|y\| \cos \theta$, where $\theta$ is the angle between $x$ and $y$; the [[geometric formula|070TXS9AXM]] proves this.
The same formula defines a symmetric bilinear form on $F^n$ for every field $F$, but over $\mathbb{C}$ or a finite field it is not positive.

## Explanations

### L1 human

The dot product multiplies two vectors component by component and adds the results.
For example, $(1, 2, 3) \cdot (4, 5, 6) = 4 + 10 + 18 = 32$.
It is zero exactly when the two vectors are perpendicular, or when one of them is zero.

### L2 human

For $x = (2, -1, 0, 3)$ and $y = (1, 4, 7, 1)$ in $\mathbb{R}^4$:

1. The products of the components are $2$, $-4$, $0$ and $3$.
2. Their sum is $x \cdot y = 1$.

A trap: both vectors must have the same number of components, or the dot product is not defined.
