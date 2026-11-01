---
tag: F6M8ME0DQR
kind: concept
name: Bloch space
msc: [30H30]
specializes: [06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/Bloch_space
same_as:
  wikidata: Q4927106
  wikipedia: Bloch space
---

## Summary

The Bloch space is the space of [[holomorphic functions|0NAHXR1FRH]] $f$ on the unit disc for which $(1 - \abs{z}^2)\abs{f'(z)}$ stays bounded.
With a natural norm it is a [[Banach space|06GZ956657]], and the seminorm $\sup_z (1 - \abs{z}^2)\abs{f'(z)}$ does not change under composition with disc automorphisms.
It contains all bounded holomorphic functions and also some unbounded ones such as $\log(1 - z)$.
It is closely tied to [[Bloch's theorem|KW31KDX7TB]], to the space of [[bounded mean oscillation|QJYTXFT8Y4]], and to the duality theory of [[Bergman spaces|2D619WTPYC]].

## Explanations

### L1 human

A function in the Bloch space may grow near the edge of the disc, but its derivative may grow at most like $1/(1 - \abs{z})$.
The factor $1 - \abs{z}^2$ is the natural scale of the disc in hyperbolic geometry, so the condition says that $f$ changes by a bounded amount over each hyperbolic step.
For example, $\log(1 - z)$ is unbounded near $z = 1$, yet it belongs to the Bloch space.
