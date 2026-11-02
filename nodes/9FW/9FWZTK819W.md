---
tag: 9FWZTK819W
kind: concept
name: Gelfand–Naimark–Segal construction
msc: ["46L30", "46L05", "22D25"]
sources:
  - url: https://en.wikipedia.org/wiki/Gelfand%E2%80%93Naimark%E2%80%93Segal_construction
same_as:
  wikidata: Q5530428
  wikipedia: Gelfand–Naimark–Segal construction
---

## Summary

The Gelfand–Naimark–Segal (GNS) construction starts from a [[state|F7MB2WREBJ]] $\rho$ on a C*-algebra $A$.
It builds a Hilbert space $H_\rho$, a representation $\pi_\rho$ of $A$ on it and a cyclic vector $\xi_\rho$ with $\rho(a) = \ip{\pi_\rho(a)\xi_\rho}{\xi_\rho}$.
It shows that states and cyclic representations are two views of the same thing.
Applied to enough states, it proves that every C\*-algebra is isomorphic to an algebra of operators on a Hilbert space.
The same idea turns a positive-definite function on a group into a unitary representation.

## Explanations

### L1 human

A state assigns a number to each element of an algebra, like the average value of an observable in physics.
The GNS construction uses the state to define an inner product on the algebra itself, by $\ip{a}{b} = \rho(b^* a)$.
After removing elements of length zero and filling in limits, the algebra acts on this space by multiplication on the left.
For the algebra of continuous functions on $[0, 1]$ with the state "integrate against $dx$", the result is the space $L^2[0, 1]$, on which functions act by multiplication.
