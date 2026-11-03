---
tag: WTN7MW3GKS
kind: definition
name: Focal mechanism
msc: [86A15, 86A22]
defines: PZJMC4XY5W
uses: [S5TXH6MZ05, ZNN5WAT301, EEPJJHC5JZ]
sources:
  - url: https://en.wikipedia.org/wiki/Focal_mechanism
---

## Definition

Let an earthquake be a shear slip on a planar fault, modelled as a [[double-couple source|S5TXH6MZ05]].
Its *focal mechanism* is the triple of angles $(\phi_s, \delta, \lambda)$ that fixes the fault plane and the slip direction:

1. the *strike* $\phi_s \in [0°, 360°)$ is the azimuth, clockwise from north, of the horizontal line in the fault plane.
This line is oriented so that the fault dips to its right.
2. the *dip* $\delta \in [0°, 90°]$ is the angle between the fault plane and the horizontal.
3. the *rake* $\lambda \in (-180°, 180°]$ is the angle in the fault plane from the strike direction to the slip.
The slip is that of the hanging wall relative to the footwall.

## Remarks

Let $n$ be the unit normal of the fault and $d$ the unit slip vector, so the [[moment tensor|ZNN5WAT301]] is $M = M_0(n d^T + d n^T)$.
The far-field [[P-wave|EEPJJHC5JZ]] leaving in the unit direction $\gamma$ has amplitude proportional to $\gamma^T M \gamma = 2M_0 (\gamma \cdot n)(\gamma \cdot d)$.
So the first motion vanishes on the two planes $\gamma \cdot n = 0$ and $\gamma \cdot d = 0$, the *nodal planes*, and changes sign across each.
Example: $\lambda = 90°$ is a pure thrust (reverse) fault, $\lambda = -90°$ a pure normal fault, $\lambda = 0°$ a left-lateral and $\lambda = 180°$ a right-lateral strike-slip fault.
Non-example: exchanging $n$ and $d$ leaves $M$ unchanged.
So the auxiliary plane, with normal $d$ and slip $n$, gives the same radiation.
Its angles fit the same seismic data, but they do not describe the true fault.
This ambiguity is resolved only by other evidence, such as the alignment of aftershocks or a surface rupture.
