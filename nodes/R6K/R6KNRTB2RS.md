---
tag: R6KNRTB2RS
kind: proof
name: Proof that the cross product is perpendicular to its factors
msc: ["15A72"]
topics: [VKVAJ94SKZ]
audience: school
proves: 0T4QHJXSD4
methods: [0NTF6DMVAP, XP5SDYKJX0]
uses: [0N5N15HWZ7, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Cross_product
    locator: Geometric meaning
---

## Proof

We compute both dot products from the coordinate formula.

1. Let $a = (a_1, a_2, a_3)$ and $b = (b_1, b_2, b_3)$. By the definition of the [[cross product|0N5N15HWZ7]], $a \times b = (a_2 b_3 - a_3 b_2, \; a_3 b_1 - a_1 b_3, \; a_1 b_2 - a_2 b_1)$.
2. By the definition of the [[dot product|0S52TNNTH9]],
$$a \cdot (a \times b) = a_1 (a_2 b_3 - a_3 b_2) + a_2 (a_3 b_1 - a_1 b_3) + a_3 (a_1 b_2 - a_2 b_1).$$
3. We expand the right side. It is $a_1 a_2 b_3 - a_1 a_3 b_2 + a_2 a_3 b_1 - a_1 a_2 b_3 + a_1 a_3 b_2 - a_2 a_3 b_1$.
4. The six terms cancel in pairs: $a_1 a_2 b_3$ with $-a_1 a_2 b_3$, $a_1 a_3 b_2$ with $-a_1 a_3 b_2$, and $a_2 a_3 b_1$ with $-a_2 a_3 b_1$.
5. So $a \cdot (a \times b) = 0$.
6. In the same way,
$$b \cdot (a \times b) = b_1 (a_2 b_3 - a_3 b_2) + b_2 (a_3 b_1 - a_1 b_3) + b_3 (a_1 b_2 - a_2 b_1).$$
7. Expanded, this is $a_2 b_1 b_3 - a_3 b_1 b_2 + a_3 b_1 b_2 - a_1 b_2 b_3 + a_1 b_2 b_3 - a_2 b_1 b_3$.
8. Again the six terms cancel in pairs. So $b \cdot (a \times b) = 0$.

## Idea

Each component of $a \times b$ is a $2 \times 2$ determinant built from $a$ and $b$.
The dot product with $a$ is the expansion of a $3 \times 3$ determinant with the rows $a$, $a$, $b$.
A determinant with two equal rows is zero, and this is why the terms cancel in pairs.

## Variants

- By [[anticommutativity|07ZS685JJC]], $b \cdot (a \times b) = -\, b \cdot (b \times a)$. The first part, applied to the pair $(b, a)$, gives $b \cdot (b \times a) = 0$. So the second computation can be skipped.
- With the [[determinant formula for the scalar triple product|059Q2XWJDC]], $a \cdot (a \times b) = \det(a, a, b) = 0$, because the matrix has two equal rows.
