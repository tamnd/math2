---
tag: 1P8WX3EGHF
kind: concept
name: Region of convergence
msc: [44A55, 30B10]
sources:
  - url: https://en.wikipedia.org/wiki/Z-transform
    locator: Region of convergence
  - url: https://en.wikipedia.org/wiki/Radius_of_convergence
---

## Summary

The region of convergence of a [[Z-transform|5FY0JQGHYZ]] is the set of complex numbers $z$ where its defining series converges absolutely.
It is an annulus centred at $0$, possibly empty, possibly with some boundary points.
It plays the part that the disc given by the [[radius of convergence|0N288P2TB5]] plays for a power series.
A Z-transform is only known together with its region of convergence: two different sequences can have the same formula for $X(z)$ on two different regions.
The position of the region with respect to the unit circle tells whether a system is causal and stable.

## Explanations

### L1 human

The Z-transform is an infinite sum, and an infinite sum only gives a number when it converges.
The region of convergence is the set of points where it does.
For the sequence $1, 2, 4, 8, \ldots$ the sum $\sum 2^n z^{-n}$ converges exactly when $\abs{z} > 2$, the outside of a circle of radius $2$.
For a sequence that is nonzero only for negative $n$, the region is instead the inside of a circle.
