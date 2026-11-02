---
tag: Q7PENKTFHA
kind: concept
name: Biorthogonal wavelet
msc: [42C40, 42C15, 65T60]
specializes: [4PZ35C0GV3]
sources:
  - url: https://en.wikipedia.org/wiki/Biorthogonal_wavelet
same_as:
  wikidata: Q4915256
  wikipedia: Biorthogonal wavelet
---

## Summary

A biorthogonal wavelet is a pair of wavelets $\psi$ and $\tilde\psi$ whose dilated and translated copies are dual to each other.
It replaces a single wavelet whose copies are orthonormal.
One family is used to compute the coefficients of a function and the other to rebuild it.
Giving up orthogonality allows wavelets that are both compactly supported and symmetric.
Among real orthonormal wavelets, only the [[Haar wavelet|JW5PA9XA7F]] has both properties.
Biorthogonal wavelets are used in image compression, for example in the JPEG 2000 standard.

## Explanations

### L1 human

With an orthonormal wavelet, the same function is used to measure a signal and to rebuild it.
A biorthogonal wavelet splits these two jobs between two different functions, an analysis wavelet and a synthesis wavelet.
The two families fit together like a basis and its dual basis in linear algebra: each analysis function sees exactly one synthesis function and is blind to all the others.
This extra freedom lets designers make both functions symmetric and short, which avoids visible distortions in compressed images.
