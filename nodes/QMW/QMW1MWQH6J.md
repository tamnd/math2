---
tag: QMW1MWQH6J
kind: concept
name: Abel transform
msc: [44A15, 44A12]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Abel_transform
same_as:
  wikidata: Q4666656
  wikipedia: Abel transform
---

## Summary

The Abel transform of a function $f$ of a radius $r \ge 0$ is $F(y) = 2 \int_y^\infty \frac{f(r)\, r}{\sqrt{r^2 - y^2}}\, dr$.
It gives the integral of a circularly symmetric function of the plane along a line at distance $y$ from the centre.
So it is the [[Radon transform|VJNZJ352PC]] of a radial function.
It can be inverted by a formula of the same type, which solves an integral equation first studied by Abel.
It is used to recover radial profiles of emission or density from line-of-sight measurements, for example in plasma physics and astronomy.

## Explanations

### L1 human

Picture a round, glowing cloud that is brighter near the centre.
Looking at it from the side, each line of sight passes through the cloud and adds up its brightness along the way.
The Abel transform turns the brightness at each radius into the total seen along each line.
For a uniform disc of radius $R$, the line at distance $y < R$ meets it in a chord of length $2\sqrt{R^2 - y^2}$, and this is the Abel transform.
