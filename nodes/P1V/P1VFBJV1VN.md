---
tag: P1VFBJV1VN
kind: concept
name: Fractional integration
msc: [42B20, 31B15, 26A33]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_potential
---

## Summary

Fractional integration on $\R^n$ is the operator $I_\alpha$, for $0 < \alpha < n$, that convolves a function with the kernel $\abs{x}^{\alpha - n}$, suitably normalized.
It is also called the Riesz potential.
On the [[Fourier transform|DPVM34ADZV]] side it multiplies by a constant times $\abs{\xi}^{-\alpha}$, so it is the inverse of the [[fractional Laplacian|F8RSNQBMBE]] $(-\Delta)^{\alpha/2}$.
It is the Euclidean analogue of the [[Riemann–Liouville integral|JTKCZ44NN3]], and it is the main tool behind the Hardy–Littlewood–Sobolev and Sobolev inequalities.

## Explanations

### L1 human

Integrating a function once makes it smoother by one order; fractional integration makes it smoother by a fractional order $\alpha$.
In $\R^n$ this is done by averaging $f$ against the weight $\abs{x - y}^{\alpha - n}$, which is large near $x$ and decays far away.
For $n = 3$ and $\alpha = 2$ the result is the Newtonian potential $\frac{1}{4\pi}\int \frac{f(y)}{\abs{x - y}} \, dy$, the gravitational potential of a mass density $f$.
Doing it twice, of orders $\alpha$ and $\beta$, is the same as doing it once of order $\alpha + \beta$, as long as $\alpha + \beta < n$.
