---
tag: 0KG4D8AP6G
kind: definition
name: Norm induced by an inner product
msc: ["46C05", "15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
defines: 0MFJJV97RJ
uses: [01EK923SKP, 0VB8BFRABH]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Norm properties
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Definition

The induced norm gives each vector the square root of its inner product with itself as its length.
Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{R}$ or $\mathbb{C}$, with inner product $\ip{\cdot}{\cdot}$.
The *norm induced by the inner product* is the map $V \to \mathbb{R}$ given by
$$\norm{x} = \sqrt{\ip{x}{x}} \qquad (x \in V),$$
where $\sqrt{\cdot}$ is the nonnegative [[square root|0VB8BFRABH]].
A vector $u$ with $\norm{u} = 1$ is a *unit vector*.
The *distance* between $x$ and $y$ is $d(x, y) = \norm{x - y}$.

## Notation

Books write $\norm{x}$, $\norm{x}_2$ or $\abs{x}$.
With this notation $\ip{x}{x} = \norm{x}^2$, and many formulas use $\norm{x}^2$ in place of $\ip{x}{x}$.

## Remarks

The square root needs a real number that is not negative, and the axioms of an inner product supply both.
Conjugate symmetry with $y = x$ gives $\ip{x}{x} = \overline{\ip{x}{x}}$, so $\ip{x}{x}$ is real, and positivity gives $\ip{x}{x} \geq 0$.
The choice of the nonnegative root makes lengths nonnegative.

The result is a [[norm|0V2WP9B1MF]].
Positivity and homogeneity follow from the axioms, and the [[triangle inequality|SRN4T2G6AM]] follows from the [[Cauchy-Schwarz inequality|0RFWW56Y22]].
The induced norm also satisfies the [[parallelogram law|026HPGYGS4]], and the [[polarization identity|05FKHRT0B4]] recovers the inner product from it.
For a nonzero $x$, the vector $x / \norm{x}$ is a unit vector, and this step is [[normalization|M2FAMD9HZN]].

A small example is the dot product on $\mathbb{R}^3$, where $\norm{(1, 2, 2)} = \sqrt{1 + 4 + 4} = 3$.
A case that fails is the same recipe for the form $x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$, which is not an inner product: at $(0, 1)$ the value is $-1$, and it has no real square root.
The concept page on the [[induced norm|0MFJJV97RJ]] gives more examples and the rules.

## Explanations

### L1 human

The length of a vector is the square root of its inner product with itself.
In the plane with the dot product, this is the formula $\sqrt{x^2 + y^2}$ of Pythagoras.
For the vector $(1, 2, 2)$ in space, we get $\sqrt{1 + 4 + 4} = 3$.
So every inner product gives a way to measure lengths.

### L2 human

Here is normalization in $\mathbb{C}^2$ with the standard inner product $\ip{x}{y} = x_1\overline{y_1} + x_2\overline{y_2}$.
Let $x = (1 + i, 1)$.
Then
$$\ip{x}{x} = \abs{1 + i}^2 + \abs{1}^2 = 2 + 1 = 3,$$
so $\norm{x} = \sqrt{3}$, and the unit vector in the direction of $x$ is $u = (1 + i, 1)/\sqrt{3}$.
Check: $\norm{u}^2 = \ip{x}{x}/3 = 1$.
The [[Gram-Schmidt process|0VT6P0GNQR]] uses this step to produce unit vectors.
Watch out: over $\mathbb{C}$, $\norm{x}^2$ is not $\sum_k x_k^2$, and for $x = (1 + i, 1)$ that sum is $(1 + i)^2 + 1 = 1 + 2i$, which is not even real.
