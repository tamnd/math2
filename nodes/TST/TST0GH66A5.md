---
tag: TST0GH66A5
kind: concept
name: Discrete Fourier transform
msc: ["65T50", "42A38", "43A25"]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_Fourier_transform
same_as:
  wikidata: Q2878
  wikipedia: Discrete Fourier transform
---

## Summary

The discrete Fourier transform turns a finite list of $N$ complex numbers into another list of $N$ numbers, its frequency components.
It is the Fourier transform of the finite cyclic group $\Z / N\Z$, built from the $N$-th [[roots of unity|0YV2CKP2AV]].
It is invertible, it preserves energy up to the factor $N$, and it turns cyclic convolution into pointwise multiplication.
The fast Fourier transform computes it in $O(N \log N)$ operations, which makes it one of the most used algorithms in numerical computing and signal processing.
See the [[definition|TJ9XPJ65YX]].

## Explanations

### L1 human

Take $N$ samples of a signal at equally spaced times.
The discrete Fourier transform tells how much of each of the $N$ basic waves, which complete $0, 1, \dots, N - 1$ full turns over the sampling window, is present in the samples.
For $N = 4$, the list $(1, 1, 1, 1)$ is a pure constant, and its transform is $(4, 0, 0, 0)$: only the frequency $0$ is present.
The list $(1, 0, 0, 0)$, a single spike, has transform $(1, 1, 1, 1)$: every frequency is present equally.
