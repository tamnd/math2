---
tag: GATNQ3T6KQ
kind: concept
name: HP lattice model of proteins
msc: [92C40, 82D60, 92C05]
sources:
  - url: https://en.wikipedia.org/wiki/Hydrophobic-polar_protein_folding_model
same_as:
  wikidata: Q5955260
  wikipedia: Hydrophobic-polar protein folding model
---

## Summary

The HP lattice model is a simplified model of protein folding.
A protein is reduced to a chain of two kinds of beads, hydrophobic ($H$) and polar ($P$).
The chain is placed along a [[self-avoiding walk|E2BVEB570S]] on a square or cubic lattice.
The energy is minus the number of pairs of $H$ beads that are lattice neighbours without being chain neighbours.
The native fold is a conformation of minimal energy.
The model captures the hydrophobic collapse of real proteins, and finding its ground states is [[NP-hard|MHA48AWBXN]].

## Explanations

### L1 human

Proteins fold so that their oily, water-fearing parts hide inside and their water-loving parts stay outside.
The HP model keeps only this effect.
The chain is laid on graph paper, one bead per grid point, with no point used twice.
Each pair of $H$ beads that touch on the grid without being next to each other in the chain earns one point, and the best folds earn the most points.
For the chain $HPPH$, bending it into a square makes the two ends touch and earns one point.
