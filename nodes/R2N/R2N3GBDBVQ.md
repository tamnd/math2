---
tag: R2N3GBDBVQ
kind: concept
name: Brauer character
msc: [20C20]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_representation_theory
---

## Summary

A Brauer character is the analogue of the [[character of a representation|RMWMYBY8TC]] for representations of a finite group over a field of prime characteristic $p$.
It is a complex-valued function on the elements of order prime to $p$.
Its values come from lifting the eigenvalues of each matrix to complex roots of unity.
Brauer characters determine the composition factors of a modular representation, which ordinary traces in characteristic $p$ cannot do.
They are the basic tool of modular representation theory.

## Explanations

### L1 human

In characteristic $p$ the trace of a matrix is only a number modulo $p$, and it loses information; for example the identity matrix of size $p$ has trace $0$.
Brauer's idea is to replace each eigenvalue, a root of unity in the finite field world, by a matching complex root of unity, and add those up.
This gives a genuine complex number that behaves like an ordinary character.
The price is that it is only defined on elements whose order is not divisible by $p$.
