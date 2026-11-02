---
tag: 4TKVXC9N46
kind: definition
name: Kardar–Parisi–Zhang equation
msc: [60H15, 35R60, 35Q82]
defines: RQ196EHXKC
uses: [PRCQG82QTK, 09EGC6F8PT, VBMQ9SJ3DH]
sources:
  - url: https://en.wikipedia.org/wiki/Kardar%E2%80%93Parisi%E2%80%93Zhang_equation
---

## Definition

Let $\nu > 0$, $\lambda \in \R$ and $D > 0$ be constants.
Let $\xi$ be a Gaussian space-time white noise on $\R \times [0, \infty)$, that is, a centred Gaussian random distribution with formal covariance $\mathbb{E}[\xi(x, t)\xi(y, s)] = \delta(x - y)\delta(t - s)$.
The *Kardar–Parisi–Zhang equation* is the [[stochastic partial differential equation|PRCQG82QTK]] for a random function $h(x, t)$:
$$\partial_t h = \nu\, \partial_x^2 h + \frac{\lambda}{2} \big(\partial_x h\big)^2 + \sqrt{D}\, \xi.$$

## Remarks

The equation is formal: a solution $h(\cdot, t)$ is only Hölder continuous of every order less than $\frac{1}{2}$ in $x$, so $(\partial_x h)^2$ is not defined.
For $\lambda \ne 0$, a standard meaning is the Cole–Hopf solution $h = \frac{2\nu}{\lambda}\log Z$, where $Z > 0$ solves the stochastic heat equation $\partial_t Z = \nu\, \partial_x^2 Z + \frac{\lambda\sqrt{D}}{2\nu} Z \xi$ in the Itô sense; see [[Cole–Hopf transformation|VBMQ9SJ3DH]].
Hairer's theory of regularity structures gives a solution theory that agrees with the Cole–Hopf solution, up to an infinite renormalization constant.
Example: with $\lambda = 0$ the equation is linear, the additive stochastic heat equation, and its solution is a Gaussian process given by a stochastic convolution with the heat kernel.
Non-example: the deterministic equation $h_t = \nu h_{xx} + \frac{\lambda}{2}(h_x)^2$ has no noise term, so it is not the KPZ equation; it is a viscous Hamilton–Jacobi equation.
