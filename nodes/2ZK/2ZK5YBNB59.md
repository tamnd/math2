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

A constant force $F = (2, 3, 1)$, in newtons, moves an object along the straight displacement $d = (4, -1, 2)$, in metres.
The work of the force is $W = F \cdot d$, the [[dot product|0S52TNNTH9]] of force and displacement.

1. The products of the components are $2 \cdot 4 = 8$, $3 \cdot (-1) = -3$ and $1 \cdot 2 = 2$.
2. Their sum is $W = 8 - 3 + 2 = 7$. So the work is $7$ joules.
3. The [[lengths|0XKBKGTCPC]] are $\|F\| = \sqrt{14}$ newtons and $\|d\| = \sqrt{21}$ metres.
4. So $\cos \theta = \dfrac{7}{\sqrt{14}\sqrt{21}} = \dfrac{7}{7\sqrt{6}} = \dfrac{1}{\sqrt{6}} \approx 0.408$, and the angle between force and motion is about $65.9^\circ$.
5. Only the part of the force along the motion does work: $\|F\| \cos \theta = \tfrac{7}{\sqrt{21}} \approx 1.53$ newtons, over $\sqrt{21}$ metres.

## Remarks

The formula $W = F \cdot d$ is the special case of the [[work done by a force field|0CDZ684TCD]] for a constant force and a straight path.
If the force is perpendicular to the motion, the work is $0$; gravity does no work on a car that drives on a level road.
If the force points against the motion, the work is negative; friction does negative work.

## Explanations

### L1 human

A force does work when it pushes an object along.
Only the part of the force in the direction of motion counts.
The dot product picks out exactly this part and multiplies it by the distance.
Here the force and the motion give $8 - 3 + 2 = 7$ joules.

### L2 human

The product in step 5 is the scalar component of $F$ along $d$ times the length of $d$: $\tfrac{7}{\sqrt{21}} \cdot \sqrt{21} = 7$.
This is the physical reading of $F \cdot d = \|F\| \, \|d\| \cos \theta$.
A trap: work is a number, not a vector, so it has no direction.
