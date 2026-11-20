---
tag: DT0H0YQ4H7
kind: example
name: The scalar triple product as an alternating trilinear form
msc: ["15A15", "15A69"]
topics: [DTBK11SR77]
audience: ug1
instance_of: [0K6CH0MT0F]
uses: [059Q2XWJDC, 0SEDGXG9S3, 05HQYM0R4G, 0MSWYWHYF5, 1C8RRWHD45]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Dimension 3 and higher
---

## Example

Let $t \colon (\mathbb{R}^3)^3 \to \mathbb{R}$ be the [[scalar triple product|059Q2XWJDC]] $t(u, v, w) = u \cdot (v \times w)$, with the [[cross product|0SEDGXG9S3]] $v \times w = (v_2 w_3 - v_3 w_2,\ v_3 w_1 - v_1 w_3,\ v_1 w_2 - v_2 w_1)$.

1. Trilinear: the cross product is bilinear in $(v, w)$, because each coordinate is a sum of products of one coordinate of $v$ and one of $w$. The [[dot product|05HQYM0R4G]] is bilinear. So $t$ is linear in each of $u, v, w$.
2. Equal second and third arguments: $v \times v = (v_2 v_3 - v_3 v_2, \dots) = 0$, so $t(u, v, v) = 0$.
3. Equal first and second arguments: $u \cdot (u \times w) = u_1(u_2 w_3 - u_3 w_2) + u_2(u_3 w_1 - u_1 w_3) + u_3(u_1 w_2 - u_2 w_1)$.
4. In step 3 the six products cancel in pairs: $u_1 u_2 w_3$ with $-u_2 u_1 w_3$, $-u_1 u_3 w_2$ with $u_3 u_1 w_2$, and $u_2 u_3 w_1$ with $-u_3 u_2 w_1$. So $t(u, u, w) = 0$.
5. Equal first and third arguments: the same computation with $v$ in place of $w$ gives $t(u, v, u) = 0$.
6. So $t$ is [[alternating|0MSWYWHYF5]].
7. Normalization: $e_2 \times e_3 = e_1$, so $t(e_1, e_2, e_3) = e_1 \cdot e_1 = 1$.
8. Numerical check: for $u = (1, 0, 2)$, $v = (0, 1, 1)$, $w = (1, 1, 0)$, $v \times w = (0 - 1, 1 - 0, 0 - 1) = (-1, 1, -1)$ and $t = -1 + 0 - 2 = -3$.

## Remarks

By the [[existence and uniqueness theorem|1C8RRWHD45]], $t(u, v, w)$ is the determinant of the matrix with rows $u, v, w$.
For the numbers of step 8 the rule of Sarrus gives $1 \cdot 1 \cdot 0 + 0 \cdot 1 \cdot 1 + 2 \cdot 0 \cdot 1 - 2 \cdot 1 \cdot 1 - 1 \cdot 1 \cdot 1 - 0 \cdot 0 \cdot 0 = -3$, the same value.
The absolute value $3$ is the volume of the parallelepiped with edges $u, v, w$.

## Explanations

### L1 human

Three arrows in space span a slanted box.
The triple product gives the volume of this box with a sign.
It is zero when two arrows are equal, because then the box is flat.

### L2 human

To show that a formula of three vectors is a determinant, check linearity in each vector, zero on equal pairs, and the value $1$ on $e_1, e_2, e_3$.
A trap: for an alternating map one must check all three pairs of positions, or use that the map changes sign under one exchange.
