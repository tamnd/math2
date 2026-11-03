---
tag: AVZ2R5C45M
kind: problem
name: Gibbs paradox
msc: [82B05, 82B30, 82D05]
uses: [TDGEGWHXCT, S1NST0AG71, 1SFZNN31JW]
about: [TDGEGWHXCT]
sources:
  - url: https://en.wikipedia.org/wiki/Gibbs_paradox
history:
  posed_by: "Josiah Willard Gibbs"
  first_stated: "1874–1875"
---

## Problem

Count the [[microstates|S1NST0AG71]] of a classical ideal gas of $N$ identical particles in volume $V$ by phase-space volume alone, without the factor $1/N!$.
The resulting [[microcanonical|TDGEGWHXCT]] entropy is not extensive: doubling $N$, $V$ and the energy does not double it.
Equivalently, removing a partition between two equal samples of the same gas at the same temperature and pressure raises this entropy by $2 N k_B \ln 2$.
Yet nothing observable changes, and reinserting the partition restores the original state.
The problem is to explain this contradiction and to find the correct count of microstates.

## Remarks

The standard resolution divides the phase-space volume by $N!$, treating permutations of identical particles as the same microstate.
With this factor the entropy is extensive, the mixing of identical gases produces no entropy, and the result is the Sackur–Tetrode equation.
For two different gases the mixing entropy $2 N k_B \ln 2$ is real, and it does not shrink as the gases become more similar; it drops to $0$ only when they are identical.
Quantum mechanics justifies the factor through the indistinguishability of identical particles, while other authors argue that it already follows from classical thermodynamic considerations; the interpretation is still discussed.

## Explanations

### L1 human

Two boxes hold the same gas at the same temperature and pressure, and we pull out the wall between them.
Nothing really happens, but a naive count of arrangements says the entropy went up.
The fix is to stop counting as different two arrangements that only swap identical molecules.
This small correction, a division by $N!$, makes entropy behave as thermodynamics requires.
