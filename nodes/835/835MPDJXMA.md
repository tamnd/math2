---
tag: 835MPDJXMA
kind: concept
name: Riesz kernel energy
msc: [31B15, 31C15]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_potential
---

## Summary

The Riesz $s$-energy of a positive measure $\mu$ on $\R^d$ is the double integral of the kernel $\abs{x - y}^{-s}$ against $\mu \times \mu$.
For $s = d - 2$ with $d \ge 3$ it is the Newtonian [[energy of a measure|SFSRQCM3EG]], and for other $s$ it is the energy attached to the [[Riesz potential|1V2N8MFSHC]].
Minimising this energy over probability measures on a compact set defines the Riesz capacity of the set.
The discrete version, a sum over pairs of points, is the energy in problems on optimal point configurations such as the [[Thomson problem|3C7V5X5FY8]].

## Explanations

### L1 human

Spread a unit of charge over a set, and let two small pieces of charge at distance $r$ repel each other with strength $r^{-s}$.
The Riesz $s$-energy adds up this repulsion over all pairs of pieces.
Charge piled up at a single point gives infinite energy, so a set can carry a measure of finite energy only if it is large enough.
For example, the uniform probability measure on the unit sphere of $\R^3$ has $1$-energy equal to $1$.
The exponent $s$ tunes how strongly close pairs are penalised.
