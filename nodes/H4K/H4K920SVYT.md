---
tag: H4K920SVYT
kind: concept
name: Unit-regular ring
msc: ["16E50", 16U90]
specializes: [DXX7GNY3HE]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Neumann_regular_ring
---

## Summary

A ring $R$ is unit-regular if every element $a$ has a unit $u$ with $aua = a$.
This strengthens [[von Neumann regularity|DXX7GNY3HE]], where $u$ is only required to be some element of $R$.
Unit-regular rings are [[Dedekind-finite|GV1HKEAWVN]], and for a vector space $V$ the ring of endomorphisms is unit-regular exactly when $V$ is finite-dimensional.
The notion matters in the study of cancellation of modules and direct sum decompositions.

## Explanations

### L1 human

In a von Neumann regular ring each element $a$ has a "partial inverse" $x$ with $axa = a$.
In a unit-regular ring the partial inverse can be chosen to be a genuinely invertible element.
For a square matrix $A$ over a field, one can write $A = PEQ$ with $P, Q$ invertible and $E$ diagonal with entries $0$ and $1$, and then $u = Q^{-1}P^{-1}$ works.
For infinite-dimensional spaces this fails: the shift operator that moves every basis vector one step forward has no such invertible partner.
