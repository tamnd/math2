---
tag: FWCGMZ8KKC
kind: example
name: Euler top
msc: ["70E40", "70E17", 37J35]
instance_of: [N0N7CMRCMH]
uses: [PN15F4ZS8D, WVGTEH6P10, FHCJDYE7YF, P071B692JF]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange,_Euler,_and_Kovalevskaya_tops
---

## Example

The *Euler top* is a rigid body that turns about a fixed point $O$ with no external torque.
This happens when $O$ is the centre of mass and gravity is the only force, or when no force acts at all.
Let $I_1, I_2, I_3 > 0$ be its principal moments of inertia at $O$ and $\omega$ its angular velocity in the principal body frame.
The motion of $\omega$ is given by [[Euler's equations|PN15F4ZS8D]] with zero torque:
$$I_1\dot\omega_1 = (I_2 - I_3)\omega_2\omega_3, \quad I_2\dot\omega_2 = (I_3 - I_1)\omega_3\omega_1, \quad I_3\dot\omega_3 = (I_1 - I_2)\omega_1\omega_2.$$

It is an [[integrable system|N0N7CMRCMH]].
Its phase space is the cotangent bundle of the rotation group, of dimension $6$, so three independent integrals in involution are needed.
These are the energy $H = \tfrac12(I_1\omega_1^2 + I_2\omega_2^2 + I_3\omega_3^2)$, the squared length $\abs{L}^2 = I_1^2\omega_1^2 + I_2^2\omega_2^2 + I_3^2\omega_3^2$ of the angular momentum, and one component of the angular momentum in a fixed frame.
The check that $H$ is conserved: $\dot H = \sum_i I_i \omega_i \dot\omega_i = \omega_1\omega_2\omega_3\big((I_2 - I_3) + (I_3 - I_1) + (I_1 - I_2)\big) = 0$.
The same computation with weights $I_i^2$ shows that $\abs{L}^2$ is conserved, and the fixed-frame angular momentum is conserved because no torque acts.

## Remarks

Using the two integrals to eliminate $\omega_1$ and $\omega_3$ leaves one first-order equation for $\omega_2$, solved by [[Jacobi elliptic functions|P071B692JF]].
Geometrically, the motion is described by [[Poinsot's ellipsoid|FHCJDYE7YF]] rolling on the invariable plane.

## Explanations

### L1 human

The Euler top is a body tumbling freely, like a thrown book or a satellite, seen from its centre of mass.
Its motion can be solved exactly because energy and angular momentum are conserved, and these give just enough equations to pin down the motion.
