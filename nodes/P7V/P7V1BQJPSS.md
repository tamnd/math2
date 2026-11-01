---
tag: P7V1BQJPSS
kind: concept
name: Group law on an elliptic curve
msc: [14H52, 11G05]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_curve
    locator: The group law
---

## Summary

The points of an [[elliptic curve|427N6S6QQW]] $E$ over a field $K$, together with the point at infinity $O$, form an [[abelian group|082GHNPJ53]] $E(K)$.
The operation is the chord-and-tangent law: three points add up to $O$ exactly when they lie on a line.
This group structure is what makes elliptic curves so useful, from [[Mordell's theorem|BZHGKN6Q3K]] to elliptic curve cryptography.

## Explanations

### L1 human

To add two points $P$ and $Q$ on the curve, draw the line through them.
It meets the cubic curve in a third point; reflect that point in the $x$-axis to get $P + Q$.
To double a point, use the tangent line at that point instead.
The point at infinity plays the role of zero, and the reflection of a point is its negative.
For example, on $y^2 = x^3 + 1$ the tangent at $(2, 3)$ has slope $2$, and doubling gives $2 \cdot (2, 3) = (0, 1)$.
