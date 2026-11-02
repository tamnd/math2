---
tag: 4K2DZV0D0D
kind: concept
name: Spherical Bessel functions
msc: [33C10, 34B30]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_function
---

## Summary

The spherical Bessel functions $j_n$ and $y_n$ are the Bessel functions of half-integer order $n + \frac{1}{2}$, rescaled by $\sqrt{\pi / (2x)}$.
They solve the radial part of the Helmholtz equation in spherical coordinates.
They are elementary: each is a combination of $\sin x$, $\cos x$ and powers of $x$.
They describe waves scattered by a sphere and the radial motion of a free quantum particle.

## Explanations

### L1 human

When a wave spreads out from a point in space, its strength along each ray is described by a spherical Bessel function.
The simplest one is $j_0(x) = \frac{\sin x}{x}$, a sine wave whose size falls off like $\frac{1}{x}$.
The next one is $j_1(x) = \frac{\sin x}{x^2} - \frac{\cos x}{x}$.
Higher ones come from a simple recurrence, so they can all be written with sines, cosines and powers.
