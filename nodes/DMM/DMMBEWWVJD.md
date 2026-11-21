---
tag: DMMBEWWVJD
kind: example
name: Multiplying by the dot product does not give the projection
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
not_instance_of:
  - target: 0JW13B48YP
    note: for v that is not a unit vector, the vector (u . v) v is not the projection of u along v, because u minus it is not perpendicular to v
uses: [0JW13B48YP, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_projection
    locator: Definitions in terms of a and b
---

## Example

Let $u = (1, 2, 3)$ and $v = (1, 1, 1)$, and let $w = (u \cdot v)\, v$, the formula with the division by $v \cdot v$ left out.
We show that $w$ is not the [[vector projection|0JW13B48YP]] of $u$ along $v$.

1. The [[dot product|0S52TNNTH9]] is $u \cdot v = 6$, so $w = 6v = (6, 6, 6)$.
2. The remainder is $u - w = (-5, -4, -3)$.
3. Its dot product with $v$ is $-5 - 4 - 3 = -12 \neq 0$, so $u - w$ is not perpendicular to $v$.
4. The projection is the only multiple of $v$ whose remainder is perpendicular to $v$, so $w$ is not the projection.
5. The correct projection is $\tfrac{6}{3}\, v = (2, 2, 2)$, and $w$ is too long by the factor $v \cdot v = 3$.

## Remarks

The formula $(u \cdot v)\, v$ is correct exactly when $v \cdot v = 1$, that is, when $v$ is a unit vector.
With the unit vector $\hat v = \tfrac{1}{\sqrt{3}}(1, 1, 1)$ the shortcut works:
$$(u \cdot \hat v)\, \hat v = \frac{6}{\sqrt{3}} \cdot \frac{1}{\sqrt{3}}(1, 1, 1) = (2, 2, 2).$$
The error grows with the length of $v$.
For $v = (2, 2, 2)$ the wrong formula gives $(24, 24, 24)$, while the true projection is still $(2, 2, 2)$.

## Explanations

### L1 human

The shadow of an arrow on a line cannot be longer than the arrow.
The arrow $(1, 2, 3)$ has length about $3.7$.
The vector $(6, 6, 6)$ has length about $10.4$, so it cannot be the shadow.

### L2 human

The test for a projection is the perpendicular remainder, as in step 3.
A quick check of length also helps, since a projection is never longer than the original vector.
Watch out: formulas in books that assume unit vectors need the extra factor $\tfrac{1}{v \cdot v}$ before you use them with other vectors.
