---
tag: DMPYWAGHQ3
kind: definition
name: Orbital resonance
msc: [70F15, 70K30]
defines: 3K553QG5BZ
uses: [K6KNWEVRY4, BXFSBB8Q46, 4F812GHFZK]
sources:
  - url: https://en.wikipedia.org/wiki/Orbital_resonance
---

## Definition

Let two bodies move on nearly [[Kepler orbits|BXFSBB8Q46]] about the same primary, with mean motions $n_1 > n_2 > 0$ and with [[orbital elements|K6KNWEVRY4]] that change slowly.
Let $\lambda_k = M_k + \omega_k + \Omega_k$ be the mean longitude and $\varpi_k = \omega_k + \Omega_k$ the longitude of periapsis of body $k$.
The bodies are in a $p : q$ *mean-motion resonance*, for coprime positive integers $p > q$, if

1. $q\, n_1 \approx p\, n_2$, so that the period ratio is close to $p / q$;
2. some resonant angle librates, that is, it oscillates in an interval shorter than $2\pi$ instead of increasing or decreasing without bound.

A resonant angle is a combination
$$\varphi = p \lambda_2 - q \lambda_1 + k_1 \varpi_1 + k_2 \varpi_2 + l_1 \Omega_1 + l_2 \Omega_2,$$
with integers $k_1, k_2, l_1, l_2$ such that $p - q + k_1 + k_2 + l_1 + l_2 = 0$.

## Remarks

The integer $p - q$ is the order of the resonance.
The condition on the sum of the coefficients makes $\varphi$ independent of the choice of reference direction.

Example: Neptune and Pluto have periods of about $164.8$ and $247.9$ years, a ratio close to $3/2$.
The angle $3\lambda_{\mathrm{P}} - 2\lambda_{\mathrm{N}} - \varpi_{\mathrm{P}}$ librates about $\pi$, with coefficient sum $3 - 2 - 1 = 0$.
So they are in a $3 : 2$ resonance, which keeps Pluto far from Neptune whenever it crosses Neptune's orbital distance.

Non-example: Jupiter and Saturn have a period ratio close to $5/2$, but the corresponding angles circulate, so clause 2 fails.
This near-commensurability causes the large periodic perturbation called the great inequality, but no resonance.

Several bodies can share a resonance: for Io, Europa and Ganymede, $\lambda_{\mathrm{I}} - 3\lambda_{\mathrm{E}} + 2\lambda_{\mathrm{G}}$ librates about $\pi$, the Laplace resonance.
Orbital resonance is a nonlinear analogue of the [[resonance|4F812GHFZK]] of a forced oscillator.
