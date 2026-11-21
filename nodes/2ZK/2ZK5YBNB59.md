---
tag: 2ZK5YBNB59
kind: example
name: Work done by a constant force as a dot product
msc: ["15A63", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [0S52TNNTH9]
uses: [0S52TNNTH9, 0XKBKGTCPC, 0CDZ684TCD]
sources:
  - url: https://en.wikipedia.org/wiki/Work_(physics)
    locator: Constant force
  - url: https://en.wikipedia.org/wiki/Dot_product
    locator: Physics
---

## Example

A constant force $F = (2, 3, 1)$, in newtons, moves an object along the straight displacement $d = (4, -1, 2)$, in meters.
The work of the force is $W = F \cdot d$, the [[dot product|0S52TNNTH9]] of force and displacement.

1. Multiply the matching components: $2 \cdot 4 = 8$, $3 \cdot (-1) = -3$ and $1 \cdot 2 = 2$.
2. Add them: $W = 8 - 3 + 2 = 7$, so the work is $7$ joules.
3. The [[lengths|0XKBKGTCPC]] are $\|F\| = \sqrt{14}$ newtons and $\|d\| = \sqrt{21}$ meters.
4. The angle between force and motion has the cosine
   $$\cos \theta = \frac{7}{\sqrt{14} \, \sqrt{21}} = \frac{7}{7\sqrt{6}} = \frac{1}{\sqrt{6}} \approx 0.408,$$
   so $\theta$ is about $65.9^\circ$.
5. Only the part of the force along the motion does work. That part is $\|F\| \cos \theta = 7 / \sqrt{21} \approx 1.53$ newtons over $\sqrt{21}$ meters, which gives $7$ joules again.

## Remarks

The formula $W = F \cdot d$ is the case of a constant force and a straight path of the [[work done by a force field|0CDZ684TCD]] along a curve.
The sign of the work follows the sign of the dot product.
A force perpendicular to the motion does no work, which is why gravity does no work on a car on a level road, and a force against the motion does negative work, as friction does.
Doubling the force or the displacement doubles the work, because the dot product is linear in each factor.

## Explanations

### L1 human

A force does work when it pushes an object along.
Only the part of the force in the direction of motion counts.
The dot product picks out exactly this part and multiplies it by the distance.
Here the force and the motion give $8 - 3 + 2 = 7$ joules.

### L2 human

Step 5 is the physical reading of $F \cdot d = \|F\| \, \|d\| \cos \theta$: the scalar component of $F$ along $d$, times the length of $d$.
In numbers, $\tfrac{7}{\sqrt{21}} \cdot \sqrt{21} = 7$.
Watch out: work is a number, not a vector, so it has a sign but no direction.
