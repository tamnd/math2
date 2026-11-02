---
tag: BA9HBM8DFR
kind: concept
name: Besicovitch almost periodic function
msc: [42A75, 43A60]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_periodic_function
---

## Summary

A Besicovitch almost periodic function is a locally integrable function on the real line with the following property.
It can be approximated in a mean sense by trigonometric polynomials with real frequencies.
The mean is the upper average of $\abs{f}^p$ over long intervals $[-T, T]$.
This class, introduced by Abram Besicovitch, is much larger than the class of [[Bohr almost periodic functions|ED69H4C3PK]].
For $p = 2$ it carries a complete Fourier theory with a Parseval identity, and it is used for signals with discrete but irregular spectrum.

## Explanations

### L1 human

Bohr's almost periodic functions must be uniformly close to sums of waves everywhere on the line.
Besicovitch only asks that they be close on average over long stretches of the line.
So a function may have jumps, or even large values on a bounded region, since a bounded region contributes nothing to a long-run average.
For instance, the indicator function of $[0, 1]$ is Besicovitch almost periodic, because its long-run average size is $0$.
