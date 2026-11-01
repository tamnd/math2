---
tag: EQ6A3ZN48K
kind: concept
name: Gauss sum
msc: [11T24, 11L05]
specializes: [VTYJ9419C7]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss_sum
same_as:
  wikidata: Q526221
  wikipedia: Gauss sum
---

## Summary

A Gauss sum is a finite sum $\sum_a \chi(a)\psi(a)$ over a [[finite field|0ZXZ82FTX2]], where $\chi$ is a multiplicative character and $\psi$ an additive character.
It mixes the multiplicative and the additive structure of the field.
Its absolute value is the square root of the field size when both characters are nontrivial.
Gauss sums are a basic tool in proofs of reciprocity laws and in the study of [[character sums|VTYJ9419C7]] and [[Dirichlet L-functions|9D2Z543EJQ]].

## Explanations

### L1 human

Take an odd prime $p$ and the complex number $\zeta = e^{2\pi i/p}$, a [[root of unity|0YV2CKP2AV]].
Weight each power $\zeta^a$, for $a = 1, \dots, p - 1$, by $+1$ or $-1$, according to whether $a$ is a square modulo $p$ or not, and add.
For $p = 3$ this gives $\zeta - \zeta^2 = i\sqrt{3}$.
The surprise is that the sum always has absolute value exactly $\sqrt{p}$, much smaller than the $p - 1$ terms suggest.
This square root is where a lot of number theory hides.
