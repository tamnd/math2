---
tag: 65PNDW38YC
kind: definition
name: Gelfand–Levitan theory
msc: [34A55, 34L25]
defines: R4MRNP9EQT
uses: [89AA6XJY5K, 7WV6B2502K]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_scattering_transform
---

## Definition

Let $q \colon [0, \infty) \to \R$ be continuous, let $h \in \R$, and consider the [[Schrödinger operator|89AA6XJY5K]] $-y'' + q y$ on $[0, \infty)$ with the boundary condition $y'(0) = h y(0)$.
For $\lambda \in \C$, let $\varphi(x, \lambda)$ be the solution of $-y'' + q y = \lambda y$ with $\varphi(0, \lambda) = 1$ and $\varphi'(0, \lambda) = h$.
Let $\rho$ be the spectral function of the operator.
This is the nondecreasing function for which $f \mapsto \int_0^\infty f(x) \varphi(x, \lambda) \, dx$ extends to a unitary map from $L^2(0, \infty)$ onto $L^2(\R, d\rho)$.
Let $\rho_0(\lambda) = \frac{2}{\pi}\sqrt{\lambda}$ for $\lambda \ge 0$ and $\rho_0(\lambda) = 0$ for $\lambda < 0$; this is the spectral function for $q = 0$ and $h = 0$.
Set
$$F(x, t) = \int_{-\infty}^{\infty} \cos(\sqrt{\lambda}\, x) \cos(\sqrt{\lambda}\, t) \, d(\rho - \rho_0)(\lambda),$$
where the integral converges in a suitable regularised sense.
The Gelfand–Levitan equation is the linear integral equation for an unknown function $K(x, t)$:
$$K(x, t) + F(x, t) + \int_0^x K(x, s) F(s, t) \, ds = 0, \qquad 0 \le t < x.$$
Gelfand–Levitan theory is the method that recovers $q$ and $h$ from $\rho$ by solving this equation and setting
$$q(x) = 2 \frac{d}{dx} K(x, x), \qquad h = K(0, 0).$$

## Remarks

The solution $K$ is the transformation kernel with $\varphi(x, \lambda) = \cos(\sqrt{\lambda}\, x) + \int_0^x K(x, t) \cos(\sqrt{\lambda}\, t) \, dt$.
Example: for $q = 0$ and $h = 0$, one has $\rho = \rho_0$, so $F = 0$, the equation gives $K = 0$, and the formulas return $q = 0$ and $h = 0$.
Non-example: an arbitrary nondecreasing function $\rho$ need not be a spectral function of such an operator; Gelfand and Levitan gave conditions on $\rho$ that characterise spectral functions.
For problems on a finite interval $[0, \pi]$ the same method works with $\rho$ a step function whose jumps sit at the eigenvalues.

## Explanations

### L1 human

The Gelfand–Levitan equation turns spectral data into a potential.
One measures how the given spectral function differs from the one of the free equation, solves a linear integral equation, and reads $q$ off the diagonal of the solution.
