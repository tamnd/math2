---
tag: J1T8NZCVTB
kind: object
name: Poincaré sphere
msc: [78A10]
instance_of: [P9CM4GQ2T0]
uses: [1WA9ASC6NF, P9CM4GQ2T0, 0J78KBPFZB]
sources:
  - url: https://en.wikipedia.org/wiki/Stokes_parameters
---

## Description

Let $(S_0, S_1, S_2, S_3)$ be the [[Stokes parameters|1WA9ASC6NF]] of fully polarized light, so that $S_0^2 = S_1^2 + S_2^2 + S_3^2$ and $S_0 > 0$.
The point $(S_1, S_2, S_3)/S_0$ lies on the unit [[sphere|P9CM4GQ2T0]] of $\R^3$.
The *Poincaré sphere* is this unit sphere, seen as the set of all states of full polarization.
Let $\psi$ be the orientation angle of the polarization ellipse, and let $\tan \chi$ be its ratio of axes, with a sign for the handedness.
In these spherical coordinates, $S_1 = S_0 \cos 2\chi \cos 2\psi$, $S_2 = S_0 \cos 2\chi \sin 2\psi$ and $S_3 = S_0 \sin 2\chi$.

## Remarks

Linear polarizations lie on the equator, and the two circular polarizations are the poles.
Horizontal polarization is the point $(1, 0, 0)$ and vertical polarization is $(-1, 0, 0)$.
Two orthogonal polarization states are always antipodal points.
The angles are doubled: turning a linear polarizer by $90^\circ$ moves the point half way around the equator.
A lossless wave plate acts on the sphere as a rotation.
Partially polarized light gives a point inside the ball, at distance equal to the degree of polarization from the centre.
The sphere is also the complex projective line of the ratio $E_y/E_x$ of the field amplitudes, that is, a copy of the [[Riemann sphere|0J78KBPFZB]].

## Explanations

### L1 human

Every pure polarization of light, linear, circular or elliptical, is a point on a globe.
The equator holds the linear states, and the north and south poles hold the two circular states.
Points in between are elliptical states.
Wave plates turn the globe, which makes it easy to see how a sequence of optical elements changes the polarization.
