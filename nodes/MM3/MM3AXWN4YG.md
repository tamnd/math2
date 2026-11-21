---
tag: MM3AXWN4YG
kind: proof
name: Proof of the Jacobi identity for the cross product
msc: ["15A72", "17B05"]
topics: [VKVAJ94SKZ]
audience: ug1
proves: NDDB9EDN84
methods: [0NTF6DMVAP, XP5SDYKJX0]
uses: [03FTB26QYD, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Triple_product
    locator: Vector triple product
---

## Proof

We expand each term by the vector triple product and add.

1. By the [[vector triple product|03FTB26QYD]], $a \times (b \times c) = (a \cdot c) \, b - (a \cdot b) \, c$.
2. The same identity with $(b, c, a)$ in place of $(a, b, c)$ gives $b \times (c \times a) = (b \cdot a) \, c - (b \cdot c) \, a$.
3. The same identity with $(c, a, b)$ in place of $(a, b, c)$ gives $c \times (a \times b) = (c \cdot b) \, a - (c \cdot a) \, b$.
4. The [[dot product|0S52TNNTH9]] is symmetric, so $b \cdot a = a \cdot b$, $c \cdot b = b \cdot c$ and $c \cdot a = a \cdot c$.
5. Add steps 1 to 3 and collect the terms by the vector they multiply. By step 4, the terms with $b$ are $(a \cdot c) \, b - (a \cdot c) \, b = 0$.
6. The terms with $c$ are $-(a \cdot b) \, c + (a \cdot b) \, c = 0$.
7. The terms with $a$ are $-(b \cdot c) \, a + (b \cdot c) \, a = 0$.
8. So the sum of the three terms is $0$.

## Idea

Each term of the Jacobi sum is a combination of $a$, $b$ and $c$ with dot products as coefficients.
The cyclic shift makes each coefficient appear twice, once with each sign, so everything cancels.

## Variants

A proof in coordinates is also possible, since both sides are polynomials in the nine coordinates.
The first coordinate of the sum has twelve terms, and they cancel in pairs.
The work is longer but needs nothing beyond the definition.

A Lie algebra proof sends $a$ to the antisymmetric matrix $[a]_\times$ with $[a]_\times v = a \times v$, which turns $\times$ into the commutator.
The [[Jacobi identity for commutators|ZKFN197MBR]] then gives the result.
