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

We write both vectors in the orthonormal basis, expand the inner product as a double sum, and use orthonormality to keep only the diagonal terms.
Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ linear in the first slot and [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$.
Let $(e_1, \dots, e_n)$ be an [[orthonormal basis|0FWJ0VW561]] of $V$.

1. For $u, w \in V$ and $a \in \mathbb{K}$, conjugate symmetry and linearity in the first slot give $\ip{u}{a w} = \overline{a}\ip{u}{w}$, and $\ip{u}{\cdot}$ is additive.
2. Let $x, y \in V$, and put $a_i = \ip{x}{e_i}$ and $b_j = \ip{y}{e_j}$.
3. The [[formula for coordinates in an orthonormal basis|09DZ8CD1AK]] gives $x = \sum_{i=1}^{n} a_i e_i$ and $y = \sum_{j=1}^{n} b_j e_j$.
4. Linearity in the first slot and step 1 give $\ip{x}{y} = \sum_{i=1}^{n}\sum_{j=1}^{n} a_i \overline{b_j}\ip{e_i}{e_j}$.
5. Since $\ip{e_i}{e_j} = \delta_{ij}$, only the terms with $i = j$ remain, so $\ip{x}{y} = \sum_{i=1}^{n} a_i \overline{b_i}$, which is part 1.
6. Part 2: take $y = x$ in part 1, which gives $\norm{x}^2 = \ip{x}{x} = \sum_{i} a_i \overline{a_i}$.
7. Each term is $a_i \overline{a_i} = \abs{a_i}^2$, by the definition of the modulus through the [[complex conjugate|0BJV24C4SY]], so $\norm{x}^2 = \sum_{i} \abs{\ip{x}{e_i}}^2$.
8. Part 3, linearity: each map $x \mapsto \ip{x}{e_i}$ is linear by linearity in the first slot, so $C$ is linear.
9. Part 3, bijectivity: the coordinates of a vector in a basis exist and are unique, and by step 3 they are the entries of $C(x)$, so $C$ is the coordinate map of the basis, which is a bijection.
10. Part 3, inner products: the [[standard inner product|TFZ8DYVJ1J]] of $C(x)$ and $C(y)$ is $\sum_i a_i \overline{b_i}$, and by step 5 this equals $\ip{x}{y}$.

This proves the three parts of [[Parseval's identity|047RFCNVSK]].

## Idea

In an orthonormal basis, the coordinates of a vector are its inner products with the basis vectors.
Expanding $\ip{x}{y}$ in these coordinates gives $n^2$ terms, one for each pair of basis vectors.
Orthonormality kills every term with two different basis vectors, so only the $n$ diagonal terms survive.
What is left is the standard inner product of the two coordinate lists.

## Variants

One can prove part 2 first, from the [[Pythagorean theorem|0BVTDM872V]] applied to the orthogonal pieces $a_i e_i$, and then deduce part 1 by the [[polarization identity|05FKHRT0B4]].
Both sides of part 1 are inner products on $V$ with the same norm, and polarization recovers an inner product from its norm.

For $V = \mathbb{K}^n$ there is a short matrix proof.
Let $Q$ be the unitary matrix with columns $e_1, \dots, e_n$, so that $C(x) = Q^* x$, since the entry $i$ of $Q^* x$ is $e_i^* x = \ip{x}{e_i}$.
Then
$$\ip{Q^* x}{Q^* y} = (Q^* y)^* (Q^* x) = y^* Q Q^* x = y^* x = \ip{x}{y},$$
because $Q Q^* = I$ for a square matrix with orthonormal columns.
