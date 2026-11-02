---
tag: N5PVGRJE1T
kind: concept
name: Mellin transform
msc: [44A15, 44A05]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
same_as:
  wikidata: Q606934
  wikipedia: Mellin transform
---

## Summary

The Mellin transform sends a function $f$ on $(0, \infty)$ to the function $\mathcal{M}f(s) = \int_0^\infty x^{s-1} f(x) \, dx$ of a complex variable $s$.
It is the integral transform adapted to the multiplicative group $(0, \infty)$, in the way the [[Fourier transform|DPVM34ADZV]] is adapted to the additive group $\R$.
It usually converges on a vertical strip of the complex plane, and it turns dilations $x \mapsto ax$ into multiplication by $a^{-s}$.
It links power series and Dirichlet series with the [[gamma function|0H5SYBSED9]] and the [[Riemann zeta function|1XWBY4N0VT]], and it is a main tool for asymptotic expansions.

## Explanations

### L1 human

The Mellin transform measures how a function on the positive reals behaves against the powers $x^{s-1}$.
Changing the variable to $x = e^{u}$ turns it into a Laplace or Fourier transform in $u$, so it is the Fourier transform of a function viewed on a logarithmic scale.
Its basic example is $f(x) = e^{-x}$, whose Mellin transform is $\Gamma(s)$ for $\operatorname{Re} s > 0$.
Scaling the input, $x \mapsto 2x$, only multiplies the transform by $2^{-s}$.
