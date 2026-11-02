---
tag: AF9NY73QHJ
kind: concept
name: Lifting scheme
msc: [65T60, 42C40, 94A12]
sources:
  - url: https://en.wikipedia.org/wiki/Lifting_scheme
same_as:
  wikidata: Q3238415
  wikipedia: Lifting scheme
---

## Summary

The lifting scheme is a way to build and compute wavelet transforms by a sequence of simple, invertible steps.
A signal is split into its even and odd samples.
The odd samples are predicted from the even ones, and the even ones are updated from the prediction errors.
Every step can be undone by reversing its sign, so perfect reconstruction is automatic.
The scheme can cut the cost of many [[fast wavelet transforms|PDVYQAW887]] by up to about one half.
It works in place, gives integer-to-integer transforms, and extends to irregular grids.

## Explanations

### L1 human

Imagine a signal as two interleaved lists: the even-numbered and the odd-numbered samples.
If the signal is smooth, each odd sample is close to its even neighbours, so it can be guessed from them.
Store only the error of the guess; for smooth signals these errors are small.
Then adjust the even samples slightly so that they keep the average of the signal.
For example, with $x = (2, 4, 6, 8)$ and the guess "odd equals the even sample before it", the errors are $(2, 2)$ and the updated evens are $(3, 7)$, the pairwise averages.
Running the steps backwards gives back the original signal exactly.
