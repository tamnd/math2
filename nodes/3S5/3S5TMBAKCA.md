---
tag: 3S5TMBAKCA
kind: concept
name: Nagata ring
msc: [13F40, 13B22]
specializes: [0670T59HGE]
sources:
  - url: https://en.wikipedia.org/wiki/Nagata_ring
same_as:
  wikidata: Q6958665
  wikipedia: Nagata ring
---

## Summary

A Nagata ring is a [[Noetherian ring|0670T59HGE]] in which [[integral closures|G0V86SJBQW]] are well behaved.
For every prime ideal $\mathfrak{p}$, the integral closure of $R/\mathfrak{p}$ in any finite extension of its fraction field is a finite module.
The notion is named after Masayoshi Nagata, who gave examples of Noetherian domains whose integral closures are not finite.
Every [[excellent ring|YF7YFQ58QJ]] is a Nagata ring, and every finitely generated algebra over a Nagata ring is again a Nagata ring.
The finiteness of integral closures is what makes normalization a finite operation in algebraic geometry.

## Explanations

### L1 human

Starting from a domain, one often wants to add all elements of the fraction field that are roots of monic polynomials, to make the ring "normal".
For the integers inside a number field this adds only finitely many new generators, and the result is a finite module over $\Z$.
For some Noetherian domains, though, infinitely many new generators are needed.
Nagata rings are the rings where this never happens, not even after passing to quotients by primes or to finite field extensions.
