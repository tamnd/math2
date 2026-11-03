---
tag: 3FZ8ANW05R
kind: definition
name: Energy balance model
msc: [86A08, 35K57]
defines: M182YC20JJ
uses: [M49PQ7BDYN, 6JQVMS9Y7R, 0NT64JV96A, VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Climate_model
---

## Definition

Let $S_0 > 0$ be the solar constant, the flux of solar radiation at the mean distance of the Earth from the Sun.
A *zero-dimensional energy balance model* is the [[ordinary differential equation|0NT64JV96A]]
$$C \frac{dT}{dt} = \frac{S_0}{4} \big( 1 - \alpha(T) \big) - E(T).$$
Here $T(t)$ is the global mean surface temperature and $C > 0$ is a heat capacity per unit area.
The planetary albedo is $\alpha(T) \in [0, 1]$, and the outgoing infrared flux $E(T)$ is an increasing function of $T$.
Common choices are $E(T) = \varepsilon \sigma T^4$, with $\sigma$ the Stefan–Boltzmann constant and an effective emissivity $0 < \varepsilon \le 1$, or the linear fit $E(T) = A + B T$ with $B > 0$.

In a *one-dimensional energy balance model*, $T(y, t)$ depends on $y = \sin(\text{latitude}) \in [-1, 1]$, and
$$C \frac{\partial T}{\partial t} = \frac{S_0}{4} s(y) \big( 1 - \alpha(y, T) \big) - E(T) + \frac{\partial}{\partial y} \Big( D (1 - y^2) \frac{\partial T}{\partial y} \Big).$$
Here $s(y) \ge 0$ is the distribution of annual mean insolation, with mean $1$ over $[-1, 1]$.
The constant $D > 0$ is a diffusion coefficient for the transport of heat toward the poles.

## Remarks

Example: with constant albedo $\alpha = 0.3$, $E(T) = \sigma T^4$ ([[Stefan–Boltzmann law|6JQVMS9Y7R]]) and $S_0 = 1361 \ \mathrm{W/m^2}$, the zero-dimensional model has the single equilibrium
$$T^* = \Big( \frac{(1 - \alpha) S_0}{4 \sigma} \Big)^{1/4} \approx 255 \ \mathrm{K}.$$
It is stable, since the right side decreases in $T$.

Non-example: a radiative-convective model resolves the vertical profile of temperature in the atmosphere.
It is not an energy balance model in this sense, since its state is not the surface temperature alone.

The factor $1/4$ is the ratio of the area of the disc that intercepts sunlight, $\pi a^2$, to the area of the sphere, $4 \pi a^2$.
The diffusion term is the [[heat equation|VP2HN86VAG]] on the sphere for a temperature that depends only on latitude.
