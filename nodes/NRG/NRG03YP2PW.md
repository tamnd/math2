---
tag: NRG03YP2PW
kind: concept
name: Fourier transform method for convolution equations
msc: ["45E10", 42A38]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_transform
---

## Summary

The Fourier transform method solves a [[convolution integral equation|EY75YD988Z]] on the whole line or on $\R^n$ by passing to the frequency side.
The [[convolution theorem|QY8ETVDA1Z]] turns the convolution with the kernel into multiplication by the transform of the kernel.
So the integral equation becomes an algebraic equation for the transform of the unknown.
One solves it by division and returns with the [[inverse Fourier transform|JB8QMT8DCH]].
The method also shows when the equation has exactly one solution in $L^2$ for every right side in $L^2$: the symbol $1 - \lambda \hat k(\xi)$ must not vanish.

## Explanations

### L1 human

A convolution mixes the values of a function along the whole line, which makes the equation hard to solve point by point.
The [[Fourier transform|DPVM34ADZV]] splits a function into pure waves $e^{i x \xi}$, and a convolution acts on each wave by a simple factor.
So in the wave picture the equation $\varphi - k * \varphi = f$ becomes $(1 - \hat k(\xi)) \hat\varphi(\xi) = \hat f(\xi)$, one equation for each frequency $\xi$.
For example, with $k(s) = \frac{1}{2} e^{-\abs{s}}$ one has $\hat k(\xi) = \frac{1}{1 + \xi^2}$, and dividing by $1 - \hat k(\xi) = \frac{\xi^2}{1 + \xi^2}$ is a problem only at $\xi = 0$.
