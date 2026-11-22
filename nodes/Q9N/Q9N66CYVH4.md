---
tag: Q9N66CYVH4
kind: example
name: Determinant of two vectors of the plane in two bases
msc: [15A15, 15A75]
topics: [DTBK11SR77]
audience: ug2
instance_of: [05CJSSXPR3]
uses: [0V94H674MB, T1WN2DHS63]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of n vectors
---

## Example

In $\mathbb{R}^2$ let $E = ((1, 0), (0, 1))$ be the standard basis and let $B = ((2, 0), (0, 1))$.
Let $v_1 = (1, 2)$ and $v_2 = (3, 4)$.
We compute the determinant of $v_1, v_2$ in each basis and check that the change of basis rule links the two values.

1. In $E$ the coordinates are the entries, so the [[definition|0V94H674MB]] gives
$$\det_E(v_1, v_2) = \det \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} = 1 \cdot 4 - 3 \cdot 2 = -2.$$
2. The vectors of $B$ have the coordinate columns $(2, 0)$ and $(0, 1)$ in $E$, so $\det_E(B) = 2 \cdot 1 - 0 \cdot 0 = 2$.
3. In $B$ we need the coordinates of $v_1$ and $v_2$.
   Halve the first entry and keep the second:
$$(1, 2) = \tfrac{1}{2} (2, 0) + 2 (0, 1), \qquad (3, 4) = \tfrac{3}{2} (2, 0) + 4 (0, 1).$$
4. So the coordinate matrix in $B$ has the columns $(\tfrac{1}{2}, 2)$ and $(\tfrac{3}{2}, 4)$, and
$$\det_B(v_1, v_2) = \tfrac{1}{2} \cdot 4 - \tfrac{3}{2} \cdot 2 = 2 - 3 = -1.$$
5. The [[change of basis rule|T1WN2DHS63]] says $\det_E(v_1, v_2) = \det_E(B) \cdot \det_B(v_1, v_2)$.
   Check: $2 \cdot (-1) = -2$, which agrees with step 1.

## Remarks

The basis $B$ doubles the first unit vector, so the unit square of $B$ has area $2$ in the usual sense.
Measured in this larger unit, the parallelogram of $v_1$ and $v_2$, whose usual area is $2$, has area $1$.
Both values are negative, because the turn from $v_1$ to $v_2$ is clockwise, while $B$ has the same orientation as $E$, since $\det_E(B) = 2 > 0$.

Change $B$ to $((0, 1), (2, 0))$, the same vectors in the other order.
Then $\det_E(B) = 0 \cdot 0 - 2 \cdot 1 = -2$, and the rule gives $\det_B(v_1, v_2) = -2 / (-2) = 1$.
The sign flips, because the new unit has the opposite orientation.

## Explanations

### L1 human

The determinant of two vectors is the signed area of their parallelogram.
The unit of area is the parallelogram of the basis.
A basis with a larger unit gives a smaller number, in the same way as a length is a smaller number in meters than in centimeters.

### L2 human

Steps 1 to 4 compute the value in each basis directly, and step 5 links the two values.
In practice we often skip step 3 and use the rule: $\det_B(v_1, v_2) = \det_E(v_1, v_2) / \det_E(B) = -2 / 2 = -1$.
Watch out: the value in $B$ is the quotient by $\det_E(B)$, not the product, which would give the wrong value $-4$.
