---
tag: 5G0AKZ8SXJ
kind: concept
name: Models of DNA evolution
msc: [92D15, 92D20, 60J27]
specializes: [8FQFR871KM]
sources:
  - url: https://en.wikipedia.org/wiki/Models_of_DNA_evolution
same_as:
  wikidata: Q6888417
  wikipedia: Models of DNA evolution
---

## Summary

Models of DNA evolution are the [[substitution models|8FQFR871KM]] whose states are the four nucleotides $A$, $C$, $G$ and $T$.
They form a nested family.
It runs from the Jukes–Cantor model with a single rate to the general time-reversible model with six exchange rates and four base frequencies.
They are used to compute likelihoods of [[phylogenetic trees|RK58WSHJSG]] and to correct observed differences between DNA sequences for multiple hits at the same site.

## Explanations

### L1 human

Two DNA sequences that split from a common ancestor long ago differ at some positions.
The fraction of differing positions underestimates how many changes happened, because one position can change twice, or change and change back.
A model of DNA evolution gives the rates of the twelve possible changes between the four letters, and from it one can correct for these hidden changes.
Biology suggests which models are useful: for example, changes between $A$ and $G$ or between $C$ and $T$ (transitions) are usually more frequent than the other changes (transversions).
