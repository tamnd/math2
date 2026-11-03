---
tag: 3KK7H7GQJJ
kind: statement
role: theorem
name: Herschel's condition
msc: [78A05]
uses: [9VGK0SP6EQ, VG0GPBKP84]
about: [VG0GPBKP84]
sources:
  - url: https://en.wikipedia.org/wiki/Herschel%27s_condition
same_as:
  wikidata: Q135111526
  wikipedia: Herschel's condition
---

## Statement

Let a rotationally symmetric optical system image an axial object point $O$ onto an axial image point $O'$ without spherical aberration.
Let $n$ and $n'$ be the [[refractive indices|9VGK0SP6EQ]] of the object and image media.
Let a ray from $O$ make the angle $\theta$ with the axis.
Let $\theta'$ be the angle of the same ray with the axis at $O'$.
Let $m_z$ be the paraxial longitudinal magnification.
Consider a small segment of the axis through $O$.
It is imaged sharply, to first order in its length, if and only if all rays from $O$ through the aperture satisfy
$$n \sin^2\frac{\theta}{2} = m_z \, n' \sin^2\frac{\theta'}{2}.$$

## Remarks

The proof is the axial analogue of the proof of the Abbe sine condition.
Moving the object point along the axis by $\delta z$ changes the optical path length along a ray by $n \, \delta z \cos\theta$ to first order, and similarly in the image space.
Requiring the change of path difference to be the same for all rays, and comparing with the axial ray, gives $n \, \delta z (1 - \cos\theta) = n' \, \delta z' (1 - \cos\theta')$, which is the condition since $1 - \cos\theta = 2\sin^2(\theta/2)$.

The [[Abbe sine condition|4WDZCHTAEZ]] governs sharp imaging of a small area perpendicular to the axis.
Except in special cases, a system cannot satisfy both conditions for all aperture angles, so it cannot sharply image a small volume around $O$.

Example: for small angles, $\sin^2(\theta/2) \approx \theta^2/4$, and paraxial optics gives $\theta' = n\theta / (n' m)$, where $m$ is the lateral magnification.
Then the condition reads $m_z = n' m^2 / n$, which is the standard paraxial relation between longitudinal and lateral magnification.
So paraxial rays always satisfy it, and it restricts only the rays at finite aperture.

## Explanations

### L1 human

Some optical tasks need sharp images of points lying along the axis, at slightly different depths.
Herschel's condition is the rule that a lens must follow for this.
It plays the same role for depth that Abbe's sine condition plays for sideways positions.
Usually a lens can satisfy only one of the two, which is one reason why perfect three-dimensional imaging is hard.

### L2 human

Herschel's condition and the sine condition together show that a stigmatic image of a small three-dimensional region is impossible for most magnifications.
In practice, systems corrected for the sine condition, such as microscope objectives, have a very small depth of sharp focus at large aperture.
