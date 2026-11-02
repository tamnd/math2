---
tag: F2CMPBHQ02
kind: concept
name: Acyclic object
msc: [18G10]
sources:
  - url: https://en.wikipedia.org/wiki/Acyclic_object
---

## Summary

For a left exact functor $F$, an object $X$ is $F$-acyclic if all the higher right [[derived functors|NPMC3K6J2F]] $R^n F(X)$ with $n \ge 1$ vanish.
Injective objects are acyclic for every such $F$, but many more objects are acyclic for a given $F$.
Derived functors can be computed with resolutions by $F$-acyclic objects, which are often much easier to find than injective resolutions.

## Explanations

### L1 human

An acyclic object is one on which a functor behaves as if it were exact.
To compute derived functors one needs a resolution by objects of this kind, and injective objects are the universal choice.
But they are large and hard to handle, so one uses objects adapted to the given functor.
For sheaf cohomology, flasque sheaves, whose sections over open sets always extend, are acyclic for the global sections functor.
For the tensor product, flat modules are acyclic, and this is why Tor can be computed with flat resolutions.
