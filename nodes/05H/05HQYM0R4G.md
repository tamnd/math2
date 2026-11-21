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

The dot product of two vectors of the same size is the sum of the products of their matching entries.
Let $n \ge 1$ and let $x = (x_1, \dots, x_n)$ and $y = (y_1, \dots, y_n)$ be vectors of the [[coordinate space|0XM8BZD76G]] $\mathbb{R}^n$.
The dot product of $x$ and $y$ is the real number
$$x \cdot y = \sum_{i=1}^{n} x_i y_i = x_1 y_1 + x_2 y_2 + \dots + x_n y_n.$$

## Notation

Other notations are $\langle x, y \rangle$ and $(x, y)$.
For column vectors, $x \cdot y = x^{\mathsf{T}} y$, a $1 \times 1$ matrix that we read as a number.
In Mathlib the dot product of $x, y : \text{Fin } n \to R$ is `dotProduct x y`, written `x ⬝ᵥ y`, and it is defined for any commutative semiring $R$.

## Remarks

The definition asks for two things: the vectors have the same number $n$ of entries, and the entries are real numbers.
The first condition gives each entry of $x$ a partner in $y$.
For example, $(1, 2, 3) \cdot (4, 5, 6) = 4 + 10 + 18 = 32$, but $(1, 2) \cdot (1, 2, 3)$ is not defined.

The second condition gives the dot product its geometry.
Over $\mathbb{R}$ the number $x \cdot x = x_1^2 + \dots + x_n^2$ is never negative and is zero only for $x = 0$, so the dot product is an [[inner product|0NB0AWGJBW]] and gives lengths and angles, as the [[concept page|0S52TNNTH9]] explains.
Over $\mathbb{C}$ the same formula fails positivity: the vector $(1, i)$ gives $1 + i^2 = 0$, and that is why complex inner products conjugate one factor.
In the plane and in space the dot product also equals $\|x\| \, \|y\| \cos \theta$, where $\theta$ is the angle between $x$ and $y$; the [[geometric formula|070TXS9AXM]] proves it.

## Explanations

### L1 human

The dot product multiplies two vectors entry by entry and adds the results.
For example, $(1, 2, 3) \cdot (4, 5, 6) = 4 + 10 + 18 = 32$.
It is zero exactly when the two vectors are perpendicular, or when one of them is zero.

### L2 human

For $x = (2, -1, 0, 3)$ and $y = (1, 4, 7, 1)$ in $\mathbb{R}^4$, multiply the matching entries and add:
$$x \cdot y = 2 - 4 + 0 + 3 = 1.$$
Watch out: a zero entry still holds its position, so do not drop it and shift the other entries.
