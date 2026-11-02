---
tag: CGY299QMC3
kind: concept
name: Completely positive map
msc: [46L07, 46L05, 81P47]
sources:
  - url: https://en.wikipedia.org/wiki/Completely_positive_map
same_as:
  wikidata: Q24107961
  wikipedia: Completely positive map
---

## Summary

A completely positive map between C*-algebras is a linear map that stays positive after tensoring with the identity on every matrix algebra $M_n(\C)$.
These maps are the natural morphisms of operator algebras when one keeps only the order structure.
The [[Stinespring dilation theorem|X8K0Z7484R]] describes them all as compressions of $*$-homomorphisms.
In quantum information theory, completely positive trace-preserving maps are the quantum channels.

## Explanations

### L1 human

A positive map sends [[positive elements|NA8DF5X3M4]] to positive elements.
Complete positivity asks more: if the map is applied entrywise to matrices whose entries are in the algebra, positive block matrices must still go to positive block matrices.
Physically, an operation on one system must remain a valid operation when the system is part of a larger one.
The transpose of $2 \times 2$ matrices is positive but not completely positive, which shows that the extra condition is real.
