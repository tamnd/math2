---
tag: GG8AYV847V
kind: concept
name: Spectral sequence
msc: [18G40, 55T05]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_sequence
same_as:
  wikidata: Q3503315
  wikipedia: Spectral sequence
---

## Summary

A spectral sequence is a sequence of pages $E_r$ of objects indexed by two integers.
Each page is the [[homology|2J4JJJYP22]] of the previous one for a differential $d_r$.
It is a bookkeeping tool that computes the homology of a filtered complex or a [[double complex|N80ABTQHEQ]] by successive approximations.
Spectral sequences connect derived functors of composites, the homology of fibrations, and many other computations in algebra and topology.

## Explanations

### L1 human

Think of a grid of groups, one at each point of the plane.
Arrows of a given length and direction connect the groups, and taking homology gives a new, smaller grid.
Then one repeats with longer arrows.
In good cases the grid stops changing after a few steps, and the final grid gives the pieces of the answer, like the layers of a cake.
If all the groups lie on one row, then from the second page on every arrow leaves the row, so the grid stops changing at once.
