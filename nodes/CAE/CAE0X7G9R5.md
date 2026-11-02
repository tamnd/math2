---
tag: CAE0X7G9R5
kind: concept
name: Peetre K-functional
msc: [46B70, 41A25, 41A65]
sources:
  - url: https://en.wikipedia.org/wiki/Interpolation_space
---

## Summary

The Peetre K-functional $K(t, x)$ measures how well an element $x$ of a sum $X_0 + X_1$ of two Banach spaces splits into pieces in $X_0$ and $X_1$.
The size of the second piece carries the weight $t$.
It is the basic tool of the real method of [[interpolation spaces|VX1R6FN6PS]].
In approximation theory it links smoothness to approximation, since for suitable pairs of spaces it is equivalent to a [[modulus of smoothness|CRPZ1RVNKQ]].

## Explanations

### L1 human

Think of $X_0$ as rough functions measured in a weak norm and $X_1$ as smooth functions measured in a strong norm.
To compute $K(t, f)$ you write $f$ as a smooth part plus a rough remainder and pay the size of the remainder plus $t$ times the size of the smooth part.
For small $t$ smoothness is cheap, so you can take a smooth part very close to $f$.
How fast $K(t, f)$ goes to $0$ as $t \to 0$ tells you how well $f$ can be approached by smooth functions.
