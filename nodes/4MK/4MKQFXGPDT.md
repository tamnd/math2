---
tag: 4MKQFXGPDT
kind: proof
name: Proof that the scalar triple product is a determinant
msc: ["15A72", "15A15"]
topics: [VKVAJ94SKZ]
audience: school
proves: 059Q2XWJDC
methods: [0NTF6DMVAP, XP5SDYKJX0]
uses: [0N5N15HWZ7, 0S52TNNTH9, 00KDZRW4C0, 0C08BQ3M05, 0XPKR18APA, 0ZN2J42SK7]
sources:
  - url: https://en.wikipedia.org/wiki/Triple_product
    locator: Scalar triple product
---

## Proof

We expand both sides and compare them term by term.

1. Let $a$, $b$, $c$ have components $a_i$, $b_i$, $c_i$, and let $M$ be the matrix with rows $a$, $b$, $c$.
2. By the definition of the [[cross product|0N5N15HWZ7]],
   $$b \times c = (b_2 c_3 - b_3 c_2, \; b_3 c_1 - b_1 c_3, \; b_1 c_2 - b_2 c_1).$$
3. By the definition of the [[dot product|0S52TNNTH9]],
   $$a \cdot (b \times c) = a_1 (b_2 c_3 - b_3 c_2) + a_2 (b_3 c_1 - b_1 c_3) + a_3 (b_1 c_2 - b_2 c_1).$$
4. By the [[Laplace expansion|0C08BQ3M05]] along row $1$, $\det M = a_1 M_{11} - a_2 M_{12} + a_3 M_{13}$, where $M_{1j}$ is the [[minor|0XPKR18APA]], the [[determinant|00KDZRW4C0]] of $M$ without row $1$ and column $j$.
5. By the [[$2 \times 2$ formula|0ZN2J42SK7]], $M_{11} = b_2 c_3 - b_3 c_2$, $M_{12} = b_1 c_3 - b_3 c_1$ and $M_{13} = b_1 c_2 - b_2 c_1$.
6. The first and last terms of steps 3 and 4 agree by step 5.
7. For the middle term, $-a_2 M_{12} = a_2 (b_3 c_1 - b_1 c_3)$, which is the middle term of step 3.
8. Hence $a \cdot (b \times c) = \det M$.

## Idea

The components of $b \times c$ are the signed $2 \times 2$ minors that the Laplace expansion along the first row multiplies by $a_1$, $a_2$ and $a_3$.
So the dot product with $a$ is that expansion, term by term, and the minus sign of the middle term is the reversed order of the middle component.

## Variants

Sarrus' rule gives a second check.
It expands $\det M$ into six products,
$$a_1 b_2 c_3 + a_2 b_3 c_1 + a_3 b_1 c_2 - a_3 b_2 c_1 - a_1 b_3 c_2 - a_2 b_1 c_3,$$
and multiplying out step 3 gives the same six products.

A structural proof avoids coordinates.
Both sides are linear in each of $a$, $b$, $c$, both change sign under a swap of two vectors, and both equal $1$ at $(\mathbf{i}, \mathbf{j}, \mathbf{k})$.
The uniqueness of such a form, proved in the sub-area on [[determinants|DTBK11SR77]], gives the equality.
