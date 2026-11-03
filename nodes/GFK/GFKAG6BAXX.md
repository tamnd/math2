---
tag: GFKAG6BAXX
kind: concept
name: Perfectly matched layer
msc: [78A40, 65N99, 65M99]
sources:
  - url: https://en.wikipedia.org/wiki/Perfectly_matched_layer
same_as:
  wikidata: Q15101726
  wikipedia: Perfectly matched layer
---

## Summary

A perfectly matched layer (PML) is an artificial absorbing layer placed around a computational domain to simulate waves that leave to infinity.
Waves enter the layer without any reflection, at every angle and frequency, and then decay exponentially inside it.
It was introduced by Bérenger in 1994 for [[Maxwell's equations|9BWWD4QK8Y]], and it is now understood as an analytic continuation of space to complex coordinates.
It is used with the [[finite-difference time-domain method|57XRW2119C]], the [[finite element method|98GZ9DVHTA]] and other methods for wave equations.

## Explanations

### L1 human

A computer can only hold a bounded piece of space, but a radiating wave should travel away forever.
If the domain simply ends, the wave bounces back from its edge and spoils the result.
A PML is a border zone made of a fictitious material that swallows the wave without letting it notice the border.
It works like the foam on the walls of a sound-proof room, but for numerical waves, and perfectly in the exact equations.
