---
tag: 4WDZCHTAEZ
kind: statement
role: theorem
name: Abbe sine condition
msc: [78A05]
uses: [9VGK0SP6EQ, VG0GPBKP84]
about: [VG0GPBKP84]
sources:
  - url: https://en.wikipedia.org/wiki/Abbe_sine_condition
same_as:
  wikidata: Q306243
  wikipedia: Abbe sine condition
---

## Statement

Let a rotationally symmetric optical system image an axial object point $O$ onto an axial image point $O'$ without spherical aberration.
Let $n$ and $n'$ be the [[refractive indices|9VGK0SP6EQ]] of the object and image media.
Let a ray from $O$ make the angle $\theta$ with the axis.
Let $\theta'$ be the angle of the same ray with the axis at $O'$.
Let $m$ be the paraxial lateral magnification.
Consider a small object element in the plane through $O$ perpendicular to the axis.
It is imaged sharply, to first order in its height, if and only if all rays from $O$ through the aperture satisfy
$$n \sin\theta = m \, n' \sin\theta'.$$

## Remarks

The condition says that the ratio $\sin\theta / \sin\theta'$ is the same for all rays, not only for paraxial ones.
One proof compares the optical path lengths from a point near $O$ in the object plane to its ideal image, along different rays.
To first order in the object height $h$, the path length changes by $n h \sin\theta - n' h' \sin\theta'$, and sharp imaging requires this change to be the same for all rays, hence zero.

A system with no spherical aberration that satisfies the sine condition is called aplanatic; it is free of coma near the axis.

Example: a microscope objective of numerical aperture $n \sin\theta = 0.9$ and magnification $m = -40$ in air on the image side needs $\abs{\sin\theta'} = 0.9 / 40 = 0.0225$ at the edge of the aperture.

Without the sine condition the image of an off-axis point is blurred into a comet-shaped spot, the [[aberration|VG0GPBKP84]] called coma.

## Explanations

### L1 human

A good microscope must make sharp images not only of the centre of the field but also of points slightly off centre.
Abbe's sine condition is the rule that a well-corrected lens must follow for this.
It ties the angle at which each ray leaves the object to the angle at which it reaches the image.
If the rule fails, small points near the centre look like tiny comets.

### L2 human

The sine condition is a design criterion for aplanatic objectives and for wide-aperture systems.
It is the large-angle replacement for the paraxial relation $n \theta = m n' \theta'$, which follows from the Lagrange invariant.
For the axial direction, the analogous condition for sharp imaging along the axis is Herschel's condition, and in general the two cannot both hold.
