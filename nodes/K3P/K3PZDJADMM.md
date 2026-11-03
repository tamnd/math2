---
tag: K3PZDJADMM
kind: definition
name: Inertial frame of reference
msc: [70A05, 70B05]
defines: Q05G0NZDNB
uses: [68W1NWECX8]
sources:
  - url: https://en.wikipedia.org/wiki/Inertial_frame_of_reference
---

## Definition

A *frame of reference* is a choice of a time coordinate $t \in \R$ and of Cartesian space coordinates $x \in \R^3$, so that each event receives coordinates $(t, x)$.
A frame of reference is *inertial* if, in its coordinates, each free particle moves with constant velocity.
That is, the position of a free particle has the form $x(t) = x_0 + v t$ with fixed $x_0, v \in \R^3$.
Here a free particle is one on which no force acts, in the sense of [[classical mechanics|68W1NWECX8]].

## Remarks

Example: if a frame with coordinates $(t, x)$ is inertial and $u \in \R^3$ is fixed, then the frame with coordinates $(t, x')$, where $x' = x - u t$, is inertial.
Indeed a free particle $x(t) = x_0 + v t$ has $x'(t) = x_0 + (v - u) t$, again of constant velocity.
Non-example: let $x'$ be the coordinates of a frame that rotates about the third axis with angular speed $\omega \ne 0$ relative to an inertial frame.
A particle at rest at $x = (1, 0, 0)$ in the inertial frame has $x'(t) = (\cos \omega t, -\sin \omega t, 0)$, a circle, so the rotating frame is not inertial.
Newton's first law can be read as the claim that inertial frames exist.

## Explanations

### L1 human

An inertial frame is a point of view from which things left alone keep going straight at a steady speed.
Frames that accelerate or turn are not inertial, because from them free bodies seem to swerve or speed up.
