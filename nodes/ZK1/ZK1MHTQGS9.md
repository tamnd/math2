---
tag: ZK1MHTQGS9
kind: concept
name: Generalized Boolean algebra
msc: ["06E75", "06E20"]
specializes: [0HM0HQCK6N]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_algebra_(structure)
---

## Summary

A generalized Boolean algebra is a [[distributive lattice|0HM0HQCK6N]] with a least element $0$ in which any two elements $a$ and $b$ have a difference $a \setminus b$.
This difference is the complement of $a \wedge b$ in the interval $[0, a]$.
It is a [[Boolean algebra|0XADJKM699]] that may lack a greatest element.
Each interval $[0, a]$ in it is a Boolean algebra.
Generalized Boolean algebras correspond to Boolean rings that need not have a unit, in the same way as Boolean algebras correspond to [[Boolean rings|0RCV1ZFP8G]].

## Explanations

### L1 human

Think of the finite subsets of the natural numbers.
You can take unions, intersections and differences of two finite sets and stay finite.
You cannot take the complement of a finite set, because it is infinite.
So the finite sets have set difference but no global complement.
A generalized Boolean algebra is exactly this kind of structure: Boolean algebra with differences, but with no top element required.
