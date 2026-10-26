---
tag: 059Q2XWJDC
kind: statement
role: proposition
name: Scalar triple product
aliases: [mixed-product, box-product]
msc: [15A72]
uses: [0N5N15HWZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Triple_product
    locator: Scalar triple product
---

## Statement

Let $a = (a_1, a_2, a_3)$, $b = (b_1, b_2, b_3)$ and $c = (c_1, c_2, c_3)$ be vectors in $\mathbb{R}^3$. Let $\times$ be the [[cross product|0N5N15HWZ7]] and let $\cdot$ be the dot product.
The scalar triple product of $a$, $b$ and $c$ is the real number $a \cdot (b \times c)$. It is equal to the determinant of the matrix whose rows are $a$, $b$ and $c$:
$$a \cdot (b \times c) = \det \begin{pmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{pmatrix}.$$

## Remarks

A cyclic shift of the three vectors does not change the value: $a \cdot (b \times c) = b \cdot (c \times a) = c \cdot (a \times b)$. A swap of two vectors changes its sign.
The absolute value $|a \cdot (b \times c)|$ is the volume of the [[parallelepiped|0SQV2VJTGY]] with the edges $a$, $b$ and $c$.
The scalar triple product is $0$ if and only if $a$, $b$ and $c$ are linearly dependent. This happens exactly when they lie in one plane through $0$.

## Explanations

### L1 human

The scalar triple product measures the volume of the slanted box that three arrows make. For the unit vectors $(1, 0, 0)$, $(0, 1, 0)$ and $(0, 0, 1)$ the box is a unit cube, and the product is $1$. If the three arrows lie flat in one plane, the box has no volume, and the product is $0$.
