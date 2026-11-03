---
tag: 83FKCHSY02
kind: statement
role: theorem
name: Malus–Dupin theorem
msc: [78A05, 53A05]
uses: [AQ5ZKPZ88R, 0WQJJCCTC8, QDV9SBK6W0, JSTZ7M5VEB]
about: [AQ5ZKPZ88R]
sources:
  - url: https://en.wikipedia.org/wiki/Malus%E2%80%93Dupin_theorem
same_as:
  wikidata: Q3527117
  wikipedia: Malus–Dupin theorem
---

## Statement

Let a smooth family of light rays be orthogonal to a smooth surface, so that the rays are the [[normals|0WQJJCCTC8]] of this surface.
Let the rays undergo finitely many reflections and refractions at smooth surfaces between homogeneous isotropic media.
These follow the [[law of reflection|JSTZ7M5VEB]] and [[Snell's law|QDV9SBK6W0]].
Then the resulting family of rays is again orthogonal to a family of surfaces.

## Remarks

The surfaces can be described explicitly.
Mark on each ray the point at which a fixed [[optical path length|AQ5ZKPZ88R]] from the original surface is reached.
These points form a surface, and it is orthogonal to the rays.
The proof shows that the first variation of the optical path length across neighbouring rays vanishes, using the laws of reflection and refraction at each interface.

Example: rays from a point source are normal to the spheres centred at the source.
After reflection in a parabolic mirror with the source at the focus, they become parallel, and they are normal to the planes perpendicular to the axis.

A family of lines that are the normals of a surface is called a normal congruence.
Not every two-parameter family of lines is a normal congruence, so the theorem has content.

## Explanations

### L1 human

Light from a lamp spreads out along rays, and the wave fronts are spheres at right angles to the rays.
Mirrors and lenses bend the rays in complicated ways.
The theorem says that, however they are bent, there are still wave fronts at right angles to all of them.
These new fronts are the surfaces of equal light travel time.

### L2 human

The theorem is the ray-optics form of the fact that the rays are the gradient lines of a solution of the eikonal equation.
It allows one to speak of wave fronts after an optical system and to define the wave aberration as the deviation of these fronts from spheres.
In symplectic terms, a normal congruence corresponds to a Lagrangian submanifold of the space of rays, and optical systems act by symplectic maps that preserve this property.
