---
tag: XNRNNT63Q7
kind: proof
name: Proof of the anticommutativity of the cross product
msc: [15A72]
proves: 07ZS685JJC
uses: [0N5N15HWZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Cross_product
    locator: Algebraic properties
---

## Proof

We compare the two vectors coordinate by coordinate.

1. Let $a = (a_1, a_2, a_3)$ and $b = (b_1, b_2, b_3)$. By the definition of the [[cross product|0N5N15HWZ7]], $a \times b = (a_2 b_3 - a_3 b_2, \; a_3 b_1 - a_1 b_3, \; a_1 b_2 - a_2 b_1)$.
2. The same definition with $a$ and $b$ exchanged gives $b \times a = (b_2 a_3 - b_3 a_2, \; b_3 a_1 - b_1 a_3, \; b_1 a_2 - b_2 a_1)$.
3. The first coordinate of $b \times a$ is $b_2 a_3 - b_3 a_2 = -(a_2 b_3 - a_3 b_2)$. This is the negative of the first coordinate of $a \times b$.
4. The second coordinate of $b \times a$ is $b_3 a_1 - b_1 a_3 = -(a_3 b_1 - a_1 b_3)$. This is the negative of the second coordinate of $a \times b$.
5. The third coordinate of $b \times a$ is $b_1 a_2 - b_2 a_1 = -(a_1 b_2 - a_2 b_1)$. This is the negative of the third coordinate of $a \times b$.
6. Two vectors of $\R^3$ are equal when their coordinates are equal. So steps 3 to 5 give $b \times a = -(a \times b)$.

## Idea

Each coordinate of $a \times b$ has the form $x y' - y x'$, a difference of two products. Swapping the roles of $a$ and $b$ swaps the two products, and this changes the sign of the difference.
