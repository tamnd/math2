---
tag: 7QNRC9SJVV
kind: concept
name: Harmonic analysis
msc: [42A99, 42B99, 43A99]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_analysis
same_as:
  wikidata: Q876215
  wikipedia: Harmonic analysis
---

## Summary

Harmonic analysis studies functions by writing them as superpositions of basic waves, and studies operators through their action on these waves.
Its classical core is the theory of [[Fourier series|G12KXDHPPS]] on the circle and of the [[Fourier transform|DPVM34ADZV]] on $\R^n$.
On a general locally compact group the waves are replaced by characters or irreducible representations, which gives [[harmonic analysis on groups|5E6KB3V8R0]].
The subject supplies tools for partial differential equations, number theory, probability and signal processing.

## Explanations

### L1 human

A chord played on a piano is a sum of single notes, and a trained ear can hear which notes are present.
Harmonic analysis does the same for functions: it splits a function into pure oscillations and records how much of each frequency it contains.
Many questions become easier on the side of the frequencies, because differentiation and translation act very simply on a pure wave.
For example, the derivative of $e^{inx}$ is $in \, e^{inx}$, so differentiation becomes multiplication by $in$.
The hard part is to put the pieces back together and control in which sense the sum of the waves gives back the function.
