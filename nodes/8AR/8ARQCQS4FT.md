---
tag: 8ARQCQS4FT
kind: definition
name: Hypersonic flow
msc: [76K05, 76J20]
defines: 5WHN8Q4QC4
uses: [G4EN6Y0ZZ2, GFHJ858AN1]
sources:
  - url: https://en.wikipedia.org/wiki/Hypersonic_speed
---

## Definition

Consider a steady flow of a gas past a body, with a uniform free stream of speed $U_\infty$ and sound speed $c_\infty$ far upstream.
Let $M_\infty = U_\infty / c_\infty$ be the free-stream [[Mach number|GFHJ858AN1]].
The flow is *hypersonic* when $M_\infty$ is much larger than $1$.
By a common convention, this means $M_\infty > 5$.

## Remarks

The threshold $5$ is a convention, not a sharp boundary.
Hypersonic flow is a special case of [[supersonic flow|G4EN6Y0ZZ2]], marked by thin shock layers, strong heating and, at high temperatures, dissociation of the gas.
For a slender body of thickness ratio $\tau$, the hypersonic similarity parameter is $K = M_\infty \tau$.
As $M_\infty \to \infty$ with the body fixed, the shock shape and the pressure coefficient tend to limits, which is the Mach number independence principle.

Example: a spacecraft re-entering the atmosphere from low Earth orbit flies at about $7.8$ km/s, while the speed of sound in air is a few hundred metres per second.
So $M_\infty$ is above $20$, far above $5$.

Non-example: an airliner cruising at $M_\infty \approx 0.85$ is not even supersonic.
