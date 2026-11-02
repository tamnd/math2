---
tag: 2ET068BZZH
kind: concept
name: Modified Bessel functions
msc: [33C10, 34B30]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_function
---

## Summary

The modified Bessel functions $I_\nu$ and $K_\nu$ solve the modified Bessel equation $z^2 y'' + z y' - (z^2 + \nu^2) y = 0$.
They are the [[Bessel functions|CZCMRDWDYW]] evaluated on the imaginary axis, made real for real arguments.
On the positive real axis $I_\nu$ grows like $e^x$ and $K_\nu$ decays like $e^{-x}$.
They appear in heat flow, diffusion and electrostatics in cylindrical geometry.

## Explanations

### L1 human

Bessel's equation behaves like $y'' + y = 0$ for large $x$, so its solutions oscillate.
Changing one sign gives an equation that behaves like $y'' - y = 0$, whose solutions grow or decay like $e^{x}$ and $e^{-x}$.
The modified Bessel functions are the solutions of this changed equation.
$I_\nu$ is the growing one, finite at the origin, and $K_\nu$ is the decaying one, infinite at the origin.
For example, $I_{1/2}(x) = \sqrt{\frac{2}{\pi x}} \sinh x$ for $x > 0$.
