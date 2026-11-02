---
tag: 3BBSXXAZKE
kind: definition
name: Anger function
msc: [33C10]
defines: 9P87VQZ0P7
uses: [CZCMRDWDYW]
sources:
  - url: https://en.wikipedia.org/wiki/Anger_function
---

## Definition

Let $\nu \in \C$ and $z \in \C$.
The *Anger function* of order $\nu$ is
$$\mathbf{J}_\nu(z) = \frac{1}{\pi} \int_0^\pi \cos(\nu\tau - z \sin\tau)\, d\tau.$$
The *Weber function* of order $\nu$ is
$$\mathbf{E}_\nu(z) = \frac{1}{\pi} \int_0^\pi \sin(\nu\tau - z \sin\tau)\, d\tau.$$

## Remarks

Both are entire functions of $z$ and of $\nu$, since the integrands are entire and the interval is compact.
If $n$ is an integer, then $\mathbf{J}_n = J_n$, the [[Bessel function of the first kind|CZCMRDWDYW]], by Bessel's integral.
Example: at $z = 0$, $\mathbf{J}_\nu(0) = \frac{1}{\pi} \int_0^\pi \cos(\nu\tau)\, d\tau = \frac{\sin(\nu\pi)}{\nu\pi}$ for $\nu \ne 0$.
A non-example: for $\nu = \frac{1}{2}$, $\mathbf{J}_{1/2}(0) = \frac{2}{\pi} \ne 0$, while $J_{1/2}(0) = 0$, so $\mathbf{J}_{1/2}$ is not the Bessel function $J_{1/2}$.
The Anger function solves $z^2 w'' + z w' + (z^2 - \nu^2)\, w = \frac{(z - \nu)\sin(\nu\pi)}{\pi}$, so it solves Bessel's equation exactly when $\nu$ is an integer.
The Weber function $\mathbf{E}_\nu$ here is different from the Bessel function of the second kind, which is also sometimes called a Weber function.
