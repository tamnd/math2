---
tag: GQFPVXEWK1
kind: concept
name: Time–frequency analysis
msc: [42A38, 94A12, 81S30]
sources:
  - url: https://en.wikipedia.org/wiki/Time%E2%80%93frequency_analysis
same_as:
  wikidata: Q7806653
  wikipedia: Time–frequency analysis
---

## Summary

Time–frequency analysis studies functions and signals through representations that depend on time and frequency together.
The [[Fourier transform|DPVM34ADZV]] shows which frequencies occur in a signal but not when; time–frequency representations try to show both.
Its main tools are the [[short-time Fourier transform|3DHNP5NEWH]], [[Gabor frames|M9WHY8E2PM]], the [[Wigner distribution|FCHW5QGG5V]] and the [[ambiguity function|CDVA7EJSSD]], and it is close to [[wavelet|4PZ35C0GV3]] analysis.
The [[uncertainty principle|S1FB2K14NV]] limits how sharply a function can be located in time and in frequency at once.

## Explanations

### L1 human

A musical score is a time–frequency picture: time runs from left to right, and the height of each note gives its pitch.
A recording is just a pressure wave in time, and its Fourier transform is a list of pitches with no times.
Time–frequency analysis builds pictures like the score from the recording.
A common method looks at the signal through a short window, takes the Fourier transform of what it sees, and slides the window along.
The price is a trade-off: a shorter window gives better timing but blurrier pitch.
