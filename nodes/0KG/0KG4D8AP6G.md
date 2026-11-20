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

Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{R}$ or $\mathbb{C}$, with inner product $\ip{\cdot}{\cdot}$.
The *norm induced by the inner product* is the map $V \to \mathbb{R}$ given by
$$\norm{x} = \sqrt{\ip{x}{x}} \qquad (x \in V),$$
where $\sqrt{\cdot}$ is the nonnegative [[square root|0VB8BFRABH]].
The square root is defined, because the inner product axioms give $\ip{x}{x} \in \mathbb{R}$ and $\ip{x}{x} \geq 0$.
A vector $u$ with $\norm{u} = 1$ is a *unit vector*.
The *distance* between $x$ and $y$ is $d(x, y) = \norm{x - y}$.

## Notation

- Books write $\norm{x}$, $\norm{x}_2$ or $|x|$.
- With this notation $\ip{x}{x} = \norm{x}^2$, and many formulas use $\norm{x}^2$ in place of $\ip{x}{x}$.

## Remarks

- The induced norm is a [[norm|0V2WP9B1MF]]: positivity and homogeneity follow from the axioms, and the [[triangle inequality|SRN4T2G6AM]] follows from the [[Cauchy-Schwarz inequality|0RFWW56Y22]].
- For the dot product on $\mathbb{R}^n$, it is the Euclidean length $\sqrt{x_1^2 + \dots + x_n^2}$.
- It satisfies the [[parallelogram law|026HPGYGS4]], and the [[polarization identity|05FKHRT0B4]] recovers the inner product from it.
- For $x \neq 0$, the vector $x / \norm{x}$ is a unit vector. This step is [[normalization|M2FAMD9HZN]].

## Explanations

### L1 human

The length of a vector is the square root of its inner product with itself.
In the plane with the dot product, this is the formula $\sqrt{x^2 + y^2}$ of Pythagoras.
For the vector $(1, 2, 2)$ in space, we get $\sqrt{1 + 4 + 4} = 3$.
So every inner product gives a way to measure lengths.

### L2 human

Worked example: normalization in $\mathbb{C}^2$.

1. Let $x = (1 + i, 1)$ with the standard inner product $\ip{x}{y} = x_1\overline{y_1} + x_2\overline{y_2}$.
2. Then $\ip{x}{x} = |1 + i|^2 + |1|^2 = 2 + 1 = 3$, so $\norm{x} = \sqrt{3}$.
3. The unit vector in the direction of $x$ is $u = (1 + i, 1)/\sqrt{3}$.
4. Check: $\norm{u}^2 = \ip{x}{x}/3 = 1$.

The typical use is to produce unit vectors, as in the [[Gram-Schmidt process|0VT6P0GNQR]].
A trap: over $\mathbb{C}$, $\norm{x}^2$ is not $\sum_k x_k^2$.
For $x = (1 + i, 1)$ that sum is $2i + 1$, which is not even real.
