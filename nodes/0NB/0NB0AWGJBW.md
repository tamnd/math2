---
tag: 0NB0AWGJBW
kind: concept
name: Inner product
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
uses: [000AYPA9AJ, 0FTH2E9TAS]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Convention variant
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 6
inventory: [HE1J3Q8VXR]
---

## Summary

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and let $V$ be a [[vector space|000AYPA9AJ]] over $\mathbb{K}$.
An inner product on $V$ is a map $V \times V \to \mathbb{K}$, $(x, y) \mapsto \ip{x}{y}$, with three properties for all $x, y, z \in V$ and all $a, b \in \mathbb{K}$.
It is linear in the first argument: $\ip{ax + by}{z} = a\ip{x}{z} + b\ip{y}{z}$.
It is conjugate symmetric: $\ip{y}{x} = \overline{\ip{x}{y}}$, where the bar is the [[complex conjugate|0FTH2E9TAS]].
It is positive definite: $\ip{x}{x} > 0$ for every $x \neq 0$.
The [[formal definition|0VGSYBWHV2]] states the same axioms.
The inner product matters because it gives lengths, angles and orthogonality in any vector space, not only in $\mathbb{R}^2$ and $\mathbb{R}^3$.

## Motivation

The [[dot product|0S52TNNTH9]] on $\mathbb{R}^n$ gives the length of a vector and the angle between two vectors.
Many proofs about the dot product use only three facts: symmetry, linearity in each factor, and $v \cdot v > 0$ for $v \neq 0$.
So any map with these three properties gives the same geometry.
Spaces of polynomials, of functions and of matrices carry such maps, and then the geometry of $\mathbb{R}^n$ applies to them.
Over $\mathbb{C}$ the plain formula $\sum_k x_k y_k$ fails, because $(1, i)$ would get the square length $1 + i^2 = 0$.
The conjugate in $\sum_k x_k \overline{y_k}$ repairs this, since $x_k \overline{x_k} = |x_k|^2 \geq 0$.
This is the reason for conjugate symmetry in place of symmetry.

## Notation

- Common symbols are $\ip{x}{y}$, $(x, y)$, $\langle x \mid y \rangle$ and, on $\mathbb{R}^n$, $x \cdot y$.
- In this tree, a complex inner product is linear in the first argument and conjugate-linear in the second. Most books of mathematics use this convention.
- Physics, engineering and computer science make the inner product linear in the second argument and conjugate-linear in the first. This convention comes from the [[bra-ket notation|ZPPGSXJ45B]] of Dirac.
- Mathlib also makes `inner` conjugate-linear in the first argument. So the Mathlib value $\langle x, y \rangle$ is our $\ip{y}{x}$.
- When two inner products are present, a subscript names each one, for example $\ip{x}{y}_A$.

## Remarks

### Examples

- The [[dot product|0S52TNNTH9]] on $\mathbb{R}^n$ is an inner product. Sub-area 1 checks the three axioms.
- The [[standard inner product on $\mathbb{C}^n$|TFZ8DYVJ1J]], $\ip{x}{y} = \sum_k x_k \overline{y_k}$, is an inner product, because $\ip{x}{x} = \sum_k |x_k|^2$.
- On $\mathbb{R}^2$, the formula $\ip{x}{y} = 2x_1 y_1 + x_2 y_2$ is an inner product, because $\ip{x}{x} = 2x_1^2 + x_2^2$.
- The [[trace inner product|JVH9RZ7QAB]] $\ip{A}{B} = \tr(B^* A)$ on $2 \times 2$ complex matrices is an inner product, because $\ip{A}{A}$ is the sum of the $|a_{jk}|^2$.
- The [[integral inner product on polynomials|W6NJ22XGWT]] $\ip{p}{q} = \int_0^1 p(t) q(t) \, dt$ is an inner product, because a nonzero polynomial is not zero on a whole interval.
- For a [[positive definite matrix|0KX66CZMBB]] $A$, the formula $\ip{x}{y} = y^* A x$ is an inner product on $\mathbb{C}^n$, and every inner product on $\mathbb{C}^n$ has this form.

### Non-examples

- The [[symmetric bilinear form $x_1 y_1 + x_2 y_2$ on $\mathbb{C}^2$|3W8AFC4A9P]] is not an inner product: it is not conjugate symmetric, and it gives $0$ on $(1, i)$.
- The [[Minkowski form|TFGECQ5C32]] $x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$ is not an inner product: positivity fails at $(1, 1)$.
- On $\mathbb{R}^2$, the form $\ip{x}{y} = x_1 y_1$ is symmetric and bilinear, but it is not positive definite: it gives $0$ on $(0, 1)$.
- The map $(x, y) \mapsto \norm{x} \, \norm{y}$ on $\mathbb{R}^2$ is not an inner product: it is not additive. For $x = (1, 0)$, $x' = (-1, 0)$ and $y = (1, 0)$, it gives $0$ on $(x + x', y)$, but $1 + 1 = 2$ on the two pairs $(x, y)$ and $(x', y)$.

### Basic properties

For all $x, y, z \in V$ and $a \in \mathbb{K}$:

- The inner product is conjugate-linear in the second argument: $\ip{x}{ay + z} = \overline{a}\ip{x}{y} + \ip{x}{z}$. Apply conjugate symmetry, then linearity in the first argument, then conjugate symmetry again.
- $\ip{0}{y} = 0$ and $\ip{x}{0} = 0$, because $\ip{0}{y} = \ip{0 \cdot 0}{y} = 0 \cdot \ip{0}{y}$.
- $\ip{x}{x}$ is a real number, because conjugate symmetry with $y = x$ gives $\ip{x}{x} = \overline{\ip{x}{x}}$.
- If $\ip{x}{y} = 0$ for all $y \in V$, then $x = 0$: take $y = x$ and use positivity.
- Over $\mathbb{R}$, an inner product is the same as a positive definite [[symmetric bilinear form|0AXZNE5XNH]]. Over $\mathbb{C}$, it is the same as a positive definite [[Hermitian form|48P4A1CX85]].
- The [[Cauchy-Schwarz inequality|0RFWW56Y22]] gives $|\ip{x}{y}| \leq \norm{x} \, \norm{y}$ for the [[induced norm|0MFJJV97RJ]].

### History

Peano was the first to use a vector space with an inner product, in 1898, according to the Wikipedia article on inner product spaces.
The same article states that the convention of linearity in the second argument comes from the bra-ket notation of Dirac.

### Common errors

- Students forget the conjugate over $\mathbb{C}$ and write $\ip{x}{ay} = a\ip{x}{y}$. The correct rule is $\ip{x}{ay} = \overline{a}\ip{x}{y}$.
- Students mix the two conventions. A formula from a physics book, such as a projection formula, can then put the conjugate on the wrong factor.
- Students check positivity only on basis vectors. The form $x_1 y_1 - 2x_1 y_2 - 2x_2 y_1 + x_2 y_2$ gives $1$ on $(1, 0)$ and on $(0, 1)$, but $-2$ on $(1, 1)$.

## Explanations

### L1 human

An inner product is a rule that takes two vectors and gives one number.
It works like the dot product of arrows in the plane.
The number of a vector with itself is the square of its length, so it is positive for every nonzero vector.
For example, with the rule "two times the first product plus the second product", the vector $(1, 1)$ gets $2 \cdot 1 + 1 = 3$.
So its length is $\sqrt{3}$ for this rule, and not $\sqrt{2}$ as for the dot product.
Different inner products thus give different lengths and different right angles on the same space.

### L2 human

Worked example: we check that $\ip{x}{y} = 2x_1 y_1 + x_2 y_2$ is an inner product on $\mathbb{R}^2$.

1. Linearity in the first argument: $\ip{ax + bz}{y} = 2(ax_1 + bz_1)y_1 + (ax_2 + bz_2)y_2 = a\ip{x}{y} + b\ip{z}{y}$.
2. Symmetry: $\ip{y}{x} = 2y_1 x_1 + y_2 x_2 = \ip{x}{y}$. Over $\mathbb{R}$ the conjugate does nothing, so this is conjugate symmetry.
3. Positivity: $\ip{x}{x} = 2x_1^2 + x_2^2$. This is a sum of nonnegative terms, and it is $0$ only when $x_1 = x_2 = 0$.
4. A computation: for $x = (1, 1)$ and $y = (1, -2)$ we get $\ip{x}{y} = 2 - 2 = 0$. So $x$ and $y$ are orthogonal for this inner product, although $x \cdot y = -1$.

The typical use is to bring the tools of Euclidean geometry, such as projections and orthonormal bases, to a new space.
A trap: over $\mathbb{C}$, the first axiom does not give linearity in the second argument.
Conjugate symmetry turns it into conjugate-linearity.

### L3 human

An inner product on a real space is a positive definite symmetric bilinear form.
On a complex space it is a positive definite Hermitian form.
It gives a map $V \to V^*$, $y \mapsto \ip{\cdot}{y}$, which is linear over $\mathbb{R}$ and antilinear over $\mathbb{C}$.
The [[Riesz representation theorem|04GYPXDXNH]] shows that this map is bijective when $V$ has finite dimension.
Every inner product on $\mathbb{K}^n$ has the form $\ip{x}{y} = y^* A x$ for a unique positive definite matrix $A$, with the entries $a_{jk} = \ip{e_k}{e_j}$.
So $A$ is the transpose of the [[Gram matrix|00SPJSDT3Z]] of the standard basis.
All inner products on a space of finite dimension $n$ are therefore equivalent.
Each one has an orthonormal basis, so each one is isometric to $\mathbb{K}^n$ with the standard inner product.
In infinite dimensions the inner product gives a metric, and completeness becomes a separate condition.
A complete inner product space is a [[Hilbert space|HM2HHE3J51]], which belongs to functional analysis.
