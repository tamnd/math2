---
tag: SKVPKD5VZN
kind: concept
name: Statically indeterminate structure
msc: [70C20, 74K10]
sources:
  - url: https://en.wikipedia.org/wiki/Statically_indeterminate
same_as:
  wikidata: Q333712
  wikipedia: Statically indeterminate
---

## Summary

A structure is statically indeterminate when the equations of static equilibrium are not enough to find all its support reactions and internal forces.
The extra unknowns are fixed only once the deformation of the members is taken into account, through compatibility conditions and the material law.
The number of extra unknowns is the degree of indeterminacy.
Such structures are common because the redundant members give stiffness and safety; they are analysed by the [[flexibility method|8CS7BCP7XS]] or the [[direct stiffness method|7511XGF6MJ]].

## Explanations

### L1 human

A table with three legs on a flat floor shares its weight among the legs in a way that balance alone decides.
Add a fourth leg and balance no longer decides it: the share of each leg depends on how much each one squeezes and on tiny differences in their lengths.
The four-legged table is statically indeterminate.
A beam resting on three supports is the textbook case: two supports would be enough to hold it, and the third makes the reactions depend on how the beam bends.
