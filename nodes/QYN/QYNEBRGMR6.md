---
tag: QYNEBRGMR6
kind: definition
name: Struve function
msc: [33C10]
defines: K290RBT8GB
uses: [0H5SYBSED9, CZCMRDWDYW]
sources:
  - url: https://en.wikipedia.org/wiki/Struve_function
---

## Definition

Let $\nu \in \C$ with $\nu + \frac{3}{2}$ not a non-positive integer, let $\Gamma$ be the [[gamma function|0H5SYBSED9]], and let $z \in \C \setminus (-\infty, 0]$ with the principal branch of powers.
The *Struve function* of order $\nu$ is
$$\mathbf{H}_\nu(z) = \sum_{m=0}^{\infty} \frac{(-1)^m}{\Gamma\left( m + \frac{3}{2} \right) \Gamma\left( m + \nu + \frac{3}{2} \right)} \left( \frac{z}{2} \right)^{2m + \nu + 1}.$$

## Remarks

It is a particular solution of the inhomogeneous Bessel equation
$$z^2 w'' + z w' + (z^2 - \nu^2)\, w = \frac{4 \left( z/2 \right)^{\nu + 1}}{\sqrt{\pi}\, \Gamma\left( \nu + \frac{1}{2} \right)}.$$
The general solution adds to $\mathbf{H}_\nu$ any solution of Bessel's equation, such as a combination of the [[Bessel functions|CZCMRDWDYW]] $J_\nu$ and $Y_\nu$.
Example: for $\nu = \frac{1}{2}$ and $x > 0$, $\mathbf{H}_{1/2}(x) = \sqrt{\frac{2}{\pi x}}\,(1 - \cos x)$; the first term of the series is $\frac{(x/2)^{3/2}}{\Gamma(3/2)\Gamma(2)} = \frac{x^{3/2}}{\sqrt{2\pi}}$, which matches $\sqrt{\frac{2}{\pi x}} \cdot \frac{x^2}{2}$.
A non-example: $J_{1/2}(x) = \sqrt{\frac{2}{\pi x}} \sin x$ is not a Struve function; it solves the equation with right-hand side $0$.
The modified Struve function is $\mathbf{L}_\nu(z) = -i e^{-i\nu\pi/2}\, \mathbf{H}_\nu(iz)$.
