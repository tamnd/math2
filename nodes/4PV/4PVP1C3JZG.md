---
tag: 4PVP1C3JZG
kind: concept
name: Multidimensional transform
msc: [44A30, 42B10]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Multidimensional_transform
same_as:
  wikidata: Q17099178
  wikipedia: Multidimensional transform
---

## Summary

A multidimensional transform is an [[integral transform|YCK709QB06]], or a discrete analogue of one, applied to a function of several variables.
The main examples are the multidimensional [[Fourier transform|DPVM34ADZV]], the [[multidimensional Laplace transform|QT3M720TCV]], the [[multidimensional Mellin transform|92JY94ZJD8]] and, for sequences indexed by $\Z^n$, the [[multidimensional Z-transform|A7NF067M7N]].
When the kernel is a product of one-variable kernels, the transform is the composition of one-variable transforms in each variable.
Such transforms are used for partial differential equations, for images and other multidimensional signals, and in probability for joint distributions.

## Explanations

### L1 human

An image is a function of two variables, the position across and the position down.
A multidimensional transform analyzes such a function in all its variables at once.
Often it is enough to transform in the first variable, then in the second, and so on.
For example, the two-dimensional Fourier transform of a picture is obtained by transforming each row and then each column.
