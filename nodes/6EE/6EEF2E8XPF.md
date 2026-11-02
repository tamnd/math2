---
tag: 6EEF2E8XPF
kind: concept
name: Poisson boundary
msc: [60J50, 60B15, 31C35]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_boundary
same_as:
  wikidata: Q28402746
  wikipedia: Poisson boundary
---

## Summary

The Poisson boundary of a [[random walk on a group|WAS9EANSJJ]] is a measure space that records where the walk goes at infinity.
Every bounded harmonic function for the walk is the Poisson integral of a unique bounded function on this boundary.
This mirrors the Poisson integral formula for bounded harmonic functions on the disc.
The boundary is trivial exactly when all bounded harmonic functions are constant, which is the [[Liouville property|Y1EGR8DF84]].
It was introduced by Furstenberg and developed by Kaimanovich and Vershik, who related its triviality to the entropy of the walk.

## Explanations

### L1 human

Let a random walker move on a group by multiplying by random elements, again and again.
Some information about the walk's position survives forever, for example on a free group the infinite word that the walk spells out in the limit.
The Poisson boundary collects exactly this surviving information, together with the probabilities of each outcome.
On $\Z^d$ nothing survives: the boundary is a single point, and every bounded harmonic function is constant.
On a free group with two generators, the boundary is the set of infinite reduced words, and it carries many bounded harmonic functions.
