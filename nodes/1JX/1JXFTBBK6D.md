---
tag: 1JXFTBBK6D
kind: statement
role: theorem
name: Fourier transform on Schwartz space
msc: ["42B10", "46F05"]
uses: [DPVM34ADZV, CG9JEATW3Q, HHNR31W3WD, JB8QMT8DCH]
about: [DPVM34ADZV, CG9JEATW3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Schwartz_space
---

## Statement

Let $n \ge 1$ and let $\mathcal{S}(\R^n)$ be the [[Schwartz space|CG9JEATW3Q]] with its Fréchet topology.
Let $\mathcal{F} f(\xi) = \int_{\R^n} f(x) e^{-2\pi i x \cdot \xi}\, dx$ be the [[Fourier transform|DPVM34ADZV]].
Then $\mathcal{F}$ maps $\mathcal{S}(\R^n)$ onto $\mathcal{S}(\R^n)$, it is a linear bijection, and both $\mathcal{F}$ and its inverse are continuous.
The inverse is the [[inverse Fourier transform|JB8QMT8DCH]]
$$\mathcal{F}^{-1} g(x) = \int_{\R^n} g(\xi)\, e^{2\pi i x \cdot \xi}\, d\xi.$$

## Remarks

By the [[rules for differentiation and multiplication|HHNR31W3WD]], $\xi^\alpha \partial^\beta \hat f$ is, up to constants, the transform of $\partial^\alpha (x^\beta f)$.
That function is in $\mathcal{S}(\R^n) \subset L^1(\R^n)$, so its transform is bounded, which shows $\hat f \in \mathcal{S}(\R^n)$.
The same estimates, with a factor $(1 + \abs{x})^{-n-1}$ to control the integral, give continuity.
Bijectivity is the inversion formula $\mathcal{F}^{-1} \mathcal{F} f = f$, proved by pairing with a Gaussian of shrinking width.
Also $\mathcal{F}^4 f = f$, since $\mathcal{F}^2 f(x) = f(-x)$.

Example: the Gaussian $e^{-\pi \abs{x}^2}$ is a Schwartz function and is fixed by $\mathcal{F}$.

On $\mathcal{S}(\R^n)$ the transform also preserves the $L^2$ norm, $\int \abs{\hat f}^2 = \int \abs{f}^2$.
Since $\mathcal{S}(\R^n)$ is dense in $L^2(\R^n)$, this is how the transform is extended to a unitary map of $L^2(\R^n)$.
By duality it also extends to tempered distributions.
The space $L^1(\R^n)$ has no such property: the transform of an integrable function need not be integrable.

## Explanations

### L1 human

Schwartz functions are smooth and decay fast, and the Fourier transform turns smoothness into decay and decay into smoothness.
So it sends this space to itself, and nothing is lost: every Schwartz function is the transform of exactly one other.

### L2 human

This is the cleanest setting for Fourier analysis on $\R^n$: all formulas (inversion, Plancherel, the convolution theorem, differentiation rules) hold on $\mathcal{S}(\R^n)$ without any conditions.
Results on $L^p$ spaces are then obtained by density, and results on tempered distributions by duality.
