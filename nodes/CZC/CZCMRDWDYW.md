---
tag: CZCMRDWDYW
kind: concept
name: Bessel function of the first kind
msc: [33C10]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_function
---

## Summary

The Bessel function of the first kind $J_\nu(z)$ is the solution of [[Bessel's equation|EAV97QH9DF]] $z^2 y'' + z y' + (z^2 - \nu^2) y = 0$ that behaves like $\frac{1}{\Gamma(\nu + 1)} \left( \frac z2 \right)^\nu$ near $z = 0$.
This description assumes that $\nu$ is not a negative integer.
It is given by a power series that converges for every $z$.
Bessel functions describe waves and heat flow in cylinders and discs, such as the vibration modes of a drum.
They appear throughout analysis, number theory and probability.

## Explanations

### L1 human

A Bessel function of the first kind looks like a cosine wave whose height slowly shrinks, roughly like $1 / \sqrt{x}$.
For example $J_0(x)$ starts at $1$ for $x = 0$ and then oscillates around $0$ with decreasing amplitude.
Its zeros give the frequencies at which a circular drum can vibrate.
For half-integer order the function is elementary: $J_{1/2}(x) = \sqrt{\frac{2}{\pi x}} \sin x$ for $x > 0$.
