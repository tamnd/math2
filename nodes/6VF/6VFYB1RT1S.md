---
tag: 6VFYB1RT1S
kind: definition
name: Gaussian beam
msc: [78A60, 78A10, 35Q60]
defines: Y0QE726BE3
uses: [53DCTAEM5M]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_beam
---

## Definition

Let $\lambda > 0$ be a wavelength, $k = 2\pi/\lambda$, and let $w_0 > 0$ be the *waist radius*.
Set $z_R = \pi w_0^2 / \lambda$, the *Rayleigh range*, and for $z \in \R$ and $r \ge 0$ set
$$w(z) = w_0 \sqrt{1 + (z/z_R)^2}, \qquad \frac{1}{R(z)} = \frac{z}{z^2 + z_R^2}, \qquad \psi(z) = \arctan(z / z_R).$$
The *Gaussian beam* with waist at $z = 0$ and amplitude $E_0 > 0$ is the field
$$E(r, z) = E_0 \, \frac{w_0}{w(z)} \exp\!\left(-\frac{r^2}{w(z)^2}\right) \exp\!\left(i\left(kz + \frac{k r^2}{2 R(z)} - \psi(z)\right)\right),$$
where $r$ is the distance from the axis.
The time dependence $e^{-i\omega t}$ is omitted.

## Remarks

Up to a constant factor, $E = A \, e^{ikz}$ with $A = q^{-1} \exp(ik r^2 / (2q))$ and $q = z - i z_R$.
Indeed $1/q = 1/R(z) + i \lambda / (\pi w(z)^2)$, and this $A$ solves the [[paraxial wave equation|53DCTAEM5M]].
So $w(z)$ is the beam radius at which the amplitude falls to $1/e$ of its value on the axis, and $R(z)$ is the radius of curvature of the wavefronts.
At the waist $1/R(0) = 0$, so the wavefront is flat there.
Far from the waist, $w(z) \approx \theta z$ with the divergence angle $\theta = \lambda / (\pi w_0)$.
The phase $\psi(z)$ is the Gouy phase.

Example: for $\lambda = 633$ nm and $w_0 = 0.5$ mm, $z_R = \pi (0.5 \times 10^{-3})^2 / (633 \times 10^{-9}) \approx 1.24$ m.
So the beam stays within a factor $\sqrt 2$ of its waist radius over about $1.24$ m on each side.

Non-example: a uniform plane wave also solves the paraxial wave equation, but its intensity does not decay away from the axis.
It carries infinite power, so it is not a Gaussian beam.
