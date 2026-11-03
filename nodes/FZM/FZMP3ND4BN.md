---
tag: FZMP3ND4BN
kind: statement
role: theorem
name: Kennedy's theorem on instant centres
msc: [70B15, 70B10]
uses: [WQT8X3V2JQ]
about: [WQT8X3V2JQ]
sources:
  - url: https://en.wikipedia.org/wiki/Instant_centre_of_rotation
---

## Statement

Let three rigid bodies $1$, $2$, $3$ move in a plane.
For distinct $i, j$, let $P_{ij}$ be the [[instant centre of rotation|WQT8X3V2JQ]] at a given instant of the motion of body $j$ relative to body $i$.
Assume that the three relative angular velocities $\omega_{ij}$ are nonzero, so that the three points exist.
Then $P_{12}$, $P_{13}$ and $P_{23}$ lie on one straight line.

## Remarks

Proof idea: compute the velocity, relative to body $1$, of the point $P_{23}$ in two ways.
As a point moving with body $2$, it has velocity $\omega_{12} J (P_{23} - P_{12})$; as a point moving with body $3$, it has velocity $\omega_{13} J (P_{23} - P_{13})$, where $J$ is the rotation by $\pi/2$.
These agree because $P_{23}$ has the same velocity in bodies $2$ and $3$, so $\omega_{12}(P_{23} - P_{12}) = \omega_{13}(P_{23} - P_{13})$.
If $\omega_{12} \ne \omega_{13}$ this writes $P_{23}$ as an affine combination of $P_{12}$ and $P_{13}$; if $\omega_{12} = \omega_{13}$ it gives $P_{12} = P_{13}$; in both cases the three points are collinear.

Example: take a four-bar linkage with fixed frame $1$, crank $2$, coupler $3$ and rocker $4$.
The centre $P_{13}$ lies on the line through the pivots $P_{12}$ and $P_{23}$ and on the line through $P_{14}$ and $P_{34}$.
So it is the intersection of the crank line and the rocker line.

The result is also called the Aronhold–Kennedy theorem or the three-centres theorem.

## Explanations

### L1 human

Take any three parts that move in a plane, such as the frame, a crank and a rod of a machine.
Each pair has a point about which one part is turning relative to the other at this instant.
The theorem says these three points always lie on a straight line.
This lets an engineer find hidden pivot points by drawing lines.

### L2 human

For a mechanism with $n$ links there are $n(n-1)/2$ instant centres.
Those at physical pin joints are known directly, and Kennedy's theorem locates the others as intersections of lines through known centres.
Once the centres are known, the velocity ratio between two links follows from distances between centres, without solving any equations.
It is the main graphical method of planar velocity analysis, and its spatial analogue concerns the instantaneous screw axes of three bodies.
