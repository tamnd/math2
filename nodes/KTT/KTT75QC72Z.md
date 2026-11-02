---
tag: KTT75QC72Z
kind: concept
name: Korteweg–De Vries equation
msc: [35Q53, 35Q51]
specializes: [GC5BDZ6QBC]
sources:
  - url: https://en.wikipedia.org/wiki/Korteweg–De_Vries_equation
same_as:
  wikidata: Q601796
  wikipedia: Korteweg–De Vries equation
---

## Summary

The Korteweg–De Vries equation, or KdV equation, is the nonlinear [[partial differential equation|GC5BDZ6QBC]] $u_t + u_{xxx} + 6 u u_x = 0$ for a real function $u(x,t)$.
It models long waves of small amplitude in shallow water.
It has solitary wave solutions that keep their shape, and it is the first equation that was solved by the inverse scattering transform.
It has infinitely many conserved quantities and is a central example of a completely integrable system.

## Explanations

### L1 human

Imagine a single smooth hump of water moving along a narrow canal without changing its shape.
Two effects act on it: the higher parts of the wave move faster, which steepens the front, and dispersion spreads the wave out.
The KdV equation contains exactly these two effects, the term $6 u u_x$ and the term $u_{xxx}$.
When they balance, one gets the soliton $u(x,t) = \tfrac{c}{2} \mathrm{sech}^2\!\big(\tfrac{\sqrt{c}}{2}(x - ct)\big)$ with speed $c > 0$.
Taller solitons are narrower and move faster.
