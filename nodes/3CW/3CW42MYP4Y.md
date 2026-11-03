---
tag: 3CW42MYP4Y
kind: concept
name: Travel-time tomography
msc: [86A22, 86A15, 44A12]
specializes: [JRN1693EHB]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_tomography
---

## Summary

Travel-time tomography is [[seismic tomography|JRN1693EHB]] that uses only the arrival times of seismic phases.
The travel time of a wave is the integral along its ray of the slowness, the reciprocal of the wave speed.
So the data are line integrals of the unknown, as in the [[Radon transform|VJNZJ352PC]].
By [[Fermat's principle|RKX9XJ0RVW]], small changes of the ray path do not change the travel time to first order.
So the problem can be linearised along the rays of a reference model.
It is the oldest and most robust form of seismic tomography, used from local to global scales.

## Explanations

### L1 human

Every wave that crosses a region is a little faster or slower than expected, depending on the rock it passed through.
Each such delay is the sum of the small delays along the path.
With many paths crossing in different directions, one can work out which parts of the region cause the delays.
For example, let a ray through two blocks be late by $0.2$ seconds, and a ray through only the first block be on time.
Then the second block is the slow one.
