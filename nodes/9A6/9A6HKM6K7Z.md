---
tag: 9A6HKM6K7Z
kind: proof
name: Proof of Parseval's identity
msc: [46C05]
proves: 047RFCNVSK
uses: [0VGSYBWHV2, 0KG4D8AP6G, 0FWJ0VW561, 09DZ8CD1AK, 0BJV24C4SY]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 6.30
---

## Proof

We expand both vectors in the basis and use orthonormality.

1. Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \R$ or $\C$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ and [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$. Let $(e_1, \dots, e_n)$ be an [[orthonormal basis|0FWJ0VW561]] of $V$.
2. For all $u, w \in V$ and $a \in \mathbb{K}$, conjugate symmetry and linearity in the first argument give $\ip{u}{a w} = \overline{a} \ip{u}{w}$. In the same way, $\ip{u}{\cdot}$ is additive.
3. Let $x, y \in V$, and set $a_i = \ip{x}{e_i}$ and $b_j = \ip{y}{e_j}$. By the [[formula for coordinates|09DZ8CD1AK]], $x = \sum_{i=1}^{n} a_i e_i$ and $y = \sum_{j=1}^{n} b_j e_j$.
4. Linearity in the first argument and step 2 give $\ip{x}{y} = \sum_{i=1}^{n} \sum_{j=1}^{n} a_i \overline{b_j} \ip{e_i}{e_j}$.
5. Since $\ip{e_i}{e_j} = \delta_{ij}$, only the terms with $i = j$ remain. So $\ip{x}{y} = \sum_{i=1}^{n} a_i \overline{b_i} = \sum_{i=1}^{n} \ip{x}{e_i} \overline{\ip{y}{e_i}}$.
6. This is the first identity. Now take $y = x$. Then $\norm{x}^2 = \ip{x}{x} = \sum_{i=1}^{n} \ip{x}{e_i} \overline{\ip{x}{e_i}}$.
7. For each $z \in \C$, the product of $z$ and its [[complex conjugate|0BJV24C4SY]] is $z \overline{z} = \abs{z}^2$. Hence $\norm{x}^2 = \sum_{i=1}^{n} \abs{\ip{x}{e_i}}^2$, which is the second identity.

## Idea

In an orthonormal basis, the coordinates of a vector are its inner products with the basis vectors. Expanding $\ip{x}{y}$ in these coordinates gives a double sum. Orthonormality kills every mixed term, so only the diagonal terms remain.
