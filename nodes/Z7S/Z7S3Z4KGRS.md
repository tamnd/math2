---
tag: Z7S3Z4KGRS
kind: concept
name: Optical transfer function
msc: [78A10, 94A08, 42B10]
sources:
  - url: https://en.wikipedia.org/wiki/Optical_transfer_function
same_as:
  wikidata: Q1942321
  wikipedia: Optical transfer function
---

## Summary

The optical transfer function of an imaging system tells how the system passes each spatial frequency of an object to the image.
It is the normalised [[Fourier transform|DPVM34ADZV]] of the [[point spread function|HHWESQD7QB]].
Its modulus, the modulation transfer function, gives the loss of contrast at each frequency, and its argument gives the shift of the pattern.
It turns the blurring of an image, a [[convolution|2Z29JN3VES]], into a simple product in frequency space.

## Explanations

### L1 human

Think of a test card with black and white stripes, and look at it through a lens.
Wide stripes come through with full contrast, but fine stripes come out grey and washed out.
The optical transfer function records, for each stripe width and direction, how much contrast survives.
For a perfect lens with a circular opening, the contrast falls to zero beyond a finest stripe spacing set by the wavelength and the opening.
Engineers use plots of it to compare camera lenses.
