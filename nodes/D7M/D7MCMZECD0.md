---
tag: D7MCMZECD0
kind: definition
name: Atmospheric refraction
msc: [85A04, 86A10]
defines: 13D4PQ5N0T
uses: [DMAYYCRMJD]
sources:
  - url: https://en.wikipedia.org/wiki/Atmospheric_refraction
---

## Definition

Fix an observer on the ground and a celestial object.
Let $a_0$ be the altitude of the object in the [[horizontal coordinate system|DMAYYCRMJD]] that the straight line of sight would give in a vacuum.
Let $a$ be the altitude of the direction from which its light actually reaches the observer through the atmosphere.
The *astronomical refraction* is $R = a - a_0$.

## Remarks

Since the refractive index of air decreases with height, rays bend towards the ground and $R \ge 0$.
Refraction changes the altitude and leaves the azimuth unchanged.
For a plane-parallel atmosphere, Snell's law gives $n_0 \sin z = \sin z_0$, where $z = 90^\circ - a$ and $n_0$ is the index of air at the ground.
This depends only on the air at the ground, so for small zenith distances $R \approx (n_0 - 1)\tan z$.
At standard pressure and temperature this is about $58''\tan z$.
Example: at the horizon $R$ is about $34'$, more than the apparent radius of the Sun.
Non-example: the twinkling of stars is a fast random fluctuation of the refraction, called scintillation, not the mean refraction $R$.
