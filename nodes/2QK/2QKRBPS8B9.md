---
tag: 2QKRBPS8B9
kind: concept
name: Wavelet packet decomposition
msc: [42C40, 65T60, 94A12]
sources:
  - url: https://en.wikipedia.org/wiki/Wavelet_packet_decomposition
same_as:
  wikidata: Q2736187
  wikipedia: Wavelet packet decomposition
---

## Summary

The wavelet packet decomposition generalizes the [[discrete wavelet transform|P3H4MMC4ZH]].
At every level it splits both the approximation and the detail coefficients again.
The result is a full binary tree of coefficient sequences, which splits the frequency axis into bands of equal width instead of octaves.
Each admissible subtree of this tree gives an orthonormal basis, so one signal has a very large library of bases to choose from.
A best-basis search picks the subtree that represents a given signal most economically, which is useful in compression and denoising.

## Explanations

### L1 human

The ordinary wavelet transform keeps refining only the low frequencies: it splits the low band in two, then the lower half in two, and so on.
Wavelet packets also refine the high bands.
Picture a tree where every node splits into a low and a high branch.
Cutting the tree at different places gives different ways to divide the signal into frequency pieces, all of which keep the full information.
A signal with sharp high-frequency tones, such as a whistle, is better served by a cut that refines the high bands, which the ordinary wavelet transform cannot do.
