---
tag: JVFQZ155S9
kind: example
name: Maclaurin spheroid
msc: [85A15, 76U05]
illustrates: [4FC5XQA2RK]
uses: [4FC5XQA2RK]
sources:
  - url: https://en.wikipedia.org/wiki/Maclaurin_spheroid
same_as:
  wikidata: Q1882430
  wikipedia: Maclaurin spheroid
---

## Example

Consider a homogeneous, incompressible fluid of density $\rho$ that attracts itself by Newtonian gravity and rotates rigidly with angular velocity $\Omega$ about a fixed axis.
A *Maclaurin spheroid* is an oblate spheroid, symmetric about the axis of rotation, that is a figure of equilibrium of this fluid.
This means that in the rotating frame the fluid is in [[hydrostatic equilibrium|4FC5XQA2RK]] and the pressure vanishes on the boundary.
With eccentricity $e$, where $0 < e < 1$, and $G$ the gravitational constant, equilibrium holds exactly when
$$\frac{\Omega^2}{\pi G \rho} = \frac{2 \sqrt{1 - e^2}}{e^3} \left( 3 - 2 e^2 \right) \arcsin e - \frac{6 (1 - e^2)}{e^2}.$$
Check: inside a homogeneous spheroid the gravitational potential is a quadratic function of the coordinates, and so is the centrifugal potential $-\frac{1}{2} \Omega^2 (x^2 + y^2)$.
So the total potential is quadratic.
Let $a$ and $c$ be the equatorial and polar semi-axes.
The total potential is constant on the surface exactly when its coefficients of $x^2 + y^2$ and of $z^2$ are proportional to $1/a^2$ and $1/c^2$.
This condition is the displayed relation.
As $e \to 0$ the right side tends to $0$, and one recovers the sphere at rest.
The right side increases with $e$ up to a maximum of about $0.4494$ at $e \approx 0.9299$ and then decreases to $0$ as $e \to 1$.

## Remarks

At $e \approx 0.8127$, where $\Omega^2 / (\pi G \rho) \approx 0.3742$, the triaxial [[Jacobi ellipsoids|WBSY27NTD1]] branch off from the Maclaurin family.
The spheroid was found by Colin Maclaurin in 1742 in a study of the figure of the Earth.

## Explanations

### L1 human

A ball of liquid floating in space and held together by its own gravity is a sphere when it does not spin.
If it spins, it flattens at the poles and bulges at the equator, like the Earth.
For a uniform liquid, the flattened shape is exactly a squashed sphere, the Maclaurin spheroid.
Spinning faster flattens it more, but only up to a certain rate: beyond it, no flattened shape can balance gravity and spin.
