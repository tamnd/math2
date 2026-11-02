---
tag: CVYHG5HKPP
kind: problem
name: Inverse spectral problem
msc: [34A55, 34B24, 34L40]
uses: [7WV6B2502K, 89AA6XJY5K]
about: [7WV6B2502K]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_problem
history:
  posed_by: "Viktor Ambartsumian"
  first_stated: "1929"
---

## Problem

Let $q$ be a real potential on an interval, and consider the [[Schrödinger operator|89AA6XJY5K]] $-y'' + q y$ with given boundary conditions.
Determine which spectral data of this operator determine $q$ uniquely, and reconstruct $q$ from such data.

## Remarks

The direct problem computes the eigenvalues from $q$; the inverse problem goes the other way.
Ambartsumian showed in 1929 that for continuous $q$ on $[0, \pi]$ with the conditions $y'(0) = y'(\pi) = 0$, if the eigenvalues are exactly $0, 1, 4, 9, \ldots$, then $q = 0$.
In general one spectrum does not determine $q$: for example, $q(x)$ and $q(\pi - x)$ on $[0, \pi]$ with Dirichlet conditions at both ends have the same eigenvalues.
Göran Borg proved that two spectra, for two different boundary conditions at one end and the same condition at the other, determine $q$.
On a half-line, the spectral measure, or equivalently the Weyl–Titchmarsh function, determines $q$; the [[Gelfand–Levitan|R4MRNP9EQT]] method reconstructs it.

## Explanations

### L1 human

If you hear all the notes a string can play, can you tell how its thickness varies along its length?
This is the inverse spectral problem for a string.
The answer is no from the notes alone, because a string and its mirror image sound the same, but yes with a little more information.
