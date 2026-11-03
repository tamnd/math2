---
tag: MM8TS81BAX
kind: concept
name: Chern–Connes character
msc: [46L80, 19D55, 58B34]
sources:
  - url: https://en.wikipedia.org/wiki/Noncommutative_geometry
---

## Summary

The Chern–Connes character is a homomorphism from the K-theory of an algebra to its [[cyclic homology|676K167XS8]].
It sends the class of an [[idempotent matrix|0KCE8CG86P]] to the class of a cyclic cycle built from the idempotent.
It extends the classical [[Chern character|6XRTXBPASW]] of vector bundles to noncommutative algebras, and it is a basic tool of [[noncommutative geometry|PS2MR7P299]].

## Explanations

### L1 human

For a manifold, the Chern character turns a vector bundle into a cohomology class, which is easier to compute with.
In noncommutative geometry a vector bundle is replaced by an idempotent matrix $e$ over an algebra $A$, and cohomology is replaced by cyclic homology.
The Chern–Connes character takes $e$ to the class of the tensor $e \otimes e \otimes \cdots \otimes e$, followed by the trace.
In the simplest degree it is just the trace of $e$; for the algebra $\C$ this trace is the rank of $e$.
Pairing the character with a cyclic cocycle gives numbers that do not change when $e$ is deformed, such as indices of operators.
