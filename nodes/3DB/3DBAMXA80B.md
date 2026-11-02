---
tag: 3DBAMXA80B
kind: concept
name: Bilateral Z-transform
msc: [44A55, 94A12]
specializes: [5FY0JQGHYZ]
sources:
  - url: https://en.wikipedia.org/wiki/Z-transform
    locator: Bilateral Z-transform
---

## Summary

The bilateral Z-transform of a sequence $(x_n)_{n \in \Z}$ sums over all integers: $X(z) = \sum_{n \in \Z} x_n z^{-n}$.
It is the form of the [[Z-transform|5FY0JQGHYZ]] for signals that extend into the past as well as the future.
Its set of convergence is an annulus centred at $0$, possibly empty.
The same formula for $X(z)$ can come from different sequences on different annuli.
It is the discrete analogue of the two-sided Laplace transform.

## Explanations

### L1 human

The bilateral transform looks at a sequence in both directions of time.
Terms with $n \ge 0$ need $\abs{z}$ large to converge, and terms with $n < 0$ need $\abs{z}$ small.
So the transform lives on a ring between two circles.
For example, $x_n = 2^{-\abs{n}}$ has transform defined for $1/2 < \abs{z} < 2$.
