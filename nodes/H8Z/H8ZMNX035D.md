---
tag: H8ZMNX035D
kind: example
name: Orthogonality depends on the inner product
msc: ["15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
not_instance_of:
  - target: 0Y2X7P2WB7
    note: the vectors (1, 1) and (1, -1) are orthogonal for the dot product of R^2, but not for the inner product 2 x_1 y_1 + x_2 y_2, which gives them the value 1
uses: [0TS7VZJBWD, 0VGSYBWHV2]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonality_(mathematics)
    locator: Definitions
---

## Example

On $\mathbb{R}^2$ let $\ip{x}{y}_w = 2x_1 y_1 + x_2 y_2$.
We show that it is an inner product, and that it changes which pairs of vectors are [[orthogonal|0TS7VZJBWD]].

1. It is an [[inner product|0VGSYBWHV2]].
   It is linear in $x$, it is symmetric because $2x_1y_1 + x_2y_2 = 2y_1x_1 + y_2x_2$, and $\ip{x}{x}_w = 2x_1^2 + x_2^2 > 0$ for $x \neq 0$.
2. Let $u = (1, 1)$ and $v = (1, -1)$.
   The dot product is $u \cdot v = 1 - 1 = 0$, so $u$ and $v$ are orthogonal for the dot product.
3. For the new inner product,
$$\ip{u}{v}_w = 2 \cdot 1 \cdot 1 + 1 \cdot (-1) = 1 \neq 0,$$
   so $u$ and $v$ are not orthogonal for $\ip{\cdot}{\cdot}_w$.
4. In the other direction, let $p = (1, -2)$ and $q = (1, 1)$.
   Then $\ip{p}{q}_w = 2 \cdot 1 \cdot 1 + (-2) \cdot 1 = 0$, so $p \perp q$ for $\ip{\cdot}{\cdot}_w$.
5. But $p \cdot q = 1 - 2 = -1 \neq 0$, so $p$ and $q$ are not orthogonal for the dot product.

## Remarks

The word "orthogonal" has a meaning only together with a fixed inner product.
The new right angles are the old ones seen through a stretch.
The map $S(x_1, x_2) = (\sqrt{2}x_1, x_2)$ satisfies $S x \cdot S y = 2x_1y_1 + x_2y_2 = \ip{x}{y}_w$, so $p \perp_w q$ exactly when $Sp \perp Sq$ for the dot product.
Check: $Sp = (\sqrt{2}, -2)$ and $Sq = (\sqrt{2}, 1)$ give $2 - 2 = 0$.

Change the weight $2$ to any $c > 0$.
Then $\ip{(1, 1)}{(1, -1)} = c - 1$, so the pair is orthogonal only for $c = 1$, the dot product.
The same vector space with two inner products gives two different inner product spaces, with different right angles and different lengths.

## Explanations

### L1 human

A right angle is not a property of two arrows alone.
It depends on the rule that measures angles.
With the usual dot product, $(1, 1)$ and $(1, -1)$ meet at a right angle.
If we count the first coordinate twice, the rule gives $2 - 1 = 1$, and the right angle is gone.

### L2 human

To decide orthogonality, compute the inner product that the problem uses, not the dot product.
Fix the inner product $2x_1y_1 + x_2y_2$, and look for all $x$ orthogonal to $u = (1, 1)$.
The condition is
$$\ip{u}{x}_w = 2x_1 + x_2 = 0,$$
and its solutions are the multiples of $(1, -2)$.
So in this space the line orthogonal to $(1, 1)$ is spanned by $(1, -2)$, not by $(1, -1)$.
Weighted inner products of this kind occur in statistics, where the weights are the reliabilities of the data, and in mechanics, where a mass matrix plays the role of the weights.
Watch out: a picture drawn with the usual axes shows the geometry of the dot product, and it misleads for a weighted inner product.
