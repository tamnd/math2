---
tag: DNVGM3YT8Q
kind: definition
name: Logarithmic kernel
msc: [31A15]
defines: VDZ5FKYC2T
uses: [BSJ8X2XRN9, 0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_solution
---

## Definition

Identify $\R^2$ with $\C$.
The *logarithmic kernel* is the function $k \colon \C \times \C \to (-\infty, +\infty]$ given by
$$k(z, w) = \log \frac{1}{\abs{z - w}} \quad (z \ne w), \qquad k(z, z) = +\infty.$$

## Remarks

Example: $k(2, 0) = -\log 2 < 0$ and $k(1/2, 0) = \log 2 > 0$.
For fixed $w$, the function $z \mapsto k(z, w)$ is [[harmonic|0DEB0JMN0W]] on $\C \setminus \set{w}$.
Indeed, on every disc that does not contain $w$ it is the real part of a holomorphic branch of $-\log(z - w)$.
Non-example: in $\R^3$ the function $\log(1/\abs{x - y})$ is not harmonic off the pole, since for $r = \abs{x - y}$ one has $\Delta \log(1/r) = -1/r^2$; the three-dimensional analogue is the Newtonian kernel.
The kernel is symmetric and lower semicontinuous, and $k(z, w) = 2\pi \, \Phi(z - w)$, where $\Phi$ is the [[fundamental solution of the Laplacian|BSJ8X2XRN9]] in the plane.
So $\Delta_z k(z, w) = -2\pi \delta_w$ in the sense of distributions.
