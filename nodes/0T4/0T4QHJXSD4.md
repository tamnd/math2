---
tag: 0T4QHJXSD4
kind: statement
role: proposition
name: The cross product is perpendicular to its factors
msc: [15A72]
uses: [0N5N15HWZ7, 03NK6RSRQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Cross_product
    locator: Geometric meaning
---

## Statement

Let $a$ and $b$ be vectors in $\mathbb{R}^3$, and let $a \times b$ be their [[cross product|0N5N15HWZ7]]. Let $u \cdot v = u_1 v_1 + u_2 v_2 + u_3 v_3$ be the dot product.
Then
$$a \cdot (a \times b) = 0 \quad \text{and} \quad b \cdot (a \times b) = 0.$$

## Remarks

By the [[test with the dot product|03NK6RSRQ1]], $a \times b$ is perpendicular to $a$ and to $b$ when all three vectors are nonzero.
The proof is a direct computation. For example, $a \cdot (a \times b) = a_1(a_2 b_3 - a_3 b_2) + a_2(a_3 b_1 - a_1 b_3) + a_3(a_1 b_2 - a_2 b_1)$, and the six terms cancel in pairs.
If $a$ and $b$ are linearly independent, then $a \times b$ is a normal vector of the plane through $0$ that contains $a$ and $b$.

## Explanations

### L1 human

Lay two pencils flat on a table, starting at the same point. Their cross product points straight up from the table, or straight down. So it makes a right angle with each pencil.
