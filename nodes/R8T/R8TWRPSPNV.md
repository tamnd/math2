---
tag: R8TWRPSPNV
kind: concept
name: Weierstrass excess function
msc: [49K05]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass%E2%80%93Erdmann_condition
---

## Summary

The Weierstrass excess function of a Lagrangian $L(x, y, p)$ is $E(x, y, p, q) = L(x, y, q) - L(x, y, p) - (q - p) \cdot L_p(x, y, p)$.
It measures how far the graph of $q \mapsto L(x, y, q)$ lies above its tangent at $q = p$.
It gives the Weierstrass necessary condition for a strong minimum, and through Hilbert's invariant integral it gives the classical sufficient condition for a strong minimum.

## Explanations

### L1 human

Fix a point and a slope $p$ of a curve, and compare the integrand at another slope $q$ with its tangent-line prediction from $p$.
The excess is the gap between the true value and the prediction.
If the integrand is convex in the slope, the gap is never negative.
For $L = p^2$ the excess is $q^2 - p^2 - 2p(q - p) = (q - p)^2$.
Along a strong minimiser the excess must be nonnegative; otherwise a short sudden switch to the slope $q$ would lower the integral.
