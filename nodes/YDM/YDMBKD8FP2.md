---
tag: YDMBKD8FP2
kind: concept
name: Successive minima
msc: [11H06, 52C07]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski%27s_second_theorem
---

## Summary

The successive minima of a [[lattice|WN9V7WSJKF]] with respect to a symmetric convex body are $n$ numbers $\lambda_1 \le \dots \le \lambda_n$.
The $k$-th one is the smallest scaling factor at which the scaled body contains $k$ linearly independent lattice vectors.
They measure how long the short vectors of the lattice are, in all independent directions at once.
[[Minkowski's second theorem|5H4XZVF9B9]] bounds their product in terms of the volume of the body and the covolume of the lattice.

## Explanations

### L1 human

Take a grid of points and a symmetric convex shape centred at the origin, such as a disc or a box.
Inflate the shape slowly.
At some moment it first catches a grid point other than the origin; the scaling factor at that moment is $\lambda_1$.
Keep inflating until it holds two grid points that do not lie on one line through the origin; that factor is $\lambda_2$, and so on.
For the integer grid $\Z^2$ and the box $[-1, 1] \times [-2, 2]$, the point $(0, 1)$ enters at factor $1/2$ and the point $(1, 0)$ at factor $1$, so $\lambda_1 = 1/2$ and $\lambda_2 = 1$.
