---
tag: ZCCHC127QS
kind: definition
name: Nonlinear Schrödinger equation in optics
msc: [78A60, 35Q55, 35Q60]
defines: BRJ36NF7KX
uses: [GEJHRXC176, Y7WQY4568B, 53DCTAEM5M]
sources:
  - url: https://en.wikipedia.org/wiki/Nonlinear_Schr%C3%B6dinger_equation
---

## Definition

Let a medium have the optical [[Kerr effect|Y7WQY4568B]] and neglect losses.
1. *Pulses in a fibre.* Let $A(z, T)$ be the complex envelope of a pulse, normalized so that $\abs{A}^2$ is the power.
Here $z$ is the distance along the fibre and $T$ is the time in a frame moving with the group velocity.
Let $\beta_2$ be the group-velocity dispersion parameter and $\gamma > 0$ the nonlinear coefficient of the fibre.
The *nonlinear Schrödinger equation for pulses* is
$$i \frac{\partial A}{\partial z} - \frac{\beta_2}{2} \frac{\partial^2 A}{\partial T^2} + \gamma \abs{A}^2 A = 0.$$
2. *Beams in a bulk medium.* Let $A(x, y, z)$ be the envelope of a monochromatic beam travelling along $z$, normalized so that $\abs{A}^2$ is the intensity.
Let the medium have linear index $n_0$ and nonlinear index $n_2$.
Let $k_0 = 2\pi/\lambda$ be the vacuum wavenumber and $k = n_0 k_0$.
The *nonlinear Schrödinger equation for beams* is
$$i \frac{\partial A}{\partial z} + \frac{1}{2k} \left( \frac{\partial^2 A}{\partial x^2} + \frac{\partial^2 A}{\partial y^2} \right) + k_0 n_2 \abs{A}^2 A = 0.$$

## Remarks

Both are cases of the cubic [[nonlinear Schrödinger equation|GEJHRXC176]], with $z$ in the role of time.
The beam equation is the [[paraxial wave equation|53DCTAEM5M]] with the extra phase $k_0 n_2 \abs{A}^2$ from the Kerr effect.
The pulse equation is focusing when $\beta_2 < 0$, anomalous dispersion, and defocusing when $\beta_2 > 0$, normal dispersion, if $\gamma > 0$.

Example: for $\beta_2 < 0$, the function $A(z, T) = \sqrt{P_0}\, \mathrm{sech}(T/T_0)\, e^{i \gamma P_0 z / 2}$ solves the pulse equation when $\gamma P_0 T_0^2 = \abs{\beta_2}$.
This is the fundamental bright soliton.

Non-example: in a medium without the Kerr effect, $\gamma = 0$ and $n_2 = 0$, and the equations become linear Schrödinger-type equations of dispersion and diffraction.
