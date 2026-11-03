---
tag: 7PWB4YS8PA
kind: concept
name: Minimum phase system
msc: [93C80, 93C05]
sources:
  - url: https://en.wikipedia.org/wiki/Minimum_phase
same_as:
  wikidata: Q489593
  wikipedia: Minimum phase
---

## Summary

A minimum phase system is a stable linear time-invariant system whose [[zeros|NSGTEGWZY0]] all lie in the stable region.
This region is the open left half-plane in continuous time, and the open unit disc in discrete time.
Equivalently, the system and its inverse are both causal and stable, under suitable properness conditions.
Among all stable systems with the same gain at each frequency, a minimum phase one has the smallest phase lag, which gives the name.
Zeros in the unstable region, called non-minimum phase zeros, put hard limits on what feedback control can achieve.

## Explanations

### L1 human

Some systems first move the wrong way before going the right way.
An example is the water level in a boiler, which first drops when cold water is added.
This initial wrong-way response is the signature of a zero in the right half-plane, and such systems are non-minimum phase.
A minimum phase system has no such zeros, so it can be undone by a stable inverse.
For example, $(s + 1)/(s + 2)$ is minimum phase, while $(1 - s)/(1 + s)$ is not.
The second one has the same size of response at every frequency as the constant $1$, but it delays the phase more and more as the frequency grows.
