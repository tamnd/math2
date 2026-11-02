---
tag: WFFGB4RK60
kind: concept
name: Jacobson topology
msc: [16D60, 46J20]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_ideal
---

## Summary

The Jacobson topology, or hull-kernel topology, is a topology on the set $\operatorname{Prim}(R)$ of [[primitive ideals|M0JDQR0V5S]] of a ring $R$.
A set of primitive ideals is closed when it consists of all primitive ideals that contain some fixed ideal.
For a commutative ring it is the [[Zariski topology|8SQK7RTB63]] restricted to maximal ideals.
So the space $\operatorname{Prim}(R)$ is a noncommutative analogue of the [[spectrum of a ring|FB45BHHA2J]].
For a commutative C*-algebra $C_0(X)$ it recovers the space $X$.
For this reason it is the standard topology on the primitive spectrum of a C*-algebra.

## Explanations

### L1 human

For a commutative ring the maximal ideals behave like points, and the Zariski topology turns them into a geometric space.
In a noncommutative ring the right replacement for points is the primitive ideals, the annihilators of simple modules.
The Jacobson topology declares a set of these points closed when it is "cut out by an ideal": it is all the points that contain that ideal.
For the integers the points are the ideals $p\Z$, and the closed sets are the finite sets of primes together with the whole space.
