---
tag: DCHKJBKCMR
kind: concept
name: BRST quantization
msc: [81T70, 81T13, 17B56]
sources:
  - url: https://en.wikipedia.org/wiki/BRST_quantization
same_as:
  wikidata: Q2752849
  wikipedia: BRST quantization
---

## Summary

BRST quantization handles gauge symmetry by enlarging the space of fields with [[ghosts|5WKBCMW1BC]] and introducing an odd operator $Q$, the BRST operator, with $Q^2 = 0$.
Physical states and physical observables are then the cohomology of $Q$: elements killed by $Q$, modulo elements of the form $Q(\cdot)$.
In its simplest form the BRST complex is the [[Chevalley–Eilenberg complex|362T9VND0H]] that computes [[Lie algebra cohomology|69NARSMQCM]].
Its degree-zero cohomology is the space of gauge-invariant states.
The method makes the gauge-fixed theory consistent and is used to prove renormalizability and unitarity of non-abelian gauge theories.

## Explanations

### L1 human

Gauge symmetry means that the description of a system contains redundant variables.
The physical content is what stays the same under the symmetry.
BRST quantization encodes "being invariant" and "being redundant" by a single operator $Q$ whose square is zero.
States with $Q\psi = 0$ are candidates, and states of the form $Q\chi$ are pure redundancy, so the physical states are the first kind modulo the second.
This is the same pattern as closed forms modulo exact forms in de Rham cohomology.
