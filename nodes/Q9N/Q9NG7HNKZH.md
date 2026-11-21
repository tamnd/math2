---
tag: Q9NG7HNKZH
kind: example
name: Components of the weight on a ramp
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [0JW13B48YP]
illustrates: [NA6Q7ME9G0]
uses: [0JW13B48YP, 0S52TNNTH9, 0XKBKGTCPC]
sources:
  - url: https://en.wikipedia.org/wiki/Inclined_plane
    locator: lead section
---

## Example

A box with a weight of $10$ newtons rests on a ramp.
In coordinates with the $y$-axis pointing up, the weight is $F = (0, -10)$, and the ramp rises in the direction $v = (4, 3)$.
We split $F$ into a part along the ramp and a part perpendicular to it with the [[vector projection|0JW13B48YP]].

1. The [[dot products|0S52TNNTH9]] are $F \cdot v = 0 \cdot 4 + (-10) \cdot 3 = -30$ and $v \cdot v = 16 + 9 = 25$.
2. The part along the ramp is
   $$p = \frac{-30}{25}\, v = -\tfrac{6}{5}(4, 3) = (-4.8, -3.6).$$
3. Its [[length|0XKBKGTCPC]] is $\|p\| = \sqrt{23.04 + 12.96} = \sqrt{36} = 6$ newtons. It points down the ramp, since its coefficient $-\tfrac{6}{5}$ is negative.
4. The part perpendicular to the ramp is $q = F - p = (4.8, -6.4)$, with length $\sqrt{23.04 + 40.96} = \sqrt{64} = 8$ newtons.
5. Check: $q \cdot v = 19.2 - 19.2 = 0$, and $6^2 + 8^2 = 100 = \|F\|^2$.

## Remarks

The ramp makes an angle $\alpha$ with the ground, where $\sin \alpha = \tfrac{3}{5}$ and $\cos \alpha = \tfrac{4}{5}$.
So the results agree with the school formulas $10 \sin \alpha = 6$ along the ramp and $10 \cos \alpha = 8$ across it.
The vector method reached the same numbers without ever naming the angle.

A steeper ramp in the direction $(3, 4)$ swaps the two numbers: $8$ newtons along the ramp and $6$ newtons into it.
The part $q$ presses the box onto the ramp, and the ramp pushes back with the normal force $-q$.
If friction is ignored, the box slides because nothing balances $p$.

## Explanations

### L1 human

Gravity pulls the box straight down with $10$ newtons.
On a slope, part of this pull drags the box down the slope, and part presses it into the slope.
The projection gives the first part, $6$ newtons, and the rest is $8$ newtons.
The two parts are at a right angle, so $6^2 + 8^2 = 10^2$.

### L2 human

In mechanics we split a force along the directions that matter for the motion, here along the ramp and across it.
The vector method needs only the direction vector of the ramp, not the angle.
Watch out: the projection is the same for $v = (4, 3)$ and for $v = (-4, -3)$, but the coefficient in step 2 changes sign.
So the sign tells you the direction only relative to the $v$ you chose.
