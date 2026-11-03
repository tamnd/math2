---
tag: M2EASY53HE
kind: concept
name: Isothermal–isobaric ensemble
msc: [82B03, 82B05]
specializes: [M0JYTP1C8B]
sources:
  - url: https://en.wikipedia.org/wiki/Isothermal–isobaric_ensemble
same_as:
  wikidata: Q13638506
  wikipedia: Isothermal–isobaric ensemble
---

## Summary

The isothermal–isobaric ensemble, or $NPT$ ensemble, describes a system with a fixed number $N$ of particles at fixed temperature $T$ and fixed pressure $P$.
Its volume can change, as for a gas under a freely moving piston.
A state with energy $E$ and volume $V$ gets weight proportional to $e^{-(E + PV) / (k_B T)}$.
Its partition function gives the Gibbs free energy, which governs chemistry and phase changes at constant pressure.

## Explanations

### L1 human

Most experiments on a lab bench happen at room temperature and at the pressure of the air.
The sample can expand or shrink, so its volume is not fixed.
This ensemble treats the volume as one more random quantity, and it penalizes large volumes by the work $PV$ needed to push the surroundings back.
For an ideal gas it gives back the law $P \langle V \rangle = (N + 1) k_B T$, which is $PV = N k_B T$ up to a negligible correction for large $N$.
