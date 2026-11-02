---
tag: QG2JHK1VXX
kind: definition
name: Parabolic cylinder function
msc: [33C15, 34M03]
defines: V7H5Z35CPN
uses: [6AZ4ZBN1M8, 0H5SYBSED9, 0QQRP17Z7S]
sources:
  - url: https://en.wikipedia.org/wiki/Parabolic_cylinder_function
---

## Definition

Let $\nu$ be a complex number.
*Weber's equation* with parameter $\nu$ is the [[linear differential equation|0QQRP17Z7S]]
$$\frac{d^2 y}{dz^2} + \left( \nu + \frac12 - \frac{z^2}{4} \right) y = 0.$$
Let $M(a, b, x)$ be [[Kummer's function|6AZ4ZBN1M8]] and $\Gamma$ the [[gamma function|0H5SYBSED9]], with $1/\Gamma$ read as $0$ at the poles of $\Gamma$.
The *parabolic cylinder function* $D_\nu$ is the entire function
$$D_\nu(z) = 2^{\nu/2} e^{-z^2/4} \left( \frac{\sqrt{\pi}}{\Gamma\left( \frac{1 - \nu}{2} \right)} M\left( -\frac{\nu}{2}, \frac12, \frac{z^2}{2} \right) - \frac{\sqrt{2\pi}\, z}{\Gamma\left( -\frac{\nu}{2} \right)} M\left( \frac{1 - \nu}{2}, \frac32, \frac{z^2}{2} \right) \right).$$

## Remarks

The function $D_\nu$ solves Weber's equation, and it is the solution with $D_\nu(z) \sim z^\nu e^{-z^2/4}$ as $z \to +\infty$.
The functions $D_\nu(z)$ and $D_\nu(-z)$ are solutions too, and they are linearly independent unless $\nu$ is a nonnegative integer.
Another common notation is $U(a, z) = D_{-a - \frac12}(z)$.
Example: for $\nu = 0$, the first coefficient is $\sqrt{\pi}/\Gamma(\frac12) = 1$ and the second is $0$, since $1/\Gamma(0) = 0$; so $D_0(z) = e^{-z^2/4}$.
Check: $y = e^{-z^2/4}$ gives $y'' = \left( \frac{z^2}{4} - \frac12 \right) y$, so $y'' + \left( \frac12 - \frac{z^2}{4} \right) y = 0$.
More generally, for $\nu = n \in \N$, one has $D_n(z) = 2^{-n/2} e^{-z^2/4} H_n(z / \sqrt{2})$ with $H_n$ the [[Hermite polynomials|MGACY98E9H]].
Non-example: $y = e^{z^2/4}$ solves Weber's equation for $\nu = -1$, since $y'' = \left( \frac12 + \frac{z^2}{4} \right) y$, but it is not $D_{-1}$: it grows as $z \to +\infty$ instead of decaying.
