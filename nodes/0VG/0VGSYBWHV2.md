---
tag: 0VGSYBWHV2
kind: definition
name: Inner product
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
defines: 0NB0AWGJBW
uses: [05EGHEQZAW, 0BJV24C4SY]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Convention variant
  - book: isbn:9783031410253
    locator: Chapter 6
inventory: [HE1J3Q8VXR]
---

## Definition

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and let $V$ be a [[vector space|05EGHEQZAW]] over $\mathbb{K}$.
An *inner product* on $V$ is a map $\ip{\cdot}{\cdot} \colon V \times V \to \mathbb{K}$ such that, for all $x, y, z \in V$ and all $a, b \in \mathbb{K}$:

1. Linearity in the first argument: $\ip{ax + by}{z} = a \ip{x}{z} + b \ip{y}{z}$.
2. Conjugate symmetry: $\ip{y}{x} = \overline{\ip{x}{y}}$, where the bar is the [[complex conjugate|0BJV24C4SY]].
3. Positive definiteness: $\ip{x}{x} > 0$ for every $x \neq 0$.

Axiom 3 is a statement about real numbers, since axiom 2 with $y = x$ gives $\ip{x}{x} = \overline{\ip{x}{x}}$, so $\ip{x}{x} \in \mathbb{R}$.

## Notation

- Books write $\ip{x}{y}$, $(x, y)$ or $\langle x \mid y \rangle$.
- This definition is linear in the first argument. Physicists, and Mathlib, make the inner product linear in the second argument and conjugate-linear in the first.
- The two conventions differ only by the order of the arguments: the physics value $\langle x \mid y \rangle$ is our $\ip{y}{x}$.
- Over $\mathbb{R}$ the two conventions agree, because the conjugate does nothing.

## Remarks

- Axioms 1 and 2 give conjugate-linearity in the second argument: $\ip{x}{ay + bz} = \overline{a}\ip{x}{y} + \overline{b}\ip{x}{z}$.
- Over $\mathbb{R}$, an inner product is a symmetric bilinear form $\ip{\cdot}{\cdot}$ with $\ip{x}{x} > 0$ for $x \neq 0$.
- The axioms imply $\ip{0}{0} = 0$, so positivity cannot hold at $x = 0$. Some books state axiom 3 as two parts: $\ip{x}{x} \geq 0$, and $\ip{x}{x} = 0$ only for $x = 0$.
- The [[dot product|0S52TNNTH9]] on $\mathbb{R}^n$ and the [[standard inner product on $\mathbb{C}^n$|TFZ8DYVJ1J]] satisfy the three axioms.
- A vector space with an inner product is an [[inner product space|01EK923SKP]].

## Explanations

### L1 human

An inner product is a rule that gives a number for each pair of vectors.
It must respect sums and multiples in the first vector.
Swapping the two vectors gives the complex conjugate of the number, and over the real numbers it gives the same number.
A nonzero vector paired with itself must give a positive number.
For the dot product on the plane, the vector $(3, 4)$ paired with itself gives $9 + 16 = 25$, which is positive.

### L2 human

Worked example: we test the rule $\ip{x}{y} = x_1 \overline{y_1} + 3 x_2 \overline{y_2}$ on $\mathbb{C}^2$.

1. Axiom 1: $\ip{ax + bz}{y} = (ax_1 + bz_1)\overline{y_1} + 3(ax_2 + bz_2)\overline{y_2} = a\ip{x}{y} + b\ip{z}{y}$.
2. Axiom 2: $\overline{\ip{x}{y}} = \overline{x_1}y_1 + 3\overline{x_2}y_2 = \ip{y}{x}$, because the conjugate of a product is the product of the conjugates.
3. Axiom 3: $\ip{x}{x} = |x_1|^2 + 3|x_2|^2$, which is positive unless $x_1 = x_2 = 0$.
4. A value: for $x = (1, i)$ and $y = (i, 1)$, we get $\ip{x}{y} = 1 \cdot (-i) + 3 \cdot i \cdot 1 = 2i$, and $\ip{y}{x} = -2i$.

The typical use is to verify that a new formula, on matrices or on functions, is an inner product.
A trap: if we drop the bars and use $x_1 y_1 + 3x_2 y_2$, axiom 3 fails at $x = (\sqrt{3}, i)$, which gives $3 - 3 = 0$.
