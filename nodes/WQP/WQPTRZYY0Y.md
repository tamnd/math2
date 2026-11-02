---
tag: WQPTRZYY0Y
kind: concept
name: Funk transform
msc: [44A12, 53C65, 33C55]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Funk_transform
same_as:
  wikidata: Q5509245
  wikipedia: Funk transform
---

## Summary

The Funk transform sends a function on the sphere $S^2$ to the function that gives its integral over each great circle.
It is the spherical analogue of the [[Radon transform|VJNZJ352PC]], with great circles in place of lines.
It kills odd functions, and it is injective on even continuous functions.
On [[spherical harmonics|3F32Y21HP4]] it acts by multiplication by explicit constants, which gives its inversion.

## Explanations

### L1 human

Think of a function on the surface of the Earth, such as temperature.
For every great circle, such as the equator or a meridian circle through both poles, add up the temperature along it.
The Funk transform records these totals, indexed by the pole of each great circle.
A function with $f(-x) = -f(x)$ gives total $0$ on every great circle, so it is invisible.
For functions with $f(-x) = f(x)$, the totals determine the function.
