---
tag: 4RDG2SJ70D
kind: definition
name: Hankel functions
msc: [33C10, 34B30]
defines: N3CC5DRGT1
uses: [CZCMRDWDYW, GRSNDJG363]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_function
---

## Definition

Let $\nu \in \C$, and let $J_\nu$ and $Y_\nu$ be the [[Bessel functions of the first kind|CZCMRDWDYW]] and of the [[second kind|GRSNDJG363]] on $\C \setminus (-\infty, 0]$.
The *Hankel functions* of order $\nu$ are
$$H^{(1)}_\nu(z) = J_\nu(z) + i\, Y_\nu(z), \qquad H^{(2)}_\nu(z) = J_\nu(z) - i\, Y_\nu(z).$$

## Remarks

Both functions solve Bessel's equation $z^2 y'' + z y' + (z^2 - \nu^2) y = 0$, since they are linear combinations of $J_\nu$ and $Y_\nu$.
They are independent: their Wronskian is $W(H^{(1)}_\nu, H^{(2)}_\nu)(z) = -\frac{4i}{\pi z}$.
Example: for $\nu = \frac{1}{2}$ and $x > 0$, $J_{1/2}(x) = \sqrt{\frac{2}{\pi x}} \sin x$ and $Y_{1/2}(x) = -\sqrt{\frac{2}{\pi x}} \cos x$, so $H^{(1)}_{1/2}(x) = -i \sqrt{\frac{2}{\pi x}}\, e^{ix}$.
For real $\nu$ and $x > 0$, $H^{(2)}_\nu(x)$ is the complex conjugate of $H^{(1)}_\nu(x)$.
A non-example: $J_\nu + Y_\nu$ also solves Bessel's equation, but it is not a Hankel function, because the coefficient of $Y_\nu$ is not $\pm i$.
They are also called Bessel functions of the third kind.
