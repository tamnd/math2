---
tag: AGM9B65HQ4
kind: definition
name: Mach wave
msc: [76J20, 76N15]
defines: C5QBSMGHCR
uses: [G4EN6Y0ZZ2, GFHJ858AN1, 7XAPBCJK3B, JSDMGGTG7G]
sources:
  - url: https://en.wikipedia.org/wiki/Mach_wave
---

## Definition

Consider a steady plane [[supersonic flow|G4EN6Y0ZZ2]], with local [[Mach number|GFHJ858AN1]] $M(x) > 1$.
At each point $x$, the *Mach angle* is $\mu(x) = \arcsin(1/M(x))$, with $0 < \mu < \pi/2$.
A *Mach wave*, or Mach line, is a curve whose tangent at each point makes the angle $\mu$ with the local flow velocity.
The angle may lie on either side of the velocity.
Through each point pass two Mach lines, one on each side of the velocity.
They are the characteristic curves of the steady equations of the flow.

## Remarks

Example: in a uniform stream at $M = 2$ the Mach lines are the straight lines at $\pm 30^\circ$ to the flow, since $\arcsin(1/2) = 30^\circ$.
A weak bump on a wall produces a disturbance that is carried along such a line.
Non-example: in a subsonic flow, $M < 1$, the angle $\arcsin(1/M)$ is not defined, and the steady equations are elliptic with no real characteristics.
A Mach wave is the limit of a [[shock wave|JSDMGGTG7G]] whose strength tends to $0$; across it the flow changes only infinitesimally.
The [[method of characteristics|7XAPBCJK3B]] computes supersonic flows by following the Mach lines.
