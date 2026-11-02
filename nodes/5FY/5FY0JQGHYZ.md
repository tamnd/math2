---
tag: 5FY0JQGHYZ
kind: concept
name: Z-transform
msc: [44A55, 39A12, 93C55]
sources:
  - url: https://en.wikipedia.org/wiki/Z-transform
same_as:
  wikidata: Q135810
  wikipedia: Z-transform
---

## Summary

The Z-transform turns a sequence $(x_n)$ of complex numbers into the function $X(z) = \sum_n x_n z^{-n}$ of a complex variable $z$, defined where the series converges.
It is the discrete analogue of the [[Laplace transform|0V49JEZW06]].
It turns shifts of sequences into multiplication by powers of $z$ and convolution into products.
So it is the main tool for linear difference equations and for discrete-time signals and control systems.

## Explanations

### L1 human

A sequence is a list of numbers $x_0, x_1, x_2, \ldots$, such as the samples of a signal.
The Z-transform packs the whole list into one function, using $z^{-n}$ as a label for position $n$.
Delaying the list by one step then just multiplies the function by $z^{-1}$.
For the constant list $1, 1, 1, \ldots$ the transform is $\sum_{n \ge 0} z^{-n} = z/(z - 1)$ for $\abs{z} > 1$.
