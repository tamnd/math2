---
tag: VJNZJ352PC
kind: concept
name: Radon transform
msc: [44A12, 92C55, 53C65]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Radon_transform
same_as:
  wikidata: Q979829
  wikipedia: Radon transform
---

## Summary

The Radon transform sends a function $f$ on $\R^n$ to the function that gives the integral of $f$ over each hyperplane.
In the plane the hyperplanes are lines.
There the Radon transform records what an X-ray scanner measures: the total absorption along each line through a body.
The [[projection-slice theorem|J7VA040MC3]] links it to the [[Fourier transform|DPVM34ADZV]], and the [[Radon inversion formula|HN93ST5CBT]] recovers $f$ from its Radon transform.
It is the mathematical basis of computed tomography and a central object of integral geometry.

## Explanations

### L1 human

Shine parallel X-rays through a body and measure how much each ray is weakened.
Each measurement is the integral of the density of the body along one line.
Doing this for every direction and every offset gives the Radon transform of the density.
For example, the indicator of the unit disk has the integral $2\sqrt{1 - s^2}$ over each line at distance $s < 1$ from the center, the length of the chord.
The surprising fact is that these line integrals determine the density completely.
