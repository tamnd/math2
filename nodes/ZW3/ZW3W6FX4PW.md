---
tag: ZW3W6FX4PW
kind: concept
name: Injective resolution
msc: [18G10, 18G05, 13D02]
sources:
  - url: https://en.wikipedia.org/wiki/Injective_module
---

## Summary

An injective resolution of an object $X$ is an exact sequence $0 \to X \to I^0 \to I^1 \to \cdots$ in which every $I^n$ is injective.
It is the dual of a [[projective resolution|HK2AA1YSQ2]].
Right [[derived functors|NPMC3K6J2F]] of a left exact functor are computed by applying the functor to an injective resolution.
Examples are Ext in the second variable and sheaf cohomology.

## Explanations

### L1 human

An injective object is a target into which maps always extend.
To resolve $X$, embed it into an injective object, then embed the cokernel into another injective object, and so on.
The chain of injective objects remembers $X$ while being easy to map into.
For the integers, $\Z$ sits inside the rationals $\Q$, and the quotient $\Q/\Z$ is again injective.
So $0 \to \Z \to \Q \to \Q/\Z \to 0$ is an injective resolution of $\Z$.
