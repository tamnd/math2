---
tag: MJEX13ZQWR
kind: counterexample
name: d'Alembert's paradox
msc: [76G25, 76B99]
uses: [84K7TEWZ2Z, ZJH90RWYQ5, XKSK2A46VS, 2JZ0C15A9C]
sources:
  - url: https://en.wikipedia.org/wiki/D%27Alembert%27s_paradox
same_as:
  wikidata: Q284938
  wikipedia: D'Alembert's paradox
---

## Counterexample

Let a rigid body move with constant velocity through an [[incompressible|2JZ0C15A9C]], [[inviscid|ZJH90RWYQ5]] fluid.
The fluid fills the rest of three-dimensional space and is at rest at infinity.
Suppose the flow is a steady [[potential flow|84K7TEWZ2Z]] in the frame of the body.
Then the total force that the fluid exerts on the body is zero; in particular the drag is zero.
In two dimensions the drag is also zero, although a lift proportional to the circulation can remain.
Experiments show that a body moving steadily through a real fluid such as air or water feels a drag force.
So the ideal-fluid model with potential flow fails to predict drag.

## Remarks

The idea of the proof: in three dimensions the velocity potential of the disturbance decays like that of a dipole, so the disturbance velocity decays like $r^{-3}$ at distance $r$.
A momentum balance on a large sphere around the body expresses the force as a flux through the sphere, and this flux tends to zero as the radius grows.
For the [[circular cylinder|XKSK2A46VS]] one can see it directly: the pressures on the front half and on the back half are mirror images.
The resolution is viscosity: however small, it enforces the [[no-slip condition|DF0M8YNQ3D]] and creates a thin [[boundary layer|XXDE4YP722]] at the surface.
The boundary layer can separate from the body, and the resulting wake has a lower pressure than the front, which gives a nonzero [[drag coefficient|NZ4E3K1J59]].

## Explanations

### L1 human

A perfect fluid with no friction, flowing smoothly around an object, would not slow the object down at all.
The fluid pushes on the front, but it pushes back just as hard on the rear.
Every real swimmer, car and aircraft feels drag, so this conclusion is plainly false in practice.
The paradox shows that even a tiny amount of friction in the fluid changes the flow near the body and cannot be ignored.
