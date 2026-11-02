---
tag: H9FSFB7T28
kind: concept
name: Z-transform as a generating function
msc: [44A55, 05A15]
sources:
  - url: https://en.wikipedia.org/wiki/Generating_function
  - url: https://en.wikipedia.org/wiki/Z-transform
---

## Summary

The [[unilateral Z-transform|EPG6JPVJE7]] of a sequence is its ordinary [[generating function|0PHAC833JF]] evaluated at $1/z$.
So the two notions carry the same information and obey the same algebra, with the variable inverted.
Engineers use the Z-transform in the variable $z$, and combinatorialists use generating functions in $w = 1/z$.
Results proved on one side, such as rules for shifts, convolution and partial fractions, transfer to the other at once.

## Explanations

### L1 human

A generating function packs a sequence $x_0, x_1, \ldots$ into $x_0 + x_1 w + x_2 w^2 + \cdots$.
The Z-transform packs it into $x_0 + x_1 z^{-1} + x_2 z^{-2} + \cdots$.
These are the same series with $w = 1/z$.
For the constant sequence $1, 1, 1, \ldots$, the generating function is $1/(1 - w)$ and the Z-transform is $z/(z - 1)$.
