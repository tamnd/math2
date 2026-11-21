---
tag: V2CJH2RJ93
kind: example
name: Vector triple product and Jacobi identity for three vectors
msc: ["15A72", "97G70"]
topics: [VKVAJ94SKZ]
audience: ug1
instance_of: [0N5N15HWZ7]
illustrates: [03FTB26QYD, NDDB9EDN84]
uses: [0N5N15HWZ7, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Triple_product
    locator: Vector triple product
---

## Example

Let $a = (1, 2, 3)$, $b = (4, 5, 6)$ and $c = (7, 8, 10)$.
We check the [[vector triple product|03FTB26QYD]] formula, show that the [[cross product|0N5N15HWZ7]] is not associative, and check the [[Jacobi identity|NDDB9EDN84]].

1. First, $b \times c = (5 \cdot 10 - 6 \cdot 8, \; 6 \cdot 7 - 4 \cdot 10, \; 4 \cdot 8 - 5 \cdot 7) = (2, 2, -3)$.
2. Then $a \times (b \times c) = (2 \cdot (-3) - 3 \cdot 2, \; 3 \cdot 2 - 1 \cdot (-3), \; 1 \cdot 2 - 2 \cdot 2) = (-12, 9, -2)$.
3. The [[dot products|0S52TNNTH9]] are $a \cdot c = 53$, $a \cdot b = 32$ and $b \cdot c = 128$.
4. The formula $(a \cdot c)\, b - (a \cdot b)\, c$ gives
   $$53\,(4, 5, 6) - 32\,(7, 8, 10) = (212 - 224, \; 265 - 256, \; 318 - 320) = (-12, 9, -2),$$
   which agrees with step 2.
5. For the other bracketing, $a \times b = (-3, 6, -3)$, so $(a \times b) \times c = (6 \cdot 10 + 3 \cdot 8, \; -3 \cdot 7 + 3 \cdot 10, \; -3 \cdot 8 - 6 \cdot 7) = (84, 9, -66)$.
6. Since $(84, 9, -66) \neq (-12, 9, -2)$, the cross product is not associative.
7. The other two Jacobi terms, by the triple product formula, are $b \times (c \times a) = 32\, c - 128\, a = (96, 0, -64)$ and $c \times (a \times b) = 128\, a - 53\, b = (-84, -9, 66)$.
8. The sum of the three terms is $(-12 + 96 - 84, \; 9 + 0 - 9, \; -2 - 64 + 66) = (0, 0, 0)$.

## Remarks

Step 7 can be checked directly.
We have $c \times a = (4, -11, 6)$, and
$$b \times (4, -11, 6) = (5 \cdot 6 + 6 \cdot 11, \; 6 \cdot 4 - 4 \cdot 6, \; -4 \cdot 11 - 5 \cdot 4) = (96, 0, -64).$$
The results also show where each bracketing lives.
The vector $a \times (b \times c) = (-12, 9, -2)$ is a combination of $b$ and $c$, so it lies in their plane.
The vector $(a \times b) \times c = (84, 9, -66) = 53\, b - 128\, a$ lies in the plane of $a$ and $b$ instead.

## Explanations

### L1 human

We take three arrows and form two cross products in two different orders.
The two results are different arrows, so the order of the brackets matters.
The Jacobi identity adds three products with the letters shifted around a circle, and the sum is exactly the zero arrow.

### L2 human

The formula in step 4 turns two cross products into two dot products and one combination, which is shorter and safer.
The other bracketing has its own formula, $(a \times b) \times c = (a \cdot c)\, b - (b \cdot c)\, a = 53\, b - 128\, a$.
Watch out: the formula $(a \cdot c)\, b - (a \cdot b)\, c$ is for $a \times (b \times c)$ only.
Using it for $(a \times b) \times c$ gives the wrong vector $(-12, 9, -2)$.
