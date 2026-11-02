---
tag: 3MQVKVGYYY
kind: concept
name: Pluricomplex Green function
msc: [32U35]
sources:
  - url: https://en.wikipedia.org/wiki/Plurisubharmonic_function
---

## Summary

Let $\Omega \subseteq \C^n$ be a domain and $w \in \Omega$.
The pluricomplex Green function $g_\Omega(\cdot, w)$ is the largest negative [[plurisubharmonic function|FF2P7ER3QT]] on $\Omega$ with a logarithmic pole at $w$.
It was introduced by Maciej Klimek as the analogue of the classical [[Green's function|M36SD56MWQ]] of a planar domain.
On bounded hyperconvex domains it is continuous and solves a homogeneous [[complex Monge–Ampère|MXRC891TQS]] equation off the pole, with a Dirac mass at the pole.
On bounded convex domains it is expressed through the [[Kobayashi distance|DY8QQ5GTTX]], by a theorem of Lempert.
The version with pole at infinity for a compact set is the [[Siciak extremal function|QBJ9R06GYE]].

## Explanations

### L1 human

In the plane, the Green function of a domain with pole at $w$ is harmonic away from $w$.
It tends to $-\infty$ like $\log\abs{z - w}$ at the pole and tends to $0$ at the boundary.
In several complex variables, harmonic is replaced by plurisubharmonic, and one takes the largest such function that is negative and has the logarithmic pole.
For the unit ball and the pole at the origin, the pluricomplex Green function is simply $\log\abs{z}$.
It measures how far a point is from the pole in a way that holomorphic maps cannot increase.
