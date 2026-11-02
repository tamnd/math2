---
tag: 3CSEGRAD75
kind: statement
role: theorem
name: Fourier transform of radial functions
msc: ["42B10", "44A20", "33C10"]
uses: [DPVM34ADZV, SASP14MA1Z, 0HFREYRSZP]
about: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Hankel_transform
---

## Statement

Let $n \ge 2$ and let $f \in L^1(\R^n)$ be radial, that is, $f(x) = f_0(\abs{x})$ for a measurable function $f_0$ on $(0, \infty)$ with $\int_0^\infty \abs{f_0(r)}\, r^{n-1}\, dr < \infty$.
Let $\hat f(\xi) = \int_{\R^n} f(x) e^{-2\pi i x \cdot \xi}\, dx$ be its [[Fourier transform|DPVM34ADZV]], and let $J_\nu$ denote the Bessel function of the first kind of order $\nu$.
Then $\hat f$ is radial, and for every $\xi \ne 0$, with $\rho = \abs{\xi}$,
$$\hat f(\xi) = 2\pi\, \rho^{1 - n/2} \int_0^\infty f_0(r)\, J_{n/2 - 1}(2\pi r \rho)\, r^{n/2}\, dr.$$

## Remarks

The transform commutes with [[rotations|0HFREYRSZP]]: if $R$ is an orthogonal matrix, then the transform of $f \circ R$ is $\hat f \circ R$.
So the transform of a radial function is radial.
To compute it, write the integral in polar coordinates $x = r \omega$ and use the formula $\int_{S^{n-1}} e^{-2\pi i r \rho\, \omega \cdot e_1}\, d\sigma(\omega) = 2\pi (r\rho)^{1 - n/2} J_{n/2-1}(2\pi r \rho)$ for the surface measure $\sigma$ on the unit sphere.
The integral converges absolutely, because $z^{-\nu} J_\nu(z)$ is bounded on $(0, \infty)$ for $\nu \ge -\frac12$ and the hypothesis on $f_0$ holds.

Example: for $n = 3$, $J_{1/2}(z) = \sqrt{2/(\pi z)}\, \sin z$, and the formula becomes
$$\hat f(\xi) = \frac{2}{\rho} \int_0^\infty f_0(r)\, r \sin(2\pi r \rho)\, dr.$$
For $n = 1$ the same formula, with $J_{-1/2}(z) = \sqrt{2/(\pi z)} \cos z$, reduces to the cosine transform of an even function.

Up to the factors of $\rho$ and $r$, the one-dimensional integral is a Hankel transform of order $n/2 - 1$.

## Explanations

### L1 human

A radial function looks the same in every direction, like the ripples around a stone thrown into water.
Its Fourier transform is radial too, so it is a function of one variable.
The formula computes it by a single integral over the radius, in which a Bessel function replaces the sine and cosine of the one-dimensional case.

### L2 human

This reduction is the main tool for radial problems on $\R^n$.
The transforms of the indicator of a ball, of the surface measure on a sphere and of the Bochner–Riesz multipliers are all computed this way.
The decay of Bessel functions, $J_\nu(z) = O(z^{-1/2})$ as $z \to \infty$, has a direct consequence.
The Fourier transform of the surface measure on a sphere decays like $\abs{\xi}^{-(n-1)/2}$, a fact at the heart of restriction theory.
