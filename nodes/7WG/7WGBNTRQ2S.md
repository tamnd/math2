---
tag: 7WGBNTRQ2S
kind: concept
name: Euler angles
msc: [70B10, 15B10]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_angles
same_as:
  wikidata: Q751290
  wikipedia: Euler angles
---

## Summary

Euler angles are three angles that describe the orientation of a rigid body in space.
Each orientation is reached from a reference orientation by three [[rotations|0HFREYRSZP]] about coordinate axes, for example about $z$, then $x$, then $z$ again.
They give coordinates on the [[special orthogonal group|0CGYNDCWRR]] $SO(3)$, and they are used for tops, gyroscopes, aircraft and spacecraft.
These coordinates are singular at some orientations, a defect known as gimbal lock.

## Explanations

### L1 human

To put a book in any position, turn it about a vertical axis and then tilt it about a horizontal axis.
Then turn it again about its own new vertical axis.
The three amounts of turning are the Euler angles.
For a spinning top, the first angle tells where the axis leans and the second how far it leans.
The third tells how much the top has spun about its own axis.
When the tilt is zero, the first and last turns are about the same axis, so only their sum matters; this is the gimbal lock.
