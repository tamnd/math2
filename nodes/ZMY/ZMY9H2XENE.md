---
tag: ZMY9H2XENE
kind: concept
name: Nest algebra
msc: [47L35, 47A15]
specializes: [672HNBV803]
sources:
  - url: https://en.wikipedia.org/wiki/Nest_algebra
same_as:
  wikidata: Q6997759
  wikipedia: Nest algebra
---

## Summary

A nest is a totally ordered and complete family of closed subspaces of a Hilbert space.
The nest algebra of a nest is the algebra of all bounded operators that leave every subspace of the nest invariant.
Nest algebras are the infinite-dimensional analogues of the algebras of upper triangular matrices.
They are the main examples of non-self-adjoint operator algebras, and every nest algebra is a [[reflexive operator algebra|672HNBV803]].

## Explanations

### L1 human

An upper triangular $n \times n$ matrix sends the span of the first $k$ basis vectors into itself, for each $k$.
These spans form a chain of subspaces, each inside the next.
A nest algebra keeps this picture but allows any complete chain of closed subspaces of a Hilbert space, possibly infinite and with no basis behind it.
For example, on $L^2[0, 1]$ the subspaces of functions vanishing on $[0, t]$, for $0 \le t \le 1$, form a nest, and the Volterra integration operator leaves each of them invariant.
