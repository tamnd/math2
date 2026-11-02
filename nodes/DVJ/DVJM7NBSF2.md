---
tag: DVJM7NBSF2
kind: concept
name: Bessel potential space
msc: ["46E35", 42B35]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_potential
---

## Summary

A Bessel potential space $H^{s,p}(\R^n)$ consists of the functions or tempered distributions whose "derivative of order $s$" lies in $L^p$.
The derivative of order $s$ is defined on the Fourier side by multiplication with $(1 + \abs{\xi}^2)^{s/2}$, so $s$ may be any real number.
These spaces extend the [[Sobolev spaces|M4CEZ5K9HP]] $W^{k,p}$ to fractional and negative orders, and for $p = 2$ they are the [[fractional Sobolev spaces|N6NX1VT837]] $H^s$.
They are a standard scale of spaces for elliptic equations and for interpolation.

## Explanations

### L1 human

Differentiating a function multiplies its Fourier transform by the frequency.
So a function is smooth when its Fourier transform still has small size after multiplication by a power of the frequency.
The Bessel potential space of order $s$ asks exactly this, with the power $(1 + \abs{\xi}^2)^{s/2}$ and with size measured in $L^p$.
For $s = 0$ the space is just $L^p$.
For $s = 1$ and $1 < p < \infty$ it is the space of $L^p$ functions with first derivatives in $L^p$.
