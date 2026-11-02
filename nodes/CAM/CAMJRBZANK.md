---
tag: CAMJRBZANK
kind: concept
name: Copula
msc: [62H05, "60E05"]
specializes: [0H8H7ZTHW2]
sources:
  - url: https://en.wikipedia.org/wiki/Copula_(statistics)
same_as:
  wikidata: Q1131601
  wikipedia: Copula (statistics)
---

## Summary

A copula is a joint [[cumulative distribution function|0H8H7ZTHW2]] on the unit cube whose one-dimensional [[marginals|0MXT6PRZZ6]] are uniform on $[0, 1]$.
By [[Sklar's theorem|ZD7V7R27R9]], every joint distribution splits into its marginal distributions and a copula that carries the dependence between the coordinates.
Copulas let one model the marginals and the dependence separately.
They are used in finance, insurance and hydrology.

## Explanations

### L1 human

Two quantities, like the rainfall in two nearby towns, each have their own distribution, and they also influence each other.
A copula describes only the way they influence each other, after each one is rescaled to a number between $0$ and $1$ by its own distribution.
The independence copula $C(u, v) = u v$ says there is no influence at all.
The copula $C(u, v) = \min(u, v)$ says that both quantities always move in perfect step.
