---
tag: P4B2Z6GS0R
kind: concept
name: Spherical mean transform
msc: [44A12, 53C65, 35L05]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Spherical_mean
---

## Summary

The spherical mean transform sends a function $f$ on $\R^n$ to a function $M f(x, r)$.
Its value is the average of $f$ over the [[sphere|P9CM4GQ2T0]] of center $x$ and radius $r$.
A continuous function is [[harmonic|0DEB0JMN0W]] exactly when all its spherical means equal its value at the center.
For a function of class $C^2$ the means satisfy the Darboux equation.
This reduces the [[wave equation|5EHD2XBQDG]] in $\R^n$ to an equation in one space variable.
Recovering $f$ from its means over spheres with centers on a fixed surface is the mathematical core of thermoacoustic and photoacoustic tomography.

## Explanations

### L1 human

Stand at a point $x$, draw a sphere of radius $r$ around it, and average the values of $f$ on that sphere.
Doing this for every center and every radius gives the spherical mean transform.
For example, for $f(x) = \abs{x}^2$ the mean over the sphere of center $x$ and radius $r$ is $\abs{x}^2 + r^2$.
For radius $0$ the mean is just the value $f(x)$, and for a harmonic function it stays the same for all radii.
