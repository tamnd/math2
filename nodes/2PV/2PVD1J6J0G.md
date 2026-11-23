---
tag: 2PVD1J6J0G
kind: example
name: The concept image of a tangent line as a line that touches once
msc: ["97C30", "97I40"]
topics: [VHGA6J4NZK]
audience: ug1
instance_of: [C5S2X0WDJ8]
uses: [C5S2X0WDJ8, 01R1HW3Y42, 0V1EJCT8G6]
sources:
  - url: https://doi.org/10.1007/BF00305619
    locator: pages 151-169
  - url: https://en.wikipedia.org/wiki/Tangent
    locator: lead section
---

## Example

Students first meet tangent lines at circles, where a tangent meets the circle at exactly one point and the circle lies on one side of it.
Many students form the [[concept image|C5S2X0WDJ8]] "a tangent line touches the curve at one point and does not cross it".
The calculus definition of the [[tangent line|01R1HW3Y42]] to $y = f(x)$ at $x = a$ is the line through $(a, f(a))$ with slope $f'(a)$.
We test the image on $f(x) = x^3$, whose [[derivative|0V1EJCT8G6]] is $f'(x) = 3x^2$.

1. At $a = 0$ we get $f'(0) = 0$, so the tangent line is $y = 0$.
2. For $x < 0$ we have $x^3 < 0$, and for $x > 0$ we have $x^3 > 0$.
   So the curve crosses the tangent line at $0$, and the part "does not cross" fails.
3. At $a = 1$ we get $f(1) = 1$ and $f'(1) = 3$, so the tangent line is $y = 1 + 3(x - 1) = 3x - 2$.
4. The curve meets this line where $x^3 = 3x - 2$, that is, where $x^3 - 3x + 2 = 0$.
5. The cubic factors as $(x - 1)^2 (x + 2)$.
   Check: $(x^2 - 2x + 1)(x + 2) = x^3 - 3x + 2$.
6. So the tangent at $x = 1$ meets the curve again at $x = -2$, at the point $(-2, -8)$, and the part "touches at one point" fails.

The image agrees with the definition for circles and fails for $y = x^3$, so this is a conflict between a concept image and the concept definition.

## Remarks

The conflict runs the other way too.
The vertical line $x = 0$ meets the parabola $y = x^2$ at exactly one point, but the tangent there is $y = 0$.
So "meets the curve at one point" is neither necessary nor sufficient for tangency to a general curve.
For circles the image is correct in both directions, which is why it survives school so well.

## Explanations

### L1 human

For a circle, a tangent line touches the circle at one point and stays on one side.
Many students think this is what "tangent" means for any curve.
For the curve $y = x^3$, the tangent at $0$ is the flat line $y = 0$, and the curve crosses it.
The tangent at $(1, 1)$ cuts the curve again at $(-2, -8)$.
So the picture from circles does not fit all curves.

### L2 human

To expose this conflict, state the image and the definition side by side.
Then choose a curve where they could differ, such as one with an inflection point or one that bends back.
Compute the tangent by the definition, and test each part of the image, "one point" and "does not cross", against it.
Watch out for showing only the picture of $y = x^3$: a student may call $y = 0$ "not really a tangent" and keep the image, while the computation $f'(0) = 0$ ties the line to the definition.
