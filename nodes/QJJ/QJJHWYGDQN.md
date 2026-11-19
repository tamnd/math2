---
tag: QJJHWYGDQN
kind: example
name: Distances from a point to a plane and to a line
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [C6GAS92QHX]
illustrates: [0K1E2S6Z69, Q6YGYNSY5H]
uses: [C6GAS92QHX, 0N5N15HWZ7, 0S52TNNTH9, 0JW13B48YP]
sources:
  - url: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_plane
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
    locator: Vector formulation
---

## Example

We compute two [[distances|C6GAS92QHX]] and the closest points.

**Point and plane.** Let $q = (1, 2, 3)$ and let $P$ be the plane $6x + 3y + 2z = 6$.

1. Normal $n = (6, 3, 2)$, with $\|n\| = \sqrt{36 + 9 + 4} = 7$.
2. $n \cdot q - 6 = 6 + 6 + 6 - 6 = 12$, by the [[dot product|0S52TNNTH9]].
3. By the [[point-plane theorem|0K1E2S6Z69]], $\operatorname{dist}(q, P) = \tfrac{12}{7}$.
4. Foot: $q - \tfrac{12}{49} n = (1 - \tfrac{72}{49}, \; 2 - \tfrac{36}{49}, \; 3 - \tfrac{24}{49}) = (-\tfrac{23}{49}, \tfrac{62}{49}, \tfrac{123}{49})$.
5. Check: $6 \cdot (-23) + 3 \cdot 62 + 2 \cdot 123 = -138 + 186 + 246 = 294 = 6 \cdot 49$. So the foot is on $P$.

**Point and line.** Let $q = (1, 1, 1)$ and let $L$ be the line $t(1, 2, 2)$, so $a = 0$ and $d = (1, 2, 2)$.

6. [[Cross product|0N5N15HWZ7]]: $q \times d = (1 \cdot 2 - 1 \cdot 2, \; 1 \cdot 1 - 1 \cdot 2, \; 1 \cdot 2 - 1 \cdot 1) = (0, -1, 1)$.
7. By the [[distance theorem|Q6YGYNSY5H]], $\operatorname{dist}(q, L) = \dfrac{\sqrt{2}}{\|d\|} = \dfrac{\sqrt{2}}{3}$.
8. Closest point by the [[projection|0JW13B48YP]]: $\tfrac{q \cdot d}{d \cdot d} d = \tfrac{5}{9}(1, 2, 2)$.
9. Check: $q - \tfrac{5}{9} d = (\tfrac{4}{9}, -\tfrac{1}{9}, -\tfrac{1}{9})$, with the length $\tfrac{\sqrt{18}}{9} = \tfrac{\sqrt{2}}{3}$.

## Remarks

The value $12 > 0$ in step 2 shows that $q$ lies on the side of $P$ into which $n$ points.
The vector from the foot to $q$ is $\tfrac{12}{49} n$, with the length $\tfrac{12}{49} \cdot 7 = \tfrac{12}{7}$.
In step 9 the vector $(\tfrac{4}{9}, -\tfrac{1}{9}, -\tfrac{1}{9})$ is perpendicular to $d$: $\tfrac{4 - 2 - 2}{9} = 0$.

## Explanations

### L1 human

The distance to the plane is the length of the shortest string from the point to the plane.
The formula gives $\tfrac{12}{7}$, a bit less than $2$.
The distance to the line is $\tfrac{\sqrt{2}}{3}$, about $0.47$.

### L2 human

Both computations give the distance first and then a check by the closest point.
For the line, the cross product route and the projection route agree, as Lagrange's identity says.
A trap: in step 7 the denominator is $\|d\| = 3$, not $\|d\|^2 = 9$.
