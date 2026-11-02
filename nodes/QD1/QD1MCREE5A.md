---
tag: QD1MCREE5A
kind: concept
name: Integral transforms of tempered distributions
msc: [46F12, 44A05]
sources:
  - url: https://en.wikipedia.org/wiki/Distribution_(mathematical_analysis)
---

## Summary

Many [[integral transforms|YCK709QB06]] extend from functions to [[tempered distributions|8TK1JNG87X]] by duality.
One moves the transform onto the [[Schwartz test functions|CG9JEATW3Q]].
The transform $Tu$ of a distribution $u$ acts on a test function $\varphi$ as $u$ acts on $T^t\varphi$.
Here $T^t$ is the transform with the transposed kernel.
This works when $T^t$ maps the Schwartz space continuously into itself.
The model case is the [[Fourier transform of tempered distributions|5PVSQXCTCT]]; the [[Laplace transform of distributions|6Z3XJVYT2Q]] uses a related construction.

## Explanations

### L1 human

Objects like the Dirac delta or the constant function $1$ on $\R$ have no Fourier transform as an ordinary integral.
The trick is never to integrate them directly.
Instead one asks how the transform of the object would act on nice test functions, and uses the rule $\int (Tf)\varphi = \int f\, (T^t\varphi)$, which holds for ordinary functions.
The right-hand side makes sense for distributions, so it is taken as the definition.
In this way the delta at $0$ gets the Fourier transform $1$.
