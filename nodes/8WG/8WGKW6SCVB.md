---
tag: 8WGKW6SCVB
kind: definition
name: Brunt–Väisälä frequency
msc: [76B70, 76B55, 86A10]
defines: XQ82TE42FH
uses: [TXQQQG9T2S, 0YG0ZJPTWG]
sources:
  - url: https://en.wikipedia.org/wiki/Brunt%E2%80%93V%C3%A4is%C3%A4l%C3%A4_frequency
---

## Definition

Consider a fluid at rest in a uniform gravitational field of strength $g > 0$, with background density $\bar\rho(z)$ at height $z$.
Treat it in the [[Boussinesq approximation|TXQQQG9T2S]] with reference density $\rho_0$.
The *Brunt–Väisälä frequency* $N$ is defined by
$$N^2 = -\frac{g}{\rho_0} \frac{d \bar\rho}{d z}.$$
The stratification is stable where $N^2 > 0$, and then $N = \sqrt{N^2}$ is a frequency in radians per unit time.
For a dry atmosphere one uses instead $N^2 = \dfrac{g}{\theta} \dfrac{d \theta}{d z}$, where $\theta(z)$ is the potential temperature.

## Remarks

A parcel moved from height $z$ to $z + \zeta$ without mixing keeps its density $\bar\rho(z)$, while its new surroundings have density $\bar\rho(z + \zeta)$.
It feels the buoyancy force per unit mass $-g \big( \bar\rho(z) - \bar\rho(z + \zeta) \big) / \rho_0 \approx (g / \rho_0) \bar\rho'(z) \zeta = -N^2 \zeta$.
Hence $\ddot\zeta = -N^2 \zeta$, the equation of a [[harmonic oscillator|0YG0ZJPTWG]] of angular frequency $N$ when $N^2 > 0$.
If $N^2 < 0$, the displacement grows exponentially and the fluid is statically unstable.

Example: a linear profile $\bar\rho(z) = \rho_0 (1 - \gamma z)$ with $\gamma > 0$ gives the constant $N^2 = g \gamma$; for $\gamma = 10^{-5}$ m$^{-1}$, $N \approx 10^{-2}$ s$^{-1}$, a period $2 \pi / N$ of about $10$ minutes.

Non-example: a fluid of uniform density has $N = 0$; a displaced parcel feels no restoring force and does not oscillate.
