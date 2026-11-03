---
tag: ANESZY4DAW
kind: definition
name: Schwarzschild radius
msc: ["83C57", "83C15"]
defines: G48AGJAZNG
uses: [6Y50T68WKY]
sources:
  - url: https://en.wikipedia.org/wiki/Schwarzschild_radius
---

## Definition

Let $M > 0$ be a mass, let $G$ be the gravitational constant and let $c$ be the speed of light.
The *Schwarzschild radius* of $M$ is
$$r_s = \frac{2GM}{c^2}.$$
In geometric units $G = c = 1$ it is $r_s = 2M$.

## Remarks

In the [[Schwarzschild metric|6Y50T68WKY]] of mass $M$, the coefficient $1 - r_s/r$ of $c^2 dt^2$ vanishes exactly at $r = r_s$.
This sphere is the event horizon, and its area is $4\pi r_s^2 = 16\pi G^2 M^2 / c^4$.

Example: for the Sun, $M \approx 1.989 \times 10^{30}$ kg.
With $G \approx 6.674 \times 10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$ and $c \approx 2.998 \times 10^8$ m/s, this gives $r_s \approx 2.95$ km.

Non-example: for a rotating Kerr black hole of mass $M$ and angular momentum $J = aM$ with $0 < \abs{a} \le M$, the horizon lies at $r_+ = M + \sqrt{M^2 - a^2} < 2M$ in Boyer–Lindquist coordinates.
So the horizon radius of a rotating black hole is not its Schwarzschild radius; the two agree only when $a = 0$.

The radius $r = 3M$ of the photon sphere and the radius $r = 6M$ of the innermost stable circular orbit are other natural radii of the Schwarzschild metric.
