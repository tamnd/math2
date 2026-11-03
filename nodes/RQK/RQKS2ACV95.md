---
tag: RQKS2ACV95
kind: statement
role: theorem
name: Taylor–Proudman theorem
msc: [76U05]
uses: [2MNWD70JN3, SCYK4FMY59, 2JZ0C15A9C, ZJH90RWYQ5]
about: [2MNWD70JN3]
sources:
  - url: https://en.wikipedia.org/wiki/Taylor%E2%80%93Proudman_theorem
same_as:
  wikidata: Q2600653
  wikipedia: Taylor–Proudman theorem
---

## Statement

Let a fluid of constant density $\rho$ occupy an open set of $\R^3$.
Describe it in a frame that rotates with a constant angular velocity $\Omega$.
Assume that its velocity $u$ is continuously differentiable and that $\nabla \cdot u = 0$.
Let $\Phi$ be a potential of the conservative body forces.
Assume that $u$ and the pressure $p$ satisfy the steady, [[inviscid|ZJH90RWYQ5]] balance with no inertia,
$$2 \Omega \times u = -\frac{1}{\rho} \nabla p - \nabla \Phi.$$
Then
$$(\Omega \cdot \nabla) u = 0,$$
that is, the velocity does not vary along the direction of the rotation axis.

## Remarks

Take the curl of both sides.
The right side is a gradient, so its curl is $0$.
Since $\Omega$ is constant, $\nabla \times (\Omega \times u) = \Omega (\nabla \cdot u) - (\Omega \cdot \nabla) u$, and the first term vanishes because the flow is [[incompressible|2JZ0C15A9C]].

The balance in the hypothesis is a good approximation for slow, nearly steady flows in fast rotation, where the [[Rossby number|SCYK4FMY59]] and the Ekman number are small.
Example: in G. I. Taylor's experiments, an obstacle moved slowly along the bottom of a rotating tank of water carries a column of fluid above it.
This column moves as if it were rigid, and it is called a Taylor column.

The hypotheses matter.
With stratification, the density is not constant, the curl of $\nabla p / \rho$ is not zero, and the velocity can vary with height (the thermal wind).
Inertia, viscosity or time dependence also break the conclusion, as in thin boundary layers.

## Explanations

### L1 human

In a fluid that spins fast and moves slowly, the motion is the same at every height along the spin axis.
The fluid behaves like a set of stiff vertical columns that slide around but do not bend or stretch.
An object moved along the bottom of a spinning tank drags a whole column of water above it, all the way to the top.

### L2 human

The theorem is the simplest consequence of [[geostrophic balance|CZ1S1P465Y]] in a homogeneous fluid.
It explains why rotating flows tend to become two-dimensional, and why ocean currents tend to follow lines of constant depth.
Departures from it are the subject of much of geophysical fluid dynamics.
Stratification gives the thermal wind relation.
Viscous [[Ekman layers|H5GNFWEW80]] at the boundaries break it in thin layers and drive a weak vertical flow.
