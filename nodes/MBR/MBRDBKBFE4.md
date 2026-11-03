---
tag: MBRDBKBFE4
kind: definition
name: Random vibration
msc: [70L05, 60G10, 70J35]
defines: KSFW7GWB5T
uses: [0QH5ENKZM1, DT0QXJE705, YCZHYY8VE5, 0RNXVVTJTJ, 3ZXN26PW4G]
sources:
  - url: https://en.wikipedia.org/wiki/Random_vibration
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a probability space.
Consider a mechanical system whose state is described by the displacement $x(t)$ and whose motion is driven by a load $F(t)$.
A *random vibration* of the system is a solution $x$ of its equation of motion whose load $F = (F(t))_{t \in \R}$ is a [[stochastic process|0QH5ENKZM1]] on $\Omega$.
The response $x = (x(t))_{t \in \R}$ is then itself a stochastic process.
It is described by its statistics: the mean $E[x(t)]$, the [[autocorrelation function|YCZHYY8VE5]] $E[x(t) \, x(t + \tau)]$, and the spectral density when it is stationary.

## Remarks

Example: the single-degree-of-freedom oscillator $m x'' + c x' + k x = F(t)$ with $m, c, k > 0$, driven by a weakly [[stationary process|DT0QXJE705]] $F$ with zero mean and spectral density $S_F$.
Its frequency response is $H(\omega) = 1 / (k - m \omega^2 + i c \omega)$.
The stationary response has spectral density $S_x(\omega) = \abs{H(\omega)}^2 S_F(\omega)$.
For white noise with constant spectral density $S_0$, normalised so that the variance is the integral of the spectral density over $\R$, the mean square response is
$$E[x^2] = S_0 \int_{-\infty}^{\infty} \abs{H(\omega)}^2 \, d\omega = \frac{\pi S_0}{k c}.$$

Non-example: the same oscillator driven by the deterministic load $F(t) = F_0 \cos \gamma t$ is a forced [[damped harmonic oscillator|0RNXVVTJTJ]] and not a random vibration, because the load is not random.

The link between the autocorrelation function and the spectral density of a stationary response is the [[Wiener–Khinchin theorem|3ZXN26PW4G]].

## Explanations

### L1 human

In a random vibration the push on the system is random, so the motion is random too.
One does not ask where the system is at a given time, but how large its motion is on average and how its energy spreads over the frequencies.
