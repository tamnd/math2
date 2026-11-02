---
tag: 1BHMWWH55N
kind: concept
name: Sumudu transform
msc: [44A10, 44A15]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Sumudu_transform
same_as:
  wikidata: Q123331358
  wikipedia: Sumudu transform
---

## Summary

The Sumudu transform of a function $f$ on $[0, \infty)$ is $G(u) = \int_0^\infty f(ut)\, e^{-t}\, dt$.
It is the [[Laplace transform|0V49JEZW06]] in disguise: $G(u) = \frac{1}{u} F\big(\frac{1}{u}\big)$, where $F$ is the Laplace transform of $f$.
Its appeal is that it keeps units and scales: it sends $t^n$ to $n!\, u^n$ and constants to the same constants.
It is used, like the Laplace transform, to solve linear differential equations with constant coefficients.

## Explanations

### L1 human

The transform averages $f$ along the stretched line $t \mapsto f(ut)$, with exponentially decaying weights.
Because the weights $e^{-t}$ have total mass $1$, a constant function is sent to itself.
A power $t^n$ is sent to $n!\, u^n$, so a polynomial becomes a polynomial in $u$ of the same degree.
The variable $u$ plays the role of a time scale.
