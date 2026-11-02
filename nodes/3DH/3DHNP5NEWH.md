---
tag: 3DHNP5NEWH
kind: concept
name: Short-time Fourier transform
msc: [42A38, 94A12]
sources:
  - url: https://en.wikipedia.org/wiki/Short-time_Fourier_transform
same_as:
  wikidata: Q1477735
  wikipedia: Short-time Fourier transform
---

## Summary

The short-time Fourier transform of a function $f$ on $\R$ is a [[Fourier transform|DPVM34ADZV]] taken through a window.
One multiplies $f$ by a window $g$ shifted to a point $x$, and transforms the product.
It is a function of position $x$ and frequency $\omega$, and so it shows which frequencies are present near each time.
It is the basic tool of [[time–frequency analysis|GQFPVXEWK1]]; its squared modulus is the spectrogram.
For a window in $L^2$ it is an isometry up to the factor $\norm{g}_2$, so no information is lost.

## Explanations

### L1 human

Listen to a piece of music through a small moving window in time.
At each position of the window, ask which pitches are sounding: this is a Fourier transform of the windowed piece.
Collecting the answers for all positions gives a two-dimensional picture, time against pitch.
A narrow window shows well when notes start but blurs their pitch, and a wide window does the opposite.
