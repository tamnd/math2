---
tag: 03FTB26QYD
kind: statement
role: proposition
name: Vector triple product
aliases: [triple-product-expansion, bac-cab-identity]
msc: [15A72]
uses: [0N5N15HWZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Triple_product
    locator: Vector triple product
inventory: [TPQYVR234A]
---

## Statement

Let $a$, $b$ and $c$ be vectors in $\mathbb{R}^3$. Let $\times$ be the [[cross product|0N5N15HWZ7]] and let $\cdot$ be the dot product. Then
$$a \times (b \times c) = (a \cdot c) \, b - (a \cdot b) \, c.$$

## Remarks

The formula is easy to remember as "BAC minus CAB": $a \times (b \times c) = b(a \cdot c) - c(a \cdot b)$.
The cross product is not associative. The formula gives $(a \times b) \times c = (a \cdot c) \, b - (b \cdot c) \, a$, which is in general different from $a \times (b \times c)$.
A consequence is the Jacobi identity $a \times (b \times c) + b \times (c \times a) + c \times (a \times b) = 0$.

## Explanations

### L1 human

The vector $b \times c$ is perpendicular to the plane of $b$ and $c$. A second cross product with $a$ gives a vector perpendicular to $b \times c$, so the result lies back in the plane of $b$ and $c$. The formula tells you exactly which combination of $b$ and $c$ it is.
