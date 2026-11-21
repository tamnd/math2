---
tag: 9C7YQTW1ZM
kind: example
name: The two definitions of the dot product agree for (3, 0) and (2, 2)
msc: ["15A63", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [0S52TNNTH9]
illustrates: [070TXS9AXM]
uses: [0S52TNNTH9, 0XKBKGTCPC, 0ZEHZY85E6]
sources:
  - url: https://en.wikipedia.org/wiki/Dot_product
    locator: Geometric definition
---

## Example

Let $u = (3, 0)$ and $v = (2, 2)$ in the plane.
We compute the [[dot product|0S52TNNTH9]] in two ways and compare.

1. The coordinate definition multiplies and adds: $u \cdot v = 3 \cdot 2 + 0 \cdot 2 = 6$.
2. The [[lengths|0XKBKGTCPC]] are $\|u\| = 3$ and $\|v\| = \sqrt{4 + 4} = 2\sqrt{2}$.
3. The vector $u$ lies on the positive $x$-axis, and $v$ lies on the line $y = x$ in the first quadrant. So the [[angle between them|0ZEHZY85E6]] is $\theta = 45^\circ$, with $\cos \theta = \tfrac{\sqrt{2}}{2}$.
4. The geometric definition gives
   $$\|u\| \, \|v\| \cos \theta = 3 \cdot 2\sqrt{2} \cdot \tfrac{\sqrt{2}}{2} = 6.$$
5. Both definitions give $6$, as the [[geometric formula|070TXS9AXM]] says they must.

## Remarks

The pair is chosen so that the angle can be read from the picture without any dot product, so the test of the formula is honest.
Turning $v$ changes both sides together.
For $v = (0, 2)$ the angle is $90^\circ$ and both definitions give $0$.
For $v = (-2, 2)$ the angle is $135^\circ$, the coordinate value is $-6 + 0 = -6$, and the geometric value is $3 \cdot 2\sqrt{2} \cdot \left(-\tfrac{\sqrt{2}}{2}\right) = -6$.

## Explanations

### L1 human

The vector $(3, 0)$ points right, and the vector $(2, 2)$ points up and right at half a right angle.
Multiplying and adding the components gives $6$.
Multiplying the two lengths and the cosine of $45^\circ$ also gives $6$.
So the quick rule with components measures the angle in a hidden way.

### L2 human

In practice you compute with the coordinate definition and interpret with the geometric one.
Here the value $6$ is positive, so the angle is acute.
Watch out: $\cos 45^\circ = \tfrac{\sqrt{2}}{2}$, but a calculator set to radians gives $\cos 45 \approx 0.525$, which is wrong here.
