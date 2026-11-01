---
tag: 4MR4YJS1ZD
kind: concept
name: Exchangeable random variables
msc: [60G09]
sources:
  - url: https://en.wikipedia.org/wiki/Exchangeable_random_variables
same_as:
  wikidata: Q4406885
  wikipedia: Exchangeable random variables
---

## Summary

A finite or infinite sequence of [[random variables|0PNRKMRC55]] is exchangeable when its [[joint distribution|0DR81R1F2B]] does not change if finitely many of the variables are permuted.
Every sequence of [[independent and identically distributed|00MRN0FARV]] random variables is exchangeable, but exchangeable variables need not be independent.
Exchangeability is the basic symmetry assumption of Bayesian statistics.
By [[de Finetti's theorem|W19129PVKQ]], an infinite exchangeable sequence is a mixture of i.i.d. sequences.

## Explanations

### L1 human

Exchangeable means that the order of the observations carries no information.
Draw balls one by one, without replacement, from an urn with $3$ red and $2$ blue balls.
The chance that the first ball is red and the second is blue equals the chance that the first is blue and the second is red: both are $\frac{3}{5} \cdot \frac{2}{4} = \frac{2}{5} \cdot \frac{3}{4} = \frac{3}{10}$.
The colours are exchangeable, yet they are not independent, since a red first ball makes a red second ball less likely.
