---
tag: 0KG4D8AP6G
kind: definition
name: Norm induced by an inner product
msc: [46C05]
defines: 0MFJJV97RJ
uses: [01EK923SKP, 08NYZ2FS6B]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Norm properties
---

## Definition

Let $V$ be an [[inner product space|0QVNCJXRY3]] over $\R$ or $\C$, with inner product $\langle \cdot, \cdot \rangle$.
The *norm induced by the inner product* is the map
$$\norm{x} = \sqrt{\langle x, x \rangle} \qquad (x \in V).$$

## Remarks

It is a [[norm|0V2WP9B1MF]]; the triangle inequality follows from the [[Cauchy–Schwarz inequality|0RFWW56Y22]].
For the dot product on $\R^n$, it is the Euclidean length $\sqrt{x_1^2 + \cdots + x_n^2}$.
It satisfies the [[parallelogram law|026HPGYGS4]], and the [[polarisation identity|05FKHRT0B4]] recovers the inner product from it.

## Explanations

### L1 human

The length of a vector is the square root of its inner product with itself.
In the plane, this is the Pythagorean formula $\sqrt{x^2 + y^2}$.
So every inner product gives a way to measure lengths.
