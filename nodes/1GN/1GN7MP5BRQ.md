---
tag: 1GN7MP5BRQ
kind: definition
name: Emden–Chandrasekhar equation
msc: [85A15, 34A34]
defines: 5MXPY6QTZ6
uses: [0NT64JV96A, 4FC5XQA2RK]
sources:
  - url: https://en.wikipedia.org/wiki/Emden%E2%80%93Chandrasekhar_equation
---

## Definition

The *Emden–Chandrasekhar equation* is the [[ordinary differential equation|0NT64JV96A]]
$$\frac{1}{\xi^2} \frac{d}{d\xi} \left( \xi^2 \frac{d\psi}{d\xi} \right) = e^{-\psi}$$
for a real function $\psi$ of $\xi > 0$, with the initial conditions $\psi(0) = 0$ and $\psi'(0) = 0$.

## Remarks

It comes from a spherically symmetric, self-gravitating gas in [[hydrostatic equilibrium|4FC5XQA2RK]] with isothermal equation of state $P = c_s^2 \rho$, where $c_s$ is the constant isothermal sound speed.
With central density $\rho_c$ and gravitational constant $G$, one sets $\rho = \rho_c e^{-\psi}$ and $r = a \xi$ with $a^2 = c_s^2 / (4 \pi G \rho_c)$.
Example: the function $\psi(\xi) = \ln(\xi^2 / 2)$ satisfies the differential equation for $\xi > 0$.
Indeed, $\xi^2 \psi' = 2 \xi$, so the left side is $2/\xi^2$, and $e^{-\psi} = 2/\xi^2$.
It is the [[singular isothermal sphere|GCPWX48XRD]], and it fails the initial condition $\psi(0) = 0$, since $\psi \to -\infty$ as $\xi \to 0$.
The regular solution with $\psi(0) = \psi'(0) = 0$ has no closed form; it starts as $\psi = \xi^2/6 - \xi^4/120 + \cdots$.
An equivalent form uses $u = -\psi$, which satisfies $\xi^{-2} (\xi^2 u')' + e^{u} = 0$.
