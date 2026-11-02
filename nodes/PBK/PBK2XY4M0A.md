---
tag: PBK2XY4M0A
kind: concept
name: Fractional factorial design
msc: [62K15]
sources:
  - url: https://en.wikipedia.org/wiki/Fractional_factorial_design
same_as:
  wikidata: Q2400745
  wikipedia: Fractional factorial design
---

## Summary

A fractional factorial design runs only a chosen fraction of the combinations of a [[factorial experiment|EHJ3R589ZX]].
An example is $2^{k-p}$ of the $2^k$ runs of a two-level design.
The fraction is chosen by a defining relation, so that the main effects and low-order interactions can still be estimated.
The price is that they are aliased with higher-order interactions.
The resolution of the design measures how severe the aliasing is.
Such designs make screening experiments with many factors affordable, on the assumption that high-order interactions are negligible.

## Explanations

### L1 human

With seven factors at two levels, a full factorial needs $128$ runs, often far too many.
A well chosen eighth of it, $16$ runs, still measures each factor's main effect.
The price is that some effects become indistinguishable: in the data, a main effect looks exactly like a certain interaction of other factors.
If those interactions are small, nothing important is lost.
