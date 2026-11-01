---
tag: H9S7RMBMFD
kind: concept
name: Galois ring
msc: [13M05, 11T30]
specializes: [X6713ZP2NH, 0310REJJY8, MZ02BKPHJA]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_ring
---

## Summary

A Galois ring is a finite [[commutative ring|0310REJJY8]] that extends $\Z/p^n\Z$ in the same way as a [[finite field|0ZXZ82FTX2]] $\F_{p^r}$ extends $\F_p$.
Galois rings are [[local rings|MZ02BKPHJA]], and their residue fields are finite fields.
They contain both the rings $\Z/p^n\Z$ and the finite fields as special cases.
They are used in the theory of codes over $\Z/4\Z$ and in the study of [[finite rings|X6713ZP2NH]].

## Explanations

### L1 human

A finite field $\F_{p^r}$ is built from arithmetic modulo a prime $p$ by adding a root of an irreducible polynomial.
A Galois ring does the same over arithmetic modulo a prime power $p^n$.
For example, take arithmetic modulo $4$ and add a symbol $x$ with $x^2 = -x - 1$.
The result has $16$ elements $a + bx$ with $a, b \in \set{0, 1, 2, 3}$.
Reducing everything modulo $2$ gives the field $\F_4$ with four elements.
