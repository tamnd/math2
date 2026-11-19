---
tag: P7X5FSFQZ1
kind: example
name: The cross product of (1, 2, 3) and (4, 5, 6)
msc: ["15A72", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [0N5N15HWZ7]
illustrates: [0T4QHJXSD4, W8V1S8TFWF]
uses: [0N5N15HWZ7, 0SEDGXG9S3, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Cross_product
    locator: Matrix notation
---

## Example

Let $a = (1, 2, 3)$ and $b = (4, 5, 6)$.
We compute $a \times b$ with the [[coordinate formula|0SEDGXG9S3]] and check two of its properties.

1. First component: $a_2 b_3 - a_3 b_2 = 2 \cdot 6 - 3 \cdot 5 = 12 - 15 = -3$.
2. Second component: $a_3 b_1 - a_1 b_3 = 3 \cdot 4 - 1 \cdot 6 = 12 - 6 = 6$.
3. Third component: $a_1 b_2 - a_2 b_1 = 1 \cdot 5 - 2 \cdot 4 = 5 - 8 = -3$.
4. So $a \times b = (-3, 6, -3)$.
5. [[Perpendicularity|0T4QHJXSD4]]: $a \cdot (a \times b) = -3 + 12 - 9 = 0$ and $b \cdot (a \times b) = -12 + 30 - 18 = 0$.
6. [[Lagrange's identity|W8V1S8TFWF]]: $\|a \times b\|^2 = 9 + 36 + 9 = 54$. Also $\|a\|^2 \|b\|^2 - (a \cdot b)^2 = 14 \cdot 77 - 32^2 = 1078 - 1024 = 54$.
7. The parallelogram spanned by $a$ and $b$ has the area $\sqrt{54} = 3\sqrt{6}$.

## Remarks

The vector $(-3, 6, -3) = -3(1, -2, 1)$, so $(1, -2, 1)$ is a simpler normal vector of the plane spanned by $a$ and $b$.
The vectors $a$ and $b$ are not parallel, so the product is not $0$.
If we replace $b$ by $(2, 4, 6) = 2a$, every component becomes $0$.
If we swap $a$ and $b$, the result is $(3, -6, 3)$, by anticommutativity.

## Explanations

### L1 human

For each component, we cover that column and cross-multiply the other two columns.
The middle component takes the opposite order, which gives its minus sign.
The result $(-3, 6, -3)$ makes a right angle with both $(1, 2, 3)$ and $(4, 5, 6)$, as the dot products in step 5 show.

### L2 human

Steps 5 and 6 are the standard checks of a computed cross product.
If either check fails, there is an arithmetic error, most often in the middle component.
A trap: writing the middle component as $a_1 b_3 - a_3 b_1 = -6$ gives $(-3, -6, -3)$, and then $a \cdot (-3, -6, -3) = -24 \neq 0$.
