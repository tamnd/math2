---
tag: V2HG4GN7TN
kind: concept
name: Bessel potential
msc: [31B15, "46E35", 47G40]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_potential
same_as:
  wikidata: Q4896404
  wikipedia: Bessel potential
---

## Summary

The Bessel potential of order $\alpha > 0$ is the operator $(I - \Delta)^{-\alpha/2}$ on functions on $\R^n$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]].
It is a convolution with a positive integrable kernel $G_\alpha$.
Near the origin $G_\alpha$ behaves like the kernel of the [[Riesz potential|1V2N8MFSHC]].
It decays exponentially at infinity, which removes the problems of the Riesz potential at large scales.
The images of $L^p$ under Bessel potentials are the [[Bessel potential spaces|DVJM7NBSF2]], which give Sobolev spaces of fractional order.

## Explanations

### L1 human

The Bessel potential smooths a function by a fractional amount $\alpha$, much like the Riesz potential.
The difference is the extra $I$ in $(I - \Delta)$, which acts like a mass term in physics and makes the smoothing kernel die off quickly far away.
In one dimension with $\alpha = 2$ the kernel is $\frac12 e^{-\abs{x}}$, so the Bessel potential averages $f$ with an exponentially decaying weight.
This operator solves $u - u'' = f$.
