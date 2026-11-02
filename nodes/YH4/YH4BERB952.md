---
tag: YH4BERB952
kind: concept
name: Scaling function and refinement equation
msc: [42C40, 65T60, 39B22]
sources:
  - url: https://en.wikipedia.org/wiki/Multiresolution_analysis
---

## Summary

The scaling function $\varphi$ of a [[multiresolution analysis|1GHQMBR7DE]] is a function whose integer translates form an orthonormal basis of the base space $V_0$.
Since $V_0 \subseteq V_1$, it satisfies a refinement equation $\varphi(x) = \sqrt2 \sum_k h_k \varphi(2x - k)$: it is a combination of half-size copies of itself.
The coefficients $h_k$ form the low-pass filter of the [[discrete wavelet transform|P3H4MMC4ZH]], and they also determine the wavelet.
Conversely, one constructs wavelets such as the [[Daubechies wavelets|90V8S5CXE6]] by choosing the coefficients first and solving the refinement equation.

## Explanations

### L1 human

The box function $1_{[0,1)}$ is made of two boxes of half the width: the one on $[0, \tfrac12)$ and the one on $[\tfrac12, 1)$.
So $\varphi(x) = \varphi(2x) + \varphi(2x - 1)$.
An equation of this kind, where a function equals a combination of squeezed and shifted copies of itself, is a refinement equation.
Many of its solutions are not simple pictures: they are fractal-like curves fixed by the equation, and the box is only the easiest one.
