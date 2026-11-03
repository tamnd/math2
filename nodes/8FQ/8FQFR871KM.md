---
tag: 8FQFR871KM
kind: concept
name: Substitution model
msc: [92D15, 60J27]
specializes: [TWQFE0FZZS]
sources:
  - url: https://en.wikipedia.org/wiki/Substitution_model
same_as:
  wikidata: Q7632136
  wikipedia: Substitution model
---

## Summary

A substitution model describes how the letters of a biological sequence (nucleotides, amino acids or codons) change into one another over evolutionary time.
It is a [[continuous-time Markov chain|TWQFE0FZZS]] on the alphabet, given by a rate matrix.
Substitution models give the probabilities used in likelihood methods of phylogenetics and turn observed differences between sequences into evolutionary distances.

## Explanations

### L1 human

Follow one position of a DNA molecule down a lineage.
Every so often a mutation replaces its letter by another one.
A substitution model says at what rate each letter turns into each other letter.
From these rates one can compute, for any length of time, the chance that an $A$ at the start has become a $G$ at the end.
The simplest model treats all changes alike; richer models let some changes, such as $A \leftrightarrow G$, happen faster than others.
