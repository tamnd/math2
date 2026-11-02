---
tag: EV25PMXVQT
kind: definition
name: Hankel transform
msc: [44A20, 33C10, 42B10]
defines: 2P9YWDGKC4
uses: [CZCMRDWDYW, DWJF7ABPR1, DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Hankel_transform
---

## Definition

Let $\nu \ge -\frac12$, and let $J_\nu$ be the [[Bessel function of the first kind|CZCMRDWDYW]] of order $\nu$.
Let $f \colon (0, \infty) \to \C$ be measurable with $\int_0^\infty \abs{f(r)}\, r^{1/2}\, dr < \infty$.
The *Hankel transform of order $\nu$* of $f$ is the function on $(0, \infty)$ given by the [[Lebesgue integral|DWJF7ABPR1]]
$$F_\nu(k) = \int_0^\infty f(r)\, J_\nu(kr)\, r\, dr.$$

## Remarks

The integral converges absolutely, because $\sqrt{z}\, \abs{J_\nu(z)}$ is bounded on $(0, \infty)$ for $\nu \ge -\frac12$, so $\abs{J_\nu(kr)}\, r \le C k^{-1/2} r^{1/2}$.
The inverse transform has the same form: under suitable conditions $f(r) = \int_0^\infty F_\nu(k)\, J_\nu(kr)\, k\, dk$.
Other normalizations use the kernel $J_\nu(kr) \sqrt{kr}$ with $dr$ instead of $r\, dr$.
Through the [[Fourier transform|DPVM34ADZV]] in the plane, the order-$0$ transform describes radial functions: if $g(x) = f(\abs{x})$ on $\R^2$, then $\int_{\R^2} g(x) e^{-i x \cdot \xi}\, dx = 2\pi F_0(\abs{\xi})$.

Example: $\nu = 0$ and $f(r) = e^{-r^2/2}$.
The plane Gaussian $e^{-\abs{x}^2/2}$ has Fourier transform $2\pi e^{-\abs{\xi}^2/2}$ with this kernel, so $F_0(k) = e^{-k^2/2}$.

Non-example: $f(r) = 1$ fails the integrability condition, and $\int_0^R J_0(kr)\, r\, dr = \frac{R}{k} J_1(kR)$ has no limit as $R \to \infty$, since $J_1(kR)$ decays only like $R^{-1/2}$.
