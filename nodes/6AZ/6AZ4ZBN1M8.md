---
tag: 6AZ4ZBN1M8
kind: concept
name: Confluent hypergeometric function
msc: [33C15]
specializes: [VDBAW9PN88]
sources:
  - url: https://en.wikipedia.org/wiki/Confluent_hypergeometric_function
same_as:
  wikidata: Q783948
  wikipedia: Confluent hypergeometric function
---

## Summary

A confluent hypergeometric function is a solution of [[Kummer's equation|NT917KFR57]] $z w'' + (b - z) w' - a w = 0$.
The main one is Kummer's function $M(a, b, z) = {}_1F_1(a; b; z)$, the [[generalized hypergeometric series|VDBAW9PN88]] with one upper and one lower parameter.
It is an [[entire function|0G4F0XB9X2]] of $z$.
Its special cases include the exponential function, the [[Laguerre polynomials|WAMRHWW82R]], the [[error function|7Y56QCZSZJ]] and the [[incomplete gamma function|YB7ZV0HG7K]].

## Explanations

### L1 human

Kummer's function is a power series in which each coefficient is obtained from the previous one by a simple rational factor.
The coefficient of $z^n$ is $\frac{a (a + 1) \cdots (a + n - 1)}{b (b + 1) \cdots (b + n - 1)} \cdot \frac{1}{n!}$.
When $a = b$ the two products cancel and the series is $\sum z^n / n! = e^z$.
So Kummer's function is a two-parameter deformation of the exponential function.
It appears whenever a physical problem leads to a second order equation with one regular and one irregular singular point, as for the hydrogen atom.
