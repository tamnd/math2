---
tag: BWBB42GNEH
kind: concept
name: Deconvolution of seismic data
msc: [86A22, 94A12, 62M10]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_inversion
---

## Summary

Deconvolution of seismic data is the removal of the source wavelet from seismic traces to recover the sequence of reflection coefficients of the layers.
It rests on the convolutional model, in which a trace is the [[convolution|2Z29JN3VES]] of a wavelet with a reflectivity series plus noise.
The standard method designs a Wiener filter from the autocorrelation of the trace, assuming white reflectivity and a minimum-phase wavelet.
It solves the resulting [[Toeplitz|GKY2WSHE26]] system by [[Levinson recursion|60XZ6DNKKW]].
It sharpens the reflections, improves the vertical resolution and suppresses short-period reverberations.

## Explanations

### L1 human

The seismic source does not send a perfectly sharp click but a short wiggle.
Every layer echoes this wiggle, and the echoes of close layers overlap and blur together.
Deconvolution undoes the wiggle, turning each blurred echo back into a sharp spike at the time of its layer.
For example, if the wiggle is "one, then minus one half", then the filter "one, one half, one quarter, and so on" turns it back into a single spike.
