---
tag: RBQ9GWY3XM
kind: definition
name: Second sound
msc: [76A25, 82D50, 80A17]
defines: SYW4JJJTW3
uses: [FFD8ZJBMMD, 4PZBRJ78X4, KK46Q2YV1D, SW8X60GYZT]
sources:
  - url: https://en.wikipedia.org/wiki/Second_sound
---

## Definition

Let a medium carry small perturbations of its [[temperature|KK46Q2YV1D]] about a uniform equilibrium.
*Second sound* is a mode of heat transport in which these perturbations propagate as weakly damped waves with a finite speed.
The perturbations satisfy a wave equation with a small damping term, rather than a diffusion equation.
This is unlike ordinary heat [[conduction|SW8X60GYZT]], where temperature perturbations only spread and decay.

## Remarks

In [[superfluid|4PZBRJ78X4]] helium-4 below the lambda point, the two-fluid model of Landau gives the speed $u_2$ of second sound by
$$u_2^2 = \frac{\rho_s}{\rho_n} \, \frac{T s^2}{c}.$$
Here $\rho_s$ and $\rho_n$ are the superfluid and normal densities, $s$ is the entropy per unit mass, and $c$ is the specific heat per unit mass.

Example: the [[Cattaneo–Vernotte equation|FFD8ZJBMMD]] $\tau T_{tt} + T_t = \alpha T_{xx}$ has the solutions $T = e^{\lambda t} \cos(\kappa x)$ with $\tau \lambda^2 + \lambda + \alpha \kappa^2 = 0$.
When $4 \tau \alpha \kappa^2 > 1$, the roots are $\lambda = -1/(2\tau) \pm i \omega$ with $\omega > 0$, so the profile oscillates while it decays.
This is a damped temperature wave, the behaviour of second sound.

Non-example: under Fourier's law, the same trial function gives $\lambda = -\alpha \kappa^2$.
The temperature profile only decays and never oscillates, so there is no second sound.
