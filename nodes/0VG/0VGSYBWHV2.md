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

An inner product is a scalar-valued pairing of vectors that is linear in one slot, conjugate symmetric and positive on nonzero vectors.
Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and let $V$ be a [[vector space|05EGHEQZAW]] over $\mathbb{K}$.
An *inner product* on $V$ is a map $\ip{\cdot}{\cdot} \colon V \times V \to \mathbb{K}$ such that, for all $x, y, z \in V$ and all $a, b \in \mathbb{K}$, the following hold.

1. Linearity in the first slot: $\ip{ax + by}{z} = a \ip{x}{z} + b \ip{y}{z}$.
2. Conjugate symmetry: $\ip{y}{x} = \overline{\ip{x}{y}}$, where the bar is the [[complex conjugate|0BJV24C4SY]].
3. Positive definiteness: $\ip{x}{x} > 0$ for every $x \neq 0$.

Axiom 3 compares real numbers, because axiom 2 with $y = x$ gives $\ip{x}{x} = \overline{\ip{x}{x}}$, so $\ip{x}{x} \in \mathbb{R}$.

## Notation

Books write $\ip{x}{y}$, $(x, y)$ or $\langle x \mid y \rangle$.
The definition above is linear in the first slot, which is the convention of math2 and of most mathematics books.
Physics books and Mathlib make the inner product linear in the second slot and conjugate-linear in the first, so their value on $(x, y)$ is our $\ip{y}{x}$.
Over $\mathbb{R}$ the two conventions agree, because the conjugate does nothing.

## Remarks

Each axiom has a job.
Axiom 1 makes the pairing compatible with sums and multiples, so that inner products can be computed on a basis and extended.
Axiom 2 replaces the symmetry of the dot product, and together with axiom 1 it forces conjugate-linearity in the second slot:
$$\ip{x}{ay + bz} = \overline{\ip{ay + bz}{x}} = \overline{a\ip{y}{x} + b\ip{z}{x}} = \overline{a}\ip{x}{y} + \overline{b}\ip{x}{z}.$$
Axiom 3 is what makes $\sqrt{\ip{x}{x}}$ a length, and it is the axiom that fails most often in practice.

Axiom 3 cannot be asked at $x = 0$, since axiom 1 with $a = b = 0$ gives $\ip{0}{z} = 0$.
Some books split it into two parts, $\ip{x}{x} \ge 0$ for all $x$ and $\ip{x}{x} = 0$ only for $x = 0$, which says the same thing.
Over $\mathbb{R}$ the three axioms say that $\ip{\cdot}{\cdot}$ is a symmetric bilinear form with $\ip{x}{x} > 0$ for $x \neq 0$.

A small example is $\ip{x}{y} = x_1 \overline{y_1} + 3 x_2 \overline{y_2}$ on $\mathbb{C}^2$, where $\ip{x}{x} = \abs{x_1}^2 + 3\abs{x_2}^2$.
A case that fails axiom 3 is the same formula without bars: at $x = (\sqrt{3}, i)$ it gives $3 + 3i^2 = 0$.
The [[dot product|0S52TNNTH9]] and the [[standard inner product on $\mathbb{C}^n$|TFZ8DYVJ1J]] satisfy all three axioms.
A vector space with a chosen inner product is an [[inner product space|01EK923SKP]], and the concept page on the [[inner product|0NB0AWGJBW]] gives more examples and uses.

## Explanations

### L1 human

An inner product gives a number for each pair of vectors.
It must respect sums and multiples in the first vector.
Swapping the two vectors gives the complex conjugate of the number, and over the real numbers it gives the same number.
A nonzero vector paired with itself must give a positive number.
For the dot product in the plane, the vector $(3, 4)$ with itself gives $9 + 16 = 25$, which is positive.

### L2 human

We test the rule $\ip{x}{y} = x_1 \overline{y_1} + 3 x_2 \overline{y_2}$ on $\mathbb{C}^2$, one axiom at a time.
Axiom 1 holds, since $(ax_1 + bz_1)\overline{y_1} + 3(ax_2 + bz_2)\overline{y_2} = a\ip{x}{y} + b\ip{z}{y}$.
Axiom 2 holds, since the conjugate of a product is the product of the conjugates:
$$\overline{\ip{x}{y}} = \overline{x_1} y_1 + 3 \overline{x_2} y_2 = \ip{y}{x}.$$
Axiom 3 holds, since $\abs{x_1}^2 + 3\abs{x_2}^2$ is positive unless $x_1 = x_2 = 0$.
Now a value: for $x = (1, i)$ and $y = (i, 1)$,
$$\ip{x}{y} = 1 \cdot (-i) + 3 \cdot i \cdot 1 = 2i, \qquad \ip{y}{x} = i \cdot 1 + 3 \cdot 1 \cdot (-i) = -2i.$$
Check: $-2i$ is the conjugate of $2i$, as axiom 2 demands.
Watch out: without the bars the rule fails axiom 3, as the remarks show at $(\sqrt{3}, i)$.
