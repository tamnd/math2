---
tag: 8GQRJ6TPVC
kind: concept
name: Gabor transform
msc: [42A38, 94A12]
specializes: [3DHNP5NEWH]
sources:
  - url: https://en.wikipedia.org/wiki/Gabor_transform
same_as:
  wikidata: Q996397
  wikipedia: Gabor transform
---

## Summary

The Gabor transform is the [[short-time Fourier transform|3DHNP5NEWH]] with a Gaussian window.
Dennis Gabor proposed it in 1946 for the analysis of signals.
The Gaussian is the window that is best concentrated in time and frequency at once, in the sense of the Heisenberg [[uncertainty principle|S1FB2K14NV]].
This makes the Gabor transform a natural choice for a time–frequency picture.

## Explanations

### L1 human

Look at a signal through a soft window shaped like a bell curve, centred at a time $\tau$.
Then measure the frequencies of what is seen.
Unlike a window with sharp edges, the bell curve introduces no sharp jumps, so it creates no spurious high frequencies.
Moving $\tau$ along the time axis gives a picture of how the frequency content of the signal changes in time.
