---
tag: BTPQHQNJVY
kind: statement
role: theorem
name: Inversion of the Weierstrass transform
msc: [44A15, 35K05, 42A38]
uses: [5HYB6DDZH8, DPVM34ADZV, SASP14MA1Z, HPZHRZ0502]
about: [5HYB6DDZH8]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass_transform
---

## Statement

Let $f \in L^2(\R)$, an element of the [[$L^2$ space|SASP14MA1Z]], and let $F = Wf$ be its [[Weierstrass transform|5HYB6DDZH8]].
Let $\hat g(\xi) = \int_\R g(x)\, e^{-i x \xi}\, dx$ denote the [[Fourier transform|DPVM34ADZV]], extended to $L^2(\R)$.
Then $F \in L^2(\R)$, $\hat F(\xi) = e^{-\xi^2} \hat f(\xi)$ for almost every $\xi$, and $f$ is recovered from $F$ as the function in $L^2(\R)$ whose Fourier transform is
$$\hat f(\xi) = e^{\xi^2}\, \hat F(\xi).$$
In particular $W$ is injective on $L^2(\R)$.

## Remarks

The kernel $k(u) = \frac{1}{\sqrt{4\pi}} e^{-u^2/4}$ is integrable with $\hat k(\xi) = e^{-\xi^2}$, and $F = k * f$.
The convolution theorem on $L^1 * L^2$ gives $\hat F = \hat k \hat f$, and the [[Plancherel theorem|HPZHRZ0502]] makes the Fourier transform a bijection of $L^2(\R)$ up to the factor $2\pi$, which yields the formula.
Formally $W = e^{D^2}$ with $D = d/dx$, and the inverse is $e^{-D^2}$; for example, $W[e^{ax}] = e^{a^2} e^{ax}$ and $e^{-D^2} e^{ax} = e^{-a^2} e^{ax}$.
The inversion is unstable: the factor $e^{\xi^2}$ grows very fast, so a small change of $F$ at high frequencies can change $f$ a lot.
Not every function in $L^2$ is a Weierstrass transform: $F$ must satisfy $e^{\xi^2} \hat F \in L^2$, and every such $F$ extends to an entire function.

## Explanations

### L1 human

The Weierstrass transform blurs a function as heat flow blurs a temperature profile.
This theorem says the blur loses no information: the original profile can be computed back from the blurred one.
In practice the computation is very sensitive to small errors, as running heat flow backwards in time always is.

### L2 human

The inversion is the uniqueness theorem for the backward heat equation at a fixed time, in the class of square-integrable data.
On the Fourier side it is division by the Gaussian $e^{-\xi^2}$, which never vanishes; this is why the transform is injective.
The same reasoning applies to any convolution with an integrable kernel whose Fourier transform has no zeros.
The operator notation $e^{D^2}$ also explains how $W$ acts on polynomials: it maps the Hermite polynomial $H_n(x/2)$ to $x^n$, since $e^{-D^2} x^n = H_n(x/2)$ for the physicists' Hermite polynomials $H_n$.
