---
tag: AFWX2ZS19Y
kind: definition
name: Lorentz oscillator model
msc: [78A40, 78A48]
defines: QSR3C1A1P9
uses: [0RNXVVTJTJ, YZ7Q9DP8RT, ASQAH710WN, F768YN0P2V, GFS95PZ5YK]
sources:
  - url: https://en.wikipedia.org/wiki/Lorentz_oscillator_model
---

## Definition

Let a medium contain $N > 0$ bound electrons per unit volume, each with charge $-e < 0$ and mass $m > 0$.
Let $x(t) \in \R^3$ be the displacement of an electron from its rest position.
The *Lorentz oscillator model* assumes that $x$ obeys the equation of a damped, driven [[harmonic oscillator|0RNXVVTJTJ]]
$$m \ddot x + m \gamma \dot x + m \omega_0^2 x = -e \, E(t).$$
Here $\omega_0 > 0$ is a natural frequency, $\gamma \geq 0$ is a damping rate, and $E$ is the local [[electric field|YZ7Q9DP8RT]].
The [[polarization density|ASQAH710WN]] is $P = -N e x$.
For a time-harmonic field $E(t) = \mathrm{Re}(E_0 e^{-i\omega t})$ and the steady-state solution, this gives $P = \varepsilon_0 \chi(\omega) E$ with the susceptibility
$$\chi(\omega) = \frac{\omega_p^2}{\omega_0^2 - \omega^2 - i \gamma \omega}, \qquad \omega_p^2 = \frac{N e^2}{\varepsilon_0 m},$$
and the relative [[permittivity|F768YN0P2V]] $\varepsilon_r(\omega) = 1 + \chi(\omega)$.

## Remarks

The steady state is $x = \mathrm{Re}(x_0 e^{-i\omega t})$ with $m(\omega_0^2 - \omega^2 - i\gamma\omega) x_0 = -e E_0$, and $P = -N e x$ gives $\chi$.
For $\gamma > 0$ the poles of $\chi$ are $\omega = -i\gamma/2 \pm \sqrt{\omega_0^2 - \gamma^2/4}$, in the lower half-plane, so $\chi$ is analytic in the upper half-plane and satisfies the [[Kramers–Kronig relations|GFS95PZ5YK]].
Several kinds of oscillators give a sum of such terms.

Example: with $\gamma = 0$ and $0 \le \omega < \omega_0$, $\chi(\omega) = \omega_p^2 / (\omega_0^2 - \omega^2)$ is positive and increasing in $\omega$, so the refractive index $\sqrt{\varepsilon_r}$ grows with frequency: this is normal dispersion, as in glass for visible light.

Non-example: a constant susceptibility $\chi \neq 0$ is not of Lorentz form, since every Lorentz susceptibility tends to $0$ as $\omega \to \infty$.

The case $\omega_0 = 0$, free electrons, gives the optical response of the Drude model.

## Explanations

### L1 human

The model writes Newton's law for an electron held by a spring and slowed by friction, pushed by the electric field of the light.
Solving it for a wave of one frequency gives how strongly the medium is polarized at that frequency.
From this one reads off the permittivity, and so the refractive index and the absorption.
