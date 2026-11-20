---
tag: 0MFJJV97RJ
kind: concept
name: Norm induced by an inner product
msc: ["46C05", "15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
specializes: [0V2WP9B1MF]
uses: [0QVNCJXRY3, 0F7FQS6XY6]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Norm properties
  - url: https://en.wikipedia.org/wiki/Norm_(mathematics)
    locator: Euclidean norm
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Summary

Let $V$ be an [[inner product space|0QVNCJXRY3]] over $\mathbb{R}$ or $\mathbb{C}$.
The norm induced by the inner product is the map $V \to \mathbb{R}$ given by $\norm{x} = \sqrt{\ip{x}{x}}$, the nonnegative [[square root|0F7FQS6XY6]].
The square root exists, because $\ip{x}{x}$ is a real number and $\ip{x}{x} \geq 0$.
The [[formal definition|0KG4D8AP6G]] states this.
The induced norm matters because it turns the inner product into lengths and distances, and it is a [[norm|0V2WP9B1MF]] in the sense of analysis.

## Motivation

In $\mathbb{R}^2$ the length of $(x_1, x_2)$ is $\sqrt{x_1^2 + x_2^2}$, by the Pythagorean theorem of plane geometry.
This is $\sqrt{x \cdot x}$, the square root of the dot product of the vector with itself.
In an abstract inner product space there is no picture, but the formula $\sqrt{\ip{x}{x}}$ still makes sense.
So we take it as the definition of length.
The positivity axiom of the inner product is the condition that makes this square root possible.

## Notation

- We write $\norm{x}$, and $\norm{x}_2$ when other norms are present. Some books write $|x|$.
- When two inner products are present, we write $\norm{x}_1 = \sqrt{\ip{x}{x}_1}$ and so on.
- A unit vector is a vector $u$ with $\norm{u} = 1$.
- The distance between $x$ and $y$ is $d(x, y) = \norm{x - y}$.

## Remarks

### Examples

- On $\mathbb{R}^n$ with the dot product, $\norm{x} = \sqrt{x_1^2 + \dots + x_n^2}$ is the [[Euclidean length|0XKBKGTCPC]]. For example, $\norm{(3, 4)} = 5$.
- On $\mathbb{C}^n$ with the [[standard inner product|~a4d9ba49]], $\norm{x} = \sqrt{|x_1|^2 + \dots + |x_n|^2}$. For example, $\norm{(1 + i, 2)} = \sqrt{6}$.
- On $M_2(\mathbb{C})$ with the [[trace inner product|~381c6461]], the induced norm is the [[Frobenius norm|JT8Q204E4R]], the square root of the sum of $|a_{jk}|^2$.
- On $\mathcal{P}_2(\mathbb{R})$ with the [[integral inner product|~8366abd2]], $\norm{t} = \sqrt{\int_0^1 t^2 \, dt} = 1/\sqrt{3}$.

### Non-examples

- The [[maximum norm on $\mathbb{R}^2$|~4a30dace]], $\max(|x_1|, |x_2|)$, is a norm, but no inner product induces it, because it fails the parallelogram law.
- The [[taxicab length|WW2RB40VYX]] $|x_1| + |x_2|$ on $\mathbb{R}^2$ is a norm, but no inner product induces it. For $(1, 0)$ and $(0, 1)$, the parallelogram law would need $4 + 4 = 2 + 2$.
- The map $x \mapsto \ip{x}{x}$, without the square root, is not a norm. On $\mathbb{R}$ with $\ip{x}{y} = xy$, it gives $1$ at $x = 1$ and $4$ at $x = 2$. Homogeneity requires the value $2 \cdot 1 = 2$ at $x = 2$.

### Basic properties

For all $x, y \in V$ and all scalars $a$:

- Positivity: $\norm{x} \geq 0$, and $\norm{x} = 0$ only for $x = 0$, by the positivity axiom of the inner product.
- Homogeneity: $\norm{ax} = |a| \, \norm{x}$, because $\ip{ax}{ax} = a\overline{a}\ip{x}{x} = |a|^2 \norm{x}^2$.
- Expansion of a square: $\norm{x + y}^2 = \norm{x}^2 + 2\operatorname{Re}\ip{x}{y} + \norm{y}^2$, because $\ip{x}{y} + \ip{y}{x} = \ip{x}{y} + \overline{\ip{x}{y}} = 2\operatorname{Re}\ip{x}{y}$.
- [[Normalization|M2FAMD9HZN]]: for $x \neq 0$, the vector $x / \norm{x}$ is a unit vector, by homogeneity with $a = 1/\norm{x}$.
- The [[Cauchy-Schwarz inequality|0RFWW56Y22]] gives $|\ip{x}{y}| \leq \norm{x} \, \norm{y}$.
- The [[triangle inequality|~0cdd82af]] gives $\norm{x + y} \leq \norm{x} + \norm{y}$. With positivity and homogeneity it shows that the induced norm is a norm, so $d(x, y) = \norm{x - y}$ is a distance.
- The induced norm satisfies the [[parallelogram law|026HPGYGS4]], and the [[polarization identity|05FKHRT0B4]] recovers the inner product from it.

### History

In $\mathbb{R}^n$ the induced norm is the Euclidean length, which the sub-area on [[vectors in Euclidean space|VKVAJ94SKZ]] treats.
The general notion appears together with the inner product, so its history is the history of the [[inner product|0NB0AWGJBW]].

### Common errors

- Students write $\norm{x + y} = \norm{x} + \norm{y}$. This holds only when one vector is a nonnegative real multiple of the other.
- Over $\mathbb{C}$, students write $\norm{x}^2 = \sum_k x_k^2$. The correct formula is $\sum_k |x_k|^2$, and for $x = (1, i)$ the wrong one gives $0$.
- Students expand $\norm{x + y}^2$ as $\norm{x}^2 + 2\ip{x}{y} + \norm{y}^2$ over $\mathbb{C}$. The middle term is $2\operatorname{Re}\ip{x}{y}$.

## Explanations

### L1 human

The norm of a vector is its length.
We get it from the inner product: pair the vector with itself, then take the square root.
For the arrow $(3, 4)$ in the plane, the dot product with itself is $9 + 16 = 25$, and the square root is $5$.
Dividing a nonzero vector by its length gives a vector of length $1$ in the same direction.
For $(3, 4)$ this is $(0.6, 0.8)$.

### L2 human

Worked example: the distance between two polynomials.

1. Use $\ip{p}{q} = \int_0^1 p(t) q(t) \, dt$ on $\mathcal{P}_2(\mathbb{R})$.
2. Let $p = t$ and $q = t^2$. Then $p - q = t - t^2$.
3. Compute $\norm{p - q}^2 = \int_0^1 (t - t^2)^2 \, dt = \int_0^1 (t^2 - 2t^3 + t^4) \, dt = \frac13 - \frac12 + \frac15 = \frac{1}{30}$.
4. So $d(p, q) = 1/\sqrt{30}$.
5. The unit vector in the direction of $p$ is $\sqrt{3}\, t$, because $\norm{t} = 1/\sqrt{3}$.

The typical use is to measure an error: the distance from a function to its approximation.
A trap: the norm of a sum is not the sum of the norms.
Here $\norm{t} + \norm{t^2} = 1/\sqrt{3} + 1/\sqrt{5}$, but $\norm{t + t^2}^2 = \frac13 + \frac12 + \frac15 = \frac{31}{30}$.

### L3 human

The induced norm is the bridge from algebra to analysis: it makes each inner product space a normed space and a metric space.
Among all norms, the induced ones are exactly those that satisfy the parallelogram law, by the [[Jordan-von Neumann theorem|46WGVM5VS6]].
The unit sphere of an induced norm on $\mathbb{R}^n$ is an ellipsoid, while the unit sphere of the maximum norm is a cube.
In finite dimension all norms are equivalent, so the topology does not depend on the inner product, but the geometry does.
In infinite dimension the induced norm defines convergence, and completeness for it gives a [[Hilbert space|HM2HHE3J51]].
