---
tag: VSD1D6ASVH
kind: definition
name: Modified Bessel functions
msc: [33C10, 34B30]
defines: 2ET068BZZH
uses: [CZCMRDWDYW, 0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_function
---

## Definition

Let $\nu \in \C$, let $\Gamma$ be the [[gamma function|0H5SYBSED9]], and let $z \in \C \setminus (-\infty, 0]$ with the principal branch of $z^\nu$.

1. The *modified Bessel function of the first kind* of order $\nu$ is
$$I_\nu(z) = \sum_{m=0}^{\infty} \frac{1}{m!\, \Gamma(m + \nu + 1)} \left( \frac{z}{2} \right)^{2m + \nu},$$
where $\frac{1}{\Gamma(m + \nu + 1)}$ is read as $0$ when $m + \nu + 1$ is a non-positive integer.
2. For $\nu \notin \Z$, the *modified Bessel function of the second kind* of order $\nu$ is
$$K_\nu(z) = \frac{\pi}{2}\, \frac{I_{-\nu}(z) - I_\nu(z)}{\sin(\nu \pi)},$$
and for an integer $n$ it is $K_n(z) = \lim_{\nu \to n} K_\nu(z)$.

## Remarks

Both functions solve the modified Bessel equation $z^2 y'' + z y' - (z^2 + \nu^2) y = 0$.
In terms of the [[Bessel function of the first kind|CZCMRDWDYW]], $I_\nu(z) = i^{-\nu} J_\nu(iz)$ for $-\pi < \arg z \le \frac{\pi}{2}$.
Example: for $x > 0$, $I_{1/2}(x) = \sqrt{\frac{2}{\pi x}} \sinh x$ and $K_{1/2}(x) = \sqrt{\frac{\pi}{2x}}\, e^{-x}$.
For $x > 0$ there is the integral form $K_\nu(x) = \int_0^\infty e^{-x \cosh t} \cosh(\nu t)\, dt$.
A non-example: $I_{-n}$ for an integer $n$ is not a second solution, since $I_{-n} = I_n$; this is why $K_n$ is defined as a limit.
$K_\nu$ is also called the Macdonald function.
