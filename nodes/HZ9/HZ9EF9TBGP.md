---
tag: HZ9EF9TBGP
kind: definition
name: Shakura–Sunyaev alpha disk model
msc: [85A30, 76U05]
defines: E5GR4K48B5
uses: [6ADKW56QGV, NM5Q4845Z4, SN4J6KP03C, BXFSBB8Q46]
sources:
  - url: https://en.wikipedia.org/wiki/Accretion_disk
---

## Definition

Let a central body of mass $M$ be surrounded by an axisymmetric [[accretion disk|6ADKW56QGV]] of gas, with $G$ the gravitational constant.
Let $R$ be the cylindrical radius and $\Sigma(R, t)$ the surface density.
Let $c_s(R, t)$ be the isothermal [[speed of sound|SN4J6KP03C]] in the midplane and $\Omega(R)$ the angular velocity of the gas.
The *Shakura–Sunyaev alpha disk model* is the disk model with these three assumptions.

1. The rotation is Keplerian, as for a [[Kepler orbit|BXFSBB8Q46]] on a circle: $\Omega(R) = \sqrt{GM/R^3}$.
2. The disk is thin: its scale height $H = c_s/\Omega$ satisfies $H \ll R$.
3. The kinematic [[viscosity|NM5Q4845Z4]] of the disk is $\nu = \alpha c_s H$, where $\alpha$ is a dimensionless constant with $0 < \alpha \le 1$.

## Remarks

Under these assumptions, $\Sigma$ obeys the diffusion equation
$$\frac{\partial \Sigma}{\partial t} = \frac{3}{R} \frac{\partial}{\partial R} \left[ R^{1/2} \frac{\partial}{\partial R} \left( \nu \Sigma R^{1/2} \right) \right].$$
A steady disk with accretion rate $\dot M$ and zero torque at an inner radius $R_*$ satisfies
$$\nu \Sigma = \frac{\dot M}{3\pi} \left( 1 - \sqrt{R_*/R} \right).$$
The heat released per unit area on each face is $D(R) = \frac{9}{8} \nu \Sigma \Omega^2 = \frac{3 G M \dot M}{8 \pi R^3} \left( 1 - \sqrt{R_*/R} \right)$.
If each face radiates as a black body of temperature $T$, then $\sigma_{SB} T^4 = D(R)$, where $\sigma_{SB}$ is the Stefan–Boltzmann constant, so $T \propto R^{-3/4}$ for $R \gg R_*$.

Example: a disk with $c_s/(\Omega R) = 0.01$ and $\alpha = 0.1$ satisfies all three clauses; its viscosity is $\nu = 0.1 \, c_s^2/\Omega = 10^{-5} \, \Omega R^2$.

Non-example: a thick torus with $H$ comparable to $R$ fails clause 2, and its pressure support makes the rotation non-Keplerian, so it is not an alpha disk in this sense.

The bound $\alpha \le 1$ expresses that turbulent eddies are at most of size $H$ and at most sonic.
