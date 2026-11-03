---
tag: Q7MXCRQR8X
kind: concept
name: Substitution matrix
msc: [92D20, 62P10]
sources:
  - url: https://en.wikipedia.org/wiki/Substitution_matrix
same_as:
  wikidata: Q493281
  wikipedia: Substitution matrix
---

## Summary

A substitution matrix gives a score for each pair of letters of an alphabet, such as the twenty amino acids.
These scores are used to score the columns of a [[sequence alignment|G42Y4TPD4N]].
A high score means that the two letters often replace each other in related sequences, a low score that they rarely do.
The common matrices, such as PAM and BLOSUM, are log-odds matrices estimated from alignments of related proteins.

## Explanations

### L1 human

Not all mismatches in protein alignments are equally bad.
Some amino acids have similar chemistry and swap easily during evolution, others almost never.
A substitution matrix is a table that rewards likely pairs and penalizes unlikely ones.
For DNA, the simplest table gives $+1$ to equal letters and $-1$ to different letters.
