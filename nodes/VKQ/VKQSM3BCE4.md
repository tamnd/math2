---
tag: VKQSM3BCE4
kind: concept
name: Deformation of complex structure
msc: [32G05, 14D15]
specializes: [SWFR1GD6QT]
sources:
  - url: https://en.wikipedia.org/wiki/Kodaira%E2%80%93Spencer_map
---

## Summary

A deformation of the complex structure of a compact [[complex manifold|JSGWAN2RJV]] $X$ is a holomorphic family of compact complex manifolds.
The family is parametrized by a base, and its fibre over a chosen base point is $X$.
By Ehresmann's theorem all fibres are diffeomorphic, so the family varies only the complex structure on a fixed smooth manifold.
Kodaira and Spencer showed that first-order deformations are measured by $H^1(X, \Theta_X)$, where $\Theta_X$ is the sheaf of holomorphic vector fields, and obstructions lie in $H^2(X, \Theta_X)$.
The theory is the analytic part of [[deformation theory|SWFR1GD6QT]] and leads to local [[moduli spaces|FJZRW9P0K3]].

## Explanations

### L1 human

A complex manifold is a smooth manifold together with a complex structure, and one can try to change that structure a little.
A deformation is a family of complex manifolds $X_t$ depending holomorphically on a parameter $t$, with $X_0 = X$.
Elliptic curves give the basic picture: the torus $\C / (\Z + \tau \Z)$ changes its complex structure as $\tau$ moves in the upper half-plane, while staying the same smooth torus.
Some manifolds, such as projective space, cannot be deformed at all; they are called rigid.
