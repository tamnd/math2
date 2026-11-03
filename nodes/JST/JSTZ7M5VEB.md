---
tag: JSTZ7M5VEB
kind: statement
role: fact
name: Law of reflection
msc: [78A05]
uses: [RKX9XJ0RVW, 0WQJJCCTC8, 06BRDF3F0E]
sources:
  - url: https://en.wikipedia.org/wiki/Specular_reflection
    locator: Law of reflection
---

## Statement

Let a ray of light with unit direction vector $d$ hit a smooth reflecting surface at a point where the unit [[normal|0WQJJCCTC8]] is $\nu$.
Let $\theta_i$ be the angle between the incident ray and the normal, and $\theta_r$ the angle between the reflected ray and the normal.
Then the reflected ray lies in the plane spanned by $d$ and $\nu$, on the other side of the normal, and
$$\theta_r = \theta_i.$$
Equivalently, the reflected direction is
$$d_r = d - 2 (d \cdot \nu) \, \nu.$$

## Remarks

The vector form says that $d_r$ is the image of $d$ under the [[reflection|06BRDF3F0E]] in the tangent plane of the surface.
The tangential part of $d$ is kept and the normal part changes sign.

One proof uses [[Fermat's principle|RKX9XJ0RVW]] for a plane mirror.
Reflecting the end point $B$ in the mirror to a point $B'$ turns a path $A \to x \to B$ into a path $A \to x \to B'$ of the same length.
This path is shortest when it is a straight line.
That line makes equal angles with the normal on both sides.

Example: a ray with direction $d = (1, -1, 0)/\sqrt{2}$ hits the mirror $y = 0$ with normal $\nu = (0, 1, 0)$.
Then $d \cdot \nu = -1/\sqrt{2}$ and $d_r = (1, 1, 0)/\sqrt{2}$: both rays make the angle $45^\circ$ with the normal.

## Explanations

### L1 human

A ball bouncing off a wall without spin leaves at the same angle as it came in.
Light does the same on a mirror: the angle of reflection equals the angle of incidence.
This is why you see a sharp image in a flat mirror.
The image seems to lie as far behind the mirror as the object is in front of it.

### L2 human

The law of reflection, with Snell's law, is all that ray tracing needs at a surface.
For curved mirrors it is applied with the normal at each point, which gives the focusing of a parabolic mirror: rays parallel to its axis reflect through its focus.
In wave optics it follows from matching the phases of the incident and reflected plane waves along the surface.
