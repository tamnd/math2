---
tag: SJQDDY9FMX
kind: concept
name: Filtered back-projection
msc: [44A12, 92C55, 65R10]
sources:
  - url: https://en.wikipedia.org/wiki/Tomographic_reconstruction
---

## Summary

Filtered back-projection is the standard method to reconstruct a function in the plane from its [[Radon transform|VJNZJ352PC]].
It has two steps.
First each projection is convolved with a filter whose Fourier transform is close to $\abs{\sigma}$.
Then the filtered projections are fed into the [[dual Radon transform|938SXZQS8G]].
With the exact ramp filter it is the [[Radon inversion formula|HN93ST5CBT]] in dimension $2$.
Practical filters cut off high frequencies, and the method then reconstructs a smoothed version of the function.
It was for a long time the main algorithm of computed tomography scanners.

## Explanations

### L1 human

Back-projection alone smears each measurement along its line and gives a blurred image.
The blur can be computed: it boosts low frequencies too much compared with high ones.
So before smearing back, each measured profile is filtered to undo this imbalance.
The filter sharpens the edges of each profile, and after back-projection the blur is gone.
