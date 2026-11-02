---
tag: ZV65XMJ9A4
kind: concept
name: Kernel density estimation
msc: [62G07]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_density_estimation
same_as:
  wikidata: Q458825
  wikipedia: Kernel density estimation
---

## Summary

Kernel density estimation estimates an unknown [[probability density|0ZY9DX8FBF]] from a sample by placing a small bump, the kernel, at each observation and averaging the bumps.
The width of the bumps, the bandwidth, controls the trade-off between bias and variance.
It is a basic method of [[nonparametric statistics|VFAJ1EG3X5]] and a smooth alternative to the histogram.

## Explanations

### L1 human

Put a small hill of total area $1/n$ on top of each of the $n$ data points and add the hills.
The result is a smooth curve of total area $1$ that is high where the data are dense.
Narrow hills give a wiggly curve that follows every point; wide hills give a smooth curve that may hide real features.
With the Gaussian bump, the estimate is an average of $n$ normal densities centred at the data points.
