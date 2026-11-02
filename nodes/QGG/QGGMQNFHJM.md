---
tag: QGGMQNFHJM
kind: example
name: Hankel transform of radial functions in the plane
msc: [44A20, 42B10, 33C10]
illustrates: [2P9YWDGKC4, 3CSEGRAD75]
uses: [2P9YWDGKC4, 3CSEGRAD75, DPVM34ADZV, CZCMRDWDYW]
sources:
  - url: https://en.wikipedia.org/wiki/Hankel_transform
---

## Example

Let $f_0 \colon (0, \infty) \to \C$ satisfy $\int_0^\infty \abs{f_0(r)}\, r\, dr < \infty$, and let $f(x) = f_0(\abs{x})$ on $\R^2$, an integrable radial function.
With the [[Fourier transform|DPVM34ADZV]] $\hat f(\xi) = \int_{\R^2} f(x) e^{-2\pi i x \cdot \xi}\, dx$, one has for $\rho = \abs{\xi}$
$$\hat f(\xi) = 2\pi \int_0^\infty f_0(r)\, J_0(2\pi r \rho)\, r\, dr,$$
which is $2\pi$ times the [[Hankel transform|2P9YWDGKC4]] of order $0$ of $f_0$ at $k = 2\pi\rho$.
Check: rotate so that $\xi$ lies along the first axis.
In polar coordinates $x = (r\cos\theta, r\sin\theta)$ one gets
$$\hat f(\xi) = \int_0^\infty f_0(r) \Big( \int_0^{2\pi} e^{-2\pi i r \rho \cos\theta}\, d\theta \Big) r\, dr.$$
The inner integral is $2\pi J_0(2\pi r\rho)$ by Bessel's integral $J_0(z) = \frac{1}{2\pi} \int_0^{2\pi} e^{-iz\cos\theta}\, d\theta$, where $J_0$ is the [[Bessel function|CZCMRDWDYW]] of order $0$.
This is the case $n = 2$ of the [[Fourier transform of radial functions|3CSEGRAD75]].

For the Gaussian $f_0(r) = e^{-\pi r^2}$, the known integral $\int_0^\infty e^{-a r^2} J_0(kr)\, r\, dr = \frac{1}{2a} e^{-k^2/(4a)}$ with $a = \pi$ and $k = 2\pi\rho$ gives $\hat f(\xi) = 2\pi \cdot \frac{1}{2\pi} e^{-\pi \rho^2} = e^{-\pi\abs{\xi}^2}$, as expected for $e^{-\pi \abs{x}^2}$.

## Explanations

### L1 human

A function in the plane that only depends on the distance to the origin has a Fourier transform with the same symmetry.
Its two-dimensional Fourier transform then reduces to a one-dimensional integral over the radius, with the Bessel function $J_0$ as kernel.
That integral is the Hankel transform of order $0$, which is why Hankel transforms appear in every problem with circular symmetry.
