---
tag: XFJDYMB91J
kind: concept
name: Kontorovich–Lebedev transform
msc: [44A20, 33C10]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Kontorovich%E2%80%93Lebedev_transform
same_as:
  wikidata: Q6430373
  wikipedia: Kontorovich–Lebedev transform
---

## Summary

The Kontorovich–Lebedev transform integrates a function $f$ on $(0, \infty)$ against the [[modified Bessel function|2ET068BZZH]] $K_{iy}(x)$ of imaginary order $iy$.
Unlike most transforms, the transform variable $y$ enters through the order of the Bessel function, not through its argument.
It has an explicit inversion formula with the weight $y \sinh(\pi y)$.
It is used to solve boundary value problems in wedge-shaped and conical regions, where the separation of variables leads to Bessel functions of imaginary order.

## Explanations

### L1 human

Many transforms take a family of functions, such as waves of every frequency, and measure how much of each one a given function contains.
Here the family is $x \mapsto K_{iy}(x)$, indexed by a real number $y$.
These functions oscillate faster and faster near $x = 0$ as $y$ grows and decay exponentially for large $x$.
The transform records the overlap of $f$ with each of them.
