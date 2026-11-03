---
tag: 7V9T5AVD3D
kind: definition
name: Transit light curve
msc: [85A04, 70F15]
defines: N7X5Y31GJQ
uses: [BXFSBB8Q46, EM7C674YV6]
sources:
  - url: https://en.wikipedia.org/wiki/Methods_of_detecting_exoplanets
---

## Definition

Let a star of radius $R_\star$ and uniform surface brightness be orbited by an opaque spherical planet of radius $R_p < R_\star$ on a [[Kepler orbit|BXFSBB8Q46]].
Let $k = R_p/R_\star$.
Let $d(t)$ be the distance between the centres of the two disks projected on the sky, in units of $R_\star$.
Only times when the planet is in front of the star are considered.
Let $\lambda(k, d)$ be the area of the intersection of two disks of radii $1$ and $k$ at centre distance $d$, divided by $\pi$.
The *transit light curve* is the normalised flux
$$F(t) = 1 - \lambda\big(k, d(t)\big).$$

## Remarks

The flux is $1$ when $d \ge 1 + k$, and equals $1 - k^2$ when $d \le 1 - k$, where the planet is fully inside the stellar disk; so the transit depth is $k^2 = (R_p/R_\star)^2$.
For a circular orbit of period $P$, radius $a$ and inclination $i$, the impact parameter is $b = a \cos i / R_\star$, and the total duration of the transit is
$$T = \frac{P}{\pi} \arcsin\left( \frac{R_\star}{a} \, \frac{\sqrt{(1 + k)^2 - b^2}}{\sin i} \right).$$
Real stars are darker near the edge; with [[limb darkening|EM7C674YV6]] the bottom of the dip becomes rounded instead of flat.

Example: a planet with $R_p = R_\star/10$ crossing the centre of the star ($b = 0$) gives $F = 1 - 0.01$ while it is fully inside the disk, a dip of $1\%$.

Non-example: if $b > 1 + k$, then $d(t) > 1 + k$ at all times, the disks never overlap, $\lambda = 0$, and the light curve shows no transit.
For randomly oriented circular orbits the probability that a transit occurs is about $R_\star/a$.
