---
tag: PSQN6H7M0Q
kind: definition
name: Polhode
msc: ["70E15", "70E17"]
defines: WWAXYRZ006
uses: [FHCJDYE7YF, PN15F4ZS8D, WVGTEH6P10]
sources:
  - url: https://en.wikipedia.org/wiki/Polhode
---

## Definition

Let a rigid body move about its centre of mass with no external torque.
Let $I$ be its positive definite [[inertia tensor|WVGTEH6P10]] in a frame attached to the body.
Let $\omega(t)$ be the angular velocity in the body frame, solving [[Euler's equations|PN15F4ZS8D]] with zero torque.
The *polhode* of the motion is the curve $t \mapsto \omega(t)$ in $\R^3$.
The *herpolhode* is the curve traced by the same angular velocity in a frame at rest.

## Remarks

Let $T = \tfrac12 \omega^T I \omega$ and $\abs{L}^2 = \abs{I\omega}^2$, both constant along the motion.
The polhode lies on the intersection of [[Poinsot's ellipsoid|FHCJDYE7YF]] $\set{x^T I x = 2T}$ with the ellipsoid $\set{\abs{Ix}^2 = \abs{L}^2}$.
In principal axes with $I_1 < I_2 < I_3$, these are the curves $\sum_i I_i x_i^2 = 2T$, $\sum_i I_i^2 x_i^2 = \abs{L}^2$.
They are closed curves around the $e_1$-axis or the $e_3$-axis, separated by the curves through the points $\pm\sqrt{2T/I_2}\,e_2$ of the middle axis.
The herpolhode lies in the invariable plane, perpendicular to the angular momentum, on which Poinsot's ellipsoid rolls.

Example: for a symmetric body with $I_1 = I_2$, the polhodes are circles $\omega_1^2 + \omega_2^2 = \text{const}$, $\omega_3 = \text{const}$ around the symmetry axis.

Non-example: if a torque acts, $T$ or $\abs{L}$ changes in general.
Then the curve of $\omega$ need not lie on a fixed ellipsoid, and it is not a polhode in the sense above.

## Explanations

### L1 human

The polhode is the path of the spin axis inside a freely tumbling body.
Because energy and the size of the angular momentum are both conserved, this path is the meeting curve of two egg-shaped surfaces.
