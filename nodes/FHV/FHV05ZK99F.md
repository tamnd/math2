---
tag: FHV05ZK99F
kind: concept
name: Cartier divisor
msc: [14C20, 14C22]
sources:
  - url: https://en.wikipedia.org/wiki/Divisor_(algebraic_geometry)
---

## Summary

A Cartier divisor on a [[scheme|5A35TYZD02]] is a hypersurface described locally by one equation.
The local equations are given up to multiplication by invertible functions.
Each Cartier divisor determines an [[invertible sheaf|7JCF2TE3V5]], and on an integral scheme every invertible sheaf arises this way.
So the classes of Cartier divisors give the [[Picard group|3Z9DCWYXQZ]] of an integral scheme.
On a Noetherian integral separated scheme whose local rings are factorial, Cartier divisors are the same as [[Weil divisors|Z9DN23DAE2]].
Cartier divisors are the right kind of divisor on singular schemes, where Weil divisors and line bundles no longer match.

## Explanations

### L1 human

On a curve, a divisor is a finite list of points with integer multiplicities.
A Cartier divisor records this through local functions: near each point you give a rational function whose zeros and poles have the desired orders.
Two local functions that differ by a nowhere vanishing function describe the same divisor there.
For example, on the affine line with coordinate $t$, the single function $t^2$ describes the point $0$ counted twice.
The function $t^2(t-1)^{-1}$ describes the point $0$ counted twice minus the point $1$.
