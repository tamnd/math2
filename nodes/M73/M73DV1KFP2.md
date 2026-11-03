---
tag: M73DV1KFP2
kind: concept
name: Backus–Gilbert method
msc: [86A22, 65R32, 45B05]
specializes: [C54MFNX576]
sources:
  - url: https://en.wikipedia.org/wiki/Backus%E2%80%93Gilbert_method
same_as:
  wikidata: Q4839810
  wikipedia: Backus–Gilbert method
---

## Summary

The Backus–Gilbert method is a technique for linear inverse problems with finitely many data.
It estimates local averages of an unknown function instead of the function itself.
Each estimate is a linear combination of the data, and it equals a weighted average of the true model.
The weight, the averaging kernel, is made as concentrated as possible around the point of interest.
The width of this kernel measures the resolution, and a trade-off parameter balances resolution against the amplification of data errors.
George Backus and Freeman Gilbert introduced it to interpret the free oscillations of the Earth.
It gave [[geophysical inversion|C54MFNX576]] a precise language for resolution.

## Explanations

### L1 human

With finitely many measurements one can never know a whole function exactly.
The Backus–Gilbert method asks a more modest question: what is the average of the unknown over a small window around a chosen point, and how small can the window be?
It builds the best window that the data allow, then reports both the averaged value and the width of the window.
For example, with only one measurement that averages the unknown over an interval, the best one can report is that same average, with a window as wide as the interval.
