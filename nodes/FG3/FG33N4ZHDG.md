---
tag: FG33N4ZHDG
kind: concept
name: Geometric quantization
msc: [53D50, 81S10]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_quantization
same_as:
  wikidata: Q630426
  wikipedia: Geometric quantization
---

## Summary

Geometric quantization is a method to build a quantum system from a classical one, using the geometry of a [[symplectic manifold|CAN490EPRT]].
It first attaches to the manifold a complex line bundle with a connection whose curvature is the symplectic form.
Then it cuts down the space of sections of this bundle with a choice of polarization.
The method was developed by Kostant and Souriau in the 1960s and 1970s, and it is closely tied to the orbit method in representation theory.

## Explanations

### L1 human

A classical system lives on a phase space, and its observables are functions there; a quantum system lives in a Hilbert space, and its observables are operators.
Geometric quantization tries to pass from the first to the second in a way that depends only on the geometry, not on chosen coordinates.
Wave functions become sections of a line bundle over phase space.
A polarization says that they should depend on only half of the variables, such as positions and not momenta.
For the sphere with total area $2\pi\hbar k$, the method produces a space of dimension $k + 1$, which is the state space of a quantum spin.
