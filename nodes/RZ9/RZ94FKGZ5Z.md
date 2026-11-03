---
tag: RZ94FKGZ5Z
kind: concept
name: Nonlinear control
msc: [93C10, 93D15, 93B52]
specializes: [JXZ0GZXET1]
sources:
  - url: https://en.wikipedia.org/wiki/Nonlinear_control
same_as:
  wikidata: Q2707001
  wikipedia: Nonlinear control
---

## Summary

Nonlinear control is the part of [[control theory|JXZ0GZXET1]] that studies [[control systems|ZPDTVZQN5K]] whose dynamics or outputs depend nonlinearly on the state or the input.
Most real systems are nonlinear, and linear methods describe them only near an operating point.
Its tools include [[control-Lyapunov functions|40ED6BYH7W]], [[feedback linearization|1J2KTGXB34]], [[backstepping|5AD7EM0388]], [[sliding mode control|FRYAQABP4P]] and [[gain scheduling|2Y785XM6P5]].

## Explanations

### L1 human

A system is linear when doubling the input doubles the response and responses to two inputs add up.
A pendulum is not like this: the restoring force is proportional to $\sin \theta$, not to the angle $\theta$.
For small swings $\sin \theta \approx \theta$ and linear methods work, but for large swings they can fail.
Nonlinear control develops methods that work for the true nonlinear equations, for example to swing a pendulum up and hold it upright.
