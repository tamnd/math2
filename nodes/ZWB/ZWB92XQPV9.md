---
tag: ZWB92XQPV9
kind: definition
name: Drude model
msc: [82D35, 78A40, 78A48]
defines: 5Y1CZ2CFPN
uses: [YZ7Q9DP8RT, F768YN0P2V, QSR3C1A1P9]
sources:
  - url: https://en.wikipedia.org/wiki/Drude_model
---

## Definition

Let a metal contain $n > 0$ free electrons per unit volume, each with charge $-e < 0$ and mass $m > 0$.
Let $\tau > 0$ be the mean time between collisions.
Let $E(t)$ be a spatially uniform [[electric field|YZ7Q9DP8RT]].
The *Drude model* assumes that the mean momentum $p(t) \in \R^3$ of an electron obeys
$$\frac{dp}{dt} = -\frac{p}{\tau} - e E(t),$$
and that the current density is $J = -n e \, p / m$.

## Remarks

For a constant field the steady state is $p = -e \tau E$, so $J = \sigma_0 E$ with the DC conductivity $\sigma_0 = n e^2 \tau / m$: this is Ohm's law.
For a time-harmonic field $\mathrm{Re}(E_0 e^{-i\omega t})$ the steady state gives $J = \sigma(\omega) E$ with
$$\sigma(\omega) = \frac{\sigma_0}{1 - i \omega \tau}.$$
The relative [[permittivity|F768YN0P2V]] $\varepsilon_r = 1 + i \sigma / (\varepsilon_0 \omega)$ is then
$$\varepsilon_r(\omega) = 1 - \frac{\omega_p^2}{\omega^2 + i \omega / \tau}, \qquad \omega_p^2 = \frac{n e^2}{\varepsilon_0 m}.$$
This is the [[Lorentz oscillator model|QSR3C1A1P9]] with natural frequency $0$ and damping rate $1/\tau$.
For $\omega \tau \gg 1$, $\varepsilon_r$ is close to $1 - \omega_p^2 / \omega^2$, negative for $\omega < \omega_p$, where the metal reflects, and positive for $\omega > \omega_p$, where it becomes transparent.

Example: in a constant field $E$, the function $p(t) = -e\tau E + (p(0) + e\tau E) e^{-t/\tau}$ solves the equation of motion and tends to the steady state $-e\tau E$.

Non-example: electrons bound to atoms by a restoring force do not fit the model.
Their equation of motion has the additional term $-m \omega_0^2 x$ with $\omega_0 > 0$, and they are described by the Lorentz oscillator model instead.

## Explanations

### L1 human

The model treats conduction electrons as free particles with friction: the field accelerates them and collisions slow them down at the rate $1/\tau$.
Their average velocity becomes proportional to the field, which gives the conductivity.
At high frequency the electrons cannot keep up with the field, and this gives the optical behaviour of metals.
