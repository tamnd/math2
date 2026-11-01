---
tag: WMXDVF36ZT
kind: concept
name: Wirtinger derivatives
msc: [30A99, 32A10]
sources:
  - url: https://en.wikipedia.org/wiki/Wirtinger_derivatives
same_as:
  wikidata: Q8027031
  wikipedia: Wirtinger derivatives
---

## Summary

The Wirtinger derivatives $\partial / \partial z$ and $\partial / \partial \bar z$ are two first-order differential operators on functions of $z = x + iy$, see the [[definition|698R12MY4G]].
They let one treat $z$ and $\bar z$ as if they were independent variables.
A continuously differentiable function is [[holomorphic|0NAHXR1FRH]] exactly when its $\partial / \partial \bar z$ derivative is zero, which is a compact form of the [[Cauchy–Riemann equations|0T71SSYZ39]].

## Explanations

### L1 human

A function of a complex variable is also a function of two real variables $x$ and $y$.
The Wirtinger derivatives repackage the two partial derivatives in $x$ and $y$ into two complex ones.
On a polynomial in $z$ and $\bar z$, the derivative in $z$ differentiates in $z$ while holding $\bar z$ fixed.
The derivative in $\bar z$ does the opposite.
For example, $\abs{z}^2 = z \bar z$ has derivative $\bar z$ in $z$ and derivative $z$ in $\bar z$, just as if $z$ and $\bar z$ were separate letters.
