---
tag: ES42SRNM4F
kind: proof
name: Proof of the vector triple product formula by coordinates
msc: [15A72]
proves: 03FTB26QYD
uses: [0N5N15HWZ7, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Triple_product
    locator: Vector triple product, Proof
---

## Proof

We compare the two sides coordinate by coordinate.

1. Let $a = (a_1, a_2, a_3)$, $b = (b_1, b_2, b_3)$ and $c = (c_1, c_2, c_3)$. Let $w = b \times c$.
2. By the definition of the [[cross product|0N5N15HWZ7]], $w_1 = b_2 c_3 - b_3 c_2$, $w_2 = b_3 c_1 - b_1 c_3$ and $w_3 = b_1 c_2 - b_2 c_1$.
3. By the same definition, $a \times w = (a_2 w_3 - a_3 w_2, \; a_3 w_1 - a_1 w_3, \; a_1 w_2 - a_2 w_1)$.
4. Let $a \cdot b$ and $a \cdot c$ be the [[dot products|0S52TNNTH9]]. Then $a_2 b_2 + a_3 b_3 = a \cdot b - a_1 b_1$ and $a_2 c_2 + a_3 c_3 = a \cdot c - a_1 c_1$.
5. The first coordinate of $a \times w$ is $a_2 (b_1 c_2 - b_2 c_1) - a_3 (b_3 c_1 - b_1 c_3)$. Grouping by $b_1$ and $c_1$, it is $b_1 (a_2 c_2 + a_3 c_3) - c_1 (a_2 b_2 + a_3 b_3)$.
6. By step 4 this is $b_1 (a \cdot c) - a_1 b_1 c_1 - c_1 (a \cdot b) + a_1 b_1 c_1 = (a \cdot c) b_1 - (a \cdot b) c_1$.
7. The second coordinate of $a \times w$ is $a_3 (b_2 c_3 - b_3 c_2) - a_1 (b_1 c_2 - b_2 c_1)$. Grouping by $b_2$ and $c_2$, it is $b_2 (a_1 c_1 + a_3 c_3) - c_2 (a_1 b_1 + a_3 b_3)$.
8. Since $a_1 c_1 + a_3 c_3 = a \cdot c - a_2 c_2$ and $a_1 b_1 + a_3 b_3 = a \cdot b - a_2 b_2$, the terms $\pm a_2 b_2 c_2$ cancel. So the second coordinate is $(a \cdot c) b_2 - (a \cdot b) c_2$.
9. The third coordinate of $a \times w$ is $a_1 (b_3 c_1 - b_1 c_3) - a_2 (b_2 c_3 - b_3 c_2)$. Grouping by $b_3$ and $c_3$, it is $b_3 (a_1 c_1 + a_2 c_2) - c_3 (a_1 b_1 + a_2 b_2)$.
10. Since $a_1 c_1 + a_2 c_2 = a \cdot c - a_3 c_3$ and $a_1 b_1 + a_2 b_2 = a \cdot b - a_3 b_3$, the terms $\pm a_3 b_3 c_3$ cancel. So the third coordinate is $(a \cdot c) b_3 - (a \cdot b) c_3$.
11. Steps 6, 8 and 10 say that each coordinate of $a \times (b \times c)$ equals the same coordinate of $(a \cdot c) b - (a \cdot b) c$. So the two vectors are equal.

## Idea

In each coordinate, two of the three terms of a dot product appear after grouping. Adding and subtracting the missing term completes both dot products, and the two added terms cancel each other.
