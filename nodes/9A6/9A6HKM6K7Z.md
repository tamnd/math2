---
tag: 9A6HKM6K7Z
kind: proof
name: Proof of Parseval's identity
msc: ["46C05", "15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
proves: 047RFCNVSK
methods: [0NTF6DMVAP]
uses: [0VGSYBWHV2, 0KG4D8AP6G, 0FWJ0VW561, 09DZ8CD1AK, 0BJV24C4SY, TFZ8DYVJ1J]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 6.30
---

## Proof

Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ and [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$.
Let $(e_1, \dots, e_n)$ be an [[orthonormal basis|0FWJ0VW561]] of $V$.

1. For $u, w \in V$ and $a \in \mathbb{K}$, conjugate symmetry and linearity give $\ip{u}{a w} = \overline{a}\ip{u}{w}$. Also $\ip{u}{\cdot}$ is additive.
2. Let $x, y \in V$, with $a_i = \ip{x}{e_i}$ and $b_j = \ip{y}{e_j}$.
3. The [[formula for coordinates|09DZ8CD1AK]] gives $x = \sum_{i=1}^{n} a_i e_i$ and $y = \sum_{j=1}^{n} b_j e_j$.
4. Linearity in the first argument and step 1 give $\ip{x}{y} = \sum_{i=1}^{n}\sum_{j=1}^{n} a_i \overline{b_j}\ip{e_i}{e_j}$.
5. Since $\ip{e_i}{e_j} = \delta_{ij}$, only the terms with $i = j$ remain. So $\ip{x}{y} = \sum_{i=1}^{n} a_i \overline{b_i}$. This is part 1.
6. Part 2. Take $y = x$ in part 1. Then $\norm{x}^2 = \sum_{i} a_i \overline{a_i}$.
7. For each $z \in \mathbb{C}$, $z\overline{z} = |z|^2$, by the [[complex conjugate|0BJV24C4SY]]. So $\norm{x}^2 = \sum_{i} |\ip{x}{e_i}|^2$.
8. Part 3, linearity. Each map $x \mapsto \ip{x}{e_i}$ is linear, by linearity in the first argument. So $C$ is linear.
9. Part 3, bijectivity. The coordinates of a vector in a basis exist and are unique. By step 3 they are the entries of $C(x)$, so $C$ is the coordinate map, which is bijective.
10. Part 3, inner products. The [[standard inner product|TFZ8DYVJ1J]] of $C(x)$ and $C(y)$ is $\sum_i a_i \overline{b_i}$. By step 5 it equals $\ip{x}{y}$.

## Idea

In an orthonormal basis, the coordinates of a vector are its inner products with the basis vectors.
Expanding $\ip{x}{y}$ in these coordinates gives a double sum.
Orthonormality removes every mixed term, so only the diagonal terms remain.

## Variants

- One can prove part 2 first, from the [[Pythagorean theorem|0BVTDM872V]], and then deduce part 1 by the [[polarization identity|05FKHRT0B4]]. Both sides of part 1 are inner products with the same norm.
- In matrix form for $V = \mathbb{K}^n$: if $Q$ is unitary with columns $e_i$, then $C(x) = Q^* x$ and $\ip{Q^* x}{Q^* y} = y^* Q Q^* x = y^* x$.
