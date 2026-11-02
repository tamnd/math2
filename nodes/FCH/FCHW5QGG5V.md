---
tag: FCHW5QGG5V
kind: concept
name: Wigner distribution function
msc: [81S30, 42A38, 94A12]
sources:
  - url: https://en.wikipedia.org/wiki/Wigner_distribution_function
same_as:
  wikidata: Q233415
  wikipedia: Wigner distribution function
---

## Summary

The Wigner distribution of a function $f$ on $\R$ is a real-valued function on the time–frequency plane built from $f$ and its complex conjugate.
Its integral over frequency gives $\abs{f}^2$, and its integral over time gives $\abs{\hat f}^2$, so it behaves like a joint density of time and frequency.
It can take negative values, so it is not a true probability density.
Eugene Wigner introduced it in 1932 in quantum mechanics, as a quasi-probability distribution on phase space.
It is also a basic tool of [[time–frequency analysis|GQFPVXEWK1]].

## Explanations

### L1 human

One would like a picture that tells how much of a signal sits at each time and each frequency.
The Wigner distribution compares the signal at times a little before and a little after each moment, and takes a Fourier transform of that comparison.
Summing it over all frequencies gives back the energy at each time, and summing over all times gives the energy at each frequency.
For a Gaussian pulse it is a Gaussian bump in the plane.
For a sum of two pulses it shows an extra wavy pattern between them, which can be negative.
