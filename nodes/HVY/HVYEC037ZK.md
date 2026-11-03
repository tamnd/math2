---
tag: HVYEC037ZK
kind: definition
name: Absolute magnitude
msc: [85A04]
defines: D7EAZ5F0YT
uses: [R8BRMEQ4DN, 93CFD71XZ5]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_magnitude
---

## Definition

Fix a photometric passband.
Let an object outside the solar system have [[apparent magnitude|R8BRMEQ4DN]] $m$ in that band and distance $d$ from the observer.
Assume there is no absorption of light between the object and the observer.
The *absolute magnitude* of the object is the apparent magnitude it would have at a distance of $10$ [[parsecs|93CFD71XZ5]]:
$$M = m - 5 \log_{10} \frac{d}{10\ \mathrm{pc}}.$$

## Remarks

The formula follows from the inverse square law: the flux scales as $d^{-2}$, and $-2.5 \log_{10} d^{-2} = 5 \log_{10} d$.
Example: the Sun has $m \approx -26.74$ at $d = 1$ au $\approx 4.848 \times 10^{-6}$ pc.
Then $5\log_{10}(d / 10\ \mathrm{pc}) \approx -31.57$, so $M \approx 4.83$.
Non-example: for asteroids and comets the name "absolute magnitude" denotes a different quantity, defined at $1$ au from both the Sun and the observer.
The magnitude over all wavelengths is the bolometric magnitude, and it is a linear function of $\log_{10}$ of the luminosity.
