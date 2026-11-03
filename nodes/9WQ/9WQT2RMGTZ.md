---
tag: 9WQT2RMGTZ
kind: concept
name: Generalized force
msc: [70G10, 70H03]
uses: [BCF1EX9W2M]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_forces
same_as:
  wikidata: Q1153787
  wikipedia: Generalized forces
---

## Summary

A generalized force is the component of the applied forces along one [[generalized coordinate|BCF1EX9W2M]].
It is defined so that the work of the forces in a small change $\delta q$ of the coordinates is $\sum_i Q_i\, \delta q_i$.
Generalized forces appear on the right-hand side of Lagrange's equations.
If the coordinate is a length the generalized force is a force, and if it is an angle the generalized force is a torque.

## Explanations

### L1 human

Describe a pendulum by its angle $\theta$.
Gravity pulls the bob down with force $mg$, but only the part of that pull along the circle matters for the angle.
Turning the angle by a small amount $\delta\theta$ moves the bob by $\ell\, \delta\theta$ along the circle, and gravity then does work $-mg\ell\sin\theta\, \delta\theta$.
The factor $-mg\ell\sin\theta$ is the generalized force for $\theta$: it is the torque of gravity about the pivot.
