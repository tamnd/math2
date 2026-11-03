---
tag: YQT405NC6B
kind: definition
name: Taylor microscale
msc: [76F05]
defines: KF7QP3GF9K
uses: [VY307F8Z0S, V47TX9AFKF, NYRS1BJKRQ, JH9EJ0HA0R]
sources:
  - url: https://en.wikipedia.org/wiki/Taylor_microscale
---

## Definition

Consider a statistically homogeneous [[turbulent|VY307F8Z0S]] velocity field with fluctuations $u_i'$ from the [[Reynolds decomposition|V47TX9AFKF]], and write $\langle \cdot \rangle$ for the mean.
Let $f(r) = \langle u_1'(\mathbf{x}) \, u_1'(\mathbf{x} + r \mathbf{e}_1) \rangle / \langle u_1'^2 \rangle$ and $g(r) = \langle u_1'(\mathbf{x}) \, u_1'(\mathbf{x} + r \mathbf{e}_2) \rangle / \langle u_1'^2 \rangle$ be the longitudinal and transverse velocity correlation functions.
The longitudinal and transverse *Taylor microscales* are
$$\lambda_f = \left( -\tfrac12 f''(0) \right)^{-1/2} = \left( \frac{2 \langle u_1'^2 \rangle}{\langle (\partial u_1' / \partial x_1)^2 \rangle} \right)^{1/2}, \qquad \lambda_g = \left( -\tfrac12 g''(0) \right)^{-1/2} = \left( \frac{2 \langle u_1'^2 \rangle}{\langle (\partial u_1' / \partial x_2)^2 \rangle} \right)^{1/2}.$$

## Remarks

The second form of each formula follows from homogeneity, which gives $f''(0) = -\langle (\partial u_1' / \partial x_1)^2 \rangle / \langle u_1'^2 \rangle$.
Near $r = 0$ one has $f(r) \approx 1 - r^2 / \lambda_f^2$, so $\lambda_f$ is where this osculating parabola meets zero.
Conventions differ between books by factors such as $\sqrt 2$, so a value should always be quoted with its definition.

In isotropic turbulence $\lambda_f = \sqrt 2 \, \lambda_g$, and the mean dissipation rate is $\varepsilon = 15 \nu u'^2 / \lambda_g^2$ with $u'^2 = \langle u_1'^2 \rangle$ and kinematic viscosity $\nu$.
The Taylor-scale [[Reynolds number|JH9EJ0HA0R]] is $\mathrm{Re}_\lambda = u' \lambda_g / \nu$.
With the [[Kolmogorov length|NYRS1BJKRQ]] $\eta$, the isotropic relation gives $\lambda_g = \sqrt{15} \, \eta^{2/3} \ell^{1/3}$ when $\varepsilon = u'^3 / \ell$ defines a large-scale length $\ell$, so $\eta \ll \lambda_g \ll \ell$ at high Reynolds number.

Example: for the correlation $f(r) = e^{-r^2 / L^2}$ one has $f''(0) = -2 / L^2$, so $\lambda_f = L$.
Non-example: for $f(r) = e^{-\abs{r} / L}$ the function is not twice differentiable at $0$, so $\lambda_f$ is not defined; such a field has infinite mean square gradient, which a viscous flow cannot have.
