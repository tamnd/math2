---
tag: 6R0BJ6WS5A
kind: problem
name: Black hole stability problem
msc: ["83C57", "35Q75", "35B35"]
uses: [X3FZC85THY, SB7BVCZJ3F, 626MENG0QH]
about: [X3FZC85THY, YHJ0PDNY8T]
sources:
  - url: https://en.wikipedia.org/wiki/Black_hole
history:
  posed_by: "Tullio Regge and John Archibald Wheeler"
  first_stated: "1957"
---

## Problem

Let $m > 0$ and $\abs{a} < m$, and consider the initial data on a spacelike hypersurface induced by the [[Kerr metric|X3FZC85THY]] of mass $m$ and spin $a$.
Take vacuum initial data sufficiently close to these data, and their maximal globally hyperbolic development under the vacuum [[Einstein field equations|3MCZ97SW6V]].
This development exists by the [[Choquet-Bruhat–Geroch theorem|626MENG0QH]].
Show that it has a complete future null infinity.
Show moreover that its domain of outer communications converges at late times to that of a Kerr metric.
The limit should have parameters $m'$ and $a'$ close to $m$ and $a$.

## Remarks

Regge and Wheeler began in 1957 the study of linear perturbations of the Schwarzschild metric.
The linear stability of Schwarzschild for the full linearised Einstein equations was proved by Dafermos, Holzegel and Rodnianski in 2016.
Klainerman and Szeftel proved nonlinear stability of Schwarzschild for polarised axisymmetric perturbations.
Dafermos, Holzegel, Rodnianski and Taylor proved in 2021 that a codimension-three family of data near Schwarzschild data converges to a nearby Schwarzschild metric.
The codimension accounts for the three components of angular momentum, since general nearby data settle to a rotating black hole.
Nonlinear stability of slowly rotating Kerr black holes, $\abs{a} \ll m$, was announced by Giorgi, Klainerman and Szeftel in 2022.
The full subextremal range $\abs{a} < m$ is still open.
The extremal case $\abs{a} = m$ is different: there are instabilities along the horizon.

## Explanations

### L1 human

The Kerr solution describes a spinning black hole, and astronomers see objects that behave like it.
That only makes sense if a Kerr black hole that is slightly disturbed rings down and settles to another Kerr black hole, instead of breaking apart.
Proving this from Einstein's equations is a hard problem in partial differential equations, because the equations are nonlinear and waves can be trapped near the photon sphere.
