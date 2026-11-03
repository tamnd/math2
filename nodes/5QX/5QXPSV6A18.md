---
tag: 5QXPSV6A18
kind: example
name: Hill's spherical vortex
msc: [76B47]
illustrates: [RW0JK9VDZE, B3SXT9TWFA]
sources:
  - url: https://en.wikipedia.org/wiki/Hill%27s_spherical_vortex
same_as:
  wikidata: Q108280743
  wikipedia: Hill's spherical vortex
---

## Example

Fix a radius $a > 0$ and a speed $U > 0$.
Use cylindrical coordinates $(\varpi, \theta, z)$ and the spherical radius $R = \sqrt{\varpi^2 + z^2}$.
Describe an axisymmetric flow without swirl by its Stokes stream function $\psi(\varpi, z)$.
Its velocity is $u_\varpi = -\frac{1}{\varpi} \partial_z \psi$ and $u_z = \frac{1}{\varpi} \partial_\varpi \psi$.
In the frame moving with the vortex, *Hill's spherical vortex* is the steady flow with the following stream function.
$$\psi = \begin{cases} \dfrac{3U}{4 a^2} \, \varpi^2 \big(a^2 - R^2\big), & R \le a, \\[2mm] -\dfrac{U}{2} \, \varpi^2 \Big(1 - \dfrac{a^3}{R^3}\Big), & R > a. \end{cases}$$
Outside the sphere $R = a$ the flow is the irrotational flow of a uniform stream of speed $U$ past a sphere.
Inside, the azimuthal [[vorticity|B3SXT9TWFA]] has magnitude $\frac{15 U}{2 a^2} \varpi$, proportional to the distance from the axis.
Both formulas give $\psi = 0$ on $R = a$, so the sphere is a streamline.
Both give $\partial_R \psi = -\frac{3U}{2} a \sin^2 \phi$ there, where $\phi$ is the polar angle, so the velocity is continuous across the sphere.
A steady axisymmetric flow without swirl solves the [[Euler equations|RW0JK9VDZE]] when the ratio of azimuthal vorticity to $\varpi$ is constant on each streamline.
Here this ratio is constant inside and zero outside, so the flow is a steady Euler solution.
Far from the sphere the fluid moves with velocity $(0, 0, -U)$.
So in the frame where the fluid at infinity is at rest, the vortex travels with speed $U$ in the positive $z$-direction.

## Explanations

### L1 human

Hill's spherical vortex is a ball of swirling fluid that travels through still fluid at a constant speed without changing shape.
Inside the ball, fluid circulates around a ring, like in a smoke ring whose hole has closed up.
Outside, the fluid flows smoothly around the ball as if it were a solid sphere.
It is one of the few exact solutions of the three-dimensional ideal fluid equations whose vorticity fills a bounded region.
