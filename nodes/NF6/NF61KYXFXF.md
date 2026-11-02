---
tag: NF61KYXFXF
kind: definition
name: Y transform
msc: [44A20, 33C10]
defines: 2KTYK7BNA9
uses: [YCK709QB06, GRSNDJG363]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_function
---

## Definition

Fix a real number $\nu$, and let $Y_\nu$ be the [[Bessel function of the second kind|GRSNDJG363]] of order $\nu$.
Let $f \colon (0, \infty) \to \C$ be such that the integral below converges for $y$ in a set $Y \subseteq (0, \infty)$.
The *Y transform* of order $\nu$ of $f$ is the function
$$(\mathcal{Y}_\nu f)(y) = \int_0^\infty f(x)\, Y_\nu(xy)\, \sqrt{xy}\, dx, \qquad y \in Y.$$

## Remarks

Example: $Y_{1/2}(z) = -\sqrt{2/(\pi z)}\, \cos z$, because $Y_{1/2} = -J_{-1/2}$ and $J_{-1/2}(z) = \sqrt{2/(\pi z)}\, \cos z$.
So $\sqrt{xy}\, Y_{1/2}(xy) = -\sqrt{2/\pi}\, \cos(xy)$, and $\mathcal{Y}_{1/2} f(y) = -\sqrt{2/\pi} \int_0^\infty f(x) \cos(xy)\, dx$, the negative of the Fourier cosine transform.

Non-example: for $\nu > 0$, $Y_\nu(z)$ behaves like $-\frac{\Gamma(\nu)}{\pi} (2/z)^{\nu}$ as $z \to 0^+$.
For $\nu = 2$ and $f$ equal to $1$ on $(0, 1]$ and $0$ elsewhere, the integrand behaves like a constant times $x^{-3/2}$ near $0$, so the integral diverges for every $y > 0$.

The [[Hankel transform|2P9YWDGKC4]] is defined in the same way with $J_\nu$ in place of $Y_\nu$.
