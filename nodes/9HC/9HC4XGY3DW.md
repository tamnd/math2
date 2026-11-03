---
tag: 9HC4XGY3DW
kind: definition
name: Gain and phase margin
msc: [93C80, 93D09, 93B35]
defines: J39ZSFW0YF
uses: [BMY8QZSD9H, 7NYES2D0Z4, 070PFSYJJR, Z7SPHAWMDX, EZ1HMS875F]
sources:
  - url: https://en.wikipedia.org/wiki/Phase_margin
---

## Definition

Let $L$ be the loop transfer function of a single-input single-output unity negative [[feedback|7NYES2D0Z4]] loop.
Let $\omega \mapsto L(i\omega)$, $\omega > 0$, be its [[frequency response|BMY8QZSD9H]], and let $\arg L(i\omega)$ be a continuous choice of its [[argument|070PFSYJJR]], in degrees.

1. A *phase crossover frequency* is an $\omega_p > 0$ with $\arg L(i\omega_p) = -180^\circ$, and the *gain margin* is $g_m = 1/\abs{L(i\omega_p)}$, often given in decibels as $-20 \log_{10} \abs{L(i\omega_p)}$.
2. A *gain crossover frequency* is an $\omega_g > 0$ with $\abs{L(i\omega_g)} = 1$, and the *phase margin* is $\varphi_m = 180^\circ + \arg L(i\omega_g)$.

If there is no phase crossover frequency, the gain margin is taken to be infinite.
If there are several, one uses the one that gives the smallest margin, and likewise for the phase margin.

## Remarks

Suppose that $L$ has all its poles in the open left half-plane and that its [[Nyquist plot|Z7SPHAWMDX]] meets the negative real axis only at $L(i\omega_p) = -1/g_m$.
Then by the [[Nyquist stability criterion|EZ1HMS875F]], the loop with $kL$ in place of $L$ is stable for $0 < k < g_m$ and unstable for $k > g_m$.

Example: for $L(s) = 1/(s(s + 1))$, $\abs{L(i\omega)} = 1/(\omega\sqrt{1 + \omega^2})$ and $\arg L(i\omega) = -90^\circ - \arctan \omega$.
The gain crossover satisfies $\omega_g^2 (1 + \omega_g^2) = 1$, so $\omega_g^2 = (\sqrt{5} - 1)/2$ and $\omega_g \approx 0.786$.
Then $\varphi_m = 90^\circ - \arctan \omega_g \approx 51.8^\circ$.
The phase stays above $-180^\circ$, so there is no phase crossover and the gain margin is infinite.

Non-example: for $L(s) = 1/(2(s + 1))$, $\abs{L(i\omega)} \le 1/2$ for all $\omega$, so there is no gain crossover frequency.
The phase margin in the sense of clause 2 is not defined, and it is conventionally taken to be infinite.
