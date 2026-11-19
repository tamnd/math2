---
tag: XNRNNT63Q7
kind: proof
name: Proof of the anticommutativity of the cross product
msc: ["15A72"]
topics: [VKVAJ94SKZ]
audience: school
proves: 07ZS685JJC
methods: [0NTF6DMVAP, XP5SDYKJX0]
uses: [0N5N15HWZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Cross_product
    locator: Algebraic properties
---

## Proof

We compare the two vectors component by component.

1. Let $a = (a_1, a_2, a_3)$ and $b = (b_1, b_2, b_3)$. By the definition of the [[cross product|0N5N15HWZ7]], $a \times b = (a_2 b_3 - a_3 b_2, \; a_3 b_1 - a_1 b_3, \; a_1 b_2 - a_2 b_1)$.
2. The same definition with $a$ and $b$ exchanged gives $b \times a = (b_2 a_3 - b_3 a_2, \; b_3 a_1 - b_1 a_3, \; b_1 a_2 - b_2 a_1)$.
3. The first component of $b \times a$ is $b_2 a_3 - b_3 a_2 = -(a_2 b_3 - a_3 b_2)$, by commutativity of real multiplication.
4. So it is the negative of the first component of $a \times b$.
5. In the same way, $b_3 a_1 - b_1 a_3 = -(a_3 b_1 - a_1 b_3)$, the negative of the second component of $a \times b$.
6. Also $b_1 a_2 - b_2 a_1 = -(a_1 b_2 - a_2 b_1)$, the negative of the third component of $a \times b$.
7. Two vectors of $\mathbb{R}^3$ are equal when their components are equal. So $b \times a = -(a \times b)$.
8. For $b = a$, this gives $a \times a = -(a \times a)$. Adding $a \times a$ to both sides gives $2(a \times a) = 0$, so $a \times a = 0$.

## Idea

Each component of $a \times b$ has the form $xy' - yx'$, a difference of two products.
Swapping the roles of $a$ and $b$ swaps the two products, and this changes the sign of the difference.

## Variants

- One can prove $a \times a = 0$ first, directly: each component is $a_i a_j - a_j a_i = 0$. Then bilinearity and $(a + b) \times (a + b) = 0$ give $a \times b + b \times a = 0$.
- With the determinant memory aid, swapping $a$ and $b$ swaps two rows of the formal determinant, and a row swap changes the sign of a determinant.
