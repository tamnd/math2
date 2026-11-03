---
tag: D2KCKEP0N4
kind: statement
role: theorem
name: Helmholtz's theorems on vortices
msc: [76B47]
uses: [B3SXT9TWFA, BTHH4Y71QR, ZJH90RWYQ5, BWMB87Q6DM]
about: [B3SXT9TWFA]
sources:
  - url: https://en.wikipedia.org/wiki/Helmholtz%27s_theorems
same_as:
  wikidata: Q985009
  wikipedia: Helmholtz's theorems
---

## Statement

Let $u$ be a smooth velocity field on an open set $\Omega \subseteq \R^3$, with [[vorticity|B3SXT9TWFA]] $\omega = \nabla \times u$.
A vortex line is an integral curve of $\omega$.
A vortex tube is the union of the vortex lines through a closed curve.
Its strength is the flux of $\omega$ through a cross-section, which equals the [[circulation|BTHH4Y71QR]] of $u$ around a curve that goes once around the tube.

1. The strength of a vortex tube is the same for every cross-section.
2. A vortex tube cannot end inside the fluid: it either closes on itself or reaches the boundary of $\Omega$ (or extends to infinity).
3. Assume moreover that the flow is [[inviscid|ZJH90RWYQ5]] and barotropic, with conservative body forces.
Then vortex lines and vortex tubes move with the fluid, and the strength of each vortex tube is constant in time.
In particular, a part of the fluid that is irrotational at one time stays irrotational.

## Remarks

Parts 1 and 2 are kinematic.
They follow from $\nabla \cdot \omega = 0$ and the divergence theorem, applied to a piece of a tube between two cross-sections.
The flux through the side is $0$, so the fluxes through the two ends are equal.
Part 3 follows from [[Kelvin's circulation theorem|BWMB87Q6DM]].
A material surface on which $\omega$ is tangent has zero circulation around each small loop in it, and the flow preserves this property.

Example: a smoke ring is a vortex tube closed into a loop, which travels through the air with its vortex lines carried along.

Without part 3's hypotheses vortex lines need not move with the fluid; viscosity lets vortex lines reconnect.

## Explanations

### L1 human

Swirling fluid organises into vortex lines, like the axis of a tornado or a smoke ring.
Helmholtz showed that these lines cannot just stop in the middle of the fluid; they end on a wall or a surface, or close into rings.
In an ideal fluid they are also glued to the fluid and keep their strength as they move.

### L2 human

The first two theorems hold for any smooth flow, since they only use that vorticity is divergence free.
The third is the local form of Kelvin's circulation theorem.
It is the basis of vortex dynamics: in all of $\R^3$, for velocity decaying at infinity, the velocity is recovered from the vorticity by the Biot–Savart law.
The vorticity is transported and stretched by the flow, as the [[vorticity equation|W5RHJENGWS]] shows.
