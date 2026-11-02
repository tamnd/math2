---
tag: V1WRSW2AA6
kind: definition
name: Z-transform
msc: [44A55, 39A12, 93C55]
defines: 5FY0JQGHYZ
uses: [0G9EKM0E15, 0GXMPDNYX3]
sources:
  - url: https://en.wikipedia.org/wiki/Z-transform
    locator: Definition
---

## Definition

Let $x = (x_n)_{n \in \Z}$ be a [[sequence|0G9EKM0E15]] of complex numbers.
The *Z-transform* of $x$ is the [[Laurent series|0GXMPDNYX3]]
$$X(z) = \mathcal{Z}\{x\}(z) = \sum_{n = -\infty}^{\infty} x_n z^{-n}.$$
It is regarded as a function of $z$ on the set of nonzero complex numbers $z$ where the series converges absolutely.
For a sequence $(x_n)_{n \ge 0}$ indexed by the natural numbers, one sets $x_n = 0$ for $n < 0$, and the transform is $X(z) = \sum_{n = 0}^{\infty} x_n z^{-n}$.

## Remarks

Example: for $x_n = a^n$ when $n \ge 0$ and $x_n = 0$ when $n < 0$, with $a \in \C$, the series is geometric with ratio $a z^{-1}$.
It converges absolutely exactly when $\abs{z} > \abs{a}$, and then $X(z) = z/(z - a)$.
Non-example: for $x_n = 1$ for all $n \in \Z$, the series $\sum_{n \in \Z} z^{-n}$ converges for no $z$.
The part with $n \ge 0$ needs $\abs{z} > 1$, and the part with $n < 0$ needs $\abs{z} < 1$, so the sequence has no Z-transform as a function.
The sum over all $n \in \Z$ is the bilateral form, and the sum over $n \ge 0$ is the unilateral form.
A function $X(z)$ alone does not determine $x$: the set of convergence is part of the data.
Substituting $z = e^{i\omega}$ gives the discrete-time Fourier transform, when the unit circle lies in the set of convergence.
