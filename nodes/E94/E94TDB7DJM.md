---
tag: E94TDB7DJM
kind: definition
name: Ernst equation
msc: [83C15, 83C05, 35Q75]
defines: G0YMK0R648
uses: [ASWJNB3804, JRV1T69FYJ, S8RG6N1PRT]
sources:
  - url: https://en.wikipedia.org/wiki/Ernst_equation
---

## Definition

Let $g$ be a stationary axisymmetric metric in [[Weyl–Lewis–Papapetrou coordinates|ASWJNB3804]],
$$g = -f\left(dt - \omega\, d\phi\right)^2 + f^{-1}\left(e^{2\gamma}\left(d\rho^2 + dz^2\right) + \rho^2 d\phi^2\right),$$
with $f > 0$, $\omega$, $\gamma$ functions of $(\rho, z)$.
The *twist potential* $\psi$ is a function of $(\rho, z)$ with
$$\partial_\rho \psi = -\frac{f^2}{\rho}\, \partial_z \omega, \qquad \partial_z \psi = \frac{f^2}{\rho}\, \partial_\rho \omega,$$
and the *Ernst potential* is $\mathcal{E} = f + i\psi$.
Let $\nabla$ and $\nabla^2 = \partial_\rho^2 + \rho^{-1}\partial_\rho + \partial_z^2$ be the gradient and the Laplacian of flat $\R^3$ in cylindrical coordinates, applied to functions of $(\rho, z)$.
The *Ernst equation* is
$$\left(\operatorname{Re}\mathcal{E}\right) \nabla^2 \mathcal{E} = \nabla\mathcal{E} \cdot \nabla\mathcal{E},$$
where the product $\nabla\mathcal{E}\cdot\nabla\mathcal{E}$ has no complex conjugation.

## Remarks

The twist potential exists locally when $\partial_\rho(\rho^{-1} f^2 \partial_\rho\omega) + \partial_z(\rho^{-1} f^2 \partial_z\omega) = 0$, which is one of the vacuum equations; sign conventions for $\psi$ vary between texts.
The metric $g$ is a [[vacuum solution|JRV1T69FYJ]] if and only if $\mathcal{E}$ solves the Ernst equation and $\gamma$ solves a pair of first-order equations.
These can be integrated once $\mathcal{E}$ is known.

Example: in the static case $\omega = 0$ one has $\psi = 0$ and $\mathcal{E} = f = e^{2U}$.
Then $\nabla f = 2f\nabla U$ and $\nabla^2 f = 2f\nabla^2 U + 4f\abs{\nabla U}^2$, so the Ernst equation becomes $2f^2\nabla^2 U = 0$, that is, [[Laplace's equation|S8RG6N1PRT]] $\nabla^2 U = 0$.
For instance $U = -M / \sqrt{\rho^2 + z^2}$ with $M > 0$ is harmonic away from the origin, so $\mathcal{E} = e^{2U}$ solves the Ernst equation (the Curzon solution).

Non-example: $\mathcal{E} = z^2$.
Here $\operatorname{Re}\mathcal{E}\, \nabla^2\mathcal{E} = 2z^2$ while $\nabla\mathcal{E}\cdot\nabla\mathcal{E} = 4z^2$, so the equation fails wherever $z \ne 0$.

An equivalent form uses $\xi$ with $\mathcal{E} = \frac{\xi - 1}{\xi + 1}$, which gives $\left(\xi\bar\xi - 1\right)\nabla^2\xi = 2\bar\xi\, \nabla\xi\cdot\nabla\xi$.
