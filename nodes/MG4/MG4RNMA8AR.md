---
tag: MG4RNMA8AR
kind: concept
name: Bernstein–Gelfand–Ponomarev reflection functors
msc: [16G20]
sources:
  - url: https://en.wikipedia.org/wiki/Gabriel%27s_theorem
---

## Summary

The reflection functors of Bernstein, Gelfand and Ponomarev pass between [[representations of quivers|TXVWFWP6VQ]] that differ by reversing all arrows at one sink or source.
On dimension vectors they act by the simple reflections of the Weyl group of the quiver.
They send each indecomposable representation, other than one simple representation, to an indecomposable one.
They gave a short proof of [[Gabriel's theorem|FC78F2E87E]] and were an early model of tilting theory.

## Explanations

### L1 human

A sink of a quiver is a vertex where all arrows arrive and none leaves.
Reversing all arrows at a sink gives a new quiver, in which that vertex is a source.
The reflection functor turns each representation of the old quiver into one of the new quiver, by replacing the space at the sink by a kernel.
Take an indecomposable representation other than the simple one at the sink.
Then the dimension at that vertex changes by the rule of a reflection: the new dimension is the sum of the neighbouring dimensions minus the old one.
Repeating this moves representations around until they become simple, which is how one classifies them.
