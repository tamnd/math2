---
tag: A7X2MQP0KM
kind: definition
name: Newtonian kernel
msc: [31B15, 31B10]
defines: 6TJTWQ5HCR
uses: [BSJ8X2XRN9, 0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Newtonian_potential
---

## Definition

Let $n \ge 3$.
The *Newtonian kernel* on $\R^n$ is the function $k \colon \R^n \times \R^n \to (0, +\infty]$ given by
$$k(x, y) = \frac{1}{\abs{x - y}^{n-2}} \quad (x \ne y), \qquad k(x, x) = +\infty.$$

## Remarks

Example: for $n = 3$, $k(x, y) = 1/\abs{x - y}$; for $x = (1, 0, 0)$ and $y = 0$ it equals $1$.
For fixed $y$, the function $x \mapsto k(x, y)$ is [[harmonic|0DEB0JMN0W]] on $\R^n \setminus \set{y}$, since $\Delta r^{2-n} = (2-n)(1-n) r^{-n} + (n-1)(2-n) r^{-n} = 0$ for $r = \abs{x - y}$.
Non-example: on $\R^4$, the function $1/\abs{x - y}$ is not the Newtonian kernel; its Laplacian in $x$ is $-\abs{x - y}^{-3} \ne 0$, so it is not harmonic off the pole.
The kernel is symmetric, $k(x, y) = k(y, x)$, lower semicontinuous, and positive.
With $\sigma_n$ the area of the unit sphere of $\R^n$, one has $k(x, y) = (n-2)\sigma_n \, \Phi(x - y)$, where $\Phi$ is the [[fundamental solution of the Laplacian|BSJ8X2XRN9]].
Some authors include this constant in the kernel; the definition above is the usual one in potential theory.
In the plane its role is played by the logarithmic kernel $\log(1/\abs{x - y})$.
