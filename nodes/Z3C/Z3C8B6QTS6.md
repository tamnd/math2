---
tag: Z3C8B6QTS6
kind: concept
name: Weierstrass equation
msc: [14H52, 11G05]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_curve
---

## Summary

A Weierstrass equation is a cubic equation $y^2 + a_1 xy + a_3 y = x^3 + a_2 x^2 + a_4 x + a_6$ with coefficients in a field.
When its discriminant is nonzero, it defines an [[elliptic curve|427N6S6QQW]], with the point at infinity as the origin.
Every elliptic curve can be written in this form, so Weierstrass equations are the standard way to compute with elliptic curves.
The name comes from the differential equation of the [[Weierstrass elliptic function|361NAK68QK]], which yields such an equation over $\C$.

## Explanations

### L1 human

A Weierstrass equation says that $y^2$, up to some correction terms, equals a cubic polynomial in $x$.
The simplest case is $y^2 = x^3 + ax + b$.
Over the real numbers its graph is symmetric about the $x$-axis, and when it is smooth it has one or two pieces.
For example, $y^2 = x^3 - x$ is a smooth curve, while $y^2 = x^3$ has a sharp cusp at the origin and does not count as an elliptic curve.
